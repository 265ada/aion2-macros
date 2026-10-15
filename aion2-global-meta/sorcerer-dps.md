# Sorcerer (魔道星) — DPS spec · AION 2 Global

**Patch covered:** Global client build **25926599** (Steam public branch, updated 2026-10-14 06:40 UTC). That is the [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374) on top of the [Oct 6 PDT patch](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544) and the [Oct 8 PDT hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1). The Oct 13 patch fixed three Sorcerer bugs: Fire Wall and Cold Storm bonus damage not applying across a height difference, your Embers/Frostbite being removed by another player's stronger Embers/Frostbite, and Bittercold Wind's Frost cooldown cut failing across a height difference. Nothing else changed for Sorcerer. Build id: [SteamCMD](https://api.steamcmd.net/v1/info/3393110). NotMeter data (week of Oct 7–14) was recorded on the previous build 25800038. **Written:** 2026-10-13, **updated for the Oct 13 patch:** 2026-10-14.

**Tags:** [Global] · [KR/TW-confirmed] = Korean or Taiwanese source checked against the Global client · UNVERIFIED.

**Main data sources:**
- **NM:** [NotMeter Global ranking](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), week of Oct 7–14. (NotMeter has since retired this generation, so the link returns 404; see the [README](README.md).) Top 20 Sorcerer parses on each of 15 bosses: 300 parses from 119 players, median CP 150,510, median DPS 70,029. Recorded before the Oct 14 patch.
- **DB:** [aion2.app Global client DB](https://aion2.app/db/skills?class=Sorcerer), client dated 18.09.2026.
- **Sheet:** [Global class sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview). Its Sorcerer page follows Est's guide.
- **Sheet snapshot:** citations of this class's sheet tab refer to the copy downloaded on Oct 14. Later that day the author replaced the tab with a link to [daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve), where the build is now maintained; differences found are noted where they matter.
- **EST:** [Est's Sorcerer guide](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), updated Oct 11. It is **written for TW/KR**: the author says "THIS GUIDE IS FOR TW/KR… some information might not work" on Global. It's used only where the Global DB shows the same skill text, marked [KR/TW-confirmed], or as KR context. **A cell that cites only EST is KR/TW** unless it says otherwise.
- **Post-patch check:** NotMeter published a newer generation on Oct 14 14:32 UTC ([NM post-patch](https://notmeter.com/g/29087b479916fb24/data/notmeter-global-ranking.json)). Its 284 top-20 Sorcerer parses recorded after the Oct 14 patch (118 players) give: class score 103.69 (still 4th); +7.6% at equal CP (still 2nd); damage shares Hellfire 22.4%, Blaze 15.0%, Fire Wall 11.4%, Bittercold Wind 9.4%, Firestorm 9.1%, Cold Storm 6.3%; stigmas Fire Wall 100%, Element Enhancement 98%, Delayed Explosion 97%, Cold Storm 87%, Hibernation 19%, Steel Barrier 9%. Picks that moved: Blaze 3+5 42%, Flame Scattershot 4+5 22%, Ice Chain 2+4 44%. Numbers below are from the pre-patch week unless marked "post-patch".

**Two Global-specific facts change how Sorcerer plays:**
1. **Fire Mark and Flame Arrow option 4.** Korea's Sep 16 patch made Fire Mark apply on every Fire attack instead of 20% of them (the aion2.app database, client 18.09.2026, still says 20%), stopped Blaze from consuming it, and changed Flame Arrow option 4 (Pyroclasm) from "applies Fire Mark" to **+5% Fire damage for 10 s** ([KR Sep 16 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6aa99cb8a279104f7d9d5c34)). Global logs show the new option 4 is live: the Pyroclasm buff appears in 275 of 282 top parses with option 4, in none without it, and lasts 10 s ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)) [KR/TW-confirmed]. The Global skill data on questlog ([Flame Arrow](https://questlog.gg/aion-2/api/trpc/database.getSkill?input=%7B%22id%22%3A%2215210000%22%2C%22language%22%3A%22en%22%7D), [Fire Mark](https://questlog.gg/aion-2/api/trpc/database.getSkill?input=%7B%22id%22%3A%2215710000%22%2C%22language%22%3A%22en%22%7D); updated Oct 7) agrees on both changes: Flame Arrow option 4 is now a +5% Fire Damage Boost for 10 s on Pyroclasm, and Fire Mark is inflicted on landing a Fire attack with no chance stated [KR/TW-confirmed]. So the rest of the Sep 16 Sorcerer package is very likely live too. The logs can't show Fire Mark's application rate, so that part rests on the two texts (UNVERIFIED in the logs). Flame Arrow 4+5 stays the standard pick (70% of top Global Sorcerers).
2. **Cooldown reduction.** Global max CDR is about **19–21%**, against 34–40% in KR/TW ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). EST's minimum for full Wish of Concentration uptime and the Bittercold Wind hit breakpoint is 25.6% CDR, which Global can't reach yet. That's why EST tells Global players to weave Ice Chain ([EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit)).

---

## 1. Overview

| Item | Recommendation / finding | Why | Source |
|---|---|---|---|
| Role | Ranged magic nuker (spellbook) | NC: "devours all with a storm of arcane power" | [NC class list](https://aion2.plaync.com/en-us/about/index#classes) |
| Playstyle | Damage is spread across many skills: Hellfire 21.7%, Blaze 14.7%, Fire Wall 13.1%, Bittercold Wind 9.2%, Firestorm 8.9%, Cold Storm 6.5%. Skills cut each other's cooldowns: Firestorm → Hellfire, Blaze → Wish of Concentration, Wish → everything. | Global damage shares; skill text | [NM], [DB Firestorm](https://aion2.app/db/skills/15040000), [DB Blaze](https://aion2.app/db/skills/15050000), [DB Wish](https://aion2.app/db/skills/15310000) |
| Strengths | <ul><li>**2nd best at equal CP on Global:** +9.8% vs the average.</li><li>Ranged, with strong AoE.</li><li>Delayed Explosion makes the target take +15% (+25% at 20) more damage from you.</li></ul> | | [NM], [DB Delayed Explosion](https://aion2.app/db/skills/15320000) |
| Weaknesses | <ul><li>About a fifth of damage is ground AoE (Fire Wall, Cold Storm) that misses moving bosses.</li><li>Poor mobility; no block.</li><li>Needs CDR, and Global caps it lower.</li></ul> | EST's cons list; Global CDR | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) [KR/TW], [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| PvE standing (Global) | **4th by NotMeter score (105.70); 2nd at equal CP (+9.8%)** | | [NM classPerformance] |
| PvP standing (Global) | **UNVERIFIED.** EST (KR/TW): "average in 1v1 PvP and top tier in zerging". | No Global data | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Difficulty | **Medium to high** (rotation knowledge, AoE placement). EST: "easy… if you slap a macro and don't think", but piloting it well takes knowledge. | | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Who should play it | Ranged players who learn boss movement and want high damage | | — |

---

## 2. Max damage

### Single target (EST's opener; every skill and effect checked in the Global DB)

| Step | What to do | Why | Source |
|---|---|---|---|
| 1 | **Element Enhancement** | <ul><li>+20% Fire and Water Attack for 10 s.</li><li>10: ×1.5 Robe of Flame.</li><li>15: ×1.5 Grace of Enhancement.</li><li>20: +10% more.</li></ul> | [DB](https://aion2.app/db/skills/15400000) |
| 2 | **Delayed Explosion** | Target takes +15% damage from you for 4 s (+10% more at 20). Since Aug 26 it also works on the ground AoEs in Korea ([KR Aug 26 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6a8ded386b722c561dc6a241)); not confirmed on Global. | [DB](https://aion2.app/db/skills/15320000), [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| 3 | **Hellfire, fully charged**, inside the Delayed Explosion window | <ul><li>21.7% of damage.</li><li>A macro fires it uncharged. By the DB, a Max cast does about 3× an uncharged one (1,137 vs 3,412 at level 1). Global Max casts: median 82.8k (middle half 71–100k); uncharged casts are too rare in the logs to measure.</li><li>Top 10% Global parses (30 by DPS): about 7.9 Hellfires a minute; all 300 parses average 5.8 ([NM]).</li></ul> | [NM], [DB](https://aion2.app/db/skills/15060000) |
| 4 | **Fire Wall** + **Cold Storm** where the boss stands | 13.1% + 6.5% of damage (post-patch 11.4% + 6.3%), split between the ground hit and the Embers / Frostbite debuff (EST) | [NM], [DB Fire Wall](https://aion2.app/db/skills/15390000), [DB Cold Storm](https://aion2.app/db/skills/15200000) |
| 5 | **Bittercold Wind** → **Firestorm** → **Wish of Concentration** → Bittercold Wind | <ul><li>Firestorm option 4: −2 s Hellfire per fireball (5 fireballs per use in Global parses, [NM]).</li><li>Wish: +10% Attack (+10% more with option 2), +10% Combat Speed (4).</li><li>Wish option 5 (16): −10 s on every cooldown.</li></ul> | [DB Firestorm](https://aion2.app/db/skills/15040000), [DB Wish](https://aion2.app/db/skills/15310000) |
| 6 | Delayed Explosion → **Winter's Shackles** → Hellfire → Firestorm | Winter's Shackles option 3: +20% PvE Damage Boost for 5 s | [DB](https://aion2.app/db/skills/15110000) |
| 7 | Hold **Flame Arrow** + the macro (Blaze / Firestorm filler); press the rest on cooldown | Flame Arrow option 4: +5% Fire damage for 10 s on Pyroclasm (Sep 16 version, live). Option 5: Blaze reset. | [DB](https://aion2.app/db/skills/15210000), [KR Sep 16 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6aa99cb8a279104f7d9d5c34), [NM] |

**Line up:** each Hellfire inside a Delayed Explosion window. Put Element Enhancement (20 s at level 20; the DB's 10 s is level 1), Wish of Concentration (18 s at the Global median level 17: 10 s at level 1 plus 0.5 s per level, [questlog Global](https://questlog.gg/aion-2/api/trpc/database.getSkill?input=%7B%22id%22%3A%2215310000%22%2C%22language%22%3A%22en%22%7D); the logs show 17.0 s at level 15) and Winter's Shackles option 3 (5 s) on the same Hellfire. The order is EST's opener ([EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), KR/TW); the effects are the DB text; stigma buff durations measured in Global parses ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)).

**Global weave:** EST recommends weaving Ice Chain on Global, because the low CDR leaves gaps. About two thirds of top-10% Global parses don't cast it. When it is cast (36% of top parses), Ice Chain is about 5% of damage and its chained Cold Wave about 6% more, but those casts replace Flame Arrow and Blaze, so it stays optional ([NM]).

### AoE

| Tool | Targets | Source |
|---|---|---|
| Hellfire, Bittercold Wind, Ice Chain, Frost, Frost Burst, Winter's Shackles | up to 4 within 4 m | [DB](https://aion2.app/db/skills?class=Sorcerer) |
| Fire Wall | up to 4 in a 1×10 m wall (+2 m width at 10) | [DB](https://aion2.app/db/skills/15390000) |
| Cold Storm | up to 4 within 5 m + Frostbite | [DB](https://aion2.app/db/skills/15200000) |
| Delayed Explosion at 15 | becomes AoE | [DB](https://aion2.app/db/skills/15320000) |

**AoE / leveling:** Korean leveling guides use ice AoE until Flame Arrow reaches 16 ([Inven](https://www.inven.co.kr/board/aion2/6453/66), KR/TW). Ice Chain is a "mobbing skill" ([EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit)). A Global pack rotation is UNVERIFIED.

---

## 3. Macros

The in-game macro: Settings → Key Settings → General → Gameplay → Macro ([Allyria §3.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Rows are numbered from the bottom (row 0 is next to the hotbar); this guide treats row 0 as the highest priority, which is UNVERIFIED on Global (see [README](README.md)).

### Macro A: Global sheet / EST layout (recommended)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Blaze | Firestorm | Winter's Shackles | Frost Burst | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

- **Hold:** Flame Arrow (left click) + the macro (right click).
- **Press yourself:**
  - key 1: Element Enhancement + Delayed Explosion;
  - key 2: Hellfire, always charged to Max;
  - key 3: Fire Wall + Cold Storm;
  - key 4: Bittercold Wind + Wish of Concentration.

The burst stays manual so it lines up with Delayed Explosion. The sheet's note: "Blaze + Firestorm (RMB) + LMB on downtime, send everything else whenever they're up."

**The author's newer layout** ([daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve), build saved Oct 13): the right-click macro stacks Blaze, Firestorm, Winter's Shackles and Ice Chain (rows 0 to 3, 10 ms delay), so Ice Chain replaces Frost Burst in row 3. Left click is Flame Arrow. Key 1 holds Element Enhancement, Fire Wall and Cold Storm; key 2 Bittercold Wind and Frost Burst; key 3 Delayed Explosion; key 4 Hellfire; R Wish of Concentration; E Frost. Its rotation order is Element Enhancement, Fire Wall, Cold Storm, Bittercold Wind, Delayed Explosion, Hellfire, Wish, Flame Arrow, then the macro.

### Macro B: in-game only, 6 entries (alternative; automates the AoEs)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 |
|---|---|---|---|---|
| 1 | Delayed Explosion | Winter's Shackles | — | — |
| 2 | Bittercold Wind | Blaze | Firestorm | Wish of Concentration |
| 3 | Element Enhancement | Fire Wall | Cold Storm | Frost Burst |
| 4 | Delayed Explosion | Winter's Shackles | — | — |
| 5 | Bittercold Wind | Blaze | Firestorm | Wish of Concentration |
| 6 | Bittercold Wind | Blaze | Firestorm | Wish of Concentration |

- **Source:** [Inven Sep 4](https://www.inven.co.kr/board/aion2/6453/16932) [KR/TW, pre-Sep 16; Sep 16 is live on Global, so re-check Fire Mark behavior on the dummy].
- **Use:** hold Flame Arrow + the macro, and charge Hellfire by hand.
- **Trade-off:** Fire Wall and Cold Storm fire even if the boss is moving. Together they're 19.6% of Global damage.
- **Global note:** the Korean dummy numbers (43% CDR) won't be reached on Global (19–21% CDR).

### Banned or nerfed on Global

| Item | Status | Source |
|---|---|---|
| In-game macro | Allowed | [Allyria FAQ](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| External macros (the KR "3 keys held" Hellfire-key setups) | **Risk.** NC's unauthorized-program rule; macros named in the Oct 10, Oct 12 and Oct 14 ban waves. | [NC Operation Policy](https://www.plaync.com/policy/operation/aion2global), [Oct 10 PDT notice](https://aion2.plaync.com/en-us/board/notice/view?articleId=6acaa7506b722c561dc6aae9), [Oct 14 notice](https://store.steampowered.com/news/app/3393110/view/1846651706673527) |
| Sorcerer nerfs on Global | None. The Oct 13 patch only fixed bugs: Fire Wall and Cold Storm bonus damage now applies across a height difference, your Embers / Frostbite are no longer removed by another player's stronger ones, and Bittercold Wind's Frost cooldown cut now also works across a height difference. | [Oct 13](https://store.steampowered.com/news/app/3393110/view/1846651706673374), [Oct 6](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544), [Oct 8](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1) |

---

## 4. Stigmas

**Global rules:** 4 slots, cap 20, free resets; a fresh 45 has 32 shards, and the AP cap allows about 20 shards a week ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). No rarity, so "n/a" ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

**Global usage (top 20 per boss):** Fire Wall 100%, Delayed Explosion 97%, Element Enhancement 97% (median 20), Cold Storm 90%. Logged stigma levels (per player): Element Enhancement median 20, Fire Wall median 11 (5 to 20), Delayed Explosion median 10, Cold Storm median 5. Hibernation 27% and Steel Barrier 11% appear as swaps ([NM]).

### PvE

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Element Enhancement | Slot 1 | **20** | n/a | EST: "core buff, non negotiable… NUMBER 1 PRIORITY". Global median 20. | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [NM], [DB](https://aion2.app/db/skills/15400000) |
| Fire Wall | Slot 2 | **10–15 now → 20** (top Global median 11) | n/a | <ul><li>5: Enhanced Embers.</li><li>20: +10 s Embers.</li><li>13.1% of damage (post-patch 11.4%).</li><li>EST: 2nd priority stigma.</li></ul> | [DB](https://aion2.app/db/skills/15390000), [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Delayed Explosion | Slot 3 | **10 → 20** | n/a | 10: −10 s cooldown (30 → 20 s). 15: AoE. 20: +10% more damage taken. | [DB](https://aion2.app/db/skills/15320000) |
| Cold Storm | Slot 4 | **5 now → 15/20** | n/a | <ul><li>5: Enhanced Frostbite.</li><li>15: +3 s storm.</li><li>20: +10 s Frostbite.</li><li>6.5% of damage.</li><li>Two Sorcerers: before Oct 13, a stronger Frostbite from another player removed yours. The Oct 13 patch stopped that; whether two Sorcerers' Frostbites stack is unconfirmed.</li></ul> | [DB](https://aion2.app/db/skills/15200000), [NM], [Oct 13 patch notes](https://store.steampowered.com/news/app/3393110/view/1846651706673374) |
| Hibernation | Swap for mechanics | **1** | n/a | 5 s immunity on a 180 s cooldown. 27% Global use at level 1. | [DB](https://aion2.app/db/skills/15410000), [NM] |
| Steel Barrier / Arctic Armor | Safety swap (hard content) | 10 / 20 | n/a | <ul><li>Steel Barrier: 16% HP shield for 60 s.</li><li>Arctic Armor: +20% PvE Damage Tolerance (+20% more at 20).</li><li>EST: Arctic "extremely powerful" for the hardest content.</li></ul> | [DB Steel](https://aion2.app/db/skills/15160000), [DB Arctic](https://aion2.app/db/skills/15230000), [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |

**Shard order:** EST's KR order cut to Global's 4 slots and cap of 20 ([EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), KR/TW):

| Step | Stigma levels |
|---|---|
| 1 | Element Enhancement 1 → Delayed Explosion 1 → Fire Wall 5 → Cold Storm 5 |
| 2 | Element Enhancement 15 → Delayed Explosion 10 → Element Enhancement 20 |
| 3 | Fire Wall 20 → Cold Storm 20 → Delayed Explosion 20 |

Top Global players today: Element Enhancement at 20, Fire Wall about 10–15, Delayed Explosion about 10, Cold Storm about 5.

[daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve) has all four at 20 on the author's character. Its shard order takes Fire Wall to 20 right after Element Enhancement, then Delayed Explosion 5, Cold Storm 1 and 5, Delayed Explosion 10, Cold Storm 20, Delayed Explosion 20. The order above keeps Fire Wall at 5 until Element Enhancement is done.

### PvP

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Arctic Armor | Core | 20 | n/a | Tolerance; Magic Displacement | [DB](https://aion2.app/db/skills/15230000) |
| Element Enhancement | Core | 20 | n/a | Damage | [DB](https://aion2.app/db/skills/15400000) |
| Hibernation | Escape | 20 | n/a | 20: triggers on Impact-type CC | [DB](https://aion2.app/db/skills/15410000) |
| Glacial Smite or Soul Freeze | Burst / Seal | 20 | n/a | Glacial Smite: "good burst of damage in PvP" | [DB Glacial](https://aion2.app/db/skills/15120000), [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |

This is **UNVERIFIED for Global**. It is Korea's 6-slot PvP list ([repo KR build](../data/stigmas.json)) cut to 4. EST covers no PvP.

### Solo

The same damage four works solo. Swap Cold Storm for Steel Barrier if you die to packs (UNVERIFIED; DB effects).

---

## 5. Skills

**EST's leveling path** (KR/TW): every core active at 14 first, then Wish 16 > Blaze 16 > Hellfire 16 > Firestorm 16 > Flame Arrow 16 > Hellfire 20 > Wish 20 > Blaze 20 > Flame Arrow 20 > Firestorm 20 ([EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit)). Specialty breakpoints are 8 / 12 / 16 / 20 ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

**Global adjustment:** reach **Flame Arrow 12** early for option 4 (+5% Fire damage for 10 s per Pyroclasm; the Sep 16 version is live, see the header). The "% at 16+" figures below come from option-5 picks, so they're lower bounds; where buff data logs the real level, that's given too.

### Actives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Hellfire | 1st | **20** (16 minimum) | n/a | 21.7%. 16: −15 s cooldown. 72% of top Global at 16+, 13% at 20. | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Wish of Concentration | 1st (tied) | **20** (16 minimum) | n/a | 16: −10 s on every cooldown. Global buff median 17. | [DB](https://aion2.app/db/skills/15310000), [NM buffs], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Blaze | 2nd | **20** (16 non-negotiable) | n/a | 14.7%. 16: −3 s Wish per hit. 77% at 16+. | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Flame Arrow | 3rd | **16** (12 first on Global; 20 for the third option per the sheet and EST) | n/a | Held filler, plus Pyroclasm's +5% Fire damage (4) and Blaze reset (5). 76% picked option 5; logged levels: 88% at 16+. | [NM], [DB](https://aion2.app/db/skills/15210000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Firestorm | 4th | **16** (20 minor per EST; the sheet says 20) | n/a | 8.9%. 12: −2 s Hellfire per fireball. 42% picked option 5; logged levels: 59% at 16+. | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Bittercold Wind | 5th | **20** (12 minimum) | n/a | 9.2%. Easy to level through the Compass Arcana. Logged levels: median 15, about half at 16+ (41 players). Option 5 (16: −1 s Frost cooldown on hit; the effect the Oct 13 patch fixed for height differences) is picked by only 2–3% of top Global Sorcerers (Korea's top 20: 60%). | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Winter's Shackles | 6th | **16** (EST: 16, or 20 for the mobile option) | n/a | 3: +20% PvE Damage Boost for 5 s. 35% picked option 5; logged levels: 49% at 16+. | [NM], [DB](https://aion2.app/db/skills/15110000) |
| Flame Scattershot | Stagger only | **16** | n/a | 5: −1 s all cooldowns per hit. 40% at 16+. | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Ice Chain | Mobbing / Global weave | **12** | n/a | 2+4 (59% Global; post-patch 44%) | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Frost | PvP / stagger | **12** | n/a | | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Frost Burst | Lifesteal | **12** | n/a | "You use this for the lifesteal" | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Defiance | CC break | **12** (EST; the sheet says 16) | n/a | Each level −1 s cooldown | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |

**daevaos plan** ([daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve)): Flame Arrow, Firestorm, Blaze and Wish of Concentration to 16 first, then Bittercold Wind and Hellfire to 20, and Robe of Flame to 30. Its specialty picks match the table in section 6 for Flame Arrow 4+5, Blaze 3+5, Firestorm 2+4 (+5 at 20), Hellfire 1+5 (+3 at 20), Wish 5+4 (+2 at 20), Bittercold Wind 1+2 now (1+2+4 at 20) and Winter's Shackles 3+5. It differs on Ice Chain (2+3), Frost Burst (1+4 now, 4+5 planned at 16) and Flame Scattershot (3+4, no option 5, level 12).

### Passives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Robe of Flame | The only key passive | as high as possible (EST: 31+, which assumes more level-20 actives than Global's gear and 5 Arcana cards allow) | n/a | Accuracy, PvE Damage Boost, Double Chance. ×1.5 under Element Enhancement 10. | [DB](https://aion2.app/db/skills/15740000), [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Grace of Enhancement | 2nd | spare lines | n/a | +20% PvE Damage Boost at ≥25% MP. EST: about 2–3% of total damage and the 2nd-best passive. The sheet ranks Fire Mark 2nd instead (and puts it 3rd on most armor lines); EST rates Fire Mark at 1–2%. Global NM shares: Fire Mark 2.5%, Grace of Enhancement 1.5%. | [DB](https://aion2.app/db/skills/15780000), [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NM] |
| Robe of Earth | MP | base level | n/a | "The solution to all of your mana issues" | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Fire Mark, Vitality Evaporation, Cold Snap | Low | base | n/a | 1–2% each (EST). Fire Mark is 2.5% of Global damage. | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [NM] |
| Robe of Cold, Absorb Essence, Grace of Resistance, Revitalization Contract | PvP | base | n/a | | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |

---

## 6. Specializations

| Item | Recommendation (picks at 8 / 12 / 16 / 20) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Hellfire | 1 / 1+4 / **1+5** / 1+3+5 or 1+4+5 | 20 | n/a | <ul><li>1: faster charge.</li><li>3: mobile.</li><li>4: multi-hit, ignores Block.</li><li>5: −15 s.</li><li>Global 1+5 36% (most common).</li><li>EST: 5 > 3 > 1. Korea's top 20: 1+4+5.</li></ul> | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Wish of Concentration | 2 / 2+4 / 4+5 / **2+4+5** | 20 | n/a | 2: +10% Attack. 4: +10% Combat Speed. 5: −10 s all cooldowns. EST 5 > 4 > 2 (KR/TW). Global per player: 2+5 40%, 4+5 34%, 2+4 18% (below 16), 2+4+5 8%. | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [DB](https://aion2.app/db/skills/15310000), [NM buffs](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |
| Blaze | 3 / 3+4 / **3+5** / 3+4+5 | 20 | n/a | 3: delayed damage (+35%, EST). 5: −3 s Wish. Global 3+5 53% (post-patch 42%). EST 5 > 3 > 4. | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Flame Arrow | 3 (or 2 for lifesteal) / 4 + 2/3 / **4+5** / 4+5+2 or 3 | 16–20 | n/a | Global 4+5 70%. EST 5 > 4 > 2. | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Firestorm | 2 / **2+4** / 4+5 / 2+4+5 | 16–20 | n/a | 4: −2 s Hellfire per fireball. 5: +15% damage per fireball, up to +75%. Global 2+4 55%, 4+5 37%. EST 4 > 5 > 2; swap 2 for 3 in PvP. | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Bittercold Wind | 1 / **1+4** (Global) or 1+2 (EST) / — / 1+2+4 | 20 | n/a | Global 1+4 61%. EST 1 > 2 > 4. | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Winter's Shackles | 3 / 1+3 or 3+4 / **3+5** / 1+3+5 | 16–20 | n/a | Global split: 1+3 / 3+5 (35% each). EST 5 > 3 > 1. | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Flame Scattershot | 3 / — / 3+5 (or 4+5) | 16 | n/a | Global 4+5 32% (post-patch 22%). EST 5 > 3. [daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve) runs 3+4 (no option 5) at level 12. | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Ice Chain | 2 / **2+4** | 12 | n/a | Global 59% (post-patch 44%). EST 2 > 3, or 4 > 2 for Shackles weaving. The sheet and [daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve) pick 2+3 (about a third of Global Ice Chain users). | [NM], [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Frost | 3 / **2+3** | 12 | n/a | Global 64–68%. Sheet: 1 / 2 | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Frost Burst | 1 / 1+2 (EST) | 12 | n/a | EST 1 > 2 (KR/TW). Sheet: 1 / 4. Global per player: 1+4 29%, 2+4 29%, 1+2 23%. [daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve) has 1+4 now and plans 4+5 at level 16. | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NM] |
| Defiance | 3 / 2+3 | 12 | n/a | EST 3 > 2 (KR/TW) | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |

**PvP:** Firestorm option 3 (−60% Incoming Heal) replaces 2 ([EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit)). Other PvP picks are UNVERIFIED.

### Daevanion boards (Global)

| Item | Recommendation | Target | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Priority | <ul><li>All skill and damage nodes.</li><li>Ignore HP / Defense / MP / Crit-resist nodes (EST's story board).</li><li>Orange > Blue > Green > White.</li><li>Blue first when it reaches a milestone.</li></ul> | — | n/a | | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [Allyria ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| CDR / Combat Speed orange tiles | Highest value for Sorcerer | — | n/a | The rotation runs on cooldown reduction, and Global CDR is scarce | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Global changes | About 316 points at 45 (+100 from shops); Ariel removed; orange % 2.5 → 1.5 | — | n/a | | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

---

## 7. Tier list

| Content | Tier | Placement reason | Source |
|---|---|---|---|
| PvE | **A** (4th by score; 2nd at equal CP) | NotMeter score 105.70; +9.8% at equal CP | [NM classPerformance] |
| PvP | **UNVERIFIED** | EST (KR/TW): average 1v1, top in zergs | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Solo / leveling | **B+ (opinion)** | Strong AoE, fragile, low mobility | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |

---

## 8. Gear

Global rules: **Unique is the settle rarity** for every slot in Season 1 ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). Phases: [README](README.md#gear-phases).

| Item | Recommendation (stat lines in order) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Weapon (spellbook) | Weapon Damage Boost > Combat Speed > Might > Precision > Damage Boost > Multi-hit > Attack | **+17** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Guard | Same, with Damage Boost 3rd | **+17** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Helmet | Incoming Heal > Robe of Flame > Fire Mark > Double Chance > Attack Increase > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Shoulders | Crit Damage Boost > Robe of Flame > Fire Mark > Accuracy > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Chest | Damage Boost > Robe of Flame > Fire Mark > Crit > Accuracy > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Legs | Damage Tolerance > Robe of Flame > Fire Mark > Perfect > Attack Increase > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Gloves / Boots | Combat Speed / Move Speed > Robe of Flame > Fire Mark > Perfect > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Cloak | Robe of Flame > Fire Mark > Double Chance (the sheet also lists "Smite", the same stat on Global) > Attack Increase > Crit > Attack | **+15** | Unique | No Perfect on capes on Global | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Earrings / Necklace | Robe of Flame > Might > Precision > Fire Mark > Accuracy > Crit > Attack | **+16** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Rings | Wish of Concentration > Hellfire > Might > Precision > Bittercold Wind > Blaze > Flame Arrow > Firestorm | **+17** | Unique | Korea's top-20 ring lines: Firestorm, Hellfire, Wish, Blaze, Bittercold, Flame Arrow | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Bracelets | Wisdom > Destruction > Time > Illusion > Death | **+15** | Unique (slot 1); Epic / blue (slot 2) | EST (KR/TW): Illusion, Wisdom, Destruction and Time are all "non-negotiable"; the sheet's order is used here | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Belt / Amulet | Upgrade early, then stop; amulet to +10, then Substance Morph (live sheet) | to Unique (yellow / "gold") | **Unique** | Allyria's "Gold" is the Unique tier (Sirin) | [Allyria §6.1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Clash Runes | | **+5 to +7** | n/a | They can break | [Allyria §6.1.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |

| Other | Recommendation | Source |
|---|---|---|
| Manastones | Weapon Damage Boost ≈ Crit Damage Boost > Damage Boost > Attack. EST: Front Damage Boost % beats Double Chance past some point, but Sorcerer's kit can't always hit from the front. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| CDR targets | EST: 25.6% minimum, 37% ideal (KR/TW). Global max is about 19–21%, so take every CDR source: Illusion Mirror, Talisra wings, CDR tiles. | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Arcana | Chalice Time · Parchment Life/Destiny · Compass Death/Freedom · Bell Destruction · **Mirror Illusion** (CDR). Skill lines: Robe of Flame, Hellfire, Blaze, Wish, Firestorm, Bittercold Wind (Compass). [daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve) (all Unique, +5): Chalice of Vigor with Robe of Flame +4 and Firestorm +2; Parchment of Vigor with Hellfire +4, Firestorm +2, Blaze +2 (Flame Arrow if possible); Compass of Magic with Bittercold Wind +4 and Winter's Shackles +2; Bell of Magic with Fire Mark / Robe of Cold; Mirror of Vigor with Robe of Flame +4 (the sheet says Mirror (Magic)). It names Wish of Concentration only as an alternative for the Chalice's +2. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR Arcana](https://notmeter.com/?view=setup-guide), [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Accuracy | Wish and Element Enhancement give about 300 Accuracy, so Sorcerer rarely needs Accuracy lines (EST, KR/TW) | [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit), [DB Element Enhancement](https://aion2.app/db/skills/15400000) |
| Pet Genus | <ul><li>Special line 4: Double Chance.</li><li>Line 4 on other boards: PvE Damage Boost.</li><li>Lines 1/5: Max Attack.</li><li>**Lines 3/6/9: Critical Hit** (top-20 Global Sorcerers: about 42–44% crit, hit-weighted, on fire skills that don't always crit; still under the 50% cap). [daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve) lists Accuracy 40 / Crit 30 here; Wish and Element Enhancement already give about 300 Accuracy (EST, KR/TW).</li><li>Line 7: PvE Damage Tolerance.</li></ul> | [Genus audit](../docs/genus-audit.md) |
| Wings | Talisra (CDR); Forest Spirit or Dark Veil Wings until then ([daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve)) | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [EST](https://docs.google.com/document/d/1XVciQ8mC7bHo7bAApRk7hLwmT61MxVWTm2III6rUzsM/edit) |
| Author's own build ([daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve)) | All Unique except Bracelet 2 (Epic). Nuakum armor set with Robe of Flame on every piece, rings with Hellfire / Wish of Concentration / Flame Arrow lines, Noble Belt, Revelation Amulet, Talisra Wings, Clash Runes +1. Armor, cloak, earrings, rings, guard and bracelets are recorded at +10. It lists items, not line priorities, so the priorities above stay on the Oct 14 sheet. | [daevaos](https://daevaos.com/guides/sorcerer-class-guide-pve) |

[NM]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM buffs]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM classPerformance]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
