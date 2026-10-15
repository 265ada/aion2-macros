# Assassin (殺星) — DPS spec · AION 2 Global

**Patch covered:** Global client build **25926599** (Steam public branch, updated 2026-10-14 06:40 UTC). That is the [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374) on top of the [Oct 6 PDT patch](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544) and the [Oct 8 PDT hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1). None of the three changed an Assassin skill. Build id: [SteamCMD](https://api.steamcmd.net/v1/info/3393110). NotMeter data (week of Oct 7–14) was recorded on the previous build 25800038. **Written:** 2026-10-13, **updated for the Oct 13 patch:** 2026-10-14.

**Tags:** [Global] · [KR/TW-confirmed] = Korean or Taiwanese source checked against the Global client · UNVERIFIED.

**Main data sources:**
- **NM:** [NotMeter Global ranking](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json): parses dated Oct 11–13 UTC (NotMeter's week of Oct 7–14), all Global regions (EU 49%, Asia 23%, NA 26%, LA 2%). Top 20 Assassin parses on each of 15 bosses: 300 parses from 124 players, median CP 150,679, median DPS 62,484. The top 10% is 30 parses from 13 players. (NotMeter has since retired this generation, so the link returns 404; see the [README](README.md).)
- **DB:** [aion2.app Global client DB](https://aion2.app/db/skills?class=Assassin), client dated 18.09.2026.
- **Sheet:** [Global class sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview).
- **Bible:** [Kanon's Bible](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview).
- **Daevaos:** [Assassin Class Guide PVE](https://daevaos.com/guides/assassin-class-guide-pve) (Global, by Castform). Its skill, stigma and gear panels did not load for us, so only its Arcana, Genus and titles were compared. The sheet's Assassin tab does not link to it.
- The [Daeva Archive Assassin guide](https://aion2-assassin-guide.onrender.com/) linked from the sheet is **KR/TW** (patch baseline Aug 12) and is used only as KR context.

**Korea's Sep 16 patch is live on Global.** In Global parses, Shadowstrike's option-2 buff lasts about 10 s (Sep 16 raised it from 5 s; the aion2.app "Global" database still says 5 s), and other classes show Sep 16 cooldowns ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [KR Sep 16 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6aa99cb8a279104f7d9d5c34), [README](README.md)). For Assassin, Sep 16 also added a longer cancel delay on Savage Roar, Savage Smash and Heart Gore, and +10% PvE on Quick, Breaking and Swift Slice and Insignia Explosion. Those are likely live but not measured on Global. Korean macro advice written after Sep 16 (the Inven Sep 30 guide) therefore applies.

---

## 1. Overview

| Item | Recommendation / finding | Why | Source |
|---|---|---|---|
| Role | Melee burst DPS with daggers, from behind the boss | NC: "approaches unseen with deadly silence" | [NC class list](https://aion2.plaync.com/en-us/about/index#classes) |
| Playstyle | <ul><li>**Insignia stacks:** Ambush option 1 (2 on a back hit), Heart Gore option 2 (1 per hit), the Savage Roar chain (Savage Roar, Savage Back Kick and Savage Smash, 1 each), Savage Fang (5), Shadow Fall option 2 (3) and Exploit Weakness clones build them.</li><li>**Insignia Explosion** detonates up to 5 stacks: 20.2% of damage.</li><li>**Heart Gore** triggers only after a crit, and at 16 it resets on crits: 28% of damage.</li><li>**Illusive Clone** removes Heart Gore's cooldown: 10 s at stigma level 1, 20 s at 20.</li></ul> | | [NM], [DB Insignia Explosion](https://aion2.app/db/skills/13130000), [DB Heart Gore](https://aion2.app/db/skills/13350000), [DB Illusive Clone](https://aion2.app/db/skills/13310000), [DB Savage Smash](https://aion2.app/db/skills/13120000), [DB Exploit Weakness](https://aion2.app/db/skills/13720000) |
| Strengths | <ul><li>Top-10% Heart Gore rate: 108 uses/min (median 49.6).</li><li>Many gap closers that put you behind the target (Shadowstrike, Infiltrate, Flash Slice).</li></ul> | | [NM], [DB Shadowstrike](https://aion2.app/db/skills/13070000) |
| Weaknesses | <ul><li>**Must hit from behind:** top Global Assassins land 85% of hits from the back. Rear Smite, Ambush (+30%) and Triniel's Dagger (+30%) are back-attack bonuses.</li><li>**Big gap between players:** at equal CP, the top 10% of these parses (30 parses, 13 players) deal about 83% more than the CP trend line, the widest gap of the 8 classes. One player supplies 13 of those 30 parses.</li></ul> | | [NM], [DB Rear Smite](https://aion2.app/db/skills/13740000), [DB Ambush](https://aion2.app/db/skills/13060000) |
| PvE standing (Global) | **5th of 8.** NotMeter score 96.66. At equal CP: −1.8% (6th) over all ranked parses, or +0.4 to +0.7% (5th) on the top-20 set ([README](README.md#overall-tier-list)). | | [NM classPerformance] |
| PvP standing (Global) | **UNVERIFIED.** Launch-week opinion lists call Assassin a top PvP burst class (low confidence). Korea's Aug 29 write-up calls Assassin PvP stigmas weak ([Inven](https://www.inven.co.kr/board/aion2/6449/20500), KR/TW). | | [ExitLag](https://www.exitlag.com/news/aion-2-class-tier-list/) (opinion) |
| Difficulty | **Medium to high.** Positioning, timing Illusive Clone, and a big skill gap. | | [NM] |
| Who should play it | Players who enjoy staying behind the boss and timing burst windows | | — |

---

## 2. Max damage

### Single target

| Step | What to do | Why | Source |
|---|---|---|---|
| 1 | Get behind the boss (Shadowstrike / Infiltrate / Flash Slice) | 85% back-hit rate for top Global players | [NM], [DB Shadowstrike](https://aion2.app/db/skills/13070000) |
| 2 | **Swift Contract**, then **Illusive Clone** | <ul><li>Swift: +20% Combat Speed. At 10, ×1.5 Rear Smite; at 15, ×1.5 Assault Stance.</li><li>Clone: no Heart Gore cooldown and +20% of damage as extra damage.</li><li>Both last 10 s at stigma level 1, 14.5 s at 10, 17 s at 15 and 20 s at 20, in the DB's per-level data and in Global parses.</li><li>NotMeter logs 2.9 Clone uses/min for the top 10% and 1.2 for the median. These are real casts (1–3 per fight; the extra hits are logged separately). The per-minute rate looks high because 73% of these fights last under 90 s.</li></ul> | [DB Swift Contract](https://aion2.app/db/skills/13390000), [DB Illusive Clone](https://aion2.app/db/skills/13310000), [NM] |
| 3 | **Savage Fang** (if slotted) → **Insignia Explosion** | <ul><li>Savage Fang engraves 5 Insignias. At 15 it adds +10% PvE Damage Boost for 10 s.</li><li>Insignia Explosion's damage scales with stacks.</li></ul> | [DB Savage Fang](https://aion2.app/db/skills/13270000), [DB Insignia Explosion](https://aion2.app/db/skills/13130000) |
| 4 | **Triniel's Dagger** from behind | +30% from behind. At stigma level 10, −10% to all your cooldowns on hit. The Korean Sep 30 guide uses it before Savage Fang for a smoother motion, but says that since Korea's latest patch it no longer cuts Savage Fang's cooldown when pressed first; this guide's inference is to press Savage Fang first to keep the cut (KR/TW; untested on Global). | [DB Triniel's Dagger](https://aion2.app/db/skills/13300000), [Inven Sep 30](https://www.inven.co.kr/board/aion2/6449/24247) |
| 5 | Hold **Quick Slice** + the macro (Insignia Explosion → Heart Gore → Savage Roar; see Macros for Ambush) | <ul><li>Quick Slice option 4: −1 s Insignia Explosion per hit.</li><li>The Quick Slice chain (Swift Slice + Breaking Slice + Quick Slice) is 20% of damage.</li></ul> | [DB Quick Slice](https://aion2.app/db/skills/13010000), [NM] |
| 6 | **Storm Rampage** during stagger | Option 5: −1 s all cooldowns per hit. 69% of top Global players use it (60% of parses), and 56% of those (39% of all players) have it at 16. | [DB Storm Rampage](https://aion2.app/db/skills/13340000), [NM] |

**Line up:** at the §4 target levels, Illusive Clone lasts 20 s (level 20) and Swift Contract 17–20 s (level 15–20). Fit Savage Fang's +10% PvE (10 s, from option 15) and Shadowstrike option 2's +20% Crit Damage Boost (10 s live on Global) inside that window. Savage Roar option 4 cuts Shadowstrike's cooldown by 1 s per hit ([DB Savage Roar](https://aion2.app/db/skills/13100000)). Durations measured in Global parses ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)); the order is derived from them.

### AoE (packs)

| Tool | Targets | Source |
|---|---|---|
| Quick Slice chain, Savage Roar chain, Heart Gore | up to 4 within 4 m | [DB Quick Slice](https://aion2.app/db/skills/13010000), [DB Heart Gore](https://aion2.app/db/skills/13350000) |
| Insignia Explosion, Savage Fang | up to 4 within 4 m | [DB](https://aion2.app/db/skills/13130000) |
| Flash Slice | up to 4; option 4 adds a second use | [DB](https://aion2.app/db/skills/13050000) |
| Whirlwind Slice option 2 | AoE | [DB](https://aion2.app/db/skills/13210000) |
| Throw Shadowblade (stigma) | 10: resets on kill; 20: AoE | [DB](https://aion2.app/db/skills/13020000) |

**AoE order:** UNVERIFIED (no Global test). The same held Quick Slice + macro hits 4 targets. Korean guides call Throw Shadowblade essential for field farming ([vortexgaming KR May](https://vortexgaming.io/postdetail/854915), KR/TW).

---

## 3. Macros

The in-game macro: Settings → Key Settings → General → Gameplay → Macro ([Allyria §3.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Row 0 fires first.

### Macro A: one line without Ambush (recommended by Global data)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Insignia Explosion | Heart Gore | Savage Roar | — | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) (row 1 there is Smoke Bomb, a stigma not in the Global four, so it's left out), [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |

- **Hold:** Quick Slice (left click) + the macro. **Delay:** 10 ms.
- **Press yourself:**
  - Illusive Clone, Swift Contract, Triniel's Dagger and Savage Fang;
  - Shadowstrike and Flash Slice;
  - Q: Infiltrate + Shadow Fall;
  - E: Whirlwind Slice + Storm Rampage, held during stagger.
- **Why no Ambush:** in Global parses at equal CP, Ambush users trail on all 15 bosses. Averaged per player: −7% (86 players with Ambush vs 51 without; 95% range about −14% to 0%). Of the top-10% parses (13 players), only 4 parses from 3 players use Ambush. This is observational data (independent re-check, [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)).

### Macro B: Korean Sep 30 line with Ambush in row 1

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Insignia Explosion | Ambush | Heart Gore | Savage Roar | [Inven Sep 30 guide](https://www.inven.co.kr/board/aion2/6449/24247) [KR/TW; post-Sep-16, and Sep 16 is live on Global] |

- **Skill queue:** ON (the guide's setting).
- **What the guide measured:** a slight overall gain on the training dummy. Its boss gain was argued from boss defense, not measured.
- **What Global data shows:** Ambush users do worse (see Macro A), so this is the alternative.

### Banned or nerfed on Global

| Item | Status | Source |
|---|---|---|
| In-game macro | Allowed | [Allyria FAQ](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| External macro software or hardware | **Risk.** NC's unauthorized-program rule (Integrated Account Ban); macros named in the Oct 10, Oct 12 and Oct 14 ban waves. The Korean Daeva Archive guide also says not to assume external automation is allowed. | [NC Operation Policy](https://www.plaync.com/policy/operation/aion2global), [NC notice](https://aion2.plaync.com/en-us/board/notice/view?articleId=6acaa7506b722c561dc6aae9), [Daeva Archive](https://aion2-assassin-guide.onrender.com/) |
| Assassin macro nerfs on Global | Korea's Sep 16 cancel-delay change (Savage Roar, Savage Smash, Heart Gore) is likely live, because Sep 16 is in the live client. No Assassin change in the Oct 6, Oct 8 or Oct 13 notes. | [Oct 13](https://store.steampowered.com/news/app/3393110/view/1846651706673374), [Oct 6](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544), [Oct 8](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1), [KR Sep 16](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6aa99cb8a279104f7d9d5c34) |

---

## 4. Stigmas

**Global rules:** 4 slots, cap 20, free resets ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). No rarity, so "n/a" ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

**Global usage (top 20 per boss, share of players):** Illusive Clone 98% (median 20), Swift Contract 95% (15), Triniel's Dagger 91%, Evasion Stance 47% (5; 38% of parses), Savage Fang 43% (15) ([NM]).

### PvE

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Illusive Clone | Slot 1 | **20** (10 first) | n/a | <ul><li>10: +20% Crit Damage Boost in the window.</li><li>15: ×1.5 Exploit Weakness.</li><li>20: 50% chance of extra damage on crit.</li><li>Global median 20.</li></ul> | [DB](https://aion2.app/db/skills/13310000), [NM] |
| Swift Contract | Slot 2 | **15**, then 20 | n/a | <ul><li>10: ×1.5 Rear Smite.</li><li>15: ×1.5 Assault Stance.</li><li>20: +10% more Combat Speed.</li><li>Global median 15.</li></ul> | [DB](https://aion2.app/db/skills/13390000), [NM] |
| Triniel's Dagger | Slot 3 | **10** | n/a | <ul><li>10: −10% all your cooldowns on hit.</li><li>15 resets on kill.</li><li>20 raises the cooldown increase on the target from 5% to 8% of duration (questlog's level text), an enemy-side effect, so treat it as a skip.</li><li>Korean guides stop it at 10 ([vortexgaming KR](https://vortexgaming.io/postdetail/601044), KR/TW).</li></ul> | [DB](https://aion2.app/db/skills/13300000), [questlog](https://questlog.gg/aion-2/api/trpc/database.getSkill?input=%7B%22id%22%3A%2213300000%22%2C%22language%22%3A%22en%22%7D) |
| Savage Fang | Slot 4 (damage) | **15** | n/a | 5 Insignias. 15: +10% PvE Damage Boost for 10 s. 20: always crits. Global 43%, median 15. No measurable damage difference vs Evasion Stance at equal CP: per player −4% to −5% (51 vs 55 players; 95% range about −11% to +2%), per parse +6% to +7%. The sign flips with the method ([method](README.md#method-notes)). Savage Fang appears in 15 of the 30 top-10% parses, against 2 for Evasion Stance. | [DB](https://aion2.app/db/skills/13270000), [NM] |
| Evasion Stance | Slot 4 (survival, learning fights) | **5** | n/a | Guaranteed evasion. 5: a second use. Global 47%, median 5. | [DB](https://aion2.app/db/skills/13080000), [NM] |

**Shard order (this guide's, from the Global medians and DB breakpoints):** Illusive Clone 10 → Swift Contract 10 → Triniel's Dagger 10 → (Savage Fang 15 or Evasion Stance 5) → Swift Contract 15 → Illusive Clone 15 → Illusive Clone 20 → Swift Contract 20. Korea's May guide ([vortexgaming KR](https://vortexgaming.io/postdetail/854915), KR/TW) puts Savage Fang alongside Clone and Swift at 10+ first, then Triniel's Dagger 10, Evasion Stance 5 and Throw Shadowblade 10. It covers 6 slots and has no 15/20 steps.

### PvP

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Swift Contract | Core | 20 | n/a | Combat Speed | [DB](https://aion2.app/db/skills/13390000) |
| Evasion Stance | Core | 20 | n/a | Two dodges; 15: move speed; 20: 10% HP | [DB](https://aion2.app/db/skills/13080000) |
| Smoke Bomb | Core | 20 | n/a | Blind; 10: AoE; 20: second use | [DB](https://aion2.app/db/skills/13250000) |
| Shadow Walk | 4th | 20 | n/a | Stealth opener. The Korean Aug 29 review says Illusive Clone isn't used in PvP. | [DB Shadow Walk](https://aion2.app/db/skills/13180000), [Inven Aug 29](https://www.inven.co.kr/board/aion2/6449/20500) (KR/TW) |

This is **this guide's own pick and UNVERIFIED for Global**, built from the DB effects. The Korean Aug 29 post ([Inven](https://www.inven.co.kr/board/aion2/6449/20500), KR/TW) is a review of all 13 stigmas, not a build. It calls Swift Contract the one still worth taking (for its attack-power bonus), Smoke Bomb marginal but used, and Illusive Clone not used in PvP.

### Solo / farming

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Throw Shadowblade | Replaces Triniel's Dagger | **20** (10 minimum) | n/a | 10: resets on kill. 20: AoE. | [DB](https://aion2.app/db/skills/13020000), [vortexgaming KR May](https://vortexgaming.io/postdetail/854915) (KR/TW) |
| Illusive Clone / Swift Contract / Savage Fang | Keep | 10 / 15 / 15 | n/a | | [DB](https://aion2.app/db/skills?class=Assassin) |

---

## 5. Skills

Global rules:
- Specialty breakpoints are 8, 12, 16 and 20.
- Skill points take a skill to 10; levels 11–20 come from ring lines, blue Daevanion tiles and Arcana ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)). Weapon and guard carry no skill lines in the Global line lists.
- Sources: [Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview); Season 1 has 5 Arcana ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).

### Actives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Heart Gore | 1st | **20** (16 is mandatory) | n/a | 28% of damage. 88% of top Global players at 16+, 21% at 20. | [NM], [DB](https://aion2.app/db/skills/13350000) |
| Insignia Explosion | 2nd | **16**, then 20 | n/a | 20.2% of damage. 77% at 16+. 16: −3 s cooldown. | [NM], [DB](https://aion2.app/db/skills/13130000) |
| Quick Slice | 3rd (held) | **16**, then 20 | n/a | Its chains are 20% of damage. 70% at 16+. 12: −1 s Insignia Explosion per hit. | [NM], [DB](https://aion2.app/db/skills/13010000) |
| Storm Rampage | Stagger | **16** | n/a | Used by 69% of top Global players (60% of parses); 56% of those (39% of all) are at 16+ | [NM] |
| Savage Roar | Filler | **12** (the sheet says 16) | n/a | Chain about 10% of damage. 0% of top Global players are past 12 (2+4 at 12). Korea's top 20: level 20. | [NM], [NotMeter KR](https://notmeter.com/?view=setup-guide), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Ambush | Optional (Macro B row 1) | **12** | n/a | 1+2 at 12 (about half of Ambush parses). Ambush appears in 66% of top parses (69% of players), but its users trail at equal CP (see Macros). 14% at 16+. | [NM], [DB](https://aion2.app/db/skills/13060000) |
| Shadowstrike | Burst helper | **12** | n/a | Option 2: +20% Crit Damage Boost for 10 s (the aion2.app DB still says 5 s; questlog's Global data and Global parses show 10 s). Global 2+3 56%. | [NM], [DB](https://aion2.app/db/skills/13070000), [questlog](https://questlog.gg/aion-2/api/trpc/database.getSkill?input=%7B%22id%22%3A%2213070000%22%2C%22language%22%3A%22en%22%7D) |
| Flash Slice, Infiltrate, Shadow Fall, Whirlwind Slice | Mobility / utility | **12** | n/a | Sheet levels; Global picks below | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NM] |
| Defiance | CC break | **16** (sheet) | n/a | Global 3 (57%) | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

### Passives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Rear Smite | 1st | as high as gear allows (KR 36) | n/a | +3% Back Damage Boost, +3% PvE Damage Boost. ×1.5 at Swift Contract 10. | [DB](https://aion2.app/db/skills/13740000), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Assault Stance | 2nd | as high as gear allows (KR 33) | n/a | +6% Crit Damage Boost | [DB](https://aion2.app/db/skills/13750000) |
| Exploit Weakness | 3rd | **17+** (Global median 17; KR 27) | n/a | +100 Crit, Attack proc; 3.0% of damage | [DB](https://aion2.app/db/skills/13720000), [NM buffs] |
| Impact Hit | 4th | KR 24 | n/a | Double Chance | [DB](https://aion2.app/db/skills/13760000) |
| Ambush Stance | 5th | **15** (Global median) | n/a | 3.3% of damage | [NM buffs], [DB](https://aion2.app/db/skills/13770000) |
| Determination | Low | KR 18 | n/a | 2.1% of damage (targets at ≤30% HP) | [NM], [DB](https://aion2.app/db/skills/13800000) |
| Defense Break, Apply Poison, Heightened Sixth Sense, Revitalization Contract | Filler | 10–15 | n/a | KR 13–15 | [NotMeter KR](https://notmeter.com/?view=setup-guide) |

"NM buffs" = buff levels from the same Global parses.

---

## 6. Specializations

| Item | Recommendation (picks at 8 / 12 / 16 / 20) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Heart Gore | 2 / 2+4 / **4+5** / 2+4+5 | 20 | n/a | <ul><li>2: Insignia per hit.</li><li>4: multi-hit.</li><li>5: resets on crit.</li><li>Global top: 4+5 55%, 3+4+5 15%.</li><li>At 20, the third pick differs: sheet 2, Korea 1, Global 3.</li></ul> | [NM], [DB](https://aion2.app/db/skills/13350000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Insignia Explosion | 2 / 2+3 / **2+5** / 2+3+5 | 20 | n/a | <ul><li>2: multi-hit.</li><li>3: keep 2 stacks.</li><li>5: −3 s cooldown.</li><li>Global 2+5 55%, 2+3 21%.</li></ul> | [NM], [DB](https://aion2.app/db/skills/13130000) |
| Quick Slice | 3 / 3+4 / **4+5** / 3+4+5 | 20 | n/a | <ul><li>4: −1 s Insignia Explosion per hit.</li><li>5: ignores Block/Evasion and crits.</li><li>Global 4+5 59%.</li></ul> | [NM], [DB](https://aion2.app/db/skills/13010000) |
| Savage Roar | 2 / **2+4** / — / 2+3+4 (Korea) | 12 | n/a | <ul><li>4: −1 s Shadowstrike per hit.</li><li>Global 2+4 68%.</li><li>The sheet's 2+3 is the minority (30%).</li></ul> | [NM], [DB](https://aion2.app/db/skills/13100000) |
| Ambush | 1 / **1+2** | 12 | n/a | <ul><li>1: 2 Insignias on a back hit.</li><li>2: absorb 3% HP.</li><li>Don't take option 5 (+2 uses): Korea's Sep 30 guide says it slowed the motion and lowered damage. Korea's top 20 run 4+5 at 16 anyway, an internal KR conflict.</li></ul> | [NM], [DB](https://aion2.app/db/skills/13060000), [Inven Sep 30](https://www.inven.co.kr/board/aion2/6449/24247) |
| Storm Rampage | 1 / 1+4 or 4 / **4+5** at 16 | 16 | n/a | Option 4 unlocks at 12. Global 4+5 45%, 1+4 30% (of users with picks). | [NM], [DB](https://aion2.app/db/skills/13340000) |
| Shadowstrike | 2 / **2+3** | 12 | n/a | Global 56% | [NM] |
| Flash Slice | 2 / **2+4** | 12 | n/a | Global 88% | [NM] |
| Infiltrate | 1 / **1+2** | 12 | n/a | Global 59% | [NM] |
| Defiance | 3 / 3+4 / 3+5 | 16 | n/a | Global 3 57% | [NM] |
| Whirlwind Slice | 1 / 1+3 | 12 | n/a | Sheet | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Shadow Fall | 1 / 1+2 | 12 | n/a | Sheet. Korea runs 1+3. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

**PvP changes (UNVERIFIED, from the DB):** Quick Slice option 5 (ignores Block/Evasion) is mandatory, and Shadowstrike option 3 (Seal) gains value.

### Daevanion boards (Global)

| Item | Recommendation | Target | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Points | About 316 at 45, +50 Shugo, +50 Nightmare | — | n/a | | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Main four boards | <ul><li>Orange > Blue > Green > White.</li><li>Heart Gore, Insignia Explosion and Quick Slice blue tiles at 8 / 12 / 16 / 20.</li><li>Rear Smite and Assault Stance green tiles.</li></ul> | — | n/a | | [Allyria ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Bible ch.7](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| White tiles | Attack first. Crit tiles have little value, because top Global Assassins already sit at the 50% crit cap. | — | n/a | | [Genus audit](../docs/genus-audit.md), [Bible ch.3](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Skip (PvE) | Multi-hit Resist, Crit Damage Tolerance | — | n/a | | [Bible ch.7](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |

A tile-by-tile path is UNVERIFIED (no Global Assassin board guide).

---

## 7. Tier list

| Content | Tier | Placement reason | Source |
|---|---|---|---|
| PvE | **B** (5th of 8) | NotMeter score 96.66; −1.8% at equal CP. High skill ceiling: the top 10% sit about 83% above the CP trend line. | [NM classPerformance] |
| PvP | **UNVERIFIED** (community: S) | No Global PvP data | [ExitLag](https://www.exitlag.com/news/aion-2-class-tier-list/) (opinion) |
| Solo / farming | **B (opinion, UNVERIFIED)** | Throw Shadowblade resets on kill and goes AoE at 20; squishy | [DB](https://aion2.app/db/skills/13020000) |

---

## 8. Gear

Global rules:
- **Unique is the settle rarity** for every slot; there's no Heroic gear in Season 1 ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- Crafted gear (5 lines) is best in slot.
- Phases: [README](README.md#gear-phases).

**A sheet error to avoid:** the Global sheet's Assassin armor rows list Spirit Strike, Mental Focus (Spiritmaster passives) and Wind's Promise (a Chanter passive). Those lines don't exist for Assassin. The rows below swap in the Assassin passives from the sheet's own accessory row (Rear Smite > Assault Stance > Exploit Weakness).

| Item | Recommendation (stat lines in order) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Weapon (daggers) | Weapon Damage Boost > Combat Speed > Might > Precision > Damage Boost > Multi-hit > Attack | **+17** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Guard | Weapon Damage Boost > Combat Speed > Damage Boost > Might > Precision > Multi-hit > Attack | **+17** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Helmet | Incoming Heal > Rear Smite > Assault Stance > Double Chance > Attack Increase > Crit > Attack | **+15** | Unique | Passives corrected (see above) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Shoulders | Crit Damage Boost > Rear Smite > Assault Stance > Accuracy > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Chest | Damage Boost > Rear Smite > Assault Stance > Accuracy > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Legs | Damage Tolerance > Rear Smite > Assault Stance > Perfect > Attack Increase > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Gloves / Boots | Combat Speed / Move Speed > Rear Smite > Assault Stance > Perfect > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Cloak | Rear Smite > Assault Stance > Impact Hit > Double Chance > Attack Increase > Attack | **+15** | Unique | No Perfect on capes on Global. The sheet's cape row starts with "Wind's Promise" (a Chanter passive, another copy error) then Impact Hit and Smite (= Double Chance). | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Earrings / Necklace | Rear Smite > Assault Stance > Exploit Weakness > Might > Precision > Accuracy > Attack | **+16** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Rings | Heart Gore > Insignia Explosion > Quick Slice > Might > Precision > Attack | **+17** | Unique | Korea's top-20 ring lines (100% each): Savage Roar, Insignia Explosion, Quick Slice, Heart Gore; then Ambush 80%, Storm Rampage 60% (Oct 14 snapshot) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Bracelets | Wisdom > Destruction > Time > Illusion. Skip Death (crit) on Global: Assassin skills that don't auto-crit already land crits about 50–56% of the time in Global parses, at the 50% stat cap. | **+15** | Unique (slot 1); Epic / blue (slot 2) | The Bible's Global update states the 50% cap; Korea's Sep 30 guide also says Freedom and Death aren't needed in PvE | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Bible ch.3](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview), [NM], [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Belt / Amulet | To Gold | Gold | Gold | | [Allyria §6.1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Clash Runes | | **+5 to +7** | n/a | Upgrades are very RNG-heavy (Allyria); runes are destroyed on a failed upgrade (Bible ch.2) | [Allyria §6.1.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Bible ch.2](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |

| Other | Recommendation | Source |
|---|---|---|
| Manastones | **Back Damage Boost** > Weapon Damage Boost ≈ Crit Damage Boost > Damage Boost > Attack | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Bible ch.5](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Arcana | Chalice Time · Parchment Life/Destiny · Compass Freedom (not Death; crit-capped) · Bell Destruction · Mirror Illusion/Wisdom. Skill lines: Rear Smite, Assault Stance, Heart Gore, Insignia Explosion. The daevaos Global guide's Chalice (Vigor set, Time) lists Heart Gore, Insignia Explosion, Quick Slice and Rear Smite | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR Arcana](https://notmeter.com/?view=setup-guide), [daevaos](https://daevaos.com/guides/assassin-class-guide-pve) |
| Pet Genus | <ul><li>Special line 4: Double Chance.</li><li>Line 4 on other boards: PvE Damage Boost. Varian line 4: Back Damage Boost ≈ PvE Damage Boost.</li><li>Lines 3/6/9: **Power Shard Damage Bonus** (crit-capped; the daevaos Global guide lists Accuracy 40 / Crit 30 there, and the Bible prefers Crit and Accuracy only below their caps).</li><li>Lines 1/5: Max Attack.</li><li>Line 7: PvE Damage Tolerance.</li></ul> | [Genus audit](../docs/genus-audit.md), [daevaos](https://daevaos.com/guides/assassin-class-guide-pve), [Bible](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Wings | Talisra (Season Shop) is the Global end goal (CDR). The Global sheet lists Awakened Pride wings (back damage), but its percentages are copied from the Bible's KR Chanter figures. Korea's Assassin pick is Talisra 58% / Awakened Pride 30%. Awakened Pride on Global is UNVERIFIED. | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Bible ch.9](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |

[NM]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM buffs]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM classPerformance]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
