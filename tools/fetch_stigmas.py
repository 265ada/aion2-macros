"""Refresh data/stigma_db.json: every Stigma skill of the 8 classes from the aion2.app client DB.

Usage (from the repo root):  python tools/fetch_stigmas.py
Keeps hand-maintained fields already in the file (s25 = level-25 specialty from KR/TW, note = KR/TW patch
differences). Downloads any missing icon into icons/. Values are skill level 1 as listed in the Global DB.
"""
import html, json, os, re, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = __file__.rsplit("tools", 1)[0]
OUT = ROOT + "data/stigma_db.json"
CLASSES = {"gladiator": "Gladiator", "templar": "Templar", "assassin": "Assassin", "ranger": "Ranger",
           "sorcerer": "Sorcerer", "spiritmaster": "Elementalist", "cleric": "Cleric", "chanter": "Chanter"}
KEEP = ("s25", "note")


def get(u, binary=False):
    for i in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=30)
            b = r.read()
            return b if binary else b.decode("utf-8")
        except Exception:
            time.sleep(1 + i)
    return b"" if binary else ""


def strip(s):
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def h1(u):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", get(u), re.S)
    return strip(m.group(1)) if m else None


def detail(sid):
    h = get(f"https://aion2.app/db/skills/{sid}")
    kind = re.search(r'<span>\W*<!-- -->(Mastery|Stigma|Passive|Active)</span>', h)
    if not kind or kind.group(1) != "Stigma":
        return None
    specs = []
    for block in re.split(r'<div class="flex items-start gap-2[^"]*"', h)[1:]:
        block = block.split("</span></div>", 1)[0]
        lv = re.search(r'>Level<!-- --> <!-- -->(\d+)</span>', block)
        if lv and strip(block[lv.end():]):
            specs.append([int(lv.group(1)), strip(block[lv.end():])])
    d = re.search(r'<p class="text-sm[^"]*whitespace-pre-line"><span>(.*?)</span></p>', h, re.S)
    icon = re.search(r"/db-item-icons/(ICON_[A-Z]{2}_SKILL_\d{3})\.webp", h)
    return {"id": sid, "en": strip(re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S).group(1)),
            "icon": icon.group(1) if icon else None, "d": strip(d.group(1)) if d else "", "s": specs,
            "m": 1 if re.search(r'whitespace-pre-line mt-2"><span>Mobile</span>', h) else 0}


old = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
out = {"_about": old.get("_about", "")}
for cid, cname in CLASSES.items():
    page = get(f"https://aion2.app/db/skills?class={cname}")
    rows = {}
    for m in re.finditer(r'href="/db/skills/(\d{8})"(.*?)</a>', page, re.S):
        t = strip(re.sub(r"<[^>]+>", " | ", m.group(2)))
        cd = re.search(r"CD ([\d.]+)s", t)
        mp = re.search(r"MP (\d+)", t)
        rows.setdefault(m.group(1), (float(cd.group(1)) if cd else None, int(mp.group(1)) if mp else None))
    with ThreadPoolExecutor(6) as ex:
        found = [x for x in ex.map(detail, rows) if x]
    for s in found:
        s["cls"] = cid
        s["cd"], s["mp"] = rows[s["id"]]
        s["tw"] = h1(f"https://aion2.app/zh/db/skills/{s['id']}")
        s["ko"] = h1(f"https://aion2.app/ko/db/skills/{s['id']}")
        key = f"{cid}:{s['en']}"
        for k in KEEP:
            if old.get(key, {}).get(k):
                s[k] = old[key][k]
        if s["icon"] and not os.path.exists(ROOT + f"icons/{s['icon']}.webp"):
            img = get(f"https://aion2.app/db-item-icons/{s['icon']}.webp", binary=True)
            if img[:4] == b"RIFF":  # the DB serves an HTML page for icons it doesn't have
                open(ROOT + f"icons/{s['icon']}.webp", "wb").write(img)
            else:
                s["icon"] = None  # page shows a lettered stand-in
        out[key] = s
    print(cid, len(found), "stigmas", flush=True)

json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("saved", len(out) - 1)
