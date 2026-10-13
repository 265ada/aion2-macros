# Pet Genus audit (Global), Oct 13, 2026

## What was audited

Every place the site gave Genus Insight advice:

| Location | What it said | Verdict |
|---|---|---|
| `data/classes.json` → each class `gear.genus` (shown in Gear as "Pet Genus") | "Slots 3 and 9: Double Chance …" (Assassin: "Back Damage Boost on up to 4 slots"; Templar: "Leftover slots: Boss Attack or Defense"; Cleric: "lock 2/5/8 …") | **Wrong for Global.** Korea's layout. Kept as `gear.genusOld` (quoted on each class page's audit note) and replaced with the verified summary. |
| `data/classes.json` → `gearCommon` | "Pet Genus slots 3 and 9: Double Chance; slots 2, 5, 8: Attack Bonus or Max Attack; the rest Boss Attack." | **Korea only.** Now labelled as Korea's layout, with a pointer to the Global tables. |
| `data/classes.json` → each class `sheet.genus` (Global class sheet) | Kanon's Global list, identical for all 8 classes | **Layout right, picks partly outdated** (see below). Still shown, collapsed, under "What the Global class sheet lists" with an explanation. |
| `index.html` Genus table (from Kanon's Bible, Oct 4) | Line 4 per board: Crit Damage Boost / Weapon Damage Boost / PvE DB / Front-Back DB / Double Chance; 3/6/9 Power Shard Bonus; 7 tolerance; 2/8 HP | **Layout right; line-4 ranking re-checked.** Replaced with the data-driven section. |
| `index.html` "Global is not Korea" bullet | "Pet Genus changed the most …" | Reworded with the actual difference. |

## Sources and how they were checked

1. **Global client tables** (VehicleCreatureSlot / VehicleCreatureOption / VehicleCreatureLevel, build 25800038, Steam update Oct 1, 2026), as published by the Aion 2 Timers Genus Insight tool (`/gamedata/genus_insight.json`). Snapshot: `tools/genus_src/aion2timers_genus_insight_25800038.json`.
2. **questlog.gg** datamine of the same tables (`characterBuilder.getGenusInsightSlots`). Snapshot: `tools/genus_src/questlog_genus_slots.json`. **All 45 slots identical** (stat, min, max and roll weight); `tools/build_genus.py` refuses to run if they ever differ.
3. Global patch notes since the build (Oct 6, Oct 8): no Pets / Genus changes.
4. Kanon's Aion 2 Bible (Oct 4 Global update): damage formula, per-stat values, Global Genus steps.
5. aion2guidance.com Global pets page: pet counts, souls per level, owned effects, crystal sources, analyze cost. Owned effects cross-checked against questlog builds (Critical Hit +82, Accuracy +130 at all pets level 3).
6. Inven KR guide (Jan 14, 2026): Korea's different layout, for the regional comparison.
7. NotMeter top Global parses (week of Oct 7): per-class crit rates, front/back share, double rate, parry rate.
8. 132 public Global questlog builds with Genus filled in: community picks per line (signal only).

## Findings

- **Global layout** (every board): 1 and 5 attack; 2 and 8 defense; 3, 6, 9 crit/accuracy (Critical Hit, positional crit, Accuracy, PvE Accuracy, Power Shard Damage Bonus, Block, Evasion); 4 damage boost (board-specific); 7 tolerance (board-specific). Line N opens at Insight N.
- **Double Chance rolls only on Special line 4** (Epic 0.5–1.5%, Unique 1.0–2.0%, Heroic 1.5–3.0%). Korea's "slots 3 and 9 Double Chance" does not exist on Global.
- **PvE Damage Boost (2.0–4.0%) rolls on line 4 of Cogni, Fera, Natura and Varian, not Special.** It out-rolls every other line-4 damage stat (1.5–3.0%), and on Global's smaller Damage Boost totals (~70–95% with a Chanter) it is worth as much as or more than each board's "signature" stat. Critical Damage Boost on Cogni is worth about half as much. Only 5% of public Global builds take Critical Damage Boost on Cogni; Whelps' Ludra-ready Ranger plan uses PvE Damage Boost on all four.
- **Lines 3/6/9 depend on class.** Top Global Gladiators, Rangers and Assassins are at the 50% stat crit cap, so Critical Hit adds nothing for them: Power Shard Damage Bonus. Templar (28%), Sorcerer (32%) and Cleric (38%) are far under the cap: Critical Hit. Chanter (44%) and Spiritmaster (46%) take crit to the cap, then Power Shard. Bosses parry top Global players ~0%, so Accuracy is conditional.
- **Grades and odds**: Unique from Insight 7 (1%), Heroic only at 9 (1%) and 10 (5%). At 10: Common 20 / Rare 30 / Epic 30 / Unique 15 / Heroic 5.
- **XP**: 100 per unlocked open line per Analyze (locked lines give none); 500 / 1,500 / 3,000 / 5,000 / 10,000 / 20,000 / 40,000 / 70,000 / 100,000 per level (250,000 to 10). Pets give 500 / 250 / 250 XP for levels 1–3.
- **Costs**: 4 crystals + 1,000 kinah per Analyze; locks add 8 / 16 / 36 / 76 / 156 / 236 / 316 / 396 crystals and 2,000 … 99,000 kinah for 1–8 locked lines.

## Confidence

- **High:** pools, ranges, odds, XP and costs (client data, two independent datamines); Double Chance only on Special 4; line-4 PvE Damage Boost over Critical Damage Boost / Multi-hit / Perfect; Max Attack first on lines 1/5; HP increase on 2/8.
- **Medium:** line-4 ties (Fera: PvE DB vs Weapon DB; Varian: PvE DB vs positional DB for melee); Critical Hit vs Power Shard on 3/6/9 (depends on your own crit rate); survival picks on 7.
- **Low:** all PvP picks (player stat totals aren't public).

## Still unverified

- The damage value per point of **Power Shard Damage Bonus** (it is the best remaining damage stat on 3/6/9 for capped classes, but no one has published its formula).
- Which **monster genus** each Global boss is (own-genus Damage Boost, 2.4–4.8%, would beat PvE Damage Boost against that genus).
- Whether **Spiritmaster spirits** inherit Genus stats.
- Whether **heals** scale with Attack (no Genus line boosts healing directly).
- Whether **Special pets** add Insight XP (one source says Special Insight only levels from Analyze).
- Global boss **crit-damage resist and Double Chance resist** (the model uses Korea's 25% and the observed Global double rates).

Re-run `python tools/build_genus.py` after refreshing the snapshots in `tools/genus_src/` when the Global client patches the Pets window.
