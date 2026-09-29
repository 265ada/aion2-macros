"""Add single-source variants found in YouTube guide comments (2026-09-29)."""
import json

ROOT = __file__.rsplit("tools", 1)[0]
p = ROOT + "data/macros.json"
M = json.load(open(p, encoding="utf-8"))
C = {c["id"]: c for c in M["classes"]}
N = None
C["chanter"]["late"]["alts"].insert(1, {
    "t": "Viewer test on the Sep 2 Chanter guide video (single source)",
    "s": ("A commenter on the 43k-view Sep 2 guide by 하구 tested moving Spinning Strike to its own key and pressing it on "
          "cooldown: +1.5–2% DPS. It's the same idea as the Impactful Crush split: stop the Dark Crush openers from overlapping."),
    "macros": [["Dark Crush", "Impactful Crush", "Marchutan's Wrath", "Incandescent Blow"]],
    "hold": ["Onslaught", "Macro key", "Gust Rampage"]})
C["sorcerer"]["late"]["alts"].insert(0, {
    "t": "Sep 17 Sorcerer guide video (신사, 50k views)",
    "s": ("Same three-key setup (skill macro, basic attack, Hellfire key). Viewers point out the author keeps Winter's Shackles "
          "on its own key instead of in the Hellfire line, and a viewer reported +250k DPS and +70 hits/min after copying the "
          "mouse-macro setup."),
    "macros": [["Bittercold Wind", "Blaze", "Firestorm", "Wish of Concentration"]],
    "hold": ["Flame Arrow", "Macro key", "Hellfire key (hold)"]})
open(p, "w", encoding="utf-8").write(json.dumps(M, ensure_ascii=False, indent=1))
print("ok")
