# Gladiator (劍星) — Tank spec (parties without a Templar) · AION 2 Global

**Patch covered:** Global client build **25926599** (Steam public branch, updated 2026-10-14 06:40 UTC). That is the [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374) on top of the [Oct 6 PDT patch](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544) and the [Oct 8 PDT hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1). None of the three changed a Gladiator skill. Build id: [SteamCMD](https://api.steamcmd.net/v1/info/3393110). NotMeter data (week of Oct 7–14) was recorded on the previous build 25800038. **Written:** 2026-10-13, **updated for the Oct 13 patch:** 2026-10-14.

**Tags:** [Global] · [KR/TW-confirmed] = Korean or Taiwanese source checked against the Global client · UNVERIFIED.

**Why this spec exists on Global.** This guide checked every NotMeter Global party, 5,303 unique boss parses from the week of Oct 7–14 ([NM data](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)): (NotMeter has since retired this generation, so the link returns 404; see the [README](README.md).)
- **Templar-less parties are common.** 1,903 parses (36%) had no Templar.
- **The Gladiator usually tanks them.** In those parties, the party member who got the most healing from others was the Gladiator in about **908 of 1,644** parties with one (55%).
- **The tanking Gladiators did not change their build.** Same stigmas (Rage Burst 98%, Lunge Stance 97%, Zikel's Blessing 89%, Focused Block 67%) and the same median levels (Lunge Stance 20, Zikel's Blessing 15, Rage Burst ~6, Focused Block 5).
- **They did fine.** Higher damage share (median 20.8% vs 17.2%) and fewer deaths (0.11 vs 0.29 per fight) than the Gladiators who weren't tanking.

So on Global, "tank Gladiator" is a **role**, not a different loadout. Korea's no-Templar Gladiator-tank set, from a forum post that asks whether the list is right (Lunge Stance, Zikel's Blessing, Rage Burst, Wave Armor, Armor of Balance, Focused Block; [Inven](https://www.inven.co.kr/board/aion2/6448/22575), KR/TW) doesn't carry over to 4 slots on Global. Armor of Balance appears in 0.1% of Global Gladiators and Tenaciousness in about 1% ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)). The method is in [README](README.md#method-notes). Everything not listed here is the same as [gladiator-dps.md](gladiator-dps.md).

---

## 1. Overview

| Item | Recommendation / finding | Why | Source |
|---|---|---|---|
| Role | Main tank when the party has no Templar | Rending Blow and Keen Strike raise Enmity | [DB Rending Blow](https://aion2.app/db/skills/11010000), [DB Keen Strike](https://aion2.app/db/skills/11020000) |
| Playstyle | <ul><li>The same Overhead Slam ↔ Rending Blow rotation.</li><li>Face the boss away from the party.</li><li>Parry big hits with Focused Block.</li><li>Keep Rage Burst's Wounded on the boss (−10% Attack, −20% at stigma level 10).</li></ul> | Wounded lowers boss damage. Focused Block guarantees a Parry. | [DB Rage Burst](https://aion2.app/db/skills/11390000), [DB Focused Block](https://aion2.app/db/skills/11110000) |
| Strengths | <ul><li>Self-healing: Blood Absorption heals 26% of max HP at ≤50% HP, plus heal-on-hit.</li><li>Experienced Counterstrike gives the party +5.4% PvE damage on each Block.</li><li>A frontal class, so facing the boss costs no damage.</li></ul> | | [DB Blood Absorption](https://aion2.app/db/skills/11730000), [DB Experienced Counterstrike](https://aion2.app/db/skills/11780000) |
| Weaknesses | <ul><li>No taunt.</li><li>No party mitigation like Templar's Shield of Protection or Nezekan's Shield.</li><li>Experienced Counterstrike's party buff doesn't stack with a Templar's Fury.</li></ul> | | [DB Experienced Counterstrike](https://aion2.app/db/skills/11780000) |
| PvE standing (Global) | Works: tanking Gladiators died less and dealt a bigger damage share than non-tanking ones in the same week | Party analysis above | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |
| PvP | Not a PvP role; see the PvP rows in [gladiator-dps.md](gladiator-dps.md#pvp) | | — |
| Difficulty | Medium: the DPS rotation plus positioning and parry timing | Derived from the above | — |
| Who should play it | Gladiators in groups without a Templar (36% of Global boss parses) | | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |

---

## 2. Max damage (while tanking)

Single target is the same as [gladiator-dps.md §2](gladiator-dps.md#2-max-damage), with three tank changes:

| Step | Change | Why | Source |
|---|---|---|---|
| Pull | Leaping Slam (option 1 gives 3 s of Prepare for Battle), then Ruinous Blow | Gets on the boss first and starts Enmity | [DB Leaping Slam](https://aion2.app/db/skills/11190000), [DB Ruinous Blow](https://aion2.app/db/skills/11100000) |
| Rage Burst | Keep it on cooldown with no gaps | Wounded lowers the boss's Attack, and Rage Burst also enables Overhead Slam | [DB](https://aion2.app/db/skills/11390000) |
| Big hits | Focused Block before the boss's heavy attack | Guaranteed Parry; restores MP and Stamina | [DB](https://aion2.app/db/skills/11110000) |

**AoE (trash):** the same tools as the DPS spec (Rending Blow and Crushing Wave hit up to 4). Leaping Slam option 5 pulls enemies together ([DB](https://aion2.app/db/skills/11190000)). The order is UNVERIFIED.

---

## 3. Macros

- **Layout:** same as [gladiator-dps.md §3](gladiator-dps.md#3-macros) (Macro A).
- **Tank rule:** keep Focused Block off the macro and press it yourself for boss hits. This is derived from the effect: a parry wasted on cooldown misses the hit it was meant for ([DB](https://aion2.app/db/skills/11110000)). UNVERIFIED by testing.
- **Banned or nerfed:** same as the DPS spec. The in-game macro is allowed. External macro software risks NC's unauthorized-program rule ([NC Operation Policy](https://www.plaync.com/policy/operation/aion2global)).

---

## 4. Stigmas

Global rules are the same as the DPS spec: 4 slots, cap 20, no rarity ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

### PvE (tanking)

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Rage Burst | Slot 1 | **10**, then 20 | n/a | <ul><li>98% of tanking Global Gladiators run it, median level ~6.</li><li>10 doubles Wounded to −20% boss Attack, a tank gain over the DPS spec's level 5.</li></ul> | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [DB](https://aion2.app/db/skills/11390000) |
| Lunge Stance | Slot 2 | **20** | n/a | 97% use, median 20 | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [DB](https://aion2.app/db/skills/11400000) |
| Zikel's Blessing | Slot 3 | **15** | n/a | 89% use, median 15 | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [DB](https://aion2.app/db/skills/11250000) |
| Focused Block | Slot 4 | **5**, then **20** | n/a | <ul><li>67% use, median 5.</li><li>20 restores 10% HP once on Parry: a tank-only reason to push it.</li></ul> | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [DB](https://aion2.app/db/skills/11110000) |
| Tenaciousness | Not used on Global (≤2%) | — | n/a | 3 s immunity (150 s cooldown). Korea's top-20 PvE builds equip it 95% of the time, with about 8 stigmas equipped on average. | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [NotMeter KR](https://notmeter.com/?view=setup-guide), [DB](https://aion2.app/db/skills/11380000) |
| Armor of Balance | Not used on Global (<2%) | — | n/a | <ul><li>×1.5 Blood Absorption and Protection Armor.</li><li>Impact resist.</li><li>Part of Korea's no-Templar tank set ([Inven](https://www.inven.co.kr/board/aion2/6448/22575), KR/TW).</li></ul> | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [DB](https://aion2.app/db/skills/11130000) |

Levels 10 and 20 for Rage Burst and Focused Block come from the DB effects. Global tanks mostly sit at 5–6, so the higher targets are UNVERIFIED as a measured gain.

### PvP / Solo
Not a tank role. Use the PvP and solo rows in [gladiator-dps.md §4](gladiator-dps.md#4-stigmas).

---

## 5. Skills

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Overhead Slam | Same as DPS | **20** | n/a | The damage core is unchanged | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |
| Rending Blow | Same; also your Enmity filler | **16** (option 5 fixes MP), then 20 | n/a | Raises Enmity on up to 4 targets | [DB](https://aion2.app/db/skills/11010000) |
| Ruinous Blow | Same | **16**, then 20 (top Global median 16) | n/a | | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |
| Keen Strike | Higher value while tanking (Enmity + MP) | **12** | n/a | Raises Enmity and restores 100 MP | [DB](https://aion2.app/db/skills/11020000) |
| Leaping Slam | Pull tool | **12** (16 for the option 5 AoE pull on trash) | n/a | Option 5 pulls enemies together | [DB](https://aion2.app/db/skills/11190000) |
| Defiance | Breaks CC on the tank | **16** | n/a | Option 5: +50% PvE Damage Tolerance during Tenacity | [DB](https://aion2.app/db/skills/11260000) |
| Sword Aura Rampage, Mocking Blade, Crushing Wave, Ankle Slice, Rush Strike, Aerial Snare | As the DPS spec | 12–16 | n/a | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

**Passives:**
- **Damage passives:** keep Experienced Counterstrike (Global median 17) and Murderous Burst (16) first, as in the DPS spec ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) buff levels).
- **Survival:** Survival Willpower (Global median 15) and Blood Absorption are the tank passives. No Global source gives tank-specific passive levels, so going past 15 is UNVERIFIED ([DB Survival Willpower](https://aion2.app/db/skills/11790000), [DB Blood Absorption](https://aion2.app/db/skills/11730000)).

---

## 6. Specializations

| Item | Recommendation (picks at 8 / 12 / 16 / 20) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Overhead Slam | 3 / 3+4 / 3+5 / 3+4+5 | 20 | n/a | Same as DPS | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |
| Rending Blow | 3 / **2+3** if you take hits often (option 2 = +200 Block while casting) / 3+5 / 3+4+5 | 20 | n/a | Option 2 is a tank-only choice. No Global source picks it, so it is UNVERIFIED. | [DB](https://aion2.app/db/skills/11010000) |
| Leaping Slam | 1 / **1+4** while tanking (+20% PvE Damage Tolerance for 3 s) / 4+5 at 16 for pulls | 16 | n/a | Derived from the DB effects; UNVERIFIED | [DB](https://aion2.app/db/skills/11190000) |
| Defiance | 3 / 3+4 / **3+5** | 16 | n/a | <ul><li>3: restores 20% HP on use.</li><li>5: +50% PvE Damage Tolerance.</li></ul> | [DB](https://aion2.app/db/skills/11260000) |
| Everything else | Same as [DPS](gladiator-dps.md#6-specializations) | | n/a | | |

**Daevanion:** the same Global rules as the DPS spec ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Allyria ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Allyria marks defense as lower priority. For a tank, HP and Defense white tiles rise after Attack and Crit; a tank-specific path is UNVERIFIED.

---

## 7. Tier list

| Content | Tier | Placement reason | Source |
|---|---|---|---|
| PvE tank (no Templar) | **B+ (viable off-tank)** | <ul><li>Takes the tank seat in 55% of Templar-less parties with a Gladiator.</li><li>Fewer deaths and higher damage share than non-tanking Gladiators.</li><li>No party mitigation compared with a Templar.</li></ul> | [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |
| PvP | n/a (see DPS spec) | | |
| Solo | n/a (see DPS spec) | | |

The B+ letter is this guide's judgment from the data above, not a published ranking.

---

## 8. Gear

Same as [gladiator-dps.md §8](gladiator-dps.md#8-gear): Unique is the settle rarity for every slot except bracelet slot 2, which is a blue (Epic) bracelet in Season 1 in Season 1, with the same enchant targets ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)). Tank-specific differences:

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Legs | Damage Tolerance first (already first in the DPS list) | +15 | Unique | Bosses have Damage Boost, so Damage Tolerance is a real defensive stat | [Bible ch.11](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Helmet | Incoming Heal first (sheet) | +15 | Unique | More healing received | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Pet Genus line 7 | PvE Damage Tolerance; Special line 7: Damage Tolerance | — | — | Bosses have Damage Boost but no Crit or Multi-hit, so those tolerances do nothing | [Genus audit](../docs/genus-audit.md), [Bible ch.11](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Endurance | Valued for tanks: a chance to take half damage, and bosses have no Endurance Penetration | — | — | | [Bible ch.11](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |

There's no Global tank gear guide for Gladiator. Swapping damage lines for defensive ones is UNVERIFIED. Global tanking Gladiators show the same damage-focused build.
