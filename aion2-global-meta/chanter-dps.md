# Chanter (護法星) — Support-DPS spec (buffer) · AION 2 Global

**Patch covered:** Global client build **25926599** (Steam public branch, updated 2026-10-14 06:40 UTC). That is the [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374) on top of the [Oct 6 PDT patch](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544) and the [Oct 8 PDT hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1). None of the three changed a Chanter skill. Build id: [SteamCMD](https://api.steamcmd.net/v1/info/3393110). NotMeter data (week of Oct 7–14) was recorded on the previous build 25800038. **Written:** 2026-10-13, **updated for the Oct 13 patch:** 2026-10-14.

**Tags:** [Global] · [KR/TW-confirmed] = Korean or Taiwanese source checked against the Global client · UNVERIFIED.

**Main data sources:**
- **NM:** [NotMeter Global ranking](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), week of Oct 7–14. Top 20 Chanter parses on each of 15 bosses: 300 parses from 104 players, median CP 148,978, median DPS 76,433. (NotMeter has since retired this generation, so the link returns 404; see the [README](README.md).)
- **DB:** [aion2.app Global client DB](https://aion2.app/db/skills?class=Chanter), client dated 18.09.2026.
- **Sheet:** [Global class sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview).
- **Sheet snapshot:** citations of this class's sheet tab refer to the copy downloaded on Oct 14. Later that day the author replaced the tab with a link to [daevaos](https://daevaos.com/guides/chanter-quick-guide), where the build is now maintained; differences found are noted where they matter.

**The other Chanter spec:** [chanter-battle-healer.md](chanter-battle-healer.md) covers parties without a Cleric. In those, the Chanter is the main healer 93% of the time ([NM]).

**Korea's Sep 16 patch is live on Global.** Global parses show Korea's Sep 16 changes are live: Templars show a second Noble Armor buff in 452 of 507 Templar fights longer than 130 s, and Chanters a second Guardian Blessing in 85 of 93 (buff applications; one cast never lasts past 120 s) (Sep 16 cut both cooldowns from 5 min to 2 min). Assassin Shadowstrike's option-2 buff lasts about 10 s (Sep 16 raised it from 5 s) ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [KR Sep 16 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6aa99cb8a279104f7d9d5c34)). The aion2.app "Global" database (client 18.09.2026) still shows the older values, so it is an older client snapshot (dated Sep 18). For Chanter that means **Guardian Blessing has a 2-min cooldown** (live Chanters recast it in 85 of 93 fights longer than 130 s). Korea's Sep 23 change (Undefeated Mantra and Power of the Storm disabled during Battlefield Might in Abyss bosses and Rifts) is UNVERIFIED on Global. The Aug 26 rework is live: Dark Crush opens after any ranged skill, Korea's Sep 2 patch then set Spinning Strike back to a 30 s cooldown (25 s with option 1) and Impactful Crush to 15 s, which is what the Global DB shows ([KR Sep 2 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6a9727b8fa34c1011d627551)) ([DB Dark Crush](https://aion2.app/db/skills/18100000), [DB Spinning Strike](https://aion2.app/db/skills/18290000)).

**Watch (Korea only, not on Global):** Korea's Oct 14 update changed Rushing Smash (defense plus all-element resistance up to 80%; its cooldown-reduction effect removed) and Focused Defense (−0.3 s cooldown per successful block) ([KR Oct 14 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6ace86b86cfe4756db5b8d81)). Global's Oct 13 notes have neither.

---

## 1. Overview

| Item | Recommendation / finding | Why | Source |
|---|---|---|---|
| Role | Melee support DPS (staff) who buffs the party | NC: "bolsters allies with divine blessings" | [NC class list](https://aion2.plaync.com/en-us/about/index#classes) |
| Playstyle | <ul><li>**Dark Crush** opens for 2 s after a ranged skill (Spinning Strike, Impactful Crush; 3 s after Marchutan's Wrath) and has no cooldown at 16. With its Piercing Strike chain it's **31.5%** of damage.</li><li>Incandescent Blow + its Bursting Blow chain: 26.9%.</li><li>Spinning Strike: 11.9%.</li></ul> | | [NM], [DB Dark Crush](https://aion2.app/db/skills/18100000) |
| Party value | <ul><li>**Undefeated Mantra:** party PvE damage and tolerance (10.5% at level 1, 17.5% at 15, **20% at 20**). It doesn't stack with Light of Protection; the higher level wins, and Mantra wins ties.</li><li>**Power of the Storm:** party +20% Combat Speed and −10% cooldowns. It can't be received while a Cleric's Earth's Blessing is active.</li><li>**Earth's Promise:** −5.4% enemy PvE Damage Tolerance. It doesn't stack with Chain of Torment.</li></ul> | | [DB Undefeated](https://aion2.app/db/skills/18190000), [DB Storm](https://aion2.app/db/skills/18250000), [DB Earth's Promise](https://aion2.app/db/skills/18780000) |
| Strengths | **Top Global class:** NotMeter score 118.79 (1st) and +22.0% at equal CP (1st). The in-game macro covers most of the damage. | | [NM classPerformance] |
| Weaknesses | <ul><li>Buff management on top of the rotation.</li><li>Its buffs clash with Cleric buffs (Light of Protection, Earth's Blessing).</li><li>Mantras are toggles: a second press turns them off, so never put them in the macro.</li></ul> | | [DB](https://aion2.app/db/skills/18190000), [repo KR notes](../data/classes.json) |
| PvE standing (Global) | **1st of 8** | | [NM classPerformance] |
| PvP standing | **UNVERIFIED** (no Global data) | | — |
| Difficulty | **Low to medium.** One macro entry plus held Onslaught. Pressing Marchutan's Wrath, Power of the Storm and the mantras is the skill part. | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Who should play it | Players who want top damage plus party value. **The easiest high-damage class on Global right now.** | 1st at equal CP, with a one-entry macro | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

---

## 2. Max damage

### Single target

| Step | What to do | Why | Source |
|---|---|---|---|
| Pre-pull | Toggle **Undefeated Mantra** and **Sprint Mantra** on | Toggles; party buffs | [DB Undefeated](https://aion2.app/db/skills/18190000), [DB Sprint](https://aion2.app/db/skills/18160000) |
| Open | **Power of the Storm** | <ul><li>You: +20% Combat Speed and −20% cooldowns. Party: +20% / −10%. Lasts 10 s at level 1, 12 s at 5, 14.5 s at 10, 17 s at 15 and 20 s at 20 ([questlog](https://questlog.gg/aion-2/en/db/skill/18250000)).</li><li>5: −30 s cooldown (120 → 90 s).</li><li>20: +20% Attack for you, +10% for the party.</li></ul> | [DB](https://aion2.app/db/skills/18250000) |
| Core | Hold **Onslaught** (left click) + the macro: Dark Crush → Spinning Strike → Impactful Crush → Incandescent Blow | <ul><li>Each opener gives a 2 s Dark Crush window. With option 5 (16) Dark Crush fires on every macro turn inside it.</li><li>Onslaught option 4: −1 s Spinning Strike per hit.</li><li>Onslaught option 5: Storm Chain, 7.2% of damage.</li></ul> | [DB Onslaught](https://aion2.app/db/skills/18010000), [NM] |
| Extend | Press **Marchutan's Wrath** between Spinning Strike / Impactful Crush windows | It opens a 3 s window. This is this guide's rule, not the sheet's; nearly every top Global Chanter slots Marchutan's Wrath (97%), and casters vs non-casters at equal CP differ by −2% (not significant). | [DB](https://aion2.app/db/skills?class=Chanter), [NM] |
| Stagger | **Gust Rampage** only while the stagger bar is up | −1 s all cooldowns per hit at 16. Gust Rampage users measured 6–9% lower at equal CP; NotMeter can't tell when it was used. The sheet lists it as N/A. | [DB](https://aion2.app/db/skills/18300000), [repo plans](../data/plans.json) |

**Line up:** Power of the Storm (20 s at level 20; the DB's 10 s is level 1) and Spinning Strike's +15% Crit Damage stacks (2× for 30 s). Keep the Spinning Strike stacks up at all times. Derived from the DB durations; stigma buff durations measured in Global parses ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)).

**Check:**
- **Global:** median top-20 Chanters log 25 Dark Crush uses a minute and the top 10% by damage at equal CP log 35, counting whole boss fights including downtime ([NM]). Without option 5, expect about 5–9.
- **Korean dummy:** the post says the 122.6% Combat Speed cap "suddenly became useless", that the skill macro should stay minimal, and that Marchutan's Wrath is no longer mandatory ([Inven Sep 17](https://www.inven.co.kr/board/aion2/6451/22932), KR/TW).

### AoE

| Tool | Targets | Source |
|---|---|---|
| Onslaught, Incandescent Blow + chains, Heat Wave Blow | up to 4 within 4 m | [DB](https://aion2.app/db/skills?class=Chanter) |
| Spinning Strike, Marchutan's Wrath, Rushing Smash | up to 4 | [DB Spinning](https://aion2.app/db/skills/18290000) |
| Impactful Crush option 1 | becomes AoE | [DB](https://aion2.app/db/skills/18060000) |

The same macro works on packs. The AoE order is UNVERIFIED.

---

## 3. Macros

The in-game macro: Settings → Key Settings → General → Gameplay → Macro ([Allyria §3.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Rows are numbered from the bottom (row 0 is next to the hotbar); this guide treats row 0 as the highest priority, which is UNVERIFIED on Global (see [README](README.md)).

### Macro A: Global sheet layout, one entry (recommended)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Dark Crush | Spinning Strike | Impactful Crush | Incandescent Blow | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

- **Delay:** 10 ms (the sheet's Chanter and Tips screenshots; Korean setups use the same). The [daevaos build](https://daevaos.com/guides/chanter-quick-guide) has the same four rows and a 10 ms delay, with Onslaught on left click and the macro column on right mouse; Tremor Crush and Wave Blow sit on Q, the Mantras and Power of the Storm on separate keys.
- **Hold:** Onslaught (left click) + the macro.
- **Press yourself:**
  - Marchutan's Wrath, between windows;
  - Power of the Storm;
  - Undefeated Mantra and Sprint Mantra (toggles; never in the macro);
  - Recuperation, Rushing Smash, Gust Rampage (stagger);
  - Q: Tremor Crush + Wave Blow.
- **How it plays:** Dark Crush on row 0 is ready on every macro turn while a window is open. When the window closes, the macro falls to the openers, then to Incandescent Blow. That is the same priority a perfect player follows.

### Macro B: Korean two-line test (alternative)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Dark Crush | Spinning Strike | Marchutan's Wrath | Incandescent Blow | [Inven Sep 3](https://www.inven.co.kr/board/aion2/6451/22314) [KR/TW-confirmed: written for the Sep 2 cooldowns (Spinning Strike 30 s, Impactful Crush 15 s), which the Global DB shows] |
| 2 | Impactful Crush | — | — | — | same |

It separates the openers so their windows don't overlap: 3–5 more Dark Crush casts than other setups in one player's full-auto dummy test (single source; the post gives no time window).

### Banned or nerfed on Global

| Item | Status | Source |
|---|---|---|
| In-game macro | Allowed | Built-in setting ([Allyria §3.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)) |
| External software (the sheet's "Option 2" mouse button holding left click + macro) | **Risk.** NC's unauthorized-program rule; macros named in the Oct 10, Oct 12 and Oct 14 ban waves. | [NC Operation Policy](https://www.plaync.com/policy/operation/aion2global), [Oct 10 notice](https://aion2.plaync.com/en-us/board/notice/view?articleId=6acaa7506b722c561dc6aae9), [Oct 14 notice](https://store.steampowered.com/news/app/3393110/view/1846651706673527) |
| Chanter nerfs on Global | None in the Oct 6, Oct 8 or Oct 13 notes. Korea's Sep 23 Battlefield Might rule is UNVERIFIED on Global. | [Oct 13](https://store.steampowered.com/news/app/3393110/view/1846651706673374), [Oct 6](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544), [Oct 8](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1) |

---

## 4. Stigmas

**Global rules:** 4 slots, cap 20, free resets ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). No rarity, so "n/a" ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

**Global usage (top 20 per boss, per player, 104 players):** Marchutan's Wrath about 97% (median 5), Undefeated Mantra about 96% (20; 98% counting a second Chanter's), Power of the Storm about 81% (20), Sprint Mantra 81% (10), Guardian Blessing 25% (15), Focused Defense 10% (5) ([NM]).

### PvE (what top Global Chanters run)

The sheet's own priority is 1. Undefeated Mantra (20), 2. Power of the Storm (5+), 3. Sprint Mantra (1+), 4. Focused Defense (5), with Guardian Blessing, Impeding Authority and Marchutan's Wrath listed as swaps ([Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)). Marchutan's Wrath in slot 4 below follows Global data (about 97% of top players). The [daevaos build](https://daevaos.com/guides/chanter-quick-guide) (the author's own level-45 character) slots the sheet's four: Undefeated Mantra 20, Power of the Storm 20, Sprint Mantra 15 (this guide's target is 10) and Focused Defense 5.

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Undefeated Mantra | Slot 1 | **20** | n/a | <ul><li>5: +100 Crit.</li><li>10: +100 Accuracy.</li><li>15: +5% Crit Damage.</li><li>20: +5% Double Chance.</li><li>Higher level wins against Light of Protection.</li><li>Global median 20.</li></ul> | [DB](https://aion2.app/db/skills/18190000), [NM] |
| Power of the Storm | Slot 2 | **20** (5 is the cheap big step) | n/a | 5: −30 s cooldown. 20: +20% / +10% Attack. Global median 20. | [DB](https://aion2.app/db/skills/18250000), [NM] |
| Sprint Mantra | Slot 3 | **10** | n/a | <ul><li>Party move speed (10.5% at level 1, 15% at 10, 20% at 20) and heal on hit.</li><li>5: +10% Incoming Heal.</li><li>10: stamina.</li><li>Two Chanters don't stack it; the higher level applies (DB; Global buff uptimes agree).</li><li>Global median 10.</li></ul> | [DB](https://aion2.app/db/skills/18160000), [NM] |
| Marchutan's Wrath | Slot 4 | **5** | n/a | The 3 s Dark Crush window works from level 1. 5: up to +20% damage on few targets. 10–20 add PvP effects. Global median 5. | [DB](https://aion2.app/db/skills/18330000), [NM] |
| Guardian Blessing | Swap (damage / survival) | **15** | n/a | <ul><li>15: ×1.5 Wind's Promise. 2-min cooldown on live Global (Sep 16); recast it with Power of the Storm.</li><li>At equal CP, Guardian Blessing users (11 players) were about 9% ahead of Sprint Mantra users (71), averaged per player, but the 95% range is −1% to +21%, so this isn't significant. Two-Chanter parties don't explain it: both Chanters run Sprint in 96% of them ([method](README.md#method-notes)).</li></ul> | [DB](https://aion2.app/db/skills/18420000), [NM], [questlog](https://questlog.gg/aion-2/en/db/skill/18420000) |

**Shard order:** derived from the DB breakpoints and the NM medians.

| Step | Stigma levels |
|---|---|
| 1 | Undefeated 5 → Storm 5 → Sprint 5 → Marchutan's 5 |
| 2 | Undefeated 20 |
| 3 | Sprint 10 → Storm 20 |

### PvP

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Marchutan's Wrath | Core | 20 | n/a | 10: stun. 15: −70% Incoming Heal and potion recovery. | [DB](https://aion2.app/db/skills/18330000) |
| Healing Touch | Core | 20 | n/a | Party heal; removes 5 debuffs at 15 | [DB](https://aion2.app/db/skills/18170000) |
| Focused Defense | Core | 20 | n/a | Guaranteed Block | [DB](https://aion2.app/db/skills/18140000) |
| Undefeated Mantra or Power of the Storm | Group PvP | 20 | n/a | Korea's Sep 23 Battlefield Might block is UNVERIFIED on Global | [DB](https://aion2.app/db/skills/18190000) |

**UNVERIFIED for Global.** Korea's Abyss/PvP list ([repo KR](../data/stigmas.json)) cut to 4.

### Solo
Undefeated, Storm, Marchutan's and Focused Defense. A Korean guide says solo Nightmare was much easier with Focused Defense ([Inven](https://www.inven.co.kr/board/aion2/6451/116), KR/TW).

---

## 5. Skills

Specialty breakpoints are 8 / 12 / 16 / 20 ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

### Actives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Dark Crush | 1st | **20** (16 is mandatory) | n/a | <ul><li>18.0% + Piercing Strike 13.5%.</li><li>16 removes the cooldown.</li><li>96% of top Global at 16+, 41% at 20.</li></ul> | [NM], [DB](https://aion2.app/db/skills/18100000) |
| Onslaught | 2nd (held) | **16**, then 20 (sheet: 20) | n/a | <ul><li>12: −1 s Spinning Strike per hit.</li><li>16: Storm Chain (7.2%).</li><li>70% at 16+.</li></ul> | [NM], [DB](https://aion2.app/db/skills/18010000) |
| Spinning Strike | 3rd | **16**, then 20 (sheet: 20) | n/a | 11.9%. 16: always crits, ignores Block. 48% at 16+. | [NM], [DB](https://aion2.app/db/skills/18290000) |
| Incandescent Blow | 4th | **16** | n/a | 12.4% + Bursting Blow 14.5%. 16: multi-hit, ignores Block. 67% at 16+. | [NM], [DB](https://aion2.app/db/skills/18040000) |
| Impactful Crush | Opener | **12** | n/a | 3+4 (67% Global); 4 = +30% skill speed | [NM], [DB](https://aion2.app/db/skills/18060000) |
| Recuperation | Party heal | **16** (Korea 20) | n/a | Option 1 (two casts) at 8; 4 at 12 | [NM], [DB](https://aion2.app/db/skills/18120000) |
| Rushing Smash | Gap closer | **12** | n/a | Global buff median 15. 3+4 (43%) or 1+4. | [NM] |
| Gust Rampage | Stagger only | **16** | n/a | 5: −1 s all cooldowns per hit | [DB](https://aion2.app/db/skills/18300000) |
| Wave Blow, Tremor Crush, Heat Wave Blow | Utility | **12** | n/a | Sheet levels | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Defiance | CC break | **16** (sheet) | n/a | Global 3 (58%) | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

### Passives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Wind's Promise | 1st | as high as possible (KR 36) | n/a | +5.7% at level 1, 19% at 20 Crit Damage Boost plus extra damage on crits (6.1% of Global damage). ×1.5 at Guardian Blessing 15. | [DB](https://aion2.app/db/skills/18800000), [NM] |
| Impact Hit | 2nd | KR 30 | n/a | Double Chance | [DB](https://aion2.app/db/skills/18760000) |
| Attack Preparation | 2nd | KR 30 | n/a | +5.5% at level 1, 15% at 20 PvE Damage Boost, +100 Accuracy | [DB](https://aion2.app/db/skills/18750000) |
| Earth's Promise | Party debuff | KR 19 | n/a | Enemy PvE Damage Tolerance −5.4% at level 1, −9% at 10, −11% at 15, −13% at 20 | [DB](https://aion2.app/db/skills/18780000) |
| Protection Circle | Party shield | **14** (Global median) | n/a | Divine Barrier for the party every 10 stacks | [NM buffs], [DB](https://aion2.app/db/skills/18730000) |
| Inspiring Spell | If room | KR 21 | n/a | +100 Crit, +0.5% Perfect | [DB](https://aion2.app/db/skills/18740000) |

---

## 6. Specializations

| Item | Recommendation (picks at 8 / 12 / 16 / 20) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Dark Crush | 3 / 3+4 / **3+5** / 3+4+5 | 20 | n/a | <ul><li>3: always crits.</li><li>4: Piercing Strike chain.</li><li>5: no cooldown.</li><li>Global 3+4+5 41%, 3+5 38%, 4+5 17%.</li><li>At 16, 3+5 vs 4+5 at equal CP: +1–2%, within noise. Korea's Inven guide recommends 3+5 at 16 and 3+4+5 at 20 ([Inven](https://www.inven.co.kr/board/aion2/6451/116), KR/TW).</li></ul> | [NM], [DB](https://aion2.app/db/skills/18100000), [repo plans](../data/plans.json) |
| Onslaught | 3 / 3+4 / **4+5** / 3+4+5 | 20 | n/a | Global 4+5 63%. Sheet: 3/4/5 at 20. ("2+4+5 for more stable lifesteal" is a repo note, not the sheet's.) Korea's Inven guide uses 2+3+5 at 20 (2+5 before) for the lifesteal ([Inven](https://www.inven.co.kr/board/aion2/6451/116), KR/TW); the [daevaos build](https://daevaos.com/guides/chanter-quick-guide) runs 3+4+5. | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Spinning Strike | 1 / **1+3** / 1+5 / 1+3+5 | 20 | n/a | <ul><li>1: −5 s cooldown; never drop it.</li><li>Global 1+3 50%, 1+5 29%.</li><li>Korea 1+3+5.</li><li>With no Cleric, a Korean note suggests 2+3+5 for healing (KR/TW, untested on Global). Cleric-less Global Chanters still run 1+3 (54%); 1+2 is 5%. See the battle-healer file.</li><li>Sheet: 1/2/3; the [daevaos build](https://daevaos.com/guides/chanter-quick-guide) runs 1+3+5.</li></ul> | [NM], [NotMeter KR](https://notmeter.com/?view=setup-guide), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Incandescent Blow | 3 / 1+3 / **3+5** | 16 | n/a | Global 3+5 61% | [NM] |
| Impactful Crush | 3 / **3+4** | 12 | n/a | Global 67% | [NM] |
| Recuperation | 1 / **1+4** / 1+4 or 1+5 / 1+4+2 (debuffs) or 1+4+5 | 16–20 | n/a | Global 1+4 64% (per player); the [daevaos build](https://daevaos.com/guides/chanter-quick-guide) runs 1+4+5. Third pick (level 20): 2 (cleanse) if the fight has debuffs, otherwise 5. | [NM], [repo KR note](../data/stigmas.json) |
| Rushing Smash | 3 / 3+4 | 12 | n/a | Global 3+4 43%, 1+4 about 30%; the sheet lists 1/4 and the [daevaos build](https://daevaos.com/guides/chanter-quick-guide) runs 1+4 | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Wave Blow | 2 / 2+4 | 12 | n/a | 4: −15% enemy PvE Damage Boost. Global 2+4 41%, 1+4 23%; sheet 1/4; [daevaos](https://daevaos.com/guides/chanter-quick-guide) 2+4. | [NM], [DB](https://aion2.app/db/skills/18080000) |
| Tremor Crush | 2 / 2+3 | 12 | n/a | Sheet | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Heat Wave Blow | 3 / 3+4 | 12 | n/a | Sheet | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Gust Rampage | 4 / 4+5 | 16 | n/a | Korea 4+5; the sheet lists it as N/A | [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Defiance | 3 / 3+4 / 3+5 | 16 | n/a | Global 3 58% | [NM] |

**PvP (UNVERIFIED):** Spinning Strike option 4 (Seal) and option 5 (ignores Block); Marchutan's Wrath at 15 for the heal cut.

### Daevanion boards (Global)

| Item | Recommendation | Target | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Priority | <ul><li>Orange > Blue > Green > White.</li><li>Dark Crush / Onslaught / Spinning Strike blue tiles at 8 / 12 / 16 / 20.</li><li>Wind's Promise green.</li></ul> | — | n/a | | [Allyria ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Bible ch.7](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Global changes | About 316 points at 45 (+100 from shops); orange % 2.5 → 1.5; Ariel removed | — | n/a | | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

A Global Chanter tile path is UNVERIFIED. The [daevaos build](https://daevaos.com/guides/chanter-quick-guide) stores a node path on five boards (Triniel 75 nodes, Vaizel 65, Nezekan 60, Zikel 60, Azphel 22) that only its planner renders; it was not checked against Global data.

---

## 7. Tier list

| Content | Tier | Placement reason | Source |
|---|---|---|---|
| PvE | **S** (1st of 8) | NotMeter score 118.79; +22.0% at equal CP; plus party buffs | [NM classPerformance] |
| PvP | **UNVERIFIED** | | — |
| Solo / leveling | **A (opinion)** | Melee, self-heals (Recuperation, Sprint Mantra), strong damage | [DB](https://aion2.app/db/skills?class=Chanter) |
| Ease of max damage | **Easiest high-damage class** | One macro entry + held Onslaught; 1st at equal CP | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NM] |

---

## 8. Gear

Global rules: **Unique is the settle rarity** for every slot in Season 1 ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). Phases: [README](README.md#gear-phases).

Enhancement targets (+17 / +16 / +15) come from the sheet roadmap's long-term "Ludra Preparations" list; Ludra isn't on Global yet, and early on the sheet says Clash Runes +1 and Unique pieces tapped to +10 ([Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)). The [daevaos build](https://daevaos.com/guides/chanter-quick-guide) shows the author's current gear, not a target: Unique armor and jewelry at +10, staff and guard at +15, Clash Runes at +1, one Unique and one Epic bracelet. Its weapons follow the sheet's order; every armor piece and the cloak carries Attack Preparation, which the sheet lists only for earrings and necklace.

| Item | Recommendation (stat lines in order) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Weapon (staff) | Weapon Damage Boost > Combat Speed > Might > Precision > Damage Boost > Multi-hit > Attack | **+17** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Guard | Same, Damage Boost 3rd | **+17** | Unique | | same |
| Helmet | Incoming Heal > Wind's Promise > Impact Hit > Double Chance > Attack Increase > Crit > Attack | **+15** | Unique | | same |
| Shoulders | Crit Damage Boost > Wind's Promise > Impact Hit > Accuracy > Crit > Attack | **+15** | Unique | | same |
| Chest | Damage Boost > Wind's Promise > Impact Hit > Crit > Accuracy > Attack | **+15** | Unique | | same |
| Legs | Damage Tolerance > Wind's Promise > Impact Hit > Perfect > Attack Increase > Crit > Attack | **+15** | Unique | | same |
| Gloves / Boots | Combat Speed / Move Speed > Wind's Promise > Impact Hit > Perfect > Crit > Attack | **+15** | Unique | | same |
| Cloak | Wind's Promise > Impact Hit > Double Chance (the sheet also lists "Smite", the same stat) > Attack Increase > Crit > Attack | **+15** | Unique | No Perfect on capes on Global per Sirin; the Bible's Global list still has it (see discrepancies) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Bible ch.3](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Earrings / Necklace | Wind's Promise > Impact Hit > Attack Preparation > Might > Precision > Accuracy > Crit > Attack | **+16** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Rings | Dark Crush > Onslaught > Might > Precision > Spinning Strike > Recuperation > Incandescent Blow > Attack | **+17** | Unique | | same |
| Bracelets | Wisdom > Destruction > Time > Illusion > Death | **+15** | Unique (slot 1); Epic / blue (slot 2) | | same, [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Belt / Amulet | Upgrade early, then stop; amulet to +10, then Substance Morph (live sheet) | to Unique (yellow / "gold") | **Unique** | Allyria's "Gold" is the Unique tier (Sirin) | [Allyria §6.1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Clash Runes | Only +1 early on, about +5 later (sheet); Allyria: not past +6/7 | **~+5** (cap +6/7) | n/a | Upgrades are RNG-heavy (Allyria), and a failed upgrade destroys the rune (Bible) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Allyria §6.1.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Bible ch.2](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |

| Other | Recommendation | Source |
|---|---|---|
| Manastones | Front Damage Boost only if you play from the front; otherwise Weapon Damage Boost ≈ Crit Damage Boost > Damage Boost > Attack. Top Global Chanters land a median 64% of hits from **behind** (44% for the CP-adjusted top 10%; Korea's top 20 run Front Damage Boost manastones 85% of the time), so Back Damage Boost fits that positioning, but no Chanter source tests it (UNVERIFIED). | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Genus audit](../docs/genus-audit.md) |
| Arcana | Chalice Time · Parchment Life/Destiny · Compass Death/Freedom · Bell Destruction · Mirror Illusion/Wisdom. Skill lines per card (sheet): Chalice Dark Crush, Wind's Promise, Impact Hit, Onslaught; Parchment Dark Crush, Onslaught, Spinning Strike; Compass Incandescent Blow, Recuperation; Bell Attack Preparation; Mirror Wind's Promise, Impact Hit, Inspiring Spell, Earth's Promise. The [daevaos guide](https://daevaos.com/guides/chanter-quick-guide) agrees: +4 levels in total on Dark Crush and Onslaught from Chalice and Parchment, +4 on Recuperation from the Compass, and the highest Attack Preparation roll on the Bell. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Pet Genus | <ul><li>Special line 4: Double Chance.</li><li>Line 4 on other boards: PvE Damage Boost. Varian: Back Damage Boost ≈ PvE Damage Boost.</li><li>Lines 3/6/9: Critical Hit until the cap (top Global Chanters at about 44%), then Power Shard.</li><li>Lines 1/5: Max Attack; line 7: PvE Damage Tolerance.</li><li>[daevaos](https://daevaos.com/guides/chanter-quick-guide): finish lines 4, 1 and 5 on every board first, then 3/6/9 (Accuracy 40 or Crit 30), then 2/7/8; Special board line 4 is Double Chance 2.5%+ or Front/Back Damage Boost 3%.</li></ul> | [Genus audit](../docs/genus-audit.md) |
| Wings | Talisra (Season Shop); Forest Spirit or Dark Veil Wings until then ([daevaos](https://daevaos.com/guides/chanter-quick-guide)) | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

[NM]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM buffs]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM classPerformance]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
