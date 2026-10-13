"""Build data/genus.json: the Global Pet Genus (Genus Insight) audit and per-class, per-build recommendations.

Inputs (snapshots in tools/genus_src/, refresh them when the Global client patches the Pets window):
  - aion2timers_genus_insight_25800038.json  Global client tables (VehicleCreatureSlot / Option / Level), build 25800038
                                             (Steam update Oct 1, 2026): every slot's pool, ranges, weights, grade odds per
                                             Insight level, XP per level, analysis and lock costs.
                                             Source: https://www.aion2timers.com/gamedata/genus_insight.json
  - questlog_genus_slots.json                questlog.gg's own datamine of the same tables (characterBuilder.getGenusInsightSlots).
                                             The script stops if the two disagree on any of the 45 slots.
  - questlog_global_build_counts.json        what 132 public Global questlog builds put on each line (community signal only).

Everything that is a judgement (which stat is best for which class) is in RULES below, with its reasoning and confidence,
so it can be re-checked when the meta or the client changes.
Usage: python tools/build_genus.py
"""
import json, math, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'tools', 'genus_src')
A = json.load(open(os.path.join(SRC, 'aion2timers_genus_insight_25800038.json'), encoding='utf-8'))
Q = json.load(open(os.path.join(SRC, 'questlog_genus_slots.json'), encoding='utf-8'))['result']['data']
COMM = json.load(open(os.path.join(SRC, 'questlog_global_build_counts.json'), encoding='utf-8'))

# ---------------------------------------------------------------- 1. verify the two datamines agree, slot by slot
GRADE_CODE = {11: 'common', 21: 'rare', 31: 'epic', 41: 'unique', 51: 'heroic'}
for q in Q:
    a = next(g for g in A['genus'] if g['id'] == q['id'])
    for s in range(1, 10):
        qs = sorted((GRADE_CODE[o['grade']], o['statId'], o['minValue'], o['maxValue'], o['probability']) for o in q['statOptions'][str(s)])
        if qs != sorted(tuple(x) for x in a['slots'][s - 1]):
            sys.exit(f'pool mismatch: {q["id"]} slot {s} -- re-check both sources before publishing')
    if q['slotOpenLevels'] != a['open']:
        sys.exit(f'slot open levels differ for {q["id"]}')
print('45/45 slots identical in the Global client dump and questlog.gg')

S = A['stats']
BOARDS = [('intellect', 'Cogni'), ('feral', 'Fera'), ('nature', 'Natura'), ('trans', 'Varian'), ('special', 'Special')]
GR = ['common', 'rare', 'epic', 'unique', 'heroic']


def fmt(stat, v):
    st = S[stat]
    return (f'{v / 100:.1f}%'.replace('.0%', '%') if st['p'] else str(v))


def name(stat):
    return S[stat]['n']


# ---------------------------------------------------------------- 2. pools (what CAN roll), per board and slot
pools = {}
for gid, gname in BOARDS:
    g = next(x for x in A['genus'] if x['id'] == gid)
    pools[gname] = []
    for s, slot in enumerate(g['slots'], 1):
        by = {}
        for gr, stat, mn, mx, w in slot:
            tot = sum(x[4] for x in slot if x[0] == gr)
            by.setdefault(gr, []).append([name(stat), fmt(stat, mn), fmt(stat, mx), round(100 * w / tot, 1)])
        pools[gname].append({'n': s, 'lines': len(slot), 'by': by})

# ---------------------------------------------------------------- 3. leveling, odds, costs
L = A['levels']['intellect']
assert all(A['levels'][g] == L for g, _ in BOARDS), 'levels differ by genus'
need = [r['need'] for r in L if r['need']]
odds = [[r['lv'], {k: v for k, v in r['odds'].items() if k != 'mythic'}] for r in L]
C = A['cost']['intellect']
assert all(A['cost'][g]['lock'] == C['lock'] and A['cost'][g]['crystal'] == C['crystal'] for g, _ in BOARDS)
PETS = {'Cogni': 41, 'Fera': 65, 'Natura': 48, 'Varian': 46, 'Special': 7}  # aion2guidance.com pets page + questlog pet list
PET_XP = sum(A['petExp'])  # 500 + 250 + 250 per pet taken to level 3 (Global max)


def analyses_to(level_target, start_xp):
    """Analyses (no locks, every open line rerolled) from level 1 with start_xp banked, to reach level_target."""
    lv, ex, n = 1, start_xp, 0
    while lv < level_target:
        r = need[lv - 1]
        if ex >= r:
            ex -= r; lv += 1; continue
        per = 100 * lv  # 100 Insight XP per open, unlocked line; line N opens at level N
        k = math.ceil((r - ex) / per)
        n += k; ex += k * per - r; lv += 1
    return n


plan = {}
for _, b in BOARDS:
    px = 0 if b == 'Special' else PETS[b] * PET_XP
    plan[b] = {'pets': PETS[b], 'petXp': px, 'to9': analyses_to(9, px), 'to10': analyses_to(10, px)}
    plan[b]['crystals10'] = plan[b]['to10'] * C['crystal']
    plan[b]['kinah10'] = plan[b]['to10'] * C['gold']


def p_line(board, slot, stat, grades=('heroic',)):
    """Chance per analysis at Insight 10 that this line rolls `stat` at one of `grades`."""
    g = next(x for x in A['genus'] if x['id'] == dict((v, k) for k, v in BOARDS)[board])
    sl = g['slots'][slot - 1]
    lv10 = L[-1]['odds']
    p = 0.0
    for gr in grades:
        tot = sum(x[4] for x in sl if x[0] == gr)
        w = sum(x[4] for x in sl if x[0] == gr and x[1] == stat)
        if tot: p += lv10[gr] / 100 * w / tot
    return p


chase = []
for label, b, s, st in [('Double Chance on Special 4', 'Special', 4, 'hardhit'), ('PvE Damage Boost on any other slot 4', 'Cogni', 4, 'pveamplifydamage'),
                         ('Max Attack on a slot 1 or 5', 'Cogni', 1, 'weapondamage'), ('Critical Hit on a slot 3, 6 or 9', 'Cogni', 3, 'critical'),
                         ('Power Shard Damage Bonus on a slot 3, 6 or 9', 'Cogni', 3, 'sealstoneadddamage'),
                         ('PvE Damage Tolerance on slot 7', 'Cogni', 7, 'pvedecreasedamage'), ('HP increase on a slot 2 or 8', 'Cogni', 2, 'maxhpratio')]:
    ph = p_line(b, s, st, ('heroic',)); pu = p_line(b, s, st, ('unique', 'heroic')); pe = p_line(b, s, st, ('epic', 'unique', 'heroic'))
    chase.append([label, round(1 / ph), round(1 / pu), round(1 / pe) if pe > pu else None])

# ---------------------------------------------------------------- 4. the value model (Global, documented assumptions)
# Kanon's damage formula (Aion 2 Bible, Oct 4 Global update):
#   ((PureAtk x WDB x MultiHit x PowerShard + AttackBonus) x AttackIncrease + PvE/Boss Atk ...) x SkillCoef ...
#   x (1 + DamageBoost + PvE DB + Boss DB + species DB) x CritFactor x Double x (1 + Front/Back DB)
# Global bucket sizes from a Ludra-ready Global Ranger plan (Whelps, questlog.gg, Oct 12): Damage Boost 44.9% + PvE DB 27.5%,
# Weapon Damage Boost 27.4%, Crit Damage Boost 15.2%, Double Chance 18.8%, Front ADB 2%; plus ~22.5% from a Chanter's mantra.
M_DB = (0.51, 0.69)        # value of +1% Damage Boost / PvE Damage Boost: 1/(1.95) with no boss resist, 1/(1.45) if bosses resist 50%
M_W = (0.62, 0.72)         # +1% Weapon Damage Boost: ~85% of attack is weapon-scaled, divided by a WDB total of ~118-137%
CRIT_MULT = 1.5 + 0.30 - 0.25   # base 150% crit + ~30% crit damage (class passives) - 25% boss crit-damage resist (Korean value)
CRIT_PER_POINT = 0.06      # % crit chance per Critical Hit point below the cap (Kanon: same curve as Accuracy, ~6-7% per 100)
MH_VALUE = 0.33            # +1% Multi-hit ~ 0.33% damage (Kanon, Korean endgame; not measured on Global)
PERF_VALUE = 0.10          # +1% Perfect ~ 0.1% (Kanon)
FLAT = {'Max Attack': 0.019, 'Attack Bonus': 0.0145, 'PvE Attack': 0.0115, 'Boss Attack': 0.0115}  # % damage per point (Kanon's ratios x ~1.4 for smaller Global totals)

# Per-class inputs from top Global boss parses (NotMeter, week of Oct 7, 2026; ~1,500 parses per class):
#   crit = overall crit rate; ng = crit rate of skills that are not guaranteed to crit (the stat-driven part, vs the 50% Global cap);
#   front/back = share of hits; dbl = Double Chance procs per hit; procs = what else crits trigger.
PROF = {
 'gladiator':   {'crit': .64, 'ng': 51, 'front': .77, 'back': .12, 'dbl': .17, 'procs': '', 'role': 'melee, front'},
 'templar':     {'crit': .40, 'ng': 28, 'front': .77, 'back': .12, 'dbl': .13, 'procs': '', 'role': 'melee tank, front'},
 'assassin':    {'crit': .69, 'ng': 53, 'front': .08, 'back': .85, 'dbl': .124, 'procs': 'Heart Gore triggers on crits', 'role': 'melee, back'},
 'ranger':      {'crit': .51, 'ng': 51, 'front': .37, 'back': .39, 'dbl': .135, 'procs': "Hunter's Soul procs on crits", 'role': 'ranged'},
 'sorcerer':    {'crit': .44, 'ng': 32, 'front': .31, 'back': .28, 'dbl': .124, 'procs': '', 'role': 'ranged caster'},
 'spiritmaster': {'crit': .46, 'ng': 46, 'front': .36, 'back': .40, 'dbl': .129, 'procs': 'Corrode procs on crits', 'role': 'ranged caster with spirits'},
 'cleric':      {'crit': .39, 'ng': 38, 'front': .34, 'back': .42, 'dbl': .143, 'procs': 'Condemnation resets its cooldown on a crit', 'role': 'ranged healer'},
 'chanter':     {'crit': .50, 'ng': 44, 'front': .15, 'back': .71, 'dbl': .148, 'procs': "Wind's Promise procs on crits", 'role': 'melee/ranged support, mostly behind'},
}
EN = {'gladiator': 'Gladiator', 'templar': 'Templar', 'assassin': 'Assassin', 'ranger': 'Ranger', 'sorcerer': 'Sorcerer',
      'spiritmaster': 'Spiritmaster', 'cleric': 'Cleric', 'chanter': 'Chanter'}


def crit_factor(c):
    return c * CRIT_MULT + (1 - c)


def v_slot4(cls, stat, pct):
    """Estimated % damage from `pct`% of a slot-4 stat (low, high) for this class in PvE."""
    p = PROF[cls]
    if stat in ('PvE Damage Boost', 'Damage Boost'):
        return (pct * M_DB[0], pct * M_DB[1])
    if stat == 'Weapon Damage Boost':
        return (pct * M_W[0], pct * M_W[1])
    if stat == 'Critical Damage Boost':
        v = pct * p['crit'] / crit_factor(p['crit']); return (v, v)
    if stat == 'Double Chance':
        v = pct / (1 + p['dbl']); return (v * .97, v)
    if stat in ('Front Attack Damage Boost', 'Back Attack Damage Boost'):
        u = p['front'] if stat.startswith('Front') else p['back']
        return (pct * u / (1 + u * .10), pct * u / (1 + u * .02))
    if stat == 'Multi-hit Chance':
        return (pct * MH_VALUE * .8, pct * MH_VALUE * 1.2)
    if stat == 'Perfect Chance':
        return (pct * PERF_VALUE, pct * PERF_VALUE * 1.5)
    return (0, 0)


def crit_line_value(cls, points=30):
    p = PROF[cls]
    head = max(0, 50 - p['ng'])
    gain = min(points * CRIT_PER_POINT, head)
    return gain * (CRIT_MULT - 1) / crit_factor(p['crit'])


def rng(v):
    lo, hi = v
    return f'+{lo:.1f}%' if abs(hi - lo) < .15 else f'+{lo:.1f}–{hi:.1f}%'


# ---------------------------------------------------------------- 5. recommendations
HEROIC_MAX = {'Double Chance': 3.0, 'PvE Damage Boost': 4.0, 'Damage Boost': 3.0, 'Weapon Damage Boost': 3.0, 'Critical Damage Boost': 3.0,
              'Front Attack Damage Boost': 3.0, 'Back Attack Damage Boost': 3.0, 'Multi-hit Chance': 3.0, 'Perfect Chance': 3.0}
SIG = {'Cogni': ['PvE Damage Boost', 'Damage Boost', 'Critical Damage Boost'], 'Fera': ['PvE Damage Boost', 'Weapon Damage Boost', 'Damage Boost'],
       'Natura': ['PvE Damage Boost', 'Multi-hit Chance', 'Perfect Chance'], 'Varian': ['PvE Damage Boost', 'Front Attack Damage Boost', 'Back Attack Damage Boost'],
       'Special': ['Double Chance', 'Damage Boost', 'Front Attack Damage Boost', 'Back Attack Damage Boost', 'Critical Damage Boost']}
TARGET = {'Double Chance': '≥2.3%', 'PvE Damage Boost': '≥3.0%', 'Damage Boost': '≥2.3%', 'Weapon Damage Boost': '≥2.3%', 'Critical Damage Boost': '≥2.3%',
          'Front Attack Damage Boost': '≥2.3%', 'Back Attack Damage Boost': '≥2.3%', 'Multi-hit Chance': '≥2.3%'}
SPECIES = {'Cogni': 'Cogni Damage Boost', 'Fera': 'Fera Damage Boost', 'Natura': 'Natura Damage Boost', 'Varian': 'Varian Damage Boost'}


def comm(board, slot):
    c = COMM.get(f'{board}|{slot}', {})
    t = sum(c.values())
    return ', '.join(f'{k} {round(100 * v / t)}%' for k, v in sorted(c.items(), key=lambda kv: -kv[1])[:3]) if t else ''


def L_(slot, best, alt, grade, target, prio, tag, why, conf, est=''):
    return {'s': slot, 'best': best, 'alt': alt, 'grade': grade, 'target': target, 'prio': prio, 'tag': tag, 'why': why, 'conf': conf, 'est': est}


def slot4_pve(cls, board, build):
    cands = [(st, v_slot4(cls, st, HEROIC_MAX[st])) for st in SIG[board]]
    cands.sort(key=lambda x: -(x[1][0] + x[1][1]))
    (b, bv), (a, av) = cands[0], cands[1]
    DBF = ('PvE Damage Boost', 'Damage Boost')  # one additive bucket: compare them under the same assumption

    def tie(x, xv, y, yv):
        if x in DBF and y in DBF:
            return min(xv[0], yv[0]) / max(xv[0], yv[0]) >= 0.9
        # different buckets: tied if the runner-up comes within 10% of the leader in any low/high combination
        return max(yv[i] / xv[j] for i in (0, 1) for j in (0, 1)) >= 0.9 and max(xv[i] / yv[j] for i in (0, 1) for j in (0, 1)) >= 0.9
    # the runner-up worth naming is the best stat from a different bucket, if one is close
    others = [(st, v) for st, v in cands[1:] if not (b in DBF and st in DBF)]
    if others and tie(b, bv, *others[0]):
        a, av = others[0]
    tied = tie(b, bv, a, av)
    p = PROF[cls]
    if board == 'Special':
        why = (f"Double Chance doubles a hit outright and sits in its own multiplier. Your hits double ~{round(p['dbl'] * 100)}% of the time on Global, "
               f"so a max roll (3%) is worth about {rng(bv)} damage, more than any other stat in the system. On Global it rolls ONLY here "
               f"(Korea's slots 3 and 9 Double Chance doesn't exist on this client). {a} is next at about {rng(av)}.")
        return L_(4, b, a, 'Heroic', TARGET[b], 1, 'BiS', why, 'High', rng(bv))
    if b == 'PvE Damage Boost':
        why = (f"PvE Damage Boost rolls higher (Heroic 2.0–4.0%) than every other damage line here (1.5–3.0%), and Global characters' "
               f"Damage Boost total is still small (~70–95% with a Chanter), so each 1% is worth ~0.5–0.7%. A max roll ≈ {rng(bv)}; ")
        if a == 'Critical Damage Boost' or 'Critical Damage Boost' in [c[0] for c in cands]:
            cv = next(v for st, v in cands if st == 'Critical Damage Boost')
            why += f"Critical Damage Boost (3%) only ≈ {rng(cv)} for you because only ~{round(p['crit'] * 100)}% of your hits crit. "
        if tied:
            why += (f"{a} (≈ {rng(av)}) is close enough to count as a tie: keep whichever lands high first. "
                    f"{a} pulls ahead as your Damage Boost total grows toward Korea's ~180%, which is why Korean guides rank it first.")
        else:
            why += f"{a} is next at ≈ {rng(av)}."
        if board in SPECIES:
            why += f" {SPECIES[board]} (2.4–4.8%) beats both, but only against {board} monsters."
        return L_(4, b + (f' ≈ {a}' if tied else ''), a, 'Heroic', TARGET[b], 2, 'BiS', why, 'Medium' if tied else 'High', rng(bv))
    # a positional stat or WDB came out on top
    why = (f"For a class landing ~{round((p['front'] if 'Front' in b else p['back']) * 100)}% of hits from that side, {b} (own multiplier, starts near 0 on Global) "
           f"≈ {rng(bv)} for a max roll vs PvE Damage Boost ≈ {rng(next(v for st, v in cands if st == 'PvE Damage Boost'))}.")
    return L_(4, b + (f' ≈ {a}' if tied else ''), a, 'Heroic', TARGET.get(b, ''), 2, 'BiS', why, 'Medium', rng(bv))


def lines_pve(cls, board, build):
    p = PROF[cls]
    tank = build == 'tank'; heal = build == 'healer'
    out = []
    # slots 1 and 5
    for s in (1, 5):
        out.append(L_(s, 'Max Attack', 'Attack Bonus · PvE Attack', 'Heroic', '≥15', 4 if (tank or heal) else 3, 'BiS',
                      "Max Attack (Heroic 10–20) raises your weapon's top roll, which Weapon Damage Boost then multiplies: the best flat attack stat per point "
                      "in Kanon's formula. Attack Bonus (8–16) is next; PvE Attack (10–20) ties it on bosses and also works on trash, Boss Attack only on bosses. "
                      "Front/Back Attack and Critical Attack only count from one side or on crits. " + (f"Global builds: {comm(board, s)}." if comm(board, s) else ''),
                      'High', '+0.3–0.4%'))
    # slots 2 and 8
    for s in (2, 8):
        if tank or heal:
            out.append(L_(s, 'HP increase', 'Boss Defense · PvE Defense', 'Unique+', '≥1.2%', 3, 'BiS',
                          'Every option on this line is defensive. HP increase (Heroic 0.8–1.6% max HP) helps in every fight. Flat Defense lines barely matter on bosses '
                          '(Defense removes only 10% of its value from each hit, per Kanon); Boss/PvE Defense values are not documented (Unverified).', 'Medium'))
        else:
            out.append(L_(s, 'HP increase', 'any (don’t lock)', 'any', '—', 5, 'Low priority',
                          'No damage stat can roll here (all 45–60 options are HP, MP, defense or crit resist). HP increase is the only one worth keeping; '
                          f'never spend a lock on this line. Global builds: {comm(board, s)}.', 'High'))
    # slots 3, 6, 9
    capped = p['ng'] >= 49
    near = 43 <= p['ng'] < 49
    cv = crit_line_value(cls)
    for s in (3, 6, 9):
        if tank and not capped:
            out.append(L_(s, 'Critical Hit', 'Block (raid tanking) · Front Attack Critical Hit', 'Heroic', '≥23', 3, 'BiS',
                          f"Your skills that don't auto-crit land crits only ~{p['ng']}% of the time, well under Global's 50% stat cap, so Critical Hit still adds "
                          f"≈ +{cv:.1f}% per max line. Front Attack Critical Hit (20–40) ties it at your 77% front uptime. For a main tank, Block (25–50) is the "
                          "survival pick: more blocks, and Fury gives your party +5.5% PvE damage on each block.", 'Medium', f'+{cv:.1f}%'))
        elif capped:
            out.append(L_(s, 'Power Shard Damage Bonus', 'PvE Accuracy (only if bosses parry you)', 'Heroic', '≥12', 4, 'BiS',
                          f"Top Global {EN[cls]}s already sit at the 50% stat crit cap (skills without guaranteed crits: {p['ng']}%) and bosses parry them ~0% "
                          "on current dungeons, so Critical Hit and Accuracy add nothing here. Power Shard Damage Bonus (8–16) is the only damage stat left on the "
                          "line and Kanon's Global pick once caps are met; its exact value per point isn't published (magnitude Unverified). If your meter shows "
                          f"parries or blocks, take PvE Accuracy (25–50) until it doesn't. Global builds: {comm(board, s)}.", 'Medium'))
        elif near:
            out.append(L_(s, 'Critical Hit → Power Shard Damage Bonus', 'PvE Accuracy (only if parried)', 'Heroic', '≥23', 3, 'Conditional',
                          f"Your skills without guaranteed crits crit ~{p['ng']}% on Global, a few points under the 50% cap: take Critical Hit (15–30, ≈ +{cv:.1f}% per max line) "
                          "on a couple of these lines until the meter shows ~50% on those skills, then switch the rest to Power Shard Damage Bonus. "
                          + (f"Crits also feed you: {p['procs']}." if p['procs'] else ''), 'Medium', f'+{cv:.1f}%'))
        else:
            extra = f" Crits also matter more for you: {p['procs']}." if p['procs'] else ''
            pos = ''
            if max(p['front'], p['back']) >= .75:
                pos = f" Front/Back Attack Critical Hit (20–40) ties it at your {round(max(p['front'], p['back']) * 100)}% uptime from that side."
            out.append(L_(s, 'Critical Hit', 'PvE Accuracy (only if parried)', 'Heroic', '≥23', 2 if cv > .4 else 3, 'BiS',
                          f"Your skills without guaranteed crits crit only ~{p['ng']}% on Global, well under the 50% stat cap, so Critical Hit (15–30) still adds "
                          f"≈ +{cv:.1f}% damage per max line.{pos}{extra} Switch to Power Shard Damage Bonus once those skills reach ~50% crit.", 'Medium', f'+{cv:.1f}%'))
    # slot 4
    out.append(slot4_pve(cls, board, build))
    # slot 7
    if board == 'Special':
        out.append(L_(7, 'Damage Tolerance', 'Endurance', 'Unique+', '≥2.0%', 3 if (tank or heal) else 4, 'BiS',
                      'Special has no PvE Damage Tolerance; Damage Tolerance (1.5–3%) cuts the damage boost of every hit you take. Endurance (1.5–3%) is the chance to take '
                      'half damage. Double Resist, Front/Back and Critical Damage Tolerance only matter against players. ' + (f'Global builds: {comm(board, 7)}.' if comm(board, 7) else ''), 'Medium'))
    else:
        useless = {'Cogni': 'Critical Damage Tolerance', 'Fera': 'Weapon Damage Tolerance', 'Natura': 'Multi-hit Resist / Perfect Resist', 'Varian': 'Front/Back Attack Damage Tolerance'}[board]
        offense = '' if (tank or heal or p['ng'] >= 49) else f" Max-damage option: Critical Hit (15–30) also rolls here and adds ≈ +{cv:.1f}% while you're under the crit cap, if you rarely die."
        out.append(L_(7, 'PvE Damage Tolerance', 'Damage Tolerance (also works in PvP)', 'Unique+', '≥3.0%', 2 if tank else (3 if heal else 4), 'BiS',
                      f"PvE Damage Tolerance (2.0–4.0%) out-rolls Damage Tolerance (1.5–3.0%) against monsters. {useless} does nothing in PvE: bosses have no "
                      f"Front/Back, Weapon, Critical or Multi-hit damage stats (Kanon).{offense}" + (f' Global builds: {comm(board, 7)}.' if comm(board, 7) else ''), 'Medium'))
    out.sort(key=lambda x: x['s'])
    return out


def lines_pvp(cls, board):
    p = PROF[cls]
    out = []
    for s in (1, 5):
        out.append(L_(s, 'Max Attack', 'Attack Bonus', 'Heroic', '≥15', 3, 'BiS',
                      'Max Attack and Attack Bonus are the only attack lines that work on players: PvE Attack and Boss Attack do nothing in PvP, and Penetration '
                      'barely matters (Defense removes only 1% of its value in PvP, per Kanon).', 'Medium', ''))
    for s in (2, 8):
        out.append(L_(s, 'HP increase', 'Critical Hit Resist · Back Attack Critical Hit Resist (vs Assassins)', 'Unique+', '≥1.2%', 3, 'BiS',
                      'Defensive line. HP increase helps against everyone; Critical Hit Resist (15–30) and Back Attack Critical Hit Resist (20–40) cut enemy crits '
                      'if one class keeps killing you. PvP resist values per point are not published (Low confidence).', 'Low'))
    for s in (3, 6, 9):
        out.append(L_(s, 'Accuracy Bonus', 'Critical Hit · Evasion Bonus (defensive)', 'Heroic', '≥30', 3, 'Conditional',
                      'Players stack Evasion and Block, so Accuracy (20–40) is what lands your hits; PvE Accuracy does nothing in PvP. Once your hits stop missing, '
                      "Critical Hit. Evasion (15–30) is the defensive choice. PvP caps aren't published (Low confidence).", 'Low'))
    pvp4 = {
        'Cogni': ('Damage Boost', 'Critical Damage Boost · Endurance Penetration', 'Damage Boost (1.5–3%) works on players; PvE Damage Boost does not. Critical Damage Boost is the alternative for crit-heavy classes; Endurance Penetration (1.5–3%) counters players who stack Endurance (the 50%-damage proc).'),
        'Fera': ('Weapon Damage Boost', 'Damage Boost', 'Weapon Damage Boost has its own multiplier and works on players; PvE Damage Boost does not.'),
        'Natura': ('Multi-hit Chance', 'Status Effect Chance (CC builds)', 'Multi-hit is the damage pick that works on players. Status Effect Chance (1.5–3%) makes your stuns, roots and freezes land more often against resist-stacked players.'),
        'Varian': ('Back Attack Damage Boost' if cls == 'assassin' else 'Front Attack Damage Boost', 'Back Attack Damage Boost' if cls != 'assassin' else 'Front Attack Damage Boost',
                   'Positional damage boost works on players. ' + ('Assassins land most PvP hits from behind.' if cls == 'assassin' else 'Most PvP hits land from the front unless you flank; take Back if you play behind targets.')),
        'Special': ('Double Chance', 'Damage Boost · Endurance Penetration', 'Double Chance still doubles hits on players (they can stack Double Resist against it); Damage Boost is the safe alternative.'),
    }[board]
    out.append(L_(4, pvp4[0], pvp4[1], 'Heroic', '≥2.3%', 1 if board == 'Special' else 2, 'BiS', pvp4[2] + ' Player-side resist stats make PvP values uncertain.', 'Medium' if board == 'Special' else 'Low'))
    pvp7 = {
        'Cogni': ('Damage Tolerance', 'Critical Damage Tolerance', 'Damage Tolerance cuts every player hit; Critical Damage Tolerance only crits. PvE Damage Tolerance does nothing in PvP.'),
        'Fera': ('Damage Tolerance', 'Weapon Damage Tolerance', 'Damage Tolerance cuts every hit; Weapon Damage Tolerance counters the enemy Weapon Damage Boost.'),
        'Natura': ('Damage Tolerance', 'Multi-hit Resist', 'Damage Tolerance cuts every hit; Multi-hit Resist removes enemy extra hits.'),
        'Varian': ('Damage Tolerance', 'Back Attack Damage Tolerance (vs Assassins)', 'Damage Tolerance cuts every hit; Back Attack Damage Tolerance counters flankers.'),
        'Special': ('Double Resist', 'Damage Tolerance', 'Double Resist (1.5–3%) cuts enemy Double Chance, the strongest offensive stat in the game; Damage Tolerance is the all-round alternative.'),
    }[board]
    out.append(L_(7, pvp7[0], pvp7[1], 'Unique+', '≥2.0%', 2, 'BiS', pvp7[2] + ' (Low confidence: PvP stat totals are not public.)', 'Low'))
    out.sort(key=lambda x: x['s'])
    return out


def ranking(cls, build, boards):
    p = PROF[cls]
    if build == 'pvp':
        return [['Special slot 4 (Double Chance)', ''], ['Slot 4 on the other four boards', ''], ['Slot 7 on all five (Damage Tolerance / Double Resist)', ''],
                ['Slots 1 and 5 (Max Attack)', ''], ['Slots 3, 6, 9 (Accuracy until hits land)', ''], ['Slots 2 and 8 (HP increase)', '']]
    sp = next(x for x in boards['Special'] if x['s'] == 4)
    others = [next(x for x in boards[b] if x['s'] == 4) for b in ('Cogni', 'Fera', 'Natura', 'Varian')]
    r = [[f"Special slot 4: {sp['best']}", sp['est']]]
    r += [[f"{b} slot 4: {x['best']}", x['est']] for b, x in zip(('Cogni', 'Fera', 'Natura', 'Varian'), others)]
    cv = crit_line_value(cls)
    if build == 'tank':
        r += [['Slot 7 on all five boards (PvE Damage Tolerance / Damage Tolerance)', 'survival'], ['Slots 2 and 8 (HP increase)', 'survival']]
    if p['ng'] < 49 and cv > 0.4:
        r += [['Slots 3, 6, 9: Critical Hit (15 lines)', f'+{cv:.1f}% each'], ['Slots 1 and 5: Max Attack (10 lines)', '+0.3–0.4% each']]
    else:
        r += [['Slots 1 and 5: Max Attack (10 lines)', '+0.3–0.4% each'], ['Slots 3, 6, 9: ' + ('Critical Hit to the cap, then Power Shard Damage Bonus' if p['ng'] < 49 else 'Power Shard Damage Bonus') + ' (15 lines)', 'Unverified' if p['ng'] >= 49 else f'+{cv:.1f}% each to the cap']]
    if build != 'tank':
        r += [['Slot 7 on all five boards (PvE Damage Tolerance / Damage Tolerance)', 'survival'], ['Slots 2 and 8 (HP increase, never lock)', 'survival']]
    return r


BUILDS = {
 'gladiator': [('pve', 'PvE damage (bosses and dungeons)'), ('pvp', 'PvP (community build)')],
 'templar': [('pve', 'PvE damage / off-tank'), ('tank', 'PvE main tank (raids)'), ('pvp', 'PvP (community build)')],
 'assassin': [('pve', 'PvE damage (bosses and dungeons)'), ('pvp', 'PvP (community build)')],
 'ranger': [('pve', 'PvE damage (bosses and dungeons)'), ('pvp', 'PvP (community build)')],
 'sorcerer': [('pve', 'PvE damage (bosses and dungeons)'), ('pvp', 'PvP (community build)')],
 'spiritmaster': [('pve', 'PvE damage (bosses and dungeons)'), ('pvp', 'PvP (community build)')],
 'cleric': [('healer', 'PvE healer (with damage between heals)'), ('pvp', 'PvP (community build)')],
 'chanter': [('pve', 'PvE damage and support (buffs are unaffected by Genus)'), ('pvp', 'PvP (community build)')],
}

classes = {}
for cls, builds in BUILDS.items():
    p = PROF[cls]
    out = []
    for bid, bname in builds:
        boards = {b: (lines_pvp(cls, b) if bid == 'pvp' else lines_pve(cls, b, bid)) for _, b in BOARDS}
        capped = p['ng'] >= 49
        caps = [f"Stat crit cap on Global: 50% (Kanon, Oct 4). Your skills without guaranteed crits: ~{p['ng']}% for top Global players → " +
                ('capped: Critical Hit lines add nothing.' if capped else f'about {50 - p["ng"]} points of headroom, so Critical Hit still pays.'),
                'Accuracy: top Global players are parried ~0% on current dungeons (NotMeter parses). Projected Ludra needs ~1,200 (Kanon, aion2guidance; unconfirmed). Take PvE Accuracy on 3/6/9 only while your meter shows parries or blocks.',
                'Slot 4 values assume Global-scale totals (Damage Boost + PvE ≈ 70–95% with a Chanter, Weapon Damage Boost ≈ 27%). As Damage Boost climbs toward Korea\'s ~180%, Weapon/positional/crit-damage boosts overtake PvE Damage Boost.',
                f"Positioning: you land ~{round(p['front'] * 100)}% of hits from the front and ~{round(p['back'] * 100)}% from behind (top Global parses)."]
        if cls == 'spiritmaster':
            caps.append('Spirits: about a third of Spiritmaster damage comes from spirits. Whether your Genus stats carry over to them is not documented (Unverified), so every offensive line may be worth up to a third less than shown.')
        if cls == 'chanter':
            caps.append('Mantras and Power of the Storm are flat buffs; no Genus line changes what they give your party.')
        if bid == 'healer':
            caps.append('No Genus stat raises healing directly. Whether heals scale with Attack is not documented (Unverified), so this build keeps damage lines and moves survival lines up.')
        conf = 'Medium' if bid != 'pvp' else 'Low'
        out.append({'id': bid, 'name': bname,
                    'role': p['role'],
                    'profile': f"Crit {round(p['crit'] * 100)}% overall, {p['ng']}% on skills without guaranteed crits; {round(p['front'] * 100)}% front / {round(p['back'] * 100)}% back hits; doubles {round(p['dbl'] * 100)}%." + (f" {p['procs']}." if p['procs'] else ''),
                    'boards': boards, 'rank': ranking(cls, bid, boards), 'caps': caps, 'conf': conf,
                    'budget': ('Before Insight 10 never lock. At 10, chase Special slot 4 first (a Unique Double Chance, 1.0–2.0%, is a fine budget target; even Epic 0.5–1.5% beats any other stat), then slot 4 on the other boards at Unique (PvE Damage Boost 1.5–3.0%). Keep whatever unlocked rolls give on the other lines.'
                               if bid != 'pvp' else 'Same order as PvE: Special slot 4 first, then the other slot 4s, then slot 7. Keep a separate PvP preset (3 presets) instead of rerolling your PvE lines.'),
                    'endgame': ('Heroic slot 4s in the top half of the range (Double Chance ≥2.3%, PvE Damage Boost ≥3.0%), then Heroic Max Attack ≥15 on slots 1/5 and your 3/6/9 pick, locking one line at a time.'
                                if bid != 'pvp' else 'Heroic slot 4 and slot 7 on every board, then Max Attack on 1/5.')})
    classes[cls] = out

out = {
 'meta': {'updated': '2026-10-13', 'client': A['build'], 'clientNote': 'AION 2 Global client build 25800038 (Steam update of Oct 1, 2026). Global patches since (Oct 6, Oct 8) did not touch Pets / Genus Insight.',
          'sources': [
            ['Global client tables via Aion 2 Timers Genus Insight tool', 'https://www.aion2timers.com/insight/'],
            ['questlog.gg Genus Insight data (45/45 slots identical) and public Global builds', 'https://questlog.gg/aion-2/en/character-builder'],
            ["Kanon's Aion 2 Bible (Oct 4 Global update): damage formula, stat values, Global Genus steps", 'https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview'],
            ['aion2guidance.com pets page (Global): pets, souls, owned effects, crystals', 'https://www.aion2guidance.com/en/pets/'],
            ['Inven KR pet guide (Jan 14, 2026): Korean slot layout, for comparison', 'https://www.inven.co.kr/board/aion2/6444/1077'],
            ['NotMeter top Global parses (week of Oct 7): crit, positional and parry rates per class', 'https://notmeter.com/'],
            ["Whelps' Ludra-ready Global Ranger plan (questlog): Global stat totals", 'https://questlog.gg/aion-2/en/character-builder/AelonCommandAndTheSharpMerchant?build-id=8655']],
          'model': ['Damage formula: Kanon (Bible, Oct 4).', f'+1% Damage Boost / PvE Damage Boost ≈ {M_DB[0]}–{M_DB[1]}% damage on Global.', f'+1% Weapon Damage Boost ≈ {M_W[0]}–{M_W[1]}%.',
                    '+1% Critical Damage Boost ≈ crit rate ÷ (crit rate × 1.55 + non-crit share): 0.35–0.45% for most classes.', '+1% Double Chance ≈ 1 ÷ (1 + your double rate) ≈ 0.87–0.89%.',
                    '+1% Front/Back Damage Boost ≈ your share of hits from that side.', 'Critical Hit: ~0.06% crit chance per point below the 50% cap.',
                    'Multi-hit +1% ≈ 0.33%, Perfect +1% ≈ 0.1% (Kanon, Korean values).', 'Flat attack per point: Max Attack ≈ 0.019%, Attack Bonus ≈ 0.0145%, PvE/Boss Attack ≈ 0.0115%.']},
 'layout': [
   [1, 'Attack', 'Max Attack, Attack Bonus, PvE / Boss / Front / Back / Critical Attack, Penetration, HP, MP'],
   [2, 'Defense', 'HP increase %, Defense Bonus, PvE / Boss / Front / Back Defense, Critical Damage Defense, Critical Hit Resist (+ front/back), HP, MP'],
   [3, 'Crit / accuracy', 'Critical Hit, Front / Back Attack Critical Hit, Accuracy Bonus, PvE Accuracy, Power Shard Damage Bonus, Block, Evasion, HP, MP'],
   [4, 'Damage boost', 'Cogni: Critical Damage Boost · Fera: Weapon Damage Boost · Natura: Multi-hit, Perfect · Varian: Front / Back Attack Damage Boost · all four: PvE Damage Boost 2–4%, Damage Boost (Cogni/Fera), own-genus Damage Boost 2.4–4.8% · Special: Double Chance, Damage Boost, Critical / Front / Back Damage Boost (no PvE Damage Boost)'],
   [5, 'Attack', 'same pool as slot 1'],
   [6, 'Crit / accuracy', 'same pool as slot 3'],
   [7, 'Tolerance', 'PvE Damage Tolerance 2–4%, Damage Tolerance, Endurance, Regeneration, Status Effect Resist, own-genus tolerance (Cogni: Critical Damage Tolerance · Fera: Weapon Damage Tolerance · Natura: Multi-hit / Perfect Resist · Varian: Front / Back Attack Damage Tolerance) · Special: Double Resist instead of PvE Damage Tolerance'],
   [8, 'Defense', 'same pool as slot 2'],
   [9, 'Crit / accuracy', 'same pool as slot 3']],
 'kr': [['1 · 4 · 7', 'Defense'], ['2 · 5 · 8', 'Attack'], ['3 · 9', 'Damage boosts incl. Double Chance (up to 2.4% each)'], ['6', 'Tolerance']],
 'odds': odds, 'need': need, 'perLine': 100, 'petExp': A['petExp'], 'plan': plan,
 'cost': {'crystal': C['crystal'], 'kinah': C['gold'], 'lock': C['lock'], 'lockKinah': C['lockGold']},
 'chase': chase,
 'pools': pools,
 'owned': [['Cogni', 41, 'Might +41, Max HP +1,230, Critical Hit +82'], ['Fera', 65, 'Dexterity +65, Accuracy +130'],
           ['Natura', 48, 'Precision +48, Critical Hit Resist +96'], ['Varian', 46, 'Constitution +46, Evasion +92'], ['Special', 7, 'none']],
 'community': {'n': 132, 'slot4': {b: comm(b, 4) for _, b in BOARDS}, 'slot7': {b: comm(b, 7) for _, b in BOARDS}, 's3': comm('Cogni', 3), 's1': comm('Cogni', 1), 's2': comm('Cogni', 2)},
 'classes': classes,
}
json.dump(out, open(os.path.join(ROOT, 'data', 'genus.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data/genus.json:', sum(len(b['boards']) * 9 for v in classes.values() for b in v), 'line recommendations,', sum(len(v) for v in classes.values()), 'builds')
for b, v in plan.items(): print(' ', b, v)
for c in chase: print(' ', c)
