"""2026-10-01 Sorcerer + Gladiator macro rework (user: "they seem to really be lacking").

Sorcerer: the old late card was the Sep 22 one-line guide, which needs three keys held at once
(Flame Arrow + macro + a Hellfire line) and Element Enhancement / Fire Wall / Cold Storm pressed by hand.
Those three are ~27% of Sorcerer damage on the meter, so an in-game-only player who misses them loses a lot.
New late card = the Sep 4 in-game-only setup (Inven 6453/16932, image-verified): 6 entries, Bittercold Wind
line 3 times, everything but Hellfire automated. Same author's Aug 26 version hit 1,008 hits / 5.34M on the
dummy (6453/16608). The Sep 22 one-line setup becomes the 'highest ceiling' alternative.

Gladiator: late card unchanged (it is the most-recommended Aug 26 / Sep 5 layout: macro Sword Aura Rampage +
Rending Blow, mash an Overhead Slam key), but the full card becomes the Aug 30 one-key in-game setup
(Inven 6448/30880, image-verified: two entries, Ruinous Blow line + Lunge Stance line, 176 Overhead Slam /
176 Rending Blow a minute with only the macro key held). Early card uses that one-key structure too.
Global notes: Lifestealing Blade is not in the Global 4-slot stigma build.

Not idempotent for the changelog (run once).
"""
import json

P = "data/macros.json"
M = json.load(open(P, encoding="utf-8"))
C = {c["id"]: c for c in M["classes"]}

# ---------------- Sorcerer ----------------
s = C["sorcerer"]
DE = ["Delayed Explosion", "Winter's Shackles", None, None]
BW = ["Bittercold Wind", "Blaze", "Firestorm", "Wish of Concentration"]
EE = ["Element Enhancement", "Fire Wall", "Cold Storm", "Frost Burst"]
old_late = s["late"]

s["late"] = {
    "src": "Inven Sep 4 in-game-only setup (image-verified); same author's Aug 26 version: 1,008 hits/min",
    "link": "https://www.inven.co.kr/board/aion2/6453/16932",
    "queue": "Not stated in the source; the most-viewed July in-game setup used ON, so test both",
    "macros": [DE, BW, EE, DE, BW, BW],
    "delays": [10, 10, 10, 10, 10, 10],
    "hold": ["Flame Arrow", "Macro key"],
    "manual": ["Hellfire", "Ice Chain"],
    "why": "No mouse software needed and only Hellfire is pressed by hand. Element Enhancement, Fire Wall and Cold Storm fire by themselves. Fire Wall and Cold Storm alone are about a quarter of Sorcerer damage on the meter, so missing them by hand costs more than the extra entries do. The Bittercold Wind line appears 3 times out of 6, so your main damage line still gets most turns. That's how this layout gets around the usual 'Sorcerer wants one line' rule. Delayed Explosion leads its own entry, so its damage-taken window is usually up when you fire Hellfire.",
    "tip": "Opener: Element Enhancement → Delayed Explosion → fully charged Hellfire → hold Flame Arrow + macro key. After that, fully charge Hellfire by hand every time it comes back, ideally right after Delayed Explosion lands. Korean dummy numbers with endgame gear (43% cooldown reduction, 112%+ Combat Speed): Hellfire 26–28 casts/min, about 960–1,000 total hits. Fresh Global characters will see fewer. If the boss moves a lot, Fire Wall and Cold Storm land on empty ground, so for those fights move them to a key you press. Ice Chain (no cooldown) stays on its own key for trash packs and MP.",
    "patch": "Sep 16 (KR/TW): Fire Mark procs 100% and Blaze no longer consumes it. The Global database still shows the old 20% Fire Mark. Until Flame Arrow reaches skill level 12 (option 4 adds Fire Mark) and 16 (option 5 resets Blaze), Blaze fires less often on Global.",
    "alts": [
        {
            "t": "Highest ceiling: Sep 22 one-line guide (3 keys held + AoE key by hand)",
            "s": "The Korean optimizer guide's setup: one macro line, then hold Flame Arrow, the macro key and a Hellfire key together. Most players do that with a mouse macro. Element Enhancement, Fire Wall and Cold Storm go on one key you mash when the boss stands still. Its author calls one line the best because Sorcerer loses the most per extra line, but every manual AoE you miss costs damage. Use this only if you can hold three keys and keep the AoEs on cooldown.",
            "macros": [old_late["macros"][0]],
            "hold": ["Flame Arrow", "Macro key", "Hellfire key (hold)"],
            "extra": old_late["keys"],
        },
        {
            "t": "Aug 26 version, same author (1,008 hits, 5.34M dummy DPS)",
            "s": "Same idea with Delayed Explosion under Element Enhancement and Winter's Shackles leading the AoE slot. Entries: Element Enhancement, Bittercold Wind, Winter's Shackles, Element Enhancement, Bittercold Wind, Bittercold Wind. The author pressed Hellfire, Delayed Explosion and Element Enhancement by hand on cooldown for the top number.",
            "macros": [["Element Enhancement", "Delayed Explosion", None, None], BW, ["Winter's Shackles", "Fire Wall", "Cold Storm", "Frost Burst"],
                       ["Element Enhancement", "Delayed Explosion", None, None], BW, BW],
            "hold": ["Flame Arrow", "Macro key"],
        },
    ] + [a for a in old_late.get("alts", []) if a["t"].startswith("Sep 17") or a["t"].startswith("TW Bahamut")],
}

f = s["full"]
f["loss"] = "Needs a held Hellfire key next to the macro, and most players run this with a mouse macro. The AoE line can fire before the Delayed Explosion and Winter's Shackles buffs are up (a 9/20 player saw exactly this). Without mouse software, the Late game card is easier and loses little."

s["early"] = {
    "macros": [DE, BW, EE, DE, BW, BW],
    "delays": [10, 10, 10, 10, 10, 10],
    "hold": ["Flame Arrow", "Macro key"],
    "manual": ["Hellfire", "Ice Chain", "Frost"],
    "why": "Same 6-entry layout as Late game, so you set it up once and it grows with you. Rows for skills you haven't learned are skipped. Bittercold Wind (Lv 3), Blaze (Lv 4) and Firestorm (Lv 1) work from the start. Winter's Shackles (Lv 8) fires from the Delayed Explosion entries, and Frost Burst (Lv 10) from the Element Enhancement entries. Wish of Concentration joins at 12. The stigma rows (Delayed Explosion, Element Enhancement, Fire Wall, Cold Storm) fill in at level 22.",
    "tip": "Press Hellfire yourself from Lv 14 and fully charge it. Frost (Lv 7) on its own key sets up Frost Burst. Ice Chain (no cooldown) is your mana and trash-pack tool. Blaze only hits a target with Fire Mark, so it fires less early. Pushing Flame Arrow to skill level 12 and 16 (options 4 and 5) fixes that. In open-world packs, press Winter's Shackles yourself when the pack reaches you.",
    "alts": [
        {
            "t": "One-line version (this sheet's old early card)",
            "s": "Just the Bittercold Wind line, with everything else pressed by hand. It's simpler to set up, but you have to keep Winter's Shackles and the AoEs going yourself.",
            "macros": [BW],
            "hold": ["Flame Arrow", "Macro key"],
        }
    ] + [a for a in s["early"].get("alts", []) if a["t"] == "Video version"],
}

# ---------------- Gladiator ----------------
g = C["gladiator"]
GL_NOTE = " Global Season 1: your 4 stigmas are Lunge Stance, Zikel's Blessing, Rage Burst and Wave Armor (see Stigmas), so Lifestealing Blade's row stays empty until you slot it."
g["late"]["tip"] = g["late"]["tip"].rstrip() + GL_NOTE
old_full = g["full"]
g["full"] = {
    "src": "Inven Aug 30 in-game-only setup (image-verified: 176 Overhead Slam + 176 Rending Blow a minute)",
    "link": "https://www.inven.co.kr/board/aion2/6448/30880",
    "queue": "Not stated in the source, so test both",
    "macros": [["Ruinous Blow", "Rage Burst", "Lifestealing Blade", "Rending Blow"], ["Lunge Stance", "Wave Armor", "Zikel's Blessing", "Overhead Slam"]],
    "delays": [10, 10],
    "hold": ["Macro key"],
    "manual": ["Leaping Slam"],
    "why": "One key, no mashing and no mouse software. The two entries alternate: entry 1 ends in Rending Blow and entry 2 ends in Overhead Slam, so holding the macro key does the Overhead Slam→Rending Blow cancel (内絕 / 내절) by itself. Ruinous Blow, the stigmas and the buffs fire from the rows above whenever they're ready. The author binds the macro to right-click and holds only that.",
    "loss": "Buffs and Ruinous Blow fire on cooldown, so they get spent on trash and during boss mechanics. Sword Aura Rampage isn't used. The Late game card with a mashed Overhead Slam key reached 192 Overhead Slam/min vs 176 here (different gear, Aug 26 vs Aug 30 tests).",
    "tip": "Bind the skill macro to a mouse button (Settings → Key Settings → General → Skill Macro) and just hold it. If MP runs dry, check that Rending Blow has its MP specialty." + GL_NOTE,
    "alts": [
        {
            "t": "Sep 5 guide's comfort layout (the old Full rotation card)",
            "s": old_full["why"] + " Hold Keen Strike and the macro key while mashing the Overhead Slam key.",
            "macros": old_full["macros"],
            "hold": old_full["hold"],
            "extra": old_full["keys"],
        }
    ],
}

old_early = g["early"]
g["early"] = {
    "macros": [["Ruinous Blow", "Rage Burst", "Lifestealing Blade", "Rending Blow"], ["Lunge Stance", "Wave Armor", "Zikel's Blessing", "Overhead Slam"]],
    "delays": [10, 10],
    "hold": ["Macro key"],
    "manual": ["Leaping Slam", "Sword Aura Rampage"],
    "why": "The one-key layout from the Full rotation card, set up from day one. Before level 22 the stigma rows are empty and get skipped, so the macro alternates Rending Blow (Lv 1) with Overhead Slam (Lv 4), which is the Overhead Slam→Rending Blow cancel, and opens with Ruinous Blow from Lv 14. Stigmas fill in their rows at 22.",
    "tip": "Leaping Slam (15 s) gaps to the next pack. For bosses, switch to the Late game card once you have Sword Aura Rampage and the stigmas. Ruinous Blow's Prepare for Battle gives +20% PvE damage, so for a boss open with it yourself before holding the macro." + GL_NOTE,
    "alts": [
        {
            "t": "Mash version (this sheet's old early card)",
            "s": old_early["why"],
            "macros": old_early["macros"],
            "hold": old_early["hold"],
        }
    ] + old_early.get("alts", []),
}

M["meta"]["updated"] = "2026-10-01"
M["changelog"].insert(0, {"date": "2026-10-01", "text": "Sorcerer and Gladiator reworked. Sorcerer Late and Early now use the Korean in-game-only 6-entry setup (only Hellfire by hand; 960–1,000 hits/min in Korean tests). The Sep 22 three-key setup moved to Other versions. Gladiator Full rotation and Early now use the one-key setup (hold the macro key, no mashing) that does the Overhead Slam→Rending Blow cancel by itself. Global stigma notes added."})
json.dump(M, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
