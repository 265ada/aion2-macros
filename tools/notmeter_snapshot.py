"""Build data/topplayers.json from NotMeter's public statistics cache.

What it reads (all public files the notmeter.com site itself loads):
  - Global (NA/EU/SA/Asia) weekly + all-time top-50 boss parses, with each parse's per-skill breakdown
  - Korea's top-20 build guide per class (skill levels, specialization picks, stigmas, passives, Arcana, rings)
  - Korea's and Global's class performance tables

What it writes: data/topplayers.json, read by class.js ("Top players" section) and home.js (tier list).
Hand-written advice lives in data/plans.json; this file is numbers only, so re-running it never loses text.

Usage:  python tools/notmeter_snapshot.py [--cache .cache/notmeter] [--top 20]
Needs ~100 MB of downloads the first time (the per-parse detail buckets); later runs reuse the cache
for the same NotMeter generation.
"""
import argparse, base64, collections, concurrent.futures, gzip, json, math, os, re, statistics as st, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB = {'검성': 'gladiator', '수호성': 'templar', '살성': 'assassin', '궁성': 'ranger', '마도성': 'sorcerer',
       '정령성': 'spiritmaster', '치유성': 'cleric', '호법성': 'chanter', '권성': 'brawler'}
CLASSES = ['gladiator', 'templar', 'assassin', 'ranger', 'sorcerer', 'spiritmaster', 'cleric', 'chanter']
UA = {'User-Agent': 'Mozilla/5.0 (aion2-macros snapshot)'}


def get(url, path=None):
    if path and os.path.exists(path):
        return open(path, 'rb').read()
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    if path:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'wb').write(data)
    return data


def maybe_gunzip(b):
    return gzip.decompress(b) if b[:2] == b'\x1f\x8b' else b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cache', default=os.path.join(ROOT, '.cache', 'notmeter'))
    ap.add_argument('--top', type=int, default=20, help='top N parses per class per boss')
    a = ap.parse_args()

    latest = json.loads(get('https://notmeter.com/data/client/notmeter-ranking-latest.json'))
    gen = latest['release']['generation']
    base = latest['pagesRoot'].rstrip('/')
    cache = os.path.join(a.cache, gen)
    print('NotMeter generation', gen, latest['publishedAt'])

    glr = json.loads(get(base + '/data/notmeter-global-ranking.json', os.path.join(cache, 'global-ranking.json')))
    guide = json.loads(maybe_gunzip(get(base + '/data/notmeter-setting-guide.json.gz', os.path.join(cache, 'setting-guide.json.gz'))))
    krov = json.loads(maybe_gunzip(get(base + '/data/notmeter-ranking-class-overall.json.gz', os.path.join(cache, 'class-overall.json.gz'))))

    rows = [dict(r, dummy=False) for r in glr['rows']] + [dict(r, dummy=True) for r in glr['trainingDummyRows']]
    prefixes = sorted({r['detailToken'][:2] for r in rows if r.get('detailToken')})

    def fetch(p):
        return p, json.loads(get(f'{base}/data/global-ranking-details/{p}.json', os.path.join(cache, 'details', p + '.json')))['details']
    details = {}
    with concurrent.futures.ThreadPoolExecutor(12) as ex:
        for p, d in ex.map(fetch, prefixes):
            details[p] = d
    print('detail buckets', len(details))

    # names: site skills/stigmas by game id, then NotMeter's own English names
    skills = json.load(open(os.path.join(ROOT, 'data', 'skills.json'), encoding='utf-8'))
    sdb = json.load(open(os.path.join(ROOT, 'data', 'stigma_db.json'), encoding='utf-8'))
    byid, byko = {}, {}
    for n, v in skills.items():
        if isinstance(v, dict) and v.get('id'):
            byid[int(v['id'])] = n
            byko.setdefault(v.get('ko'), n)
    stig = {}
    for k, v in sdb.items():
        if ':' in k and isinstance(v, dict):
            stig[int(v['id']) // 10000] = (v['cls'], v['en'])
            byko.setdefault(v.get('ko'), v['en'])
    seen_names = collections.defaultdict(collections.Counter)

    parses = []
    for r in rows:
        x = details.get(r['detailToken'][:2], {}).get(r['detailToken'])
        if not x:
            continue
        rec = json.loads(gzip.decompress(base64.b64decode(x)))['record']
        me = [q for q in rec['players'] if q['actorId'] == r['actorId']]
        if not me or me[0]['jobName'] not in JOB:
            continue
        q = me[0]
        sk = []
        for s in q['skills']:
            seen_names[s['skillCode']][s['skillName']] += 1
            sk.append((s['skillCode'], s.get('rawSkillCode') or 0, s.get('damagePercentage') or 0, s.get('useCount') or 0))
        bf = [(b.get('code') or 0, b.get('skillLevel') or 0) for b in q.get('buffs', []) if b.get('sourceActorId') == q['actorId']]
        parses.append({'cls': JOB[q['jobName']], 'name': q['name'], 'boss': r['bossKey'], 'dummy': r['dummy'],
                       'cp': q['combatPower'], 'dps': q['dps'], 'dur': rec['durationSeconds'], 'sk': sk, 'bf': bf})
    print('parses', len(parses))

    def name(code):
        if code in byid:
            return byid[code]
        c = seen_names.get(code)
        if c:
            en = [k for k in c if re.fullmatch(r"[A-Za-z0-9 '\-:,()]+", k)]
            if en:
                return max(en, key=lambda k: c[k]).replace(' - Max', '').replace(' MAX', '')
        return str(code)

    def specs(base, raw):
        """rawSkillCode = base + picked options (sorted digits) + charge stage digit"""
        r = raw - base
        if base % 10000 or r < 0 or r >= 10000:
            return None
        return ''.join(sorted(set(str(r // 10)) - {'0'}))

    def lvl(sp):
        return 20 if len(sp) >= 3 else 16 if '5' in sp else 12 if (len(sp) == 2 or '4' in sp) else 8 if sp else 0

    out = {'meta': {'source': 'NotMeter public statistics (notmeter.com)', 'generation': gen,
                    'published': latest['publishedAt'][:10], 'top': a.top,
                    'week': glr['classPerformance'].get('periodLabel', '').split('|')[1:3]},
           'classes': {}, 'tiers': {}}

    # best parse per player per boss (bosses only), CP-adjusted residuals for top-10% splits
    best = {}
    for p in parses:
        if p['dummy'] or not p['cp'] or p['dps'] <= 0:
            continue
        k = (p['cls'], p['name'], p['boss'])
        if k not in best or p['dps'] > best[k]['dps']:
            best[k] = p
    allbest = list(best.values())

    for cls in CLASSES:
        mine = [p for p in allbest if p['cls'] == cls]
        by = collections.defaultdict(list)
        for p in mine:
            by[p['boss']].append(p)
        sel = []
        for l in by.values():
            l.sort(key=lambda p: -p['dps'])
            sel += l[:a.top]
        if not sel:
            continue
        # residual vs CP within boss -> top 10% of the selection
        xs, ys = [], []
        for l in by.values():
            l2 = [p for p in l[:a.top]]
            if len(l2) < 5:
                continue
            mx = st.mean(math.log(p['cp']) for p in l2); my = st.mean(math.log(p['dps']) for p in l2)
            for p in l2:
                p['_x'] = math.log(p['cp']) - mx; p['_y'] = math.log(p['dps']) - my
                xs.append(p['_x']); ys.append(p['_y'])
        slope = sum(x * y for x, y in zip(xs, ys)) / max(1e-9, sum(x * x for x in xs))
        for p in sel:
            p['_r'] = p.get('_y', 0) - slope * p.get('_x', 0)
        ranked = sorted(sel, key=lambda p: -p['_r'])
        top10 = ranked[:max(1, len(ranked) // 10)]

        share = collections.defaultdict(list); cpm = collections.defaultdict(list); pres = collections.Counter()
        cpm_top = collections.defaultdict(list)
        for p in sel:
            seen = collections.defaultdict(lambda: [0.0, 0])
            for code, raw, sh, use in p['sk']:
                seen[code][0] += sh; seen[code][1] += use
            for code, (sh, use) in seen.items():
                share[code].append(sh); cpm[code].append(use / p['dur'] * 60); pres[code] += 1
        for p in top10:
            seen = collections.Counter()
            for code, raw, sh, use in p['sk']:
                seen[code] += use
            for code in share:
                cpm_top[code].append(seen.get(code, 0) / p['dur'] * 60)
        N = len(sel)
        dmg = []
        for code in sorted(share, key=lambda c: -sum(share[c])):
            avg = sum(share[code]) / N
            if avg < 0.8:
                break
            dmg.append([name(code), round(avg, 1), round(st.median(cpm[code]), 1), round(st.median(cpm_top[code]), 1), round(100 * pres[code] / N)])

        # levels implied by specialization picks, per player (highest pick set seen)
        pl = collections.defaultdict(dict)
        for p in sel:
            for code, raw, sh, use in p['sk']:
                sp = specs(code, raw)
                if sp is None or code // 10000 in stig:
                    continue
                cur = pl[p['name']].get(code)
                if cur is None or len(sp) > len(cur):
                    pl[p['name']][code] = sp
        levels = []
        for code in sorted(share, key=lambda c: -sum(share[c])):
            d = [v[code] for v in pl.values() if code in v and v[code]]
            if len(d) < len(pl) * 0.3 or (skills.get(name(code)) or {}).get('chain'):
                continue  # chain skills carry their parent's picks
            L = [lvl(x) for x in d]
            picks = collections.Counter(d).most_common(4)
            levels.append([name(code), round(100 * sum(x >= 16 for x in L) / len(L)), round(100 * sum(x >= 20 for x in L) / len(L)),
                           [[k, round(100 * v / len(d))] for k, v in picks]])

        # stigmas: union per player (skills used + own buffs), highest buff level seen
        sp = collections.defaultdict(dict)
        for p in sel:
            for code, raw, sh, use in p['sk']:
                t = stig.get(code // 10000)
                if t and t[0] == cls:
                    sp[p['name']].setdefault(t[1], 0)
            for code, lv in p['bf']:
                t = stig.get(code // 100000) or stig.get(code // 10000)
                if t and t[0] == cls:
                    sp[p['name']][t[1]] = max(sp[p['name']].get(t[1], 0), lv)
        cnt = collections.Counter(); lvs = collections.defaultdict(list)
        for d in sp.values():
            for s, lv in d.items():
                cnt[s] += 1
                if lv:
                    lvs[s].append(lv)
        stigmas = [[s, round(100 * k / max(1, len(sp))), (collections.Counter(lvs[s]).most_common(1)[0][0] if lvs[s] else None)]
                   for s, k in cnt.most_common(7) if k / max(1, len(sp)) >= 0.08]

        out['classes'][cls] = {
            'parses': N, 'players': len({p['name'] for p in sel}), 'bosses': len(by),
            'cp': int(st.median(p['cp'] for p in sel)), 'dps': int(st.median(p['dps'] for p in sel)),
            'topGain': round((math.exp(st.mean(p['_r'] for p in top10)) - 1) * 100),
            'dmg': dmg[:14], 'levels': levels[:12], 'stigmas': stigmas,
        }

    # ---- tiers: Global CP-matched (boss + class fixed effects, common CP slope), NotMeter Global, Korea 800k+
    cls_list = [c for c in CLASSES if any(p['cls'] == c for p in allbest)]
    bos = sorted({p['boss'] for p in allbest})
    cf = {c: 0.0 for c in cls_list}; bf = {b: 0.0 for b in bos}; b = 1.5
    byb = collections.defaultdict(list); byc = collections.defaultdict(list)
    for p in allbest:
        byb[p['boss']].append(p); byc[p['cls']].append(p)
    for _ in range(40):
        for bb, l in byb.items():
            bf[bb] = st.mean(math.log(p['dps']) - cf[p['cls']] - b * math.log(p['cp']) for p in l)
        for c, l in byc.items():
            cf[c] = st.mean(math.log(p['dps']) - bf[p['boss']] - b * math.log(p['cp']) for p in l)
        m = st.mean(cf.values()); cf = {c: v - m for c, v in cf.items()}
        xs = [math.log(p['cp']) for p in allbest]; ys = [math.log(p['dps']) - bf[p['boss']] - cf[p['cls']] for p in allbest]
        mx, my = st.mean(xs), st.mean(ys)
        b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    spread = {}
    for c, l in byc.items():
        pp = collections.defaultdict(list)
        for p in l:
            pp[p['name']].append(math.log(p['dps']) - bf[p['boss']] - cf[c] - b * math.log(p['cp']))
        pm = sorted(st.mean(v) for v in pp.values())
        spread[c] = round((math.exp(pm[int(.9 * (len(pm) - 1))] - pm[int(.1 * (len(pm) - 1))]) - 1) * 100)
    out['tiers']['globalCp'] = [[c, round((math.exp(cf[c]) - 1) * 100, 1), spread[c]] for c in sorted(cf, key=lambda c: -cf[c])]
    out['tiers']['globalNm'] = [[JOB[r['jobName']], r['score']] for r in glr['classPerformance']['rows']]
    for key, label in [('classPerformance', 'kr800'), ('classPerformance1000K', 'kr1000')]:
        if key in krov:
            out['tiers'][label] = [[JOB[r['jobName']], r['score']] for r in krov[key]['rows']]

    # ---- Korea endgame builds (top 20 per class)
    def kname(x):
        n = x.get('name', '')
        return byko.get(n, n)
    kr = {}
    for j in guide['jobs']:
        c = JOB.get(j['jobName'])
        if c not in CLASSES:
            continue
        act = []
        for s in j['skills']['active']:
            if s['equippedRatePercent'] < 50:
                continue
            spc = {o['index']: o['usageRatePercent'] for o in (s.get('specializations') or [])}
            picks = ''.join(str(i) for i in range(1, 6) if spc.get(i, 0) >= 50)
            act.append([kname(s), s['medianLevel'], picks])
        kr[c] = {
            'n': j['sampledCharacters'], 'asof': j['newestSnapshotAt'][:10],
            'act': act,
            'stig': [[kname(s), s['equippedRatePercent'], s['medianLevel']] for s in sorted(j['skills']['stigma'], key=lambda s: -s['equippedRatePercent']) if s['equippedRatePercent'] >= 50],
            'pas': [[kname(s), s['medianLevel']] for s in j['skills']['passive']],
            'arcana': [[kname(s), s['medianLevel'], s['usageRatePercent']] for s in j['arcana']['skills']],
            'rings': next(([kname(k) for k in sl['skills'] if k['usageRatePercent'] >= 50] for sl in j['soulEngravings'] if sl['slotName'] == '반지'), []),
        }
    out['kr'] = kr
    dst = os.path.join(ROOT, 'data', 'topplayers.json')
    json.dump(out, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote', dst)


if __name__ == '__main__':
    sys.exit(main())
