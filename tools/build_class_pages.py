"""Writes the 8 class pages (gladiator.html, templar.html, ...) from one template.

The pages are thin shells: class.js fills them from the JSON files in data/. Re-run this only when the shell
itself changes (nav, header, fonts); content edits go in the JSON files.
Usage: python tools/build_class_pages.py
"""
import html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDER = ["gladiator", "templar", "assassin", "ranger", "sorcerer", "spiritmaster", "cleric", "chanter"]
M = {c["id"]: c for c in json.load(open(os.path.join(ROOT, "data/macros.json"), encoding="utf-8"))["classes"]}
O = json.load(open(os.path.join(ROOT, "data/classes.json"), encoding="utf-8"))["classes"]

SECTIONS = [("overview", "Overview"), ("macros", "Macros"), ("stigmas", "Stigmas"), ("skills", "Skills"),
            ("specs", "Specializations"), ("tiers", "Tier list"), ("gear", "Gear"), ("patches", "Patches")]

TPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{en} · Aion 2 Class Guide</title>
<meta name="description" content="Aion 2 {en} ({tw}): {glance} Macros, Global Season 1 stigmas, skill levels, specializations, gear and patches.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..900&family=Barlow:wght@400;500;600;700&family=Barlow+Condensed:wght@500;600;700&family=Noto+Sans+TC:wght@500;700&display=swap">
<link rel="stylesheet" href="site.css">
</head>
<body data-class="{id}" data-mode="gl">
<div class="wrap">
<nav class="sitenav" aria-label="Classes">
  <a class="home" href="index.html">Home</a>
{nav}
</nav>

<header>
  <h1 id="h1">{en}<span class="tc">{tw}</span></h1>
  <div class="role" id="role">{role}</div>
  <p class="sub" id="glance">{glance}</p>
  <div class="stamp" id="stamp"></div>
  <p class="notice" id="notice" hidden></p>
</header>

<nav class="secnav" id="secnav" aria-label="On this page">
{secnav}
</nav>

<main id="view" style="display:grid;gap:clamp(22px,3vw,36px)"><p class="loading">Loading {en}…</p></main>

<footer>
  <p><b style="color:#fff">How this was checked.</b> Macros come from the newest Korean Inven class guides and the replies under them, checked against Taiwanese guides and in-game screenshots (rows marked “likely” were matched by icon). Global Season 1 stigma builds use what Korean players ran in their own 4-slot, level-20 season, updated for the Global client's balance. Skill names, icons, cooldowns and effects come from the aion2.app game-client database (Global). Every card links its source. Skill icons and names © NC; this is a fan-made reference.</p>
  <p><a href="index.html">← All classes and the basics</a></p>
</footer>
</div>
<script src="class.js" charset="utf-8"></script>
</body>
</html>
"""

def main():
    for cid in ORDER:
        m, o = M[cid], O[cid]
        nav = "\n".join(f'  <a href="{c}.html"{" aria-current=\"page\"" if c == cid else ""}>{M[c]["en"]}<small>{M[c]["tw"]}</small></a>' for c in ORDER)
        sec = "\n".join(f'  <a href="#{a}">{t}</a>' for a, t in SECTIONS)
        page = TPL.format(id=cid, en=m["en"], tw=m["tw"], role=html.escape(m["role"], quote=False), glance=o["glance"].replace('"', "&quot;"), nav=nav, secnav=sec)
        open(os.path.join(ROOT, cid + ".html"), "w", encoding="utf-8", newline="\n").write(page)
        print("wrote", cid + ".html")

if __name__ == "__main__":
    main()
