"""Templar update (2026-09-29): switch late/early to the optimizer's Sep 5 guide (pinned as current after Sep 16)."""
import json, re, urllib.request, html

ROOT = __file__.rsplit("tools", 1)[0]


def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read().decode("utf-8")


S = json.load(open(ROOT + "data/skills.json", encoding="utf-8"))
if "Flash Rampage" not in S:
    sid = "12340000"
    en = get(f"https://aion2.app/db/skills/{sid}")
    ic = re.search(r"/db-item-icons/(ICON_[A-Z]{2}_SKILL_\d{3})\.webp", en).group(1)
    h1 = lambda u: re.sub(r"<[^>]+>", "", html.unescape(re.search(r"<h1[^>]*>(.*?)</h1>", get(u), re.S).group(1))).strip()
    img = urllib.request.urlopen(urllib.request.Request(f"https://aion2.app/db-item-icons/{ic}.webp", headers={"User-Agent": "Mozilla/5.0"})).read()
    open(ROOT + f"icons/{ic}.webp", "wb").write(img)
    S["Flash Rampage"] = {"cls": "templar", "id": sid, "tw": h1(f"https://aion2.app/zh/db/skills/{sid}"),
                          "ko": h1(f"https://aion2.app/ko/db/skills/{sid}"), "cd": None, "mp": None, "icon": ic}
    open(ROOT + "data/skills.json", "w", encoding="utf-8").write(json.dumps(S, ensure_ascii=False, indent=0))

p = ROOT + "data/macros.json"
M = json.load(open(p, encoding="utf-8"))
T = next(c for c in M["classes"] if c["id"] == "templar")
N = None
old = T["late"]
T["late"] = {
    "src": "Inven 9/5 optimizer guide, pinned as current after 9/16 (image-verified)",
    "link": "https://www.inven.co.kr/board/aion2/6438/25862",
    "queue": "Not stated; the 9/16 and 9/17 players disagree (OFF / ON), so test both",
    "macros": [["Judgment", "Warding Strike", "Shield Smite", "Pummel"], ["Annihilate", N, N, N]],
    "keys": [{"label": "Punishment key (hold to charge)", "stack": ["Punishment", "Flash Rampage", N, N]}],
    "hold": ["Vicious Strike", "Macro key", "Punishment key (hold)"],
    "manual": ["Doom Shield", "Noble Armor", "Battlefield Banner", "Empyrean Lord's Punishment", "Taunt", "Shield of Protection"],
    "why": ("Pummel sits in the same line as Judgment. That's what makes your held Vicious Strike cancel straight into Judgment "
            "(the 'Vicious–Judgment' cancel), which the guide's author pinned as the one to use after the Sep 16 patch killed the "
            "Pummel–Judgment cancel. Shield Smite and Warding Strike are shield attacks, so they re-open Judgment (Aug 26 rework). "
            "Annihilate gets its own macro line. Flash Rampage sits above Punishment on the charge key so its stagger cancel fires "
            "on its own."),
    "tip": ("Opener: press Noble Armor, Battlefield Banner and Empyrean Lord's Punishment, full-charge Punishment for the "
            "Executor buff, then rush in. Top-end trick: Doom Shield resets Annihilate, so Annihilate → Doom Shield → Annihilate. "
            "Pummel and Judgment go to 20. Use Shield of Protection every ~20 s or on boss crowd-control mechanics."),
    "patch": old.get("patch", ""),
    "alts": [
        {"t": "Inven 9/16 'current top DPS' post (image-verified)",
         "s": "Doom Shield instead of Shield Smite in row 2, skill queue OFF, and Annihilate and Punishment on their own mouse-macro keys.",
         "macros": [["Judgment", "Warding Strike", "Doom Shield", "Pummel"]], "hold": ["Vicious Strike", "Macro key"]},
        {"t": "Inven 9/17 one-click player",
         "s": ("Doom Shield and Shield Smite both in the line, no Pummel, skill queue ON; a second key "
               "(Annihilate → Noble Armor → Battlefield Banner → Empyrean Lord's Punishment) is mashed. See the Full rotation tab."),
         "macros": [["Judgment", "Warding Strike", "Doom Shield", "Shield Smite"]], "hold": ["Vicious Strike", "Macro key"]},
    ] + [a for a in old.get("alts", []) if "9/19" in a.get("t", "")],
}
E = T["early"]
E["macros"] = [["Judgment", "Warding Strike", "Shield Smite", "Pummel"]]
E["manual"] = ["Doom Shield", "Punishment", "Taunt", "Annihilate"]
E["why"] = ("The same line the late-game guide uses, and every skill in it is learned early (Doom Shield is a level-22 stigma, "
            "so it stays manual). With one line, Judgment is checked every loop. Shield Smite and Warding Strike are shield "
            "attacks, so they keep re-opening Judgment, and Pummel in the same line makes your held Vicious Strike cancel "
            "into it.")
E["tip"] = ("Hold Vicious Strike (left click) with the macro, and take its +20% MP-restored specialty for leveling. When you get "
            "Doom Shield, press it to open fights (it rushes 20 m and shields you).")
M["changelog"][0]["text"] += (" Templar switched to the optimizer's Sep 5 guide, pinned as current after Sep 16 "
                              "(Shield Smite in the Judgment line, Annihilate as line 2, Flash Rampage above Punishment).")
open(p, "w", encoding="utf-8").write(json.dumps(M, ensure_ascii=False, indent=1))
print("templar updated")
