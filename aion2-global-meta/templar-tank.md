# Templar (守護星) — Tank spec · AION 2 Global

**Patch covered:** Global client build **25926599** (Steam public branch, updated 2026-10-14 06:40 UTC). That is the [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374) on top of the [Oct 6 PDT patch](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544) and the [Oct 8 PDT hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1). None of the three changed a Templar skill. Build id: [SteamCMD](https://api.steamcmd.net/v1/info/3393110). NotMeter data (week of Oct 7–14) was recorded on the previous build 25800038. **Written:** 2026-10-13, **updated for the Oct 13 patch:** 2026-10-14.

**Tags:** [Global] · [KR/TW-confirmed] = Korean or Taiwanese source checked against the Global client · UNVERIFIED.

**Main data sources:**
- **NM:** [NotMeter Global ranking](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), week of Oct 7–14. (NotMeter has since retired this generation, so the link returns 404; see the [README](README.md).) Top 20 Templar parses on each of 15 bosses: 300 parses from 121 players, median CP 140,113, median DPS 58,553.
- **DB:** [aion2.app Global client DB](https://aion2.app/db/skills?class=Templar), client dated 18.09.2026.
- **Sheet:** [Global class sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview).
- **Sheet snapshot:** citations of this class's sheet tab refer to the copy downloaded on Oct 14. Later that day the author replaced the tab with a link to [daevaos](https://daevaos.com/guides/templar-class-guide-pve), where the build is now maintained; differences found are noted where they matter.
- **Bible:** [Kanon's Bible](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview).

**Why there is only one Templar spec on Global.** Korea also runs a "natural-block DPS" Templar. In the 85 Global parties with two Templars, both received similar healing (median ratio 0.91). 35 had Taunt on both Templars; in 13, one Templar ran neither Taunt nor Noble Armor. That is too few, and too mixed, to show a separate Global DPS-Templar build ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json); method in [README](README.md#method-notes)). The damage-leaning and safety-leaning versions below are two **loadouts** of this one spec.

**Korea's Sep 16 patch is live on Global.** Global parses show Korea's Sep 16 changes are live: Templars show a second Noble Armor buff in 452 of 507 Templar fights longer than 130 s, and Chanters a second Guardian Blessing in 85 of 93 (buff applications; one cast never lasts past 120 s) (Sep 16 cut both cooldowns from 5 min to 2 min). Assassin Shadowstrike's option-2 buff lasts about 10 s (Sep 16 raised it from 5 s) ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [KR Sep 16 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6aa99cb8a279104f7d9d5c34)). The aion2.app "Global" database (client 18.09.2026) still shows the older values, so it is an older client snapshot (dated Sep 18).

For Templar, Sep 16:
- lengthened the Pummel / Punishing Strike / Judgment cancel delay (aimed at mouse macros);
- gave Warding Strike, Annihilate and Punishment +10% PvE damage, and Shield Smite +20%;
- cut Noble Armor's cooldown to 2 min;
- made Taunt's threat scale with damage.

Only the Noble Armor change can be measured in Global logs; the cancel delay, the damage changes and Taunt's threat are likely live but UNVERIFIED. Korean advice written after Sep 16 therefore probably applies to Global. From Korea's Aug 26 rework, "Judgment opens after any shield attack" is live (DB and logs), but Warding Strike's 30 → 25 s cut is **not**: the DB, questlog and Global use rates all fit a 30 s base ([DB](https://aion2.app/db/skills/12350000), [NM]).

**Watch (Korea only, not on Global):** Korea's Oct 14 patch changed Assault Fury (Defense and all-element tolerance up to 80%, no cooldown-reduction effect) and gave Shield of Protection −0.3 s cooldown on Block ([KR Oct 14 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6ace86b86cfe4756db5b8d81)). Neither is in Global's Oct 13 notes or questlog's Global data.

---

## 1. Overview

| Item | Recommendation / finding | Why | Source |
|---|---|---|---|
| Role | Main tank (sword and shield) | NC: "holding the battlefield with an unbreakable shield" | [NC class list](https://aion2.plaync.com/en-us/about/index#classes) |
| Playstyle | <ul><li>Judgment is **42.5%** of damage. Every shield attack (Warding Strike, Shield Smite, Doom Shield, Shield Rush) opens it for 2–3 s, and at skill level 16 it has no cooldown.</li><li>Every Punishment cast gives Executor (+20% PvE Damage Boost, +200 Accuracy for 20 s), charged or not: Executor is up in 642 of 648 Global parses with only uncharged Punishments. Charging only adds damage.</li></ul> | Damage shares and skill text | [NM], [DB Judgment](https://aion2.app/db/skills/12240000), [DB Punishment](https://aion2.app/db/skills/12090000) |
| Strengths | <ul><li>**Taunt's Shrink:** boss −10% Attack and −200 Accuracy, and at level 5 −10% PvE Damage Tolerance, which raises the damage of the whole party.</li><li>**Fury:** +PvE damage to the party on every Block: 5.5% at level 1, about 13.5% at the Global median level 17. It doesn't stack with a Gladiator's Experienced Counterstrike.</li><li>**Party saves:** Nezekan's Shield (max-HP shield for the party: 41% at level 1, 55% at 15) and Comrade in Arms.</li></ul> | | [DB Taunt](https://aion2.app/db/skills/12120000), [DB Fury](https://aion2.app/db/skills/12780000), [DB Nezekan's Shield](https://aion2.app/db/skills/12320000), [DB Comrade in Arms](https://aion2.app/db/skills/12250000), [README party-buff rules](README.md#party-buffs) |
| Weaknesses | <ul><li>Low personal damage: NotMeter score 92.92, 6th of 8; only Spiritmaster and Cleric are lower.</li><li>Damage depends on Judgment windows and Judgment's level.</li><li>You hold aggro and face the boss.</li></ul> | | [NM classPerformance] |
| PvE standing (Global) | **Essential tank.** 64% of Global boss parses (3,400 of 5,303) have a Templar. At equal CP, top Templars deal +2.1% vs the class average (4th of 8). | Party presence and damage | [NM] |
| PvP standing (Global) | **UNVERIFIED.** No Global PvP data. | | — |
| Difficulty | **Medium.** Tank positioning, a charged Punishment and Judgment windows. The in-game macro handles the Judgment windows (see Macros). | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Who should play it | Players who want to lead pulls and carry party safety; the class every party looks for | Presence in 64% of parses | [NM] |

---

## 2. Max damage

### Single target (boss)

| Step | What to do | Why | Source |
|---|---|---|---|
| Pre-pull | **Noble Armor**, recast on cooldown | +max HP (5.4% at level 1, 11% at 15); at 15, ×1.5 Fury. Cooldown is **2 min** on live Global (Sep 16); the aion2.app database's 300 s is outdated. Global logs show a second Noble Armor buff in 452 of 507 Templar fights over 130 s, and questlog's Global data gives 120 s duration and cooldown. | [DB](https://aion2.app/db/skills/12230000), [questlog](https://questlog.gg/aion-2/en/db/skill/12230000), [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |
| Pre-pull | **Charge Punishment to Max** (3 charge levels) | Any cast gives Executor (+20% PvE Damage Boost, +200 Accuracy for 20 s; 30 s cooldown); charging only adds damage. Uncharged (macro) casts do about one third of a Max cast (DB 1,268 vs 3,805; Global parses 26–44% depending on method). Punishment is 11.5% of damage. | [DB](https://aion2.app/db/skills/12090000), [NM] |
| Open | **Doom Shield** (rush, knockdown, opens Judgment for 3 s; at 5 resets Annihilate) → **Taunt** (Shrink 15 s) → **Battlefield Banner** (Attack from Defense; 10 s at level 1, 20 s at 20) | Doom Shield is the gap closer and a Judgment opener. Taunt's Shrink is the party's damage debuff. | [DB Doom Shield](https://aion2.app/db/skills/12070000), [DB Taunt](https://aion2.app/db/skills/12120000), [DB Banner](https://aion2.app/db/skills/12450000) |
| Core | Hold **Vicious Strike** (left click) + the macro: Judgment → Warding Strike / Shield Smite → Pummel | Each shield attack reopens Judgment. Top 10% Global: 51.2 Judgment uses a minute (median 44). | [NM], [DB Judgment](https://aion2.app/db/skills/12240000) |
| Burst | **Annihilate → Doom Shield → Annihilate** | Doom Shield 5 resets Annihilate's cooldown. Annihilate is 6.9% of damage. Option 3: +100% vs Incapacitated-immune bosses. | [DB Annihilate](https://aion2.app/db/skills/12300000), [DB Doom Shield](https://aion2.app/db/skills/12070000), [NM] |
| Recast | Charged Punishment every 30 s; Taunt and Banner on cooldown | Executor 20 s; Shrink 15 s (20 s at Taunt 20) | [DB](https://aion2.app/db/skills/12120000) |

**Line up:** Banner (20 s at level 20), Executor (20 s) and Empyrean Lord's Punishment's +10% PvE (10 s at 15, if slotted) together. Keep Taunt's Shrink up all the time. Derived from the DB durations; stigma buff durations measured in Global parses ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)).

### AoE (packs)

| Tool | Targets | Source |
|---|---|---|
| Vicious Strike and its chains, Pummel + Punishing Strike | up to 4 within 4 m | [DB Vicious Strike](https://aion2.app/db/skills/12010000), [DB Pummel](https://aion2.app/db/skills/12040000) |
| Warding Strike | up to 4 within 5 m; Warding = +20% PvE Damage Tolerance | [DB](https://aion2.app/db/skills/12350000) |
| Punishment | up to 4 within 4 m of the target | [DB](https://aion2.app/db/skills/12090000) |
| Shield Smite option 5 / Annihilate option 5 | AoE stun / AoE | [DB Shield Smite](https://aion2.app/db/skills/12100000), [DB Annihilate](https://aion2.app/db/skills/12300000) |
| Grapple (stigma) | pulls up to 4 within 7 m | [DB](https://aion2.app/db/skills/12220000) |

**AoE order:** UNVERIFIED (no Global AoE test). From the DB: Poach or Doom Shield to pull, Warding Strike, then the held Vicious + macro line, with a charged Punishment on the group.

---

## 3. Macros

The in-game macro: Settings → Key Settings → General → Gameplay → Macro ([Allyria §3.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Rows are numbered from the bottom; this guide treats row 0 as the highest priority, which is UNVERIFIED on Global (see [README](README.md)). Charge skills fire uncharged from a macro, so Punishment stays on its own key ([NM]: Global parses log uncharged Punishment casts; Allyria's FAQ says the same for Ranger's Deadshot).

### Macro A: Global sheet layout (Oct 14 snapshot)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Battlefield Banner | Taunt | Debilitating Smash | — | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| 2 | Annihilate | Judgment | Warding Strike | Pummel | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| 3 | Shield Smite | — | — | — | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

- **Delays:** 10 ms.
- **Hold:** Vicious Strike + the macro key. The sheet's option 1: hold left click (Quick Use 1) and the macro key (a mouse button, RMB recommended). Both are native key bindings; the sheet names no external software.
- **Press yourself:**
  - Noble Armor;
  - charged Punishment;
  - Doom Shield (E), Shield of Protection (Q) and Shield Rush (key 2), as in the sheet's key layout;
  - Poach.
- **Debilitating Smash:** the sheet keeps it on row 2 of the Banner entry. It is under 1% of damage, and Defense only counts for 10% of its value in PvE, so dropping it costs little ([Bible ch.11](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview), [NM]).

**Why it works (this guide's reading of the sheet):** Annihilate on row 0 fires on cooldown; Judgment on row 1 fires whenever a shield attack opens it, with Warding Strike and Pummel as fillers. Shield Smite on its own key lets you open a Judgment window yourself. Pummel in the same entry lets the held Vicious Strike cancel into the line. The sheet gives the layout, not this explanation.

**Pummel → Judgment cancel:** Korea's Sep 16 cancel-delay increase is live on Global, so the old Pummel → Judgment cancel is slower. Pummel in the same line as Judgment lets the held Vicious Strike cancel into Judgment ([Inven Sep 5](https://www.inven.co.kr/board/aion2/6438/25862), KR/TW; written before Sep 16, and that author then recommended a separate Pummel line). After Sep 16, the Sep 17 post uses plain Vicious + Judgment ([Inven Sep 17](https://www.inven.co.kr/board/aion2/6438/26762), KR/TW). The exact timing on Global is UNVERIFIED by a Global test.

### Macro A2: the sheet author's current layout (daevaos, Oct 14)

| Key | Stack (row 0 first) | Source |
|---|---|---|
| Right mouse (macro) | Judgment, Warding Strike, Shield Smite, Pummel | [daevaos](https://daevaos.com/guides/templar-class-guide-pve) |
| 4 | Annihilate (its own macro entry) | same |
| 2 | Battlefield Banner, Taunt, Debilitating Smash | same |
| Q / E | Doom Shield / Shield of Protection | same |

This replaces the screenshot layout above on the author's new page. Both put Judgment and its openers in one line; they differ in where Annihilate and Shield Smite sit.

### Macro B: Korean one-button variant (needs external software: not recommended)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Judgment | Warding Strike | Doom Shield | Shield Smite | [Inven Sep 17](https://www.inven.co.kr/board/aion2/6438/26762) [KR/TW-confirmed: the same skills and the Aug 26 Judgment opener are on Global] |
| 2 | Annihilate | Noble Armor | Battlefield Banner | Empyrean Lord's Punishment | same |

- **How the post runs it:** the in-game skill macro holds only entry 1 (the Judgment chain). Everything else runs through an **external one-button mouse macro**: on press it sends left click (Vicious Strike), the skill-macro key and Punishment, and while held it repeats entry 2 every 2 ms ([Inven Sep 17](https://www.inven.co.kr/board/aion2/6438/26762), KR/TW). External macro software is a ban risk on Global (table below). Without it, entry 2 has to be pressed by hand.
- **Cost:** buffs fire on cooldown, during mechanics too.
- **Power of the Storm:** after a few tries the author judged that under a Chanter's Power of the Storm, the Vicious → Pummel → Judgment line produced no extra Pummels, so they use plain Vicious + Judgment ([Inven Sep 17](https://www.inven.co.kr/board/aion2/6438/26762), KR/TW).
- **Global note:** Noble Armor has a 2-min cooldown on live Global, so its macro row keeps it on cooldown.

### Banned or nerfed on Global

| Item | Status | Source |
|---|---|---|
| In-game skill macro | Allowed (built-in) | [Allyria FAQ](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| External macro software or hardware | **Risk.** NC bans programs or devices "enabling actions impossible for regular users"; the Oct 10, Oct 12 and Oct 14 ban waves named macros | [NC Operation Policy](https://www.plaync.com/policy/operation/aion2global), [NC restrictions notice](https://aion2.plaync.com/en-us/board/notice/view?articleId=6acaa7506b722c561dc6aae9), [Oct 14 notice](https://store.steampowered.com/news/app/3393110/view/1846651706673527) |
| Templar macro nerfs on Global | Korea's **Sep 16 cancel-delay change is live** (Pummel / Punishing Strike / Judgment). No Templar change in the Oct 6, Oct 8 or Oct 13 notes. | [Oct 13](https://store.steampowered.com/news/app/3393110/view/1846651706673374), [Oct 6](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544), [Oct 8](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1), [NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json) |

---

## 4. Stigmas

**Global rules:**
- 4 slots, cap 20; resets are free ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- Stigmas have no rarity tiers, so "n/a" (an inference: no source lists stigma rarities).
- 75 shards to 20 (1/2/4/8 per level), confirmed in questlog's Global skill data ([questlog](https://questlog.gg/aion-2/en/db/skill/17410000)).

**Global usage:**
- **All parties:** Taunt 76–78%, Noble Armor 74–79%, Doom Shield 65–71%, Battlefield Banner 63–67%, Shield of Protection 50–56%, Empyrean Lord's Punishment 16–23%, Nezekan's Shield 9–12%, Executing Blade 9–11%, Comrade in Arms about 1% ([NM], party analysis).
- **Top 20 per boss (per player):** Noble Armor 89% (median 15), Doom Shield 77% (median about 14), Taunt 77% (only 12% at 20; 44% at 15–19), Banner 77% (median 18–20), Shield of Protection 46% (median about 8), Executing Blade 4%.

### PvE: damage-tank loadout (most used on Global)

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Taunt | Always | **20** (5 first) | n/a | <ul><li>5: Shrink adds −10% boss PvE Damage Tolerance for the party.</li><li>15: −5 s cooldown.</li><li>20: Shrink +5 s, to 20 s on a 25 s cooldown. Global CDR tops out around 19–21% with best gear (Sirin); in Global logs the median time between Taunt casts in fights over 150 s is 33 s at level 20 and 38 s at 15–19, so Shrink isn't up all the time.</li><li>20 is the target, but only 12% of top-20 Global Templars are there yet (44% at 15–19).</li></ul> | [DB](https://aion2.app/db/skills/12120000), [Sirin CDR](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Noble Armor | Always | **15** (20 later) | n/a | <ul><li>89% use, median 15.</li><li>+max HP: 5.4% at level 1, 11% at 15.</li><li>10: ×1.5 Insulting Roar.</li><li>15: ×1.5 Fury.</li><li>20: +10% Incoming Heal.</li></ul> | [NM], [DB](https://aion2.app/db/skills/12230000) |
| Battlefield Banner | Damage slot | **20** | n/a | <ul><li>77% use, median 20.</li><li>10: +10% Weapon Damage Boost.</li><li>15: +20% Attack from Defense.</li><li>20: −30 s cooldown.</li><li>At equal CP, Banner users (63 players) were about 2–3% ahead of Shield of Protection users (21), averaged per player (independent re-check: +3.2% ±5.0). That isn't significant ([method](README.md#method-notes)).</li></ul> | [NM], [DB](https://aion2.app/db/skills/12450000) |
| Doom Shield | Damage / engage slot | **15** (5 minimum) | n/a | <ul><li>77% use, median about 14 (10–14: 39%, 15+: 28%).</li><li>5: resets Annihilate.</li><li>10: +200 Block.</li><li>15: resets on kill.</li><li>20 only adds knockdown chance.</li></ul> | [NM], [DB](https://aion2.app/db/skills/12070000) |

**The sheet author's current build (daevaos, Oct 14):** Taunt, Battlefield Banner, Shield of Protection and Doom Shield, all at 20, with no Noble Armor ([daevaos](https://daevaos.com/guides/templar-class-guide-pve)). The older sheet ranked Taunt, Noble Armor, Shield of Protection, Doom Shield. This guide keeps Noble Armor because 89% of top-20 Global Templars slot it ([NM]).

### PvE: safety-tank loadout (hard or new content)

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Taunt | Always | 20 | n/a | As above | [DB](https://aion2.app/db/skills/12120000) |
| Noble Armor | Always | 15 | n/a | As above | [NM] |
| Shield of Protection | Replaces Banner | **5** (10 if you move a lot) | n/a | <ul><li>Guaranteed Block and +100% Block Damage Reduction.</li><li>5: second use.</li><li>10: mobile.</li><li>47–56% Global use, median about 8 (5–10).</li></ul> | [DB](https://aion2.app/db/skills/12110000), [NM] |
| Empyrean Lord's Punishment or Nezekan's Shield | Replaces Doom Shield | **15** | n/a | <ul><li>Empyrean Lord's Punishment 15: +10% PvE Damage Boost for 10 s, 50 stagger.</li><li>Nezekan's Shield: max-HP party shield (41% at level 1, 55% at 15); 15 adds +20% PvE Damage Tolerance. 9–12% of all Global Templars use it.</li></ul> | [DB ELP](https://aion2.app/db/skills/12310000), [DB Nezekan's](https://aion2.app/db/skills/12320000) |

Comrade in Arms at 20 (restores 50% HP when it ends): Korea's Feb guide calls it the best party stigma, needing level 20 ([Inven Feb](https://www.inven.co.kr/board/aion2/6438/7621), KR/TW; effect confirmed in the [DB](https://aion2.app/db/skills/12250000)). It's rare on Global, about 1%.

Executing Blade is on the sheet's stigma list; 9–11% of all Global Templars and 4% of the top 20 use it ([Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NM]).

**Shard order (damage loadout):** derived from the DB breakpoints and the NM medians.

| Step | Stigma levels |
|---|---|
| 1 | Taunt 5 → Doom Shield 5 → Noble Armor 10 → Banner 10 |
| 2 | Noble Armor 15 → Taunt 15 → Banner 15 → Doom Shield 15 |
| 3 | Banner 20 → Taunt 20 |

### PvP

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Comrade in Arms | Core (party) | 20 | n/a | 20: restores 50% HP when it ends | [Inven Feb](https://www.inven.co.kr/board/aion2/6438/7621) (KR/TW), [DB](https://aion2.app/db/skills/12250000) |
| Noble Armor | Core | 20 | n/a | 20: +10% Incoming Heal | [Inven Feb](https://www.inven.co.kr/board/aion2/6438/7621) (KR/TW), [DB](https://aion2.app/db/skills/12230000) |
| Shield of Protection | Core | 20 | n/a | Guaranteed Block; 20 restores 10% HP | [Inven Feb](https://www.inven.co.kr/board/aion2/6438/7621) (KR/TW), [DB](https://aion2.app/db/skills/12110000) |
| Second Skin | Survival | 20 | n/a | +30% PvE / +15% PvP Damage Tolerance; 20 adds +10% PvP | [Inven Feb](https://www.inven.co.kr/board/aion2/6438/7621) (KR/TW), [DB](https://aion2.app/db/skills/12190000) |

This is the PvP all-in set from Korea's Feb guide; out of a party, it swaps in Grapple or Armor of Balance. The same guide doesn't recommend Doom Shield except in special situations, and doesn't list Banner. It's **UNVERIFIED for Global**: the guide predates Global's launch, and the Oct 13 patch adjusted Battlefield stats ([Oct 13 notes](https://store.steampowered.com/news/app/3393110/view/1846651706673374)).

### Solo / open world

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Doom Shield | Pull opener | 15 | n/a | Resets on kill at 15 | [DB](https://aion2.app/db/skills/12070000) |
| Noble Armor | Keep | 15 | n/a | | [DB](https://aion2.app/db/skills/12230000) |
| Second Skin | Replaces Taunt (Taunt does nothing solo) | 20 | n/a | 20: +20% more PvE Damage Tolerance | [DB](https://aion2.app/db/skills/12190000), [Inven Feb](https://www.inven.co.kr/board/aion2/6438/7621) (KR/TW) |
| Battlefield Banner | Damage | 15 | n/a | | [DB](https://aion2.app/db/skills/12450000) |

The solo list is derived from the DB effects and is UNVERIFIED on Global.

---

## 5. Skills

Global rules:
- Skill points take a skill to 10; 11–20 come from ring lines, blue Daevanion tiles and Arcana ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)). Weapon and guard carry no skill lines in the Global line lists.
- Specialty breakpoints: 8 (options 1–3), 12 (option 4 and a second slot), 16 (option 5), 20 (third slot).
- Sources: [Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview); Season 1 has 5 Arcana cards ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).

### Actives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Judgment | 1st; the class | **20** (16 is mandatory) | n/a | <ul><li>42.5% of damage.</li><li>98% of top Global Templars are at 16+, 36% at 20.</li><li>16 = no cooldown (option 5).</li></ul> | [NM], [DB](https://aion2.app/db/skills/12240000) |
| Vicious Strike | 2nd (held) | **16**, then 20 | n/a | <ul><li>Its chain adds Vicious 3.4% + Decisive 3.9% + Desperate 4.3% + Threatening Blow 4.4% (means over all 300 parses).</li><li>12: −2 s Warding Strike per hit, which means more Judgment windows.</li><li>55% of top Global Templars at 16+.</li></ul> | [NM], [DB](https://aion2.app/db/skills/12010000) |
| Pummel | 3rd | **16**, then 20 | n/a | <ul><li>4.6% + Punishing Strike 6.0%.</li><li>12: −1 s Punishment cooldown on hit (Global text, Sep 16 version).</li><li>40% at 16+.</li></ul> | [NM], [DB](https://aion2.app/db/skills/12040000) |
| Punishment | 4th | **16** | n/a | <ul><li>11.5% of damage.</li><li>16: ignores Block/Evasion and crits.</li><li>32% at 16+; Korea's top 20 at 20.</li></ul> | [NM], [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Annihilate | Burst | **12** | n/a | 6.9% of damage. 12 = 3+4 (76% of top Global). Korea's top 20: median 15, all 3+4, none with option 1. | [NM], [DB](https://aion2.app/db/skills/12300000), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Warding Strike | Judgment opener + mitigation | **16** (sheet) / 12 minimum | n/a | 12: option 4. 16: option 5 shares tolerance with the party. Global picks vary. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NM] |
| Shield Smite | Judgment opener | **12** | n/a | 12: −2 s cooldown. 2.9% of damage. | [NM], [DB](https://aion2.app/db/skills/12100000) |
| Debilitating Smash | Low | **12** | n/a | Under 1% of damage. 71% of top Global run 2+4. | [NM] |
| Shield Rush | Mobility / opener | **12** | n/a | 85% run 2+4 | [NM] |
| Poach | Pull | **12** | n/a | 1+3 (42%) or 1+4 (35%) | [NM] |
| Defiance | CC break | **16** (sheet) | n/a | Option 5: +50% PvE Damage Tolerance | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [DB](https://aion2.app/db/skills/12260000) |
| Flash Rampage | Stagger only | **12** | n/a | Korea's top 20: median 14 (7–16); those at 16+ run 4+5. Not in Global's top-damage list. | [NotMeter KR](https://notmeter.com/?view=setup-guide) |

**Stop points:** don't take Annihilate, Shield Smite, Debilitating Smash, Shield Rush or Poach past 12 until Judgment is 20 and Vicious / Pummel / Punishment are 16. Derived from the breakpoints and the NM damage shares. The sheet (Oct 14 snapshot) puts Vicious Strike, Pummel, Judgment and Punishment at 20 with 3/4/5; this guide's targets follow Global medians.

### Passives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Fury | 1st | **17+** (Global median 17; KR 36) | n/a | Front Damage Boost; +PvE damage to the party on Block (5.5% at level 1, about 13.5% at 17, 15% at 20) | [DB](https://aion2.app/db/skills/12780000), [NM buffs] |
| Impact Hit | 2nd (sheet) | as high as gear allows (KR 31) | n/a | Double Chance | [DB](https://aion2.app/db/skills/12760000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Insulting Roar | 3rd (sheet) | **17+** (Global median 17; KR 30) | n/a | +Attack on front attacks (5.5% at level 1, about 13.5% at 17); Enmity | [DB](https://aion2.app/db/skills/12770000), [NM buffs], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Punishing Benediction | 4th | **15** (Global median) | n/a | +Crit (100 at level 1, 240 at 15); 2.6% of damage from procs | [DB](https://aion2.app/db/skills/12730000), [NM] |
| Block Pain | Defensive | **15** (Global median) | n/a | +PvE Damage Tolerance when hit (11% at level 1, 25% at 15) | [NM buffs], [DB](https://aion2.app/db/skills/12800000) |
| Guarding Seal / Survival Willpower | Defensive | **11** (Global median) | n/a | | [NM buffs] |
| Ironclad Defense, Warding Shield, Enhance Health | Defensive filler | 10–15 | n/a | KR 12–16 | [NotMeter KR](https://notmeter.com/?view=setup-guide) |

---

## 6. Specializations

| Item | Recommendation (picks at 8 / 12 / 16 / 20) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Judgment | 3 / 3+4 / **4+5 or 3+5** / **3+4+5** | 20 | n/a | <ul><li>3: extra damage.</li><li>4: always crits.</li><li>5: no cooldown.</li><li>Global top: 3+4+5 36%, 3+5 34%, 4+5 27%.</li></ul> | [NM], [DB](https://aion2.app/db/skills/12240000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Vicious Strike | 3 / 3+4 / **4+5** / 3+4+5 | 16–20 | n/a | <ul><li>4: −2 s Warding Strike per hit.</li><li>5: Threatening Blow chain.</li><li>Global top: 4+5 50%, 3+4 32%.</li></ul> | [NM], [DB](https://aion2.app/db/skills/12010000) |
| Pummel | 3 / **3+4** / 4+5 / 3+4+5 | 16–20 | n/a | <ul><li>4: −1 s Punishment cooldown on hit. 5: Punishing Strike deals extra damage on hit. This is questlog's Global text and Korea's Sep 16 version; Global logs agree (option-4 holders cast Punishment 2.3 times a minute vs 1.7–1.8; option 5 adds about 42% to Punishing Strike, not a full extra activation) [Global-confirmed].</li><li>Global top: 3+4 41%, 4+5 30%.</li></ul> | [NM], [DB](https://aion2.app/db/skills/12040000) |
| Punishment | 3 / **2+3** / 3+5 / 2+3+5 | 16–20 | n/a | <ul><li>2: damage over time.</li><li>3: +30% skill speed.</li><li>5: crits, ignores Block.</li><li>Global top: 2+3 42%, 3+5 28%.</li></ul> | [NM], [DB](https://aion2.app/db/skills/12090000) |
| Annihilate | 3 / **3+4** | 12 (Korea's top 20: 15) | n/a | 3: +100% vs Incapacitated-immune bosses. 4: −10 s cooldown. Global 77%; Korea's top 20 100%. | [NM], [DB](https://aion2.app/db/skills/12300000), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Warding Strike | 1 / 1+4 / **1+5** | 16 | n/a | 1: −5 s cooldown. 5: party tolerance share. Global picks are split. | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NM] |
| Shield Smite | 3 / **3+4** (or 2+4 if MP-short) | 12 | n/a | Global 3+4 56%, 2+4 36%. 2 removes the MP cost. | [NM], [DB](https://aion2.app/db/skills/12100000) |
| Debilitating Smash | 2 / 2+4 | 12 | n/a | Global 71% | [NM] |
| Shield Rush | 2 / 2+4 | 12 | n/a | Global 85% | [NM] |
| Poach | 1 / 1+3 or 1+4 | 12 | n/a | Global 42% / 35% | [NM] |
| Defiance | 3 / 3+4 / 3+5 | 16 | n/a | Global 3 (41%), 3+4 (29%); sheet 3+5 | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

**PvP changes (UNVERIFIED, from the DB text):**
- Punishment option 5 (ignores Block/Evasion) becomes mandatory.
- Poach option 5 (stun) and Shield Smite option 1 (+1 s stun) gain value.

### Daevanion boards (Global)

| Item | Recommendation | Target | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Points | About 316 at 45, +50 Shugo, +50 Nightmare | — | n/a | | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Main four boards | <ul><li>Orange > Blue > Green > White.</li><li>A Judgment / Vicious / Pummel blue tile first when it reaches 8, 12, 16 or 20.</li><li>Fury and Insulting Roar green tiles next.</li></ul> | — | n/a | | [Allyria ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Bible ch.7](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Defense tiles | Higher priority for Templar than for DPS | — | n/a | Battlefield Banner turns Defense into Attack | [DB Banner](https://aion2.app/db/skills/12450000) |
| Skip (PvE) | Multi-hit Resist (Triniel), Crit Damage Tolerance (Vaizel) | — | n/a | | [Bible ch.7](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Global changes | Orange % 2.5 → 1.5; Ariel board removed; about 200 fewer points | — | n/a | | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

Korea has a node guide that says it works for every class ([Inven](https://www.inven.co.kr/board/aion2/6438/22546), KR/TW). Its paths assume Korea's boards and point totals, so a Global path is UNVERIFIED.

---

## 7. Tier list

| Content | Tier | Placement reason | Source |
|---|---|---|---|
| PvE tank | **S** (the only dedicated tank) | In 64% of Global boss parses; Taunt's Shrink and Fury raise the whole party's damage | [NM], [DB Taunt](https://aion2.app/db/skills/12120000) |
| PvE personal damage | **C+** (6th of 8) | NotMeter score 92.92; +2.1% at equal CP (4th) | [NM classPerformance] |
| PvP | **UNVERIFIED** | No Global PvP data | — |
| Solo / leveling | **B (opinion, UNVERIFIED)** | Very safe; lower damage | [DB](https://aion2.app/db/skills?class=Templar) |

---

## 8. Gear

Global rules:
- Season 1 has no Heroic gear, so **Unique is the settle rarity for every slot except bracelet slot 2, which is a blue (Epic) bracelet in Season 1** ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- Unique goes to +15, then 5 Amp levels ([Bible ch.1](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).
- Crafted gear has 5 lines and is best in slot ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- Phases: see [README → Gear phases](README.md#gear-phases), which follows the live sheet roadmap (MSQ → Draupnir → Vakron → Uruguru → Transcendence → Ludra prep; [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)). Kromede and Ferocious Horn Den come from the sheet's older Oct 2 roadmap and Allyria.

| Item | Recommendation (stat lines in order) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Weapon (longsword) | Crafted if you can, else the best dungeon weapon (older roadmap: Kromede). Weapon Damage Boost > Combat Speed > Might > Precision > Damage Boost > Multi-hit > Attack | **+17** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Guard (shield) | Best available (older roadmap: Ferocious Horn Den). Same lines (Damage Boost before Might) | **+17** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Helmet | Incoming Heal > Fury > Impact Hit > Double Chance > Attack Increase > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Shoulders | Crit Damage Boost > Fury > Impact Hit > Accuracy > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Chest | Damage Boost > Fury > Impact Hit > Crit > Accuracy > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Legs | Damage Tolerance > Fury > Impact Hit > Perfect > Attack Increase > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Gloves / Boots | Combat Speed / Move Speed > Fury > Impact Hit > Perfect > Crit > Attack | **+15** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Cloak | Fury > Impact Hit > Double Chance (the sheet also lists "Smite", the same stat) > Attack Increase > Crit > Attack | **+15** | Unique | Sirin says Perfect was removed from capes on Global; the Bible's Global list still has it (see discrepancies) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Bible ch.3](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Earrings / Necklace | Fury > Impact Hit > Insulting Roar > Might > Precision > Accuracy > Crit > Attack | **+16** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Rings | Vicious Strike > Punishment > Judgment > Might > Precision > Pummel > Warding Strike > Attack | **+17** | Unique | Korea's top 20 ring lines: Vicious, Judgment, Pummel, Punishment | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Bracelets | Wisdom > Destruction > Time > Illusion > Death | **+15** | Unique (slot 1); Epic / blue (slot 2) | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Belt / Amulet | Upgrade with scrolls; amulet to +10, then Substance Morph to the next grade (live sheet) | to Unique (yellow / "gold"), then stop for Season 1 | **Unique** | Gets expensive early | [Allyria §6.1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Clash Runes | Only +1 early on (live sheet), about +5 later | **+5** (Allyria: not past +6/7) | n/a | Upgrades are RNG-heavy (Allyria), and a failed upgrade destroys the rune (Bible) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Allyria §6.1.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Bible ch.2](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |

| Other | Recommendation | Source |
|---|---|---|
| Manastones | Front Damage Boost > Weapon Damage Boost ≈ Crit Damage Boost > Damage Boost > Attack | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Bible ch.5](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Arcana | God stats: Chalice Time · Parchment Life/Destiny · Compass Death/Freedom · Bell Destruction · Mirror Illusion/Wisdom (sheet). Skill lines from the sheet author's current build, all five cards Unique at level 5: Chalice Pummel, Punishment +2, Judgment +2, Fury; Parchment Judgment +2, Punishment +2; Compass Pummel +4, Shield Smite +2, Warding Strike +2; Bell Fury, Insulting Roar; Mirror Impact Hit. Korea's top 20 (a bigger card set including Scales, not on Global): Fury 12 levels, Impact Hit 8, Insulting Roar 7, Vicious 7, Judgment 6, Punishment 5, Pummel 4 (KR/TW) | [daevaos](https://daevaos.com/guides/templar-class-guide-pve), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Pet Genus | <ul><li>Special line 4: Double Chance.</li><li>Line 4 on other boards: PvE Damage Boost.</li><li>Lines 1/5: Max Attack.</li><li>**Lines 3/6/9: Critical Hit** (the sheet and daevaos also list Accuracy as a co-priority). Top-20 Global Templars sit at about 36–38% crit on skills that don't always crit (per-player median 38%; all Global Templars 24%), below the 50% cap.</li><li>Line 7: PvE Damage Tolerance.</li></ul> | [Genus audit](../docs/genus-audit.md) |
| Wings | Can't be enhanced in S1; Talisra (Season Shop) is the CDR goal. The sheet's "meta wings" (Eroded 77%, Talisra 18.5%) aren't labeled by region; the repo's archived data tags the same figures as Korea, Aug 21. Eroded on Global is UNVERIFIED | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

[NM]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM buffs]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM classPerformance]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
