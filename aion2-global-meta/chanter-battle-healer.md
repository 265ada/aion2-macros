# Chanter (護法星) — Battle-healer spec (parties without a Cleric) · AION 2 Global

**Patch covered:** Global client build **25926599** (Steam public branch, updated 2026-10-14 06:40 UTC). That is the [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374) on top of the [Oct 6 PDT patch](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544) and the [Oct 8 PDT hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1). None of the three changed a Chanter skill. Build id: [SteamCMD](https://api.steamcmd.net/v1/info/3393110). NotMeter data (week of Oct 7–14) was recorded on the previous build 25800038. **Written:** 2026-10-13, **updated for the Oct 13 patch:** 2026-10-14.

**Tags:** [Global] · [KR/TW-confirmed] = Korean or Taiwanese source checked against the Global client · UNVERIFIED.

**Why this spec exists on Global.** This guide checked every NotMeter Global party, 5,303 unique boss parses from the week of Oct 7–14 ([NM data](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)): (NotMeter has since retired this generation, so the link returns 404; see the [README](README.md).)
- **Sheet snapshot:** citations of this class's sheet tab refer to the copy downloaded on Oct 14. Later that day the author replaced the tab with a link to [daevaos](https://daevaos.com/guides/chanter-quick-guide), where the build is now maintained; differences found are noted where they matter.
- **Cleric-less parties exist.** 582 parses had no Cleric.
- **The Chanter heals them.** In the 565 of those with a Chanter, the Chanter gave the most healing in **524 (93%)**; 39 of the 565 had no healing between players at all, so it's 524 of the 526 that did, a median 100% of the party's healing from others.
- **The heal is mostly Recuperation,** then Sprint Mantra's heal on hit, then Healing Touch.
- **The build barely changes.** Across 709 Chanter appearances in Cleric-less parties, they keep the buffer four (Marchutan's Wrath 99%, Sprint Mantra 91%, Undefeated Mantra 90%, Power of the Storm 77%).
- **Only small stigma shifts:** Healing Touch 14% (vs 3% with a Cleric) and Impeding Authority 9% (vs 3%).
- **Damage cost:** median damage share drops from 19.0% to 16.4%.

So on Global, battle healer is mostly a **role** played with the support-DPS build plus Recuperation, with a stigma swap for hard fights. Everything not covered here is in [chanter-dps.md](chanter-dps.md). The method is in [README](README.md#method-notes).

---

## 1. Overview

| Item | Recommendation / finding | Why | Source |
|---|---|---|---|
| Role | Main healer when no Cleric is in the party, still dealing damage | Chanter is the top healer in 93% of Cleric-less parties | [NM] |
| Playstyle | The Dark Crush rotation, plus Recuperation on cooldown (party heal + 1 cleanse + heal over time), Sprint Mantra heal-on-hit, and the Protection Circle party shield | | [DB Recuperation](https://aion2.app/db/skills/18120000), [DB Sprint](https://aion2.app/db/skills/18160000), [DB Protection Circle](https://aion2.app/db/skills/18730000) |
| Strengths | You keep the party buffs and most of your damage (16.4% median damage share) | | [NM] |
| Weaknesses | No resurrection; weaker burst healing than a Cleric; Recuperation has a 15 s cooldown | | [DB](https://aion2.app/db/skills/18120000) |
| PvE standing | Viable in current Global content: 565 Cleric-less parses ranked on NotMeter boss boards | | [NM] |
| PvP | n/a (see the DPS spec) | | — |
| Difficulty | Medium: rotation plus watching party HP | | — |
| Who should play it | Chanters in groups without a Cleric | | [NM] |

---

## 2. Max damage (while healing)

The same as [chanter-dps.md §2](chanter-dps.md#2-max-damage), with three changes:

| Step | Change | Why | Source |
|---|---|---|---|
| Heal | **Recuperation** on cooldown when the party is hurt. Option 1 (8) gives a second consecutive cast and stacks the heal over time twice. | Most of the healing in Cleric-less parties | [DB](https://aion2.app/db/skills/18120000), [NM] |
| Spinning Strike | Option 2 (+10% Heal Boost, stacking to 20%) instead of 3 | The Korean no-Cleric note says "use 2, 3, 5 for more healing"; this guide keeps option 1 (−5 s cooldown), so 1+2 at 12 and 1+2+5 at 20. Derived from the DB and untested on Global: Cleric-less Global Chanters run 1+3 (54%), 1+2 only 5%. | [DB](https://aion2.app/db/skills/18290000), [repo KR note](../data/stigmas.json) |
| Burst heal | Healing Touch (stigma, if slotted) | Party heal; removes 5 debuffs at 15 | [DB](https://aion2.app/db/skills/18170000) |

**AoE:** the same as the DPS spec.

---

## 3. Macros

- **Layout:** the DPS spec's one-entry macro ([Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)).
- **Heals stay manual:** keep Recuperation and Healing Touch off the macro so you can time them. The Korean Cleric guide gives the same reason: a charge or filler should never delay a heal ([Inven](https://www.inven.co.kr/board/aion2/6452/29213), KR/TW).
- **Ban / nerf status:** same as the DPS spec. In-game macro allowed; external software is a risk ([NC Operation Policy](https://www.plaync.com/policy/operation/aion2global)).

---

## 4. Stigmas

Global rules: 4 slots, cap 20, no rarity ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

### PvE: normal content (what Global battle healers run)

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Undefeated Mantra | Keep | **20** | n/a | Party PvE damage and **tolerance** (10.5% at level 1, 20% at 20) | [DB](https://aion2.app/db/skills/18190000), [NM] |
| Sprint Mantra | Keep | **15** (higher than the DPS spec) | n/a | Party heal on hit. 15: +50% heal when HP ≤ 50%. 20: +10% Restoration. | [DB](https://aion2.app/db/skills/18160000) |
| Power of the Storm | Keep | **20** | n/a | | [DB](https://aion2.app/db/skills/18250000) |
| Marchutan's Wrath | Keep | **5** | n/a | 99% keep it on Global | [NM] |

Raising Sprint Mantra to 15 is derived from the DB effect; Global battle healers' Sprint levels aren't logged, so it is UNVERIFIED as a measured gain. The [daevaos build](https://daevaos.com/guides/chanter-quick-guide) also runs Sprint Mantra at 15 (as a DPS build).

### PvE: hard content swap (Korea's battle-healer picks; effects checked in the Global DB)

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Healing Touch | Replaces Marchutan's Wrath | **15** (20 adds +5% heal) | n/a | Party heal; 15 removes 5 debuffs. 14% of Global battle healers. The Korean post is a 6-slot, level-25 Sanctuary setup (not on Global); this swap and its levels are derived from the DB. | [DB](https://aion2.app/db/skills/18170000), [NM], [Inven KR](https://www.inven.co.kr/board/aion2/6451/22811) |
| Impeding Authority | Replaces Sprint Mantra or Power of the Storm on mechanic-heavy bosses | **15** (20: 7% HP when the shield ends) | n/a | Party shield of 16% max HP; 15: +10% PvE Damage Tolerance. 9% of Global battle healers. | [DB](https://aion2.app/db/skills/18240000), [NM], [vortexgaming KR Mar](https://vortexgaming.io/postdetail/688518) |
| Barrier Spell | Emergency | **5** | n/a | The party can't drop below 10% HP for 3 s (180 s cooldown) | [DB](https://aion2.app/db/skills/18440000) |

**Shard order:** Undefeated 20 → Sprint 15 → Storm 20 → Healing Touch 15 (if used). Derived from the DB effects.

### PvP / Solo
See [chanter-dps.md §4](chanter-dps.md#4-stigmas).

---

## 5. Skills

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Recuperation | 1st heal | **16** (−3 s cooldown), then 20 | n/a | 62% of Global battle healers run 1+4. Korea's top 20: level 20. The [daevaos build](https://daevaos.com/guides/chanter-quick-guide) runs 1+4+5 with +4 Recuperation levels from the Compass. | [NM], [DB](https://aion2.app/db/skills/18120000), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Dark Crush / Onslaught / Spinning Strike / Incandescent Blow | Same as DPS | 20 / 16 / 16 / 16 | n/a | Damage stays the job | [NM] |
| Others | Same as DPS | 12–16 | n/a | | [chanter-dps.md](chanter-dps.md#5-skills) |

**Passives:**
- **Protection Circle** (party Divine Barrier; Global median 14) is worth more to a battle healer.
- **Wind's Promise** still comes first for damage.
- Sources: [NM buffs](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [DB Protection Circle](https://aion2.app/db/skills/18730000).

---

## 6. Specializations

| Item | Recommendation (picks at 8 / 12 / 16 / 20) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Recuperation | 1 / **1+4** / 1+5 or 1+4 / 1+4+5, or 1+4+2 when there are debuffs | 16–20 | n/a | <ul><li>1: 2 consecutive casts, heal over time stacks twice.</li><li>4: +5% HP.</li><li>5: −3 s.</li><li>2: removes 2 debuffs.</li></ul> | [DB](https://aion2.app/db/skills/18120000), [NM] |
| Spinning Strike | 1 / 1+2 / 1+2+5 at 20 (healing) | 20 | n/a | 2: +10% Heal Boost (stacks to 20%). Global battle healers mostly still run 1+3 (54–55%); 1+2 is 5%. Derived from the DB, untested on Global. | [DB](https://aion2.app/db/skills/18290000), [NM] |
| Onslaught | 3 / 3+4 / 4+5 (or 2+4+5 for lifesteal, a repo note; Korea's Inven guide uses 2+3+5 at 20, [Inven](https://www.inven.co.kr/board/aion2/6451/116), KR/TW; the sheet says 3/4/5 at 20) | 20 | n/a | Global battle healers: 3+4 39%, 4+5 34% | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Dark Crush and the rest | Same as [DPS](chanter-dps.md#6-specializations) | | n/a | | |

**Daevanion:** same as the DPS spec. HP tiles rise in value for a healer, but no Global source sets a path, so that is UNVERIFIED.

---

## 7. Tier list

| Content | Tier | Placement reason | Source |
|---|---|---|---|
| PvE healer (no Cleric) | **A−** | <ul><li>Top healer in 93% of Cleric-less parties.</li><li>Keeps party buffs and most of its damage.</li><li>No resurrection and less burst healing than a Cleric.</li></ul> | [NM] |
| PvP / Solo | n/a (see the DPS spec) | | |

The A− letter is this guide's judgment from the data above.

---

## 8. Gear

Same as [chanter-dps.md §8](chanter-dps.md#8-gear): Unique is the settle rarity in Season 1, with the same enchant targets ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)). Healer-specific notes:

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Rings | Keep Recuperation in the ring lines (the sheet lists it 6th) | +17 | Unique | Recuperation levels | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Helmet | Incoming Heal first (already first) | +15 | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Heal Boost / Restoration lines | UNVERIFIED | — | — | No Global source tests heal stats for Chanter | — |
