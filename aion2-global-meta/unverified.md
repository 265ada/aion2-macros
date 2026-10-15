# Unverified items

**Patch:** Global build 25926599 (Oct 13 PDT / Oct 14 CEST patch, on top of the Oct 6 patch and Oct 8 hotfix). **Written:** 2026-10-13; **updated:** 2026-10-14.

Everything the spec files mark **UNVERIFIED** is collected here, with what would confirm it. Claims listed here are kept out of the "recommended" columns, or are clearly flagged where they appear.

## All classes

| Item | Why it's unverified | What would confirm it |
|---|---|---|
| Global PvP tiers, PvP stigma fours and all PvP sections, for every class | No official Global PvP ranking or Global PvP guide exists yet. The KR 6-slot PvP lists don't transfer to 4 slots. | Global arena or Abyss ranking data by class, or a Global PvP guide with tested 4-slot builds |
| Solo / leveling tiers | No Global leveling-speed data. Placements are opinion, based on class kits. | Timed Global leveling runs or an XP/hour comparison |
| AoE rotations | No Global pack-clear tests. Each file lists the AoE tools from the Global DB, but not a tested order. | Timed pack clears or multi-target dummy parses on Global |
| ~~Stigma shard cost per level (1/2/4/8 → 75 to 20)~~ | **Resolved in Pass 2:** questlog's Global skill data shows the same costs ([questlog](https://questlog.gg/aion-2/en/db/skill/17410000)) | — |
| Stigma slot unlock levels (22/27/32/37 vs "4th slot after 45") | Global sources disagree | Checking the Global stigma window on a sub-45 character |
| Extendable weapon line count (3 vs 4) | Sirin vs Kanon's Bible | Inspecting a Kromede extendable weapon on Global |
| Heroic grade belt and amulet in Season 1 | Sirin says no Heroic gear in S1; belt/amulet morphing isn't covered | Substance Morph preview on Global |
| Exact Daevanion tile paths per class | The Global boards differ from Korea's (Ariel removed, values cut). Only Allyria and Sirin publish Global boards, as images. | A Global board planner, or the image boards in those guides |
| Wing availability beyond Talisra (Eroded, Awakened Pride) | Korean wing picks may not drop on Global (Sirin: wings now only drop from dungeon cubes) | Item source checks on Global |
| Power Shard Damage Bonus value per point | Unpublished formula (genus audit) | A controlled dummy test with and without the stat |
| Whether boss crit-damage resist and Double Chance resist on Global match Korea's | The genus audit's model uses Korea's 25% and the observed Global rates | Global boss stat datamine |
| NotMeter use counts above cooldown limits (casts vs hits) | NotMeter field semantics | NotMeter documentation, or comparing with in-game combat logs |
| ~~The next maintenance (Oct 13 23:30 PDT)~~ | **Resolved:** NC published the notes (build 25926599: Spiritmaster Ancient Spirit and Sorcerer Fire Wall / Cold Storm / Bittercold Wind fixes) ([Steam](https://store.steampowered.com/news/app/3393110/view/1846651706673374)) | — |
| Korea's Sep 23 changes on Global (Chanter Undefeated Mantra and Power of the Storm disabled under Battlefield Might; Gladiator Fracturing Rush follows key direction) | Sep 16 is live on Global, but nothing shows whether Sep 23 shipped | Global patch notes that list them, or an in-game test |
| Korea's Oct 14 changes (Cleric attack elements and level-25 stigma options; Templar Assault Fury and Shield of Protection; Chanter Rushing Smash and Focused Defense; Sorcerer element changes) | Korea only so far; no Global notice | Global patch notes, or the Global skill text on questlog changing |
| Macro row firing order (row 0 first) | No cited source states it. The guides list each stack row 0 first, as the Korean setups do | An in-game test of a stacked macro on Global |
| Skill lines on weapon and guard | The Bible's gear chapter lists them, but none of the Global weapon/guard line lists (Bible ch.3, Sirin, Allyria) does | Inspecting a Global weapon and guard line pool |
| Global passive levels | Global NotMeter data doesn't give most passive levels (it can't log Gladiator Attack Preparation or Impact Hit, for example); the guides show Korean levels, labeled KR/TW, and DB effects | Passive levels in Global NotMeter data, or an in-game check of top players |
| NC class-list quotes | The NC Global class page ([NC class list](https://aion2.plaync.com/en-us/about/index#classes)) is rendered by the client, so its text could not be re-read in a plain fetch | Reading the rendered page in a browser |


## Gladiator
- Global PvP standing and PvP stigma four — would be confirmed by Global PvP rankings/arena data or a Global PvP guide.
- Solo/leveling tier — no Global leveling-speed data.
- AoE rotation order — needs a Global pack-clear test (e.g. dummy group or timed dungeon clears).
- ~~Stigma shard cost per level (1/2/4/8, 75 to Lv 20) on Global~~ — resolved in Pass 2 (questlog Global data).
- Whether KR/TW Sep 16 "can't use Leaping Slam/Ruinous Blow while bound" exists on Global — test in game.
- Gladiator-specific Daevanion tile path on Global boards — needs a Global board planner/guide.
- Wings: whether Eroded Wings (KR front-damage pick) are obtainable on Global S1.
- Belt/Amulet Heroic grade availability in S1.
- NotMeter use count = casts or hits (Ruinous Blow 4.4/min > cooldown limit).
- Gladiator tank: Rage Burst 10 and Focused Block 20 as tank gains (DB effects; Global tanks sit at 5–6); Rending Blow option 2 / Leaping Slam option 4 tank picks; tank gear swaps; tank passive levels.

## Templar
- Whether Korea's Sep 16 longer Pummel / Punishing Strike → Judgment cancel delay (and the damage and Taunt-threat changes) works as described on Global. Sep 16 is live, but only Noble Armor is measurable in logs; needs an in-game cast-rate test.
- Templar PvP stigma four and PvP picks on Global.
- Solo tier; AoE order.
- Global Templar Daevanion path (Korean node guide assumes KR boards).
- Eroded Wings availability on Global.
- ~~Stigma shard cost per level on Global.~~ — resolved: questlog's Global skill data shows 1/2/4/8 per level ([questlog](https://questlog.gg/aion-2/en/db/skill/17410000)).
- ~~Pummel options 4/5 on Global (Sep 16 rework).~~ — resolved: questlog's Global text is the Sep 16 version and Global logs agree (option-4 holders cast Punishment 2.3 times a minute vs 1.7–1.8) ([questlog](https://questlog.gg/aion-2/en/db/skill/12040000)).
- ~~Noble Armor 2-min cooldown on Global.~~ — resolved: a second Noble Armor buff appears in 452 of 507 Templar fights over 130 s, and questlog's Global data gives 120 s ([questlog](https://questlog.gg/aion-2/en/db/skill/12230000)).

## Assassin
- ~~Ambush-in-row-1 gain on the Global (pre-Sep-16) client.~~ — resolved: Sep 16 is live, and at equal CP Ambush users trail (per player −7%), so Macro A no longer uses Ambush (assassin-dps.md).
- ~~Triniel's Dagger level 20 "+3% all skill cooldowns" — whose cooldowns (DB text ambiguous).~~ — resolved: questlog's Global text raises the target's cooldowns from 5% to 8% of duration, so the effect is enemy-side ([questlog](https://questlog.gg/aion-2/api/trpc/database.getSkill?input=%7B%22id%22%3A%2213300000%22%2C%22language%22%3A%22en%22%7D)).
- PvP four on Global; PvP tier; solo tier; AoE order; Global Daevanion path; Awakened Pride wings on Global.
- ~~NotMeter use counts for Illusive Clone exceed its cooldown (likely includes extra-damage hits).~~ — resolved: the counts are real casts (useCount and hitCount are separate fields); short fights inflate the per-minute rate.

## Ranger
- Ranger elements (Korea's Sep 16: every Ranger attack has an element). Sep 16 is live on Global, so likely live, but NotMeter has no element field to confirm it.
- Allyria's tile-by-tile Daevanion path (images only in the guide).
- PvP stigma four / PvP tier; Allyria has no PvP section.
- Allyria's exact in-game macro rows (credited to JOEI; image only).
- Stigma slot unlock levels on Global (22/27/32/37 vs "after 45").

## Sorcerer
- Fire Mark application rate in the logs. Questlog's Global skill text ("Inflicts Fire Mark for 5s on landing a Fire attack", no chance) supports Korea's Sep 16 100% change, while the aion2.app DB (client 18.09.2026) still says 20%; the parses can't separate the two. A dummy test counting Fire Mark applications per Fire hit would confirm it.
- ~~Flame Arrow option 4: Sep 16 version (Pyroclasm +5% Fire damage for 10 s) on Global.~~ — resolved: the Pyroclasm buff appears in 275 of 282 option-4 parses and in none without, and questlog's Global text agrees ([questlog](https://questlog.gg/aion-2/api/trpc/database.getSkill?input=%7B%22id%22%3A%2215210000%22%2C%22language%22%3A%22en%22%7D)).
- Global pack/AoE rotation; PvP four; PvP tier; solo tier.
- Meaning of the "level 5" logged for Fire Wall / Cold Storm in NotMeter buff data (could be a debuff level rather than the stigma level).
- Whether Ice Chain weaving gains damage on Global (Est says yes for low CDR; Global top parses mostly skip it; +3% ±2.4 measured earlier, inside noise).

## Spiritmaster
- Sirin's exact in-game macro rows (image) and the icon→skill mapping of the specialty table.
- Whether Jointstrike: Destruction's KR/TW double-hit bug exists on Global (Sirin hasn't seen it).
- Global AoE order; PvP (Sirin: impossible to predict).
- Whether spirits inherit Genus stats (from the genus audit).

## Cleric
- Global healing output data (NotMeter ranks damage only) — needed to rank heal skills/loadouts on Global.
- Cleric attack-speed cap (94.4% KR) on Global.
- Cleric PvP four; solo tier; Global Daevanion path; heal scaling with Attack.

## Chanter
- ~~Guardian Blessing 2-min cooldown on Global.~~ — resolved: Chanters recast it in 85 of 93 fights longer than 130 s, and questlog's Global data agrees ([questlog](https://questlog.gg/aion-2/en/db/skill/18420000)).
- Back Damage Boost on manastones for Chanter (71% back hits on Global) — no Chanter source tests it.
- Global battle-healer Sprint Mantra level (not logged); heal-stat gear lines.
- PvP four; AoE order; Global Daevanion path.
