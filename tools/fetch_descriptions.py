"""Refresh data/descriptions.json from the aion2.app skill database (English).

Usage (from the repo root):  python tools/fetch_descriptions.py
Reads skill IDs from data/skills.json. Values are skill level 1 as listed in the DB.
"""
import html, json, re, sys, time, urllib.request

ROOT = __file__.rsplit("tools", 1)[0]
skills = json.load(open(ROOT + "data/skills.json", encoding="utf-8"))

def strip(s):
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()

def fetch(sid):
    req = urllib.request.Request(f"https://aion2.app/db/skills/{sid}", headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8")

out, fails = {}, []
for name, s in skills.items():
    if name.startswith("_"):
        continue
    try:
        h = fetch(s["id"])
        d = re.search(r'<p class="text-sm[^"]*whitespace-pre-line"><span>(.*?)</span></p>', h, re.S)
        desc = strip(d.group(1)) if d else ""
        mobile = bool(re.search(r'whitespace-pre-line mt-2"><span>Mobile</span>', h))
        specs = []
        for block in re.split(r'<div class="flex items-start gap-2 ">', h)[1:]:
            block = block.split("</div>", 1)[0]
            lv = re.search(r'>Level<!-- --> <!-- -->(\d+)</span>', block)
            if not lv:
                continue
            text = strip(block[lv.end():])
            if text:
                specs.append([int(lv.group(1)), text])
        rng = re.search(r'>Range</span><span[^>]*>([^<]+)</span>', h)
        kind = re.search(r'<span>\W*<!-- -->(Mastery|Stigma)</span>', h)
        req = re.search(r'Required level<!-- --> <!-- -->(\d+)', h)
        out[name] = {"d": desc, "s": specs, "m": 1 if mobile else 0,
                     "r": rng.group(1).strip() if rng else None,
                     "k": kind.group(1) if kind else None,
                     "q": int(req.group(1)) if req else None}
        if not desc:
            fails.append(name + " (no description)")
    except Exception as e:  # keep going; report at the end
        fails.append(f"{name}: {e}")
    time.sleep(0.15)

json.dump({"_about": "English skill descriptions from aion2.app (Global client DB), skill level 1 values. d=description, s=[[unlock level, specialty]], m=castable while moving, r=range, k=Mastery/Stigma, q=required level. Regenerate with tools/fetch_descriptions.py.", **out},
          open(ROOT + "data/descriptions.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(f"saved {len(out)} skills; problems: {fails or 'none'}")
