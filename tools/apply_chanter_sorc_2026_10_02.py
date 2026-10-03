"""2026-10-02 Chanter Dark Crush card + Sorcerer leveling rework (user: Sorcerer early game is terrible because it is
mostly stigmas; levels 1-22 have no stigmas. Chanter: a working Dark Crush macro with its cooldown removed).

Facts used:
- Stigma slots (Global): 1 at character level 22, 2 at 27, 3 at 32, 4 at 37 (game8 Sep 30 + metabot Oct 1 guides).
- Chanter, Global DB: Dark Crush opt 4 (skill Lv 12) adds the Piercing Strike chain, opt 5 (Lv 16) removes its cooldown.
  Since Aug 26 Dark Crush is usable for 2 s after Impactful Crush / Spinning Strike (3 s after Marchutan's Wrath /
  Ensnaring Mark). Inven 6451/22932 (Sep 17): one line, Dark-Spin-Impact-Incandescent, hold Onslaught + macro +
  Gust Rampage. 6451/21098 + 20651: weave cycle 650 ms at 122% Combat Speed before Aug 26, +100 ms after
  (so ~750 / 800 / 850 ms at 122 / 118.5 / 90.5%); holding Dark Crush alone ~550 ms. 6451/22369: Sep 4 bug where
  Impactful Crush's +30% skill speed option delayed Dark Crush (fixed per the Sep 17 guide).
- Sorcerer leveling: Inven 6453/42 (Nov 20 2025) levels on ice AoE (Ice Chain main hit, Frost -> Frost Burst,
  Bittercold Wind, Winter's Shackles; Cold Snap passive). 6453/66 (Nov 2025 - Jan 2026): before Flame Arrow skill
  Lv 16 weave Flame Arrow + Ice Chain with Blaze / Frost Burst combo; after 16 a one-button Wish of Concentration,
  Blaze, Firestorm, Frost Burst; Hellfire 1-charge while leveling. Ice Chain costs 120 MP (DB); Flame Arrow restores
  100. Grace of Enhancement (Lv 21 passive): +20% PvE damage while MP >= 25%. Beginner stigma path (Feb 4 guide):
  Element Enhancement, then Delayed Explosion, then Fire Wall.
Not idempotent for the changelog (run once).
"""
import json

P = "data/macros.json"
M = json.load(open(P, encoding="utf-8"))
C = {c["id"]: c for c in M["classes"]}

# ---------------- Chanter ----------------
ch = C["chanter"]
LINE = ["Dark Crush", "Spinning Strike", "Impactful Crush", "Incandescent Blow"]
late = ch["late"]
late.update({
    "src": "Inven Sep 17 optimizer guide (image-verified) + Korean Dark Crush timing tests (Aug 14 – Sep 4)",
    "link": "https://www.inven.co.kr/board/aion2/6451/22932",
    "macros": [LINE],
    "delays": [10],
    "hold": ["Onslaught", "Macro key", "Gust Rampage"],
    "manual": ["Power of the Storm", "Guardian Blessing", "Undefeated Mantra", "Sprint Mantra", "Recuperation"],
    "why": "This is the Dark Crush build, and it needs only one macro entry. Dark Crush can only be used for 2 s after a ranged skill: Impactful Crush or Spinning Strike (Marchutan's Wrath gives 3 s, but it isn't in the Global 4). With option 5 (skill level 16) Dark Crush has no cooldown, so while a window is open, row 0 is ready on every macro turn. The macro then casts Dark Crush, the Piercing Strike chain (option 4), and Dark Crush again until the window closes. Korean players count about 3 Dark Crush / Piercing Strike casts per window. When the window closes, Dark Crush isn't usable, so the macro drops to rows 1–2 and casts Spinning Strike or Impactful Crush. That opens the next window. Incandescent Blow fills the gaps. A second entry only makes the macro check Dark Crush less often during its 2 s window.",
    "tip": "Settings: one entry, delay 10 ms (raise it to 30–50 ms only if skills get skipped), and Dark Crush options 3 · 4 · 5 (crit on hit, Piercing Strike chain, no cooldown). Hold Onslaught + the macro key, and Gust Rampage too for its stagger cancel. How to check it's working: in the DPS meter, the average time between Dark Crush casts should be about 750 ms at 122% Combat Speed, ~800 ms at 118.5% and ~850 ms at 90.5%. Those are Korean values after the Aug 26 patch added 100 ms. If you're much slower, check Combat Speed and ping before the macro. If Incandescent Blow fires right after Impactful Crush instead of Dark Crush, that's the Sep 4 Korean bug tied to Impactful Crush's +30% skill speed option; drop that option until it's fixed on Global. Stack Guardian Blessing on top of Power of the Storm. Undefeated Mantra and Sprint Mantra are toggles: never put them in a macro, because a second press switches them off.",
    "patch": "Aug 26: Dark Crush now opens after any ranged skill (was: stunned target). Minimum cancel time added; the Onslaught → Dark Crush weave got 100 ms slower. Sep 16: Guardian Blessing 5 min → 2 min.",
})
for a in late["alts"]:
    if a["t"].startswith("Inven 9/3 two-line"):
        a["s"] += " Global: Marchutan's Wrath isn't in your 4 stigmas, so its row is skipped. What's left is Dark Crush / Spinning Strike / Incandescent Blow plus Impactful Crush on its own entry."
full = ch["full"]
full["loss"] = full["loss"] + " Global: Marchutan's Wrath isn't in the Global 4 stigma build, so its row is skipped unless you slot it."

ch["early"] = {
    "macros": [LINE],
    "delays": [10],
    "hold": ["Onslaught", "Macro key"],
    "manual": ["Rushing Smash", "Wave Blow", "Recuperation"],
    "why": "The same Dark Crush line as Late game, and every skill in it is a regular skill, so it works from level 4. Impactful Crush (Lv 3) opens Dark Crush (Lv 4) for 2 s; Spinning Strike joins at Lv 14 (its row is skipped until then). Skill points stop at skill level 10, so while leveling Dark Crush still has its 5 s cooldown: one Dark Crush per window. The Piercing Strike chain comes at skill level 12 and no cooldown at 16 (through gear lines, Daevanion and Arcana). The macro doesn't change when that happens.",
    "tip": "Rushing Smash (Lv 1) gap-closes to the next pack; keep it manual if you take its charge option. Impactful Crush stuns normal mobs, so Wave Blow (Lv 12, needs a stunned target) hits hard right after it. Add Gust Rampage (Lv 5) as a third held key once you're fighting bosses with stagger bars. Stigmas from level 22 don't change the macro. Slot them in this order: 22 Undefeated Mantra (toggle it on), 27 Power of the Storm, 32 Guardian Blessing (stack it on Power of the Storm's key), 37 Sprint Mantra (toggle).",
    "alts": [a for a in ch["early"].get("alts", []) if a["t"] == "Video version"],
}
for a in ch["early"]["alts"]:
    a["s"] = "Two entries, where the improved build needs one. Marchutan's Wrath is a stigma (level 22+), so before 22 that row is empty."

# ---------------- Sorcerer ----------------
so = C["sorcerer"]
ICE = ["Bittercold Wind", "Blaze", "Frost Burst", "Ice Chain"]
so["late"]["tip"] = so["late"]["tip"].replace(
    "Ice Chain (no cooldown) stays on its own key for trash packs and MP.",
    "Ice Chain (no cooldown) stays on its own key for trash packs. It costs 120 MP; Flame Arrow is what refills MP.")
so["late"]["why"] = "Needs all 4 Global stigmas (4th slot at level 37), so use the Early game card until then. " + so["late"]["why"]
old_early_alts = [a for a in so["early"].get("alts", []) if a["t"] == "Video version"]
so["early"] = {
    "macros": [ICE],
    "delays": [10],
    "hold": ["Flame Arrow", "Macro key"],
    "manual": ["Winter's Shackles", "Frost", "Hellfire", "Wish of Concentration"],
    "why": "For levels 1–21, with no stigmas yet (the first slot opens at 22). Built from the Korean leveling guides: until Flame Arrow reaches skill level 16, Sorcerer levels on ice AoE, not fire. Ice Chain (Lv 1) is your main hit on packs: it hits 4 targets and slows them, which feeds the Cold Snap passive. Bittercold Wind (Lv 3) hits 4 and goes first. Frost Burst (Lv 10) fires whenever a target is frozen. Blaze (Lv 4) sits above Ice Chain, but it only fires when Fire Mark procs (20% on fire hits in the Global database). When it does, it hits harder and gives back 100 MP.",
    "tip": "MP: Ice Chain costs 120 MP, and every Flame Arrow hit restores 100, so holding both keeps you roughly even. If you run low, let go of the macro key for a few Flame Arrows. From Lv 21 the Grace of Enhancement passive gives +20% PvE damage only while MP is at 25% or more, so don't run dry. Winter's Shackles (Lv 8): press it when the pack is on you. Frost (Lv 7) freezes, and its option 3 resets Frost Burst, so Frost → Frost Burst is your burst. Hellfire (Lv 14): a 1-charge cast is enough for packs (Korean leveling guide); fully charge it on bosses. Wish of Concentration (Lv 12): before big pulls and bosses.",
    "alts": [
        {
            "t": "Levels 22–36: add stigmas by hand as slots open",
            "s": "Keep the same line and press your stigmas yourself. Slot order (Korean beginner path): 22 Element Enhancement, 27 Delayed Explosion, 32 Fire Wall, 37 Cold Storm. On bosses: Element Enhancement → Delayed Explosion → Hellfire inside the Delayed Explosion window → hold. Fire Wall goes down where the pack or boss stands. At 37, with all 4 stigmas, switch to the Late game card.",
            "macros": [ICE],
            "hold": ["Flame Arrow", "Macro key"],
            "extra": [{"label": "Stigma key, press yourself (fills as slots open)", "stack": ["Element Enhancement", "Delayed Explosion", "Fire Wall", "Cold Storm"]}],
        },
        {
            "t": "Bosses once Flame Arrow is skill level 16 (Korean Jan guide one-button)",
            "s": "When Flame Arrow reaches skill level 16 (options 4 and 5: it applies Fire Mark and resets Blaze), Sorcerer switches to fire. This is the leveling guide's one-button line from that point. Hold Flame Arrow with it, and press Hellfire and the stigmas yourself.",
            "macros": [["Wish of Concentration", "Blaze", "Firestorm", "Frost Burst"]],
            "hold": ["Flame Arrow", "Macro key"],
        },
    ] + old_early_alts,
}

M["meta"]["updated"] = "2026-10-02"
M["changelog"].insert(0, {"date": "2026-10-02", "text": "Chanter: the Late game card now explains the Dark Crush build (no-cooldown Dark Crush, the Piercing Strike chain, why it's one entry, delay, how to check your timing). Its Early card no longer uses stigmas. Sorcerer: new Early card for levels 1–21 with no stigmas (the Korean leveling setup on ice AoE), plus a levels 22–36 version that adds stigmas as slots open (22 / 27 / 32 / 37). Fixed: Ice Chain costs MP; Flame Arrow refills it. Macro rows now show which skills are stigmas, which aren't in your Global 4, and the level each skill is learned."})
json.dump(M, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
