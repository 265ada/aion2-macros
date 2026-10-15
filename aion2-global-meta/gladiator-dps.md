# Gladiator (劍星) — DPS spec · AION 2 Global

**Patch covered:** Global client build **25926599** (Steam public branch, updated 2026-10-14 06:40 UTC). That is the [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374) on top of the [Oct 6 PDT patch](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544) and the [Oct 8 PDT hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1). None of the three changed a Gladiator skill. Build id: [SteamCMD](https://api.steamcmd.net/v1/info/3393110). NotMeter data (week of Oct 7–14) was recorded on the previous build 25800038. **Written:** 2026-10-13, **updated for the Oct 13 patch:** 2026-10-14.

**Tags used:**
- **[Global]:** Global client data, NC's official notices, or Global players' data.
- **[KR/TW-confirmed]:** a Korean or Taiwanese source, used only where the Global client shows the same skill, effect or number.
- **UNVERIFIED:** nothing confirms it on Global.

**Main data sources:**
- **NM:** [NotMeter Global ranking](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), week of Oct 7–14, published 2026-10-13. It covers the top 20 Gladiator parses on each of 15 bosses: 300 parses from 114 players, median CP 153,291, median DPS 72,103. (NotMeter has since retired this generation, so the link returns 404; see the [README](README.md).)
- **DB:** [aion2.app Global client database](https://aion2.app/db/skills?class=Gladiator), client dated 18.09.2026.
- **Sheet:** the [Global class sheet by zxcastform](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview).
- **TEN:** [Tenyon's Gladiator guide](https://docs.google.com/document/d/15J0xIIlOGvp0NSGui7NK0MJpbgZTjXuZKAahHnkr2G4/edit), linked from the sheet's Class Guides tab. The author played on Taiwan from day 1 and now plays on Global (Asia), so it's a mixed TW/Global source.
- **Bible:** [Kanon's Aion 2 Bible](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) (Oct 4 Global update).

**The spec:** this is the default Gladiator role, damage from the front of the boss. It is a build path, not an official subclass: NC lists 8 classes and no specs ([NC class list](https://aion2.plaync.com/en-us/about/index#classes)). The other Gladiator path is [gladiator-tank.md](gladiator-tank.md).

---

## 1. Overview

| Item | Recommendation / finding | Why | Source |
|---|---|---|---|
| Role | Frontline melee DPS with a greatsword. | NC: "A frontline vanguard who carries a colossal blade". | [NC class list](https://aion2.plaync.com/en-us/about/index#classes) |
| Playstyle | Two skills cancelling into each other. Overhead Slam with its Upward Strike chain is 33.5% + 27.4% of damage, and Rending Blow with its Smashing Blow chain is 9.5% + 10.8%: about **81%** together. Ruinous Blow adds 7.8%. | Shares of damage in top Global boss parses. | [NM] |
| Strengths | <ul><li>Simple core.</li><li>Self-healing: Blood Absorption restores HP on hit, plus 26% of max HP at 50% HP, and Lifestealing Blade absorbs 10%.</li><li>It can off-tank (see the battle-tank spec).</li></ul> | Skill effects. | [DB Blood Absorption](https://aion2.app/db/skills/11730000), [DB Lifestealing Blade](https://aion2.app/db/skills/11340000) |
| Weaknesses | <ul><li>**Positional:** Experienced Counterstrike boosts front-attack damage, and 77% of top Global Gladiator hits land from the front.</li><li>**Needs a trigger:** Overhead Slam only hits knocked-down targets, targets for 10 s after Rage Burst, or (7% chance per attack) targets immune to knockdown, which includes bosses.</li><li>**Ping:** a hit-count rotation. Kanon's test (KR/Asia; Templar, Brawler and Assassin, not Gladiator) found 150–200 ms of extra ping costs a lot of damage, with no major difference between classes.</li></ul> | Skill text; front rate from NotMeter; ping test. | [DB Overhead Slam](https://aion2.app/db/skills/11170000), [DB Rage Burst](https://aion2.app/db/skills/11390000), [NM], [Bible ch.11](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| PvE standing (Global) | **3rd of 8.** NotMeter class score 110.46. At equal Combat Power, top Gladiators deal +5.3% more than the class average (3rd). | Global boss parses, week of Oct 7–14. | [NM classPerformance](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |
| PvP standing (Global) | **UNVERIFIED.** There's no Global PvP data. Launch-week opinion pieces rate Gladiator S or A for PvP (low confidence). | No official or Global PvP rankings exist. | [ExitLag tier list](https://www.exitlag.com/news/aion-2-class-tier-list/) (opinion) |
| Difficulty | **Low to medium.** The one-key in-game macro does the Overhead Slam → Rending Blow cancel by itself (see Macros). Top numbers need high hit counts: the top 10% log 66.7 Overhead Slam and 57.2 Rending Blow uses a minute. | Most damage comes from two skills, and the in-game macro handles the cancel. | [NM], [Inven Aug 30 one-key macro](https://www.inven.co.kr/board/aion2/6448/30880) [KR/TW-confirmed] |
| Who should play it | Players who want a durable melee DPS that can tank in a pinch, and who will stay in front of the boss. | Front-damage passive; self-healing. | [DB Experienced Counterstrike](https://aion2.app/db/skills/11780000) |

---

## 2. Max damage

### Single target (boss)

| Step | What to do | Why | Source |
|---|---|---|---|
| 1 | **Lunge Stance** (+20% Combat Speed, 60 s cooldown) and **Zikel's Blessing** (+20% Attack and +100 Accuracy, 120 s cooldown; +10% PvE Damage Boost at stigma level 10). Both last 10 s at level 1 and +0.5 s per level (20 s at 20). | Both windows should cover the burst below. | [DB Lunge Stance](https://aion2.app/db/skills/11400000), [DB Zikel's Blessing](https://aion2.app/db/skills/11250000) |
| 2 | **Ruinous Blow**: grants Prepare for Battle for 20 s (+20% PvE Damage Boost, +100 Crit, +15% Status Effect Chance) on a 45 s cooldown. Recast it every cooldown. | It is 7.8% of damage by itself, and the buff covers everything. NotMeter logs 3.0 uses/min (top 10%: 4.5), more than a 45 s cooldown seems to allow. It isn't a hit count (hits are logged separately). Short fights and cooldown cuts inflate the per-minute rate, so read it as "uses logged". | [DB Ruinous Blow](https://aion2.app/db/skills/11100000), [NM] |
| 3 | **Rage Burst**: Wounded on the boss (−10% Attack, −20% at level 10), +10% PvE Damage Boost for you, and Overhead Slam becomes usable on the target for 10 s. | Against knockdown-immune bosses, Overhead Slam otherwise only procs (7% chance per attack). Rage Burst is the reliable trigger. | [DB Rage Burst](https://aion2.app/db/skills/11390000) |
| 4 | **Overhead Slam ↔ Rending Blow alternation** (the "내절" cancel). Rending Blow cuts Overhead Slam's recovery. At skill level 16 Overhead Slam has no cooldown (option 5). | About 81% of damage. Top 10% Global: 66.7 Overhead Slam and 57.2 Rending Blow uses/min. | [DB Overhead Slam](https://aion2.app/db/skills/11170000), [NM], [Inven Aug 26 cancel](https://www.inven.co.kr/board/aion2/6448/30223) [KR/TW-confirmed: the Global client includes the Aug 26 balance, and the Global cast rates match] |
| 5 | **Sword Aura Rampage** in stagger windows only. It hits Staggered targets, and at level 16 option 5 cuts all cooldowns by 1 s per hit. | 1.2% of damage, used by 48% of top Global players. | [DB Sword Aura Rampage](https://aion2.app/db/skills/11280000), [NM] |
| 6 | Keep pressing Rage Burst and Ruinous Blow on cooldown. Keen Strike (left click) only when MP is short. | Keen Strike restores 100 MP. The sheet says MP runs short until Rending Blow is skill level 16 (option 5 restores MP on crits). | [DB Keen Strike](https://aion2.app/db/skills/11020000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

**Line up:** stack Lunge Stance, Zikel's Blessing, Prepare for Battle (Ruinous Blow, 20 s) and Rage Burst at the start of the pull and again on each Zikel's Blessing cooldown. At the §4 levels, Lunge Stance lasts 20 s (level 20) and Zikel's Blessing 17 s (level 15); the DB's "10 s" is the level-1 value. Stigma buff durations measured in Global parses ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)). Party buffs (Chanter Undefeated Mantra / Cleric Light of Protection) are in [README](README.md#party-buffs). The ordering is derived from these durations and cooldowns; no Global source writes it down.

**Stay in front.** Experienced Counterstrike adds Front Attack Damage Boost. 77% of top Global Gladiator hits are frontal ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) frontAttackRate). Front/Back Damage Boost is a separate multiplicative bucket ([Bible ch.11](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

### AoE (packs)

| Tool | Targets | Source |
|---|---|---|
| Rending Blow + Smashing Blow chain (your filler) | up to 4 within 4 m | [DB Rending Blow](https://aion2.app/db/skills/11010000) |
| Crushing Wave | up to 4 within 5 m; option 4 resets on crit | [DB Crushing Wave](https://aion2.app/db/skills/11050000) |
| Lifestealing Blade (stigma) | up to 4 within 4 m, absorbs 10% | [DB](https://aion2.app/db/skills/11340000) |
| Murderous Burst (passive) | every 5 hits, up to 4 within 5 m | [DB](https://aion2.app/db/skills/11800000) |
| Overhead Slam option 2 | changes it to AoE (costs the Upward Strike / crit / no-cooldown pick slots) | [DB](https://aion2.app/db/skills/11170000) |
| Leaping Slam option 5 | AoE + pulls enemies | [DB](https://aion2.app/db/skills/11190000) |

**AoE order:** UNVERIFIED. No Global AoE test exists. From the DB text: gather with Leaping Slam, open with Ruinous Blow (it also hits up to 4), keep the Rending Blow filler going, and add Crushing Wave and Lifestealing Blade.

---

## 3. Macros

**How the in-game macro works.**
- **Setup:** Settings → Key Settings → General → Gameplay → Macro ([Allyria Global Ranger guide §3.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).
- **Entries:** each entry points to a hotbar slot that stacks up to 4 skills. In the tables below, row 0 fires first.
- **Charge skills fire uncharged** from a macro ([Allyria FAQ](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Gladiator's core has no charge skills, so nothing is lost here.

### Macro A: Global sheet layout (recommended)

| Entry | Row 0 | Row 1 | Row 2 | What it does | Source |
|---|---|---|---|---|---|
| 1 | Zikel's Blessing | Ruinous Blow | — | Keeps Zikel's and Prepare for Battle on cooldown | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview). Ruinous Blow added by this guide, because top Global players keep it on cooldown ([NM]) |
| 2 | Lifestealing Blade* | Lunge Stance | Rending Blow | Buff + filler (the Rending Blow half of the cancel) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| 3 | Rage Burst | Overhead Slam | — | Rage Burst enables Overhead Slam for 10 s; then the Overhead Slam half of the cancel | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [DB Rage Burst](https://aion2.app/db/skills/11390000) |

- **Delays:** 10 ms on every entry ([Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)).
- **Hold:** the macro key, plus Keen Strike (left click) for MP.
- **Press yourself:**
  - Leaping Slam, Rush Strike and Aerial Snare on one key;
  - Mocking Blade, Crushing Wave and Ankle Slice;
  - Sword Aura Rampage in stagger windows.
- **\*Lifestealing Blade:** only 27% of top Global Gladiators slot it ([NM]). If you run Focused Block as your 4th stigma, that row stays empty and is skipped. Press Focused Block yourself, because it's a parry and needs timing.

### Macro B: one key, no mashing (alternative)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Ruinous Blow | Rage Burst | Lifestealing Blade | Rending Blow | [Inven Aug 30](https://www.inven.co.kr/board/aion2/6448/30880) [KR/TW-confirmed] |
| 2 | Lunge Stance | Wave Armor | Zikel's Blessing | Overhead Slam | same (the author's Lunge Stance and Zikel's are KR level 25; Global caps at 20) |

- **Use:** hold the macro key only. The two entries alternate Rending Blow and Overhead Slam, which is the cancel. The author measured 176 Overhead Slam and 176 Rending Blow hits a minute on the Korean dummy.
- **Cost:** buffs fire on cooldown even during mechanics, and Sword Aura Rampage isn't used.
- **Global note:** Wave Armor and Lifestealing Blade rows stay empty unless you slot those stigmas (Global has 4 slots). The rows are skipped.

### Banned or nerfed on Global

| Item | Status | Source |
|---|---|---|
| In-game skill macro | **Allowed.** It's a built-in game feature. | [Allyria FAQ](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| External software or hardware macros (Razer, G-Hub) | **Risk; not officially allowed.** NC's policy bans programs, devices or equipment "enabling actions impossible for regular users" (Integrated Account Ban). NC's ban waves on Oct 10, Oct 12 and Oct 14 named "use of macros, bots or other unauthorized programs". One Global guide says hold-to-run mouse macros aren't bannable, but that is not NC's word. | [NC Operation Policy](https://www.plaync.com/policy/operation/aion2global), [NC Oct 11 restrictions notice](https://aion2.plaync.com/en-us/board/notice/view?articleId=6acaa7506b722c561dc6aae9), [Oct 14 notice](https://store.steampowered.com/news/app/3393110/view/1846651706673527) |
| Gladiator macro nerfs on Global | **None** in the Oct 6, Oct 8 or Oct 13 notes. | [Oct 13](https://store.steampowered.com/news/app/3393110/view/1846651706673374), [Oct 6 notes](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544), [Oct 8 notes](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1) |
| KR/TW Sep 16: "Leaping Slam and Ruinous Blow can't be used while bound" | **Likely live.** Korea's Sep 16 patch is live on Global (see the [README](README.md)); this specific change is UNVERIFIED. Korea's Sep 23 change (Fracturing Rush follows your key direction) is UNVERIFIED. | [repo patch log](../data/classes.json) (KR/TW notes), [README](README.md) |

---

## 4. Stigmas

**Global rules:**
- **Slots and cap:** 4 slots, stigma level capped at 20 ([Sirin, Global SM guide](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). This matches NM: top Global Gladiators average about 4 stigmas each.
- **Shards:** a fresh level 45 has 32 shards, and the Abyss Point cap limits you to about 20 shards a week. Resetting stigma levels is free ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- **Cost to 20:** 75 shards per stigma (1/2/4/8 shards per level for levels 1–5/6–10/11–15/16–20). Confirmed in questlog's Global skill data ([questlog](https://questlog.gg/aion-2/en/db/skill/17410000)).
- **Settle rarity:** stigmas have no rarity, only levels ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)). The column says "n/a" for that reason.

### PvE (party, someone else tanks)

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Lunge Stance | Slot 1, always | **20** | n/a | <ul><li>97% of top Global Gladiators run it, median level 20.</li><li>5: +5% Double Chance.</li><li>15: ×1.5 Identify Weakness.</li><li>20: 50% chance to cut all cooldowns 1 s on a crit.</li></ul> | [NM], [DB](https://aion2.app/db/skills/11400000) |
| Zikel's Blessing | Slot 2, always | **15** (20 last) | n/a | <ul><li>94% use, median 15.</li><li>10: +10% PvE Damage Boost.</li><li>15: +50% multi-hit.</li><li>20 only adds +20% status chance.</li></ul> | [NM], [DB](https://aion2.app/db/skills/11250000) |
| Rage Burst | Slot 3, always | **5 now, 20 later** | n/a | <ul><li>99% use. Median buff level 7 (most players at 5).</li><li>5: −15 s cooldown.</li><li>10: Wounded −20% boss Attack.</li><li>15: always crits.</li><li>20: +10% more PvE Damage Boost.</li></ul> | [NM], [DB](https://aion2.app/db/skills/11390000) |
| Focused Block | Slot 4 (pugs, learning fights) | **5** | n/a | <ul><li>64% use, median 5.</li><li>5: a second consecutive parry.</li><li>A Korean tank post says Focused Block parries trigger Experienced Counterstrike's party buff. The DB says it triggers "on Block", so whether a Parry counts is UNVERIFIED on Global.</li></ul> | [NM], [DB](https://aion2.app/db/skills/11110000), [DB Experienced Counterstrike](https://aion2.app/db/skills/11780000) |
| Wave Armor | Slot 4 alternative (damage, behind a Templar) | **15** | n/a | <ul><li>10: ×1.5 Experienced Counterstrike.</li><li>15: ×1.5 Murderous Burst.</li><li>Only 15% of top Global players use it. In the sheet it's the second alternate for slot 4, after Lifestealing Blade.</li><li>At equal CP, Wave Armor users (16 players) vs Focused Block users (72), averaged per player: +3–4% (independent re-check: +2.6%, 95% range −8% to +15%). The data can't separate them ([method](README.md#method-notes)).</li></ul> | [DB](https://aion2.app/db/skills/11410000), [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Lifestealing Blade | Slot 4 alternative (TEN's 4th; the sheet's first alternate) | **10** (TEN), 15 (−30 s cooldown) | n/a | <ul><li>About 4.3% of damage when slotted (1.0% averaged over all top parses).</li><li>27% use, median 15.</li><li>TEN runs it as the 4th, at least level 10 for party Predation.</li><li>Lifestealing Blade vs Focused Block at equal CP: −1.5% per player (25 vs 66 players; the sign flips to +1.2% under another grouping), so no difference.</li></ul> | [NM], [TEN](https://docs.google.com/document/d/15J0xIIlOGvp0NSGui7NK0MJpbgZTjXuZKAahHnkr2G4/edit), [DB](https://aion2.app/db/skills/11340000) |

**Shard order:** derived from the NM medians and DB breakpoints. TEN's order: Rage Burst 5 → 20, Zikel's at least 10, Lunge Stance 5 → 20, Lifestealing Blade at least 10. Lunge Stance 10 only adds move speed, and its level-15 Identify Weakness boost mostly adds crit, which top Gladiators already have at the cap. So it's reasonable to push Zikel's to 15 before Lunge Stance 10–15.

| Step | Stigma levels | Shards |
|---|---|---|
| 1 | Rage Burst 5 → Lunge Stance 5 → Zikel's Blessing 10 → Focused Block 5 (or Lifestealing Blade 10) | 5 + 5 + 15 + 5 = 30 |
| 2 | Zikel's Blessing 15 → Lunge Stance 15 | +20 / +30 |
| 3 | Lunge Stance 20 | +40 |
| 4 | Rage Burst 10 → 15 → 20 | +70 |

Shard counts use the KR/TW costs, so they're UNVERIFIED on Global.

### PvP

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Focused Block | Core | 20 | n/a | 2 parries, movable at 10, +20% move speed on parry at 15 | [DB](https://aion2.app/db/skills/11110000) |
| Tenaciousness | Core | 20 | n/a | 3 s damage and CC immunity; 20 triggers it on Impact-type CC | [DB](https://aion2.app/db/skills/11380000) |
| Rage Burst | Core | 20 | n/a | +5% PvP Damage Boost; always crits at 15 | [DB](https://aion2.app/db/skills/11390000) |
| Blade Toss | 4th (vs healers) | 15 | n/a | −50% Incoming Heal on target; breaks shields at 15 | [DB](https://aion2.app/db/skills/11080000) |

This PvP four is **this guide's own pick, UNVERIFIED for Global**, built from the DB effects. The Korean post it was first tied to ([Inven Sep 9](https://www.inven.co.kr/board/aion2/6448/31743)) only asks which PvP stigmas people use, and lists none. The Oct 13 patch also adjusted Battlefield stats, so older PvP experience may not hold ([Oct 13 notes](https://store.steampowered.com/news/app/3393110/view/1846651706673374)).

### Solo / open world

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Lifestealing Blade | Slot 4 instead of Focused Block | 15 | n/a | Heals 10% of damage on up to 4 targets; 15 = −30 s cooldown | [DB](https://aion2.app/db/skills/11340000) |
| Lunge Stance / Zikel's Blessing / Rage Burst | Keep | as PvE | n/a | Same damage core | [NM] |

The solo list is derived from the DB effects and is UNVERIFIED (no source tests it).

---

## 5. Skills

**Global rules:**
- **Levels:** skill points (Wisdom Stones) take actives to 10. Levels 11–20 come from ring lines, blue Daevanion tiles and Arcana ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)). Weapon and guard skill lines are UNVERIFIED on Global (see the [README](README.md)).
- **Breakpoints:** specialty options 1–3 unlock at 8 with the first slot; option 4 and a second slot at 12; option 5 at **16**; the third slot at **20** (Bible ch.4). So 8 / 12 / 16 / 20 are the only levels where a skill changes. Levels in between add base damage only.
- **Season 1 limits:** 5 Arcana cards and 4–5 gear lines make 20 hard to reach ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Allyria ch.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).

### Actives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Overhead Slam | Keep; 1st priority | **20** (16 is required) | n/a (skills have no rarity) | 33.5% + 27.4% (Upward Strike chain) of damage. 100% of top Global players are at 16+, 54% at 20. | [NM], [DB](https://aion2.app/db/skills/11170000) |
| Rending Blow | Keep; 2nd | **16**, then 20 | n/a | 9.5% + 10.8% (Smashing Blow) of damage. 83% of top Global players have option 5 (so 16+), 6% have three picks (20). 16 fixes MP (option 5). TEN: mandatory to 16. | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [TEN](https://docs.google.com/document/d/15J0xIIlOGvp0NSGui7NK0MJpbgZTjXuZKAahHnkr2G4/edit) |
| Ruinous Blow | Keep; 3rd | **16**, then 20 | n/a | <ul><li>7.8% of damage plus the Prepare for Battle buff.</li><li>The buff logs the real skill level: top Global players' median is **16** (69% at 16+, 100% at 12+; 55 players). 33% have picked option 5.</li><li>Sheet and Korea's top 20: 20. TEN: at least 12.</li></ul> | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide), [TEN](https://docs.google.com/document/d/15J0xIIlOGvp0NSGui7NK0MJpbgZTjXuZKAahHnkr2G4/edit) |
| Sword Aura Rampage | Keep (stagger only) | **16** | n/a | 1.2% of damage. Used by 59 of 114 top players; 39% of those (20% of all) are at 16+. Option 5 at 16 = −1 s all cooldowns per hit. | [NM], [DB](https://aion2.app/db/skills/11280000) |
| Leaping Slam | Keep (gap closer) | **12** | n/a | Median buff level 14 in Global parses. Options 1+3 at 12. | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Keen Strike | Keep (MP, left click) | **12** | n/a | Option 4: −1 s Ruinous Blow cooldown per hit (needs 12). | [DB](https://aion2.app/db/skills/11020000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Defiance | Keep (CC break) | **16** | n/a | Option 5 at 16: +50% PvE damage tolerance during Tenacity. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [DB](https://aion2.app/db/skills/11260000) |
| Mocking Blade | Utility | **12** (sheet 16) | n/a | Knockdown; option 5 at 16 ignores Block/Evasion. Used by 23 of 114 top Global players (20%); most common pick 1+4 (39% of users), not the sheet's 1+5. | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Crushing Wave | AoE / leveling | **12** | n/a | Option 4 at 12 resets on crit. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [DB](https://aion2.app/db/skills/11050000) |
| Ankle Slice | Utility (root) | **12** | n/a | Sheet level. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Rush Strike | Mobility | **12** | n/a | Option 4 at 12: −10 s cooldown. 83% of the 83 top players who use it run 2+4. TEN: mandatory −10 s. | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [TEN](https://docs.google.com/document/d/15J0xIIlOGvp0NSGui7NK0MJpbgZTjXuZKAahHnkr2G4/edit) |
| Aerial Snare | Optional | **12** | n/a | Sheet level. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

**Stop points:** leave the utility skills (Leaping Slam, Keen Strike, Mocking Blade, Crushing Wave, Ankle Slice, Rush Strike, Aerial Snare) at 12; nothing past 12 adds damage for them. Push Overhead Slam to 20 and Rending Blow and Ruinous Blow to 16 first. Derived from the breakpoints and NM data.

### Passives

The order differs by source: Korea's top 20 put Experienced Counterstrike > Murderous Burst > Attack Preparation ≈ Impact Hit (they roll EC and MB on every armor piece); the Global sheet's order is Impact Hit > Attack Preparation > Experienced Counterstrike; TEN's is Attack Preparation > Experienced Counterstrike > Murderous Burst. The gear lines below follow the sheet. Passives level the same way as actives, plus green Daevanion tiles and armor/accessory lines ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)). Global target = the median level of top Global players (from NotMeter buff levels). Korean endgame levels are shown for direction only.

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Experienced Counterstrike | 1st (KR) / 2nd (TEN) | **17+** (Global median 17; KR 35) | n/a | Front Attack Damage Boost; the party gets +5.4% PvE damage on Block (level-1 values) | [DB](https://aion2.app/db/skills/11780000), [NM buffs], [NotMeter KR](https://notmeter.com/?view=setup-guide), [TEN](https://docs.google.com/document/d/15J0xIIlOGvp0NSGui7NK0MJpbgZTjXuZKAahHnkr2G4/edit) |
| Murderous Burst | 2nd (KR) / 3rd (TEN) | **16+** (Global median 16; KR 31) | n/a | AoE proc + 5.5% Crit Damage Boost (level 1) | [DB](https://aion2.app/db/skills/11800000), [NM buffs], [TEN](https://docs.google.com/document/d/15J0xIIlOGvp0NSGui7NK0MJpbgZTjXuZKAahHnkr2G4/edit) |
| Attack Preparation | 3rd (KR) / **1st (TEN)** / 2nd (sheet) | as high as gear allows (KR 27) | n/a | +5.5% PvE Damage Boost, +100 Accuracy (level 1). NotMeter can't log its level. | [DB](https://aion2.app/db/skills/11750000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [TEN](https://docs.google.com/document/d/15J0xIIlOGvp0NSGui7NK0MJpbgZTjXuZKAahHnkr2G4/edit) |
| Impact Hit | 4th (KR) / **1st (sheet)** | as high as gear allows (KR 27) | n/a | +11.2% Impact-type Chance and +0.3% Double Chance (level 1). NotMeter can't log its level. | [DB](https://aion2.app/db/skills/11760000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Identify Weakness | 5th | as high as gear allows (KR 18) | n/a | +100 Crit, +0.5% Perfect. Ranks lower on Global because top Gladiators already sit at the 50% crit cap | [DB](https://aion2.app/db/skills/11740000), [genus audit](../docs/genus-audit.md) |
| Survival Willpower | Defensive | **15** (Global median) | n/a | CC resist + tolerance | [NM buffs] |
| Blood Absorption, Protection Armor, Survival Stance, Destructive Impulse | Leave at skill-point level | 10 | n/a | Not damage-priority in any source | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

"NM buffs" = buff skill levels inside the same NotMeter Global parses (median of the top-20-per-boss set).

---

## 6. Specializations

### Skill specialties (pick 3 of 5)

| Item | Recommendation (picks at 8 / 12 / 16 / 20) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Overhead Slam | 3 / 3+4 / 3+5 / **3+4+5** | 20 | n/a | <ul><li>3: Upward Strike chain.</li><li>4: always crits.</li><li>5: no cooldown.</li><li>Global top: 3+4+5 54%, 3+5 27%, 4+5 18%.</li></ul> | [NM], [DB](https://aion2.app/db/skills/11170000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Rending Blow | 3 / 3+4 / 3+5 / **3+4+5** | 20 | n/a | <ul><li>3: mobile.</li><li>4: +12% vs few targets.</li><li>5: MP on crit.</li><li>Global: 3+5 75%.</li></ul> | [NM], [DB](https://aion2.app/db/skills/11010000) |
| Ruinous Blow | 1 or 3 / **1+4 or 3+4** / 4+5 / **1+4+5** | 16–20 | n/a | <ul><li>4: extra damage, the fixed pick.</li><li>Global top split: 3+4 (32%), 1+4 (19%), 4+5 (19%).</li><li>The sheet and Korea's top 20 run 1+4+5.</li></ul> | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Sword Aura Rampage | 4 / 4+5 at 16 | 16 | n/a | <ul><li>4: multi-hit.</li><li>5: −1 s all cooldowns per hit.</li><li>Global picks are mixed (2+4, 4+5, 2+5).</li><li>Korea runs 4+5.</li></ul> | [NM], [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Keen Strike | 1 / **1+4** (Global) or 2+4 (sheet) | 12 | n/a | <ul><li>4: −1 s Ruinous Blow cooldown per hit.</li><li>1 (MP) is the Global top pick (39%).</li><li>The sheet takes 2 (lifesteal).</li></ul> | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Leaping Slam | 1 / **1+3** | 12 | n/a | 1: 3 s Prepare for Battle. 3: resets on kill. Global 67%. | [NM], [DB](https://aion2.app/db/skills/11190000) |
| Rush Strike | 2 / **2+4** | 12 | n/a | Global 83% of its users. | [NM] |
| Defiance | 3 / **3+4**, 3+5 at 16 (sheet) | 16 | n/a | Global mixed: 3 (33%), 3+4 (32%). | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Mocking Blade | 1 / 1+5 at 16 | 16 | n/a | Sheet. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Crushing Wave | 1 / 1+4 | 12 | n/a | Sheet. (Korea's "4+5" rests on one sample.) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Ankle Slice | 3 / 3+4 | 12 | n/a | Sheet. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Aerial Snare | 1 / 1+3 | 12 | n/a | Sheet. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

**PvP changes (UNVERIFIED, from the DB text):**
- Overhead Slam keeps 3+4+5.
- Ruinous Blow option 5 ignores Block/Evasion. It is the PvP pick over option 1.
- Defiance option 1 adds the Wrath Burst chain.

### Daevanion boards (Global)

| Item | Recommendation | Target | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Points | About 316 at 45 after Sealed Dungeons and side quests, +50 Shugo Festival shop, +50 Nightmare shop (416) | — | n/a | Global start | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Nezekan / Zikel / Vaizel / Triniel (shared points) | <ul><li>Priority: Orange > Blue > Green > White.</li><li>Take a blue Overhead Slam / Rending Blow tile first whenever it lifts a skill to 8 / 12 / 16 / 20.</li><li>White: Attack > Crit > HP.</li></ul> | — | n/a | Blue tiles = active skill levels; orange = big % stats | [Allyria ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Bible ch.7](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Skip in PvE | Multi-hit Resist (Triniel orange), Critical Damage Tolerance (Vaizel orange) | — | n/a | No PvE value | [Bible ch.7](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Global changes | <ul><li>Orange % tiles cut 2.5% → 1.5%.</li><li>Attack 5 → 3, Crit 10 → 5.</li><li>**Ariel (PvE) board removed.**</li><li>Azphel PvP stats reduced.</li><li>About 200 fewer points at 45.</li></ul> | — | n/a | Global-specific | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Azphel (PvP board) | Fill for PvP; 36 points from the Abyss Monolith feathers, more from the Abyss Trade Shop | — | n/a | PvP only | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Bible ch.7](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Resets | Kinah, nearly free | — | n/a | | [Allyria ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |

A Gladiator-specific tile-by-tile path is UNVERIFIED. No Global Gladiator board guide exists, and the Global boards differ from Korea's.

---

## 7. Tier list

| Content | Tier | Placement reason | Source |
|---|---|---|---|
| PvE (dungeons / bosses) | **A** (3rd of 8) | NotMeter Global class score 110.46 (Chanter 118.79, Ranger 114.85 ahead). +5.3% vs average at equal CP (all ranked parses; +6.4% on the top-20-per-boss set alone). | [NM classPerformance](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |
| PvP | **UNVERIFIED** (community: S–A) | No Global PvP data. Launch-week opinion lists rank Gladiator high in PvP. | [ExitLag](https://www.exitlag.com/news/aion-2-class-tier-list/) (opinion) |
| Solo / leveling | **A (opinion, UNVERIFIED)** | <ul><li>Self-heal on hit (Blood Absorption).</li><li>AoE filler hits 4 targets.</li><li>Lifestealing Blade.</li></ul> No Global leveling data exists. | [DB](https://aion2.app/db/skills/11730000) |

The full cross-class tier list is in [README](README.md#overall-tier-list).

---

## 8. Gear

**Global gear rules:**
- **Grades:**
  - **No Heroic gear in Season 1**, so **Unique (yellow) is the settle rarity for every slot** ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
  - Unique gear goes to +15, then 5 Amp levels ([Bible ch.1](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).
- **Stat lines:** crafted gear has 5 lines and is best in slot. Dungeon gear has 4 ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Allyria ch.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).
- **PvE Damage Boost and Potential:** PvE Damage Boost was removed from weapons, guards and accessories on Global ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). Potential stats are PvP-only ([Bible ch.1](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).
- **Not on Global yet:** Brooch, Seals and Pendant ([Allyria §6.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). The Ludra raid (Sanctuary) hasn't arrived either; NC calls it upcoming ([Producer's Letter](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac95cd8d97eae18cc40e3d7)).

### Phases

| Phase | What to get | Source |
|---|---|---|
| All phases | See [README → Gear phases](README.md#gear-phases): the live Global sheet roadmap (Draupnir → Vakron → Uruguru accessories → Transcendence) plus later dungeons (Kromede, Ferocious Horn Den) from the sheet's older Oct 2 roadmap and Allyria. | [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [README](README.md#gear-phases) |

### Per slot (endgame)

| Item | Recommendation (stat lines in order) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Weapon (greatsword) | Crafted weapon if you can, else the best dungeon weapon (older roadmap: Kromede / crafted Splendent Dark Dragon Lord). Weapon Damage Boost > Combat Speed > Might > Precision > Damage Boost > Multi-hit > Attack. TEN: Weapon Damage Boost > Damage Boost > Combat Speed > Might > Multi-hit > Precision. | **+17** | Unique | Highest offensive base and lines | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [TEN](https://docs.google.com/document/d/15J0xIIlOGvp0NSGui7NK0MJpbgZTjXuZKAahHnkr2G4/edit) |
| Guard | Best available (older roadmap: Ferocious Horn Den). Weapon Damage Boost > Combat Speed > Damage Boost > Might > Precision > Multi-hit > Attack | **+17** | Unique | Same pool as the weapon | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Bible ch.2](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Helmet | Incoming Heal > Impact Hit > Attack Preparation > Double Chance > Attack Increase > Crit > Attack | **+15** | Unique | Passive lines carry Impact Hit / Attack Preparation | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Shoulders | Crit Damage Boost > Impact Hit > Attack Preparation > Accuracy > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Chest | Damage Boost > Impact Hit > Attack Preparation > Crit > Accuracy > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Legs | Damage Tolerance > Impact Hit > Attack Preparation > Perfect > Attack Increase > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Gloves / Boots | Combat Speed (gloves) / Move Speed (boots) > Impact Hit > Attack Preparation > Perfect > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Bible ch.3](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Cloak | Impact Hit > Attack Preparation > Smite > Double Chance > Attack Increase > Crit > Attack. TEN: Double Chance > Perfect > Attack Increase > Attack. | **+15** | Unique | The sheet lists Smite and Double Chance separately (Sirin writes "Smite/Double Chance"). The Bible's Global list allows Perfect on capes; Sirin says it was removed on Global (see discrepancies) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [TEN](https://docs.google.com/document/d/15J0xIIlOGvp0NSGui7NK0MJpbgZTjXuZKAahHnkr2G4/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Bible ch.3](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Earrings / Necklace | Impact Hit > Attack Preparation > Experienced Counterstrike > Might > Precision > Accuracy > Crit > Attack. Necklace: add **Combat Speed** (new on Global necklaces); earrings: Move Speed. | **+16** | Unique | Passive lines | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Bible ch.3](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Rings | Overhead Slam > Rending Blow > Ruinous Blow > Might > Precision > Attack | **+17** | Unique | The only accessory with active-skill lines | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Bible ch.2](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Bracelets | Story Unique + side-quest blue for now; later Sanctuary bracelets. Wisdom > Destruction > Time > Illusion > Death | **+15** | Unique (slot 1); Epic / blue (slot 2) | Divine stats, at half value on Global (10 = 1%) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Belt / Amulet | Upgrade with scrolls (strongholds / feathers). Amulet: +10, then Substance Morph to the next grade (live sheet). | to Unique (yellow / "gold"), then stop for Season 1 | **Unique** | Gets expensive in the first weeks | [Allyria §6.1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Clash Runes (×2) | Fixed stats per level; they can break | **+5** (sheet) to **+6/7** (Allyria) | n/a | High risk past 7 | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Allyria §6.1.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |

### Other systems

| Item | Recommendation | Source |
|---|---|---|
| Manastones | Front Damage Boost > Weapon Damage Boost ≈ Crit Damage Boost > Damage Boost > Attack (yellow +100 lines) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Bible ch.5](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Arcana (5 cards in S1) | <ul><li>Chalice: Time.</li><li>Parchment: Life or Destiny.</li><li>Compass: Death or Freedom.</li><li>Bell: Destruction.</li><li>Mirror: Illusion or Wisdom.</li></ul> Aim the skill lines at Overhead Slam, Rending Blow, Experienced Counterstrike and Murderous Burst. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Pet Genus | <ul><li>Special line 4: Double Chance.</li><li>Line 4 on other boards: PvE Damage Boost. On Varian, Front Attack Damage Boost is a close alternative for a 77%-frontal class (the Bible and sheet put it first; the audit rates it a tie).</li><li>Lines 1/5: Max Attack.</li><li>Lines 3/6/9: Power Shard Damage Bonus (top Gladiators are crit-capped).</li><li>Line 7: PvE Damage Tolerance.</li></ul> | [Genus audit (Global client tables)](../docs/genus-audit.md), [aion2timers data](https://www.aion2timers.com/insight/) |
| Wings | <ul><li>Can't be enhanced in Season 1.</li><li>Talisra (Season Shop) is the end goal for Cooldown Reduction.</li><li>The sheet's Eroded 45% / Talisra 23% figures are copied from the Bible's KR Chanter data, so Eroded on Global is UNVERIFIED.</li></ul> | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Allyria §6.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Titles | Global removed Double Chance from all titles and cut Combat Speed / CDR about 30%. The sheet: Playing God > Unbound Genus > Guardian of Verteron. | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

[NM]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM buffs]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
