"""2026-10-01 Assassin: Sep 30 Korean optimizer guide (Inven 6449/24247, posted the evening of Sep 30).

Image-verified Heart Gore line, row 0 first: Insignia Explosion, Ambush, Heart Gore, Savage Roar.
The guide's author: one macro line only; Ambush in row 1 lowers Heart Gore hits but raises overall damage
(more on real bosses with Defense than on the dummy) and its lifesteal replaces Heart Gore's, because Heart Gore
now needs option 2 (Insignia) or damage drops. Avoid Ambush option 5. Swift Contract before Illusive Clone.
A tester in the replies showed Triniel's Dagger only shortens cooldowns already running (Savage Fang first).
Not idempotent for the changelog (run once).
"""
import json

P, PS = "data/macros.json", "data/stigmas.json"
M = json.load(open(P, encoding="utf-8"))
a = {c["id"]: c for c in M["classes"]}["assassin"]
LINE = ["Insignia Explosion", "Ambush", "Heart Gore", "Savage Roar"]
old = a["late"]

a["late"] = {
    "src": "Inven Sep 30 optimizer guide (image-verified row order); builds on the Sep 18 line",
    "link": "https://www.inven.co.kr/board/aion2/6449/24247",
    "queue": "The guide's in-game setup turns it ON",
    "macros": [LINE],
    "hold": ["Quick Slice", "Macro key", "Storm Rampage line"],
    "manual": ["Swift Contract", "Illusive Clone", "Savage Fang", "Triniel's Dagger"],
    "why": "One macro line, in the row order the Sep 30 guide found best after dozens of tries. Insignia Explosion goes first, then Ambush, Heart Gore and Savage Roar. Ambush in row 1 costs some Heart Gore hits but raised overall damage, more on real bosses (which have Defense) than on the dummy. Its lifesteal also replaces Heart Gore's: Heart Gore now needs its Insignia option, or damage drops. Savage Roar stays as the filler for moments with no Heart Gore, and it cuts Shadowstrike's cooldown. Hold the Storm Rampage key too, so its stagger cancel fires during groggy windows. That cancel also keeps Illusive Clone up longer.",
    "tip": "Press Swift Contract before Illusive Clone, because the attack-speed buff shortens Clone's animation. Press Savage Fang before Triniel's Dagger: a tester showed the Dagger only cuts cooldowns that are already running (30 s left vs 34 s the other way round). Don't take Ambush's option 5 (+2 uses), which made the motion worse and lowered damage. Smoke Bomb is under 2% of damage, so a mobility stigma is fine in its place. Level Heart Gore, Insignia Explosion and Quick Slice to 20, and Savage Roar next.",
    "patch": old.get("patch", ""),
    "alts": [
        {
            "t": "Sep 18 line without Ambush (the sheet's previous card)",
            "s": "Insignia Explosion, Heart Gore, Savage Roar, with Ambush pressed by hand. The Sep 18 tester saw hits drop with Ambush in the line, and the Sep 30 guide found more total damage with it. Try both on the dummy, and remember that real bosses favor the Ambush version.",
            "macros": old["macros"],
            "hold": old["hold"],
        }
    ] + old.get("alts", []),
}
a["full"]["macros"][0] = LINE
a["full"]["manual"] = [x for x in a["full"]["manual"] if x != "Ambush"]
a["full"]["tip"] = "Storm Slice stays out of the macro; press it yourself."
e = a["early"]
e["macros"] = [LINE]
e["manual"] = ["Triniel's Dagger", "Shadowstrike"]
e["why"] = "This is the late-game order, so you never have to relearn it. Rows you haven't learned yet are skipped: Savage Roar (Lv 1), Ambush (Lv 3) and Heart Gore (Lv 4) work right away, and Insignia Explosion joins at Lv 14 to detonate up to 5 Insignia stacks. Heart Gore only lights up after a crit, so the macro skips it until then."
M["changelog"].insert(0, {"date": "2026-10-01", "text": "Assassin: macro line updated to the Sep 30 Korean optimizer guide (Insignia Explosion, Ambush, Heart Gore, Savage Roar), with the stigma press order and option notes. The Sep 18 line without Ambush is kept under Other versions."})
json.dump(M, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

S = json.load(open(PS, encoding="utf-8"))
c = {x["id"]: x for x in S["classes"]}["assassin"]
for sp in c["specs"]:
    if sp["n"] == "Heart Gore":
        sp["note"] = "Sep 30 guide: option 2 is now required, or damage drops. Ambush's lifesteal in the macro covers sustain."
    if sp["n"] == "Ambush":
        sp["note"] = "Not 5 (extra uses): it slows the motion and lowered damage. Ambush now sits in row 1 of the macro line (Sep 30 guide)."
for row in c["skills"]["act"]:
    if row[0] == "Ambush":
        row[3] = "Ranked just below the four above. Row 1 of the Heart Gore line since the Sep 30 guide."
json.dump(S, open(PS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
