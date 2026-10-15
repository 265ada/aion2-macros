# AION 2 Global (NA/EU) — Class Meta Reference

**Patch covered:**
- **Global client build 25926599.** This is the Steam public branch, updated 2026-10-14 06:40 UTC ([SteamCMD](https://api.steamcmd.net/v1/info/3393110)).
- **What's in it, newest first:**
  - **The [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374).**
    - Spiritmaster: Summon: Ancient Spirit fixed at stigma level 15 and below.
    - Sorcerer: Fire Wall and Cold Storm fixed for height differences and for being overwritten by another player's stronger Embers/Frostbite; Bittercold Wind fixed for height differences.
    - Also: Halloween event (which sells Superior Power Shards and a 10,000 Pet Soul Crystal chest), Battlefield stat adjustment, Abyss entry-time changes.
    - No other class changes.
  - **The [Oct 6 PDT / Oct 7 CEST update](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544).** Founder's Pack items, Substance Morph limits, drop rates. No class balance.
  - **The [Oct 8 PDT / Oct 9 CEST hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1).** Server stability, quest-wing flight power.
- **Version name:** NC doesn't publish one for Global; the build id is the version marker.
- **Timing of the data:** the NotMeter data used here (week of Oct 7–14) was recorded on the previous build 25800038, so it shows Spiritmaster and Sorcerer before their Oct 13 fixes.
- **Post-patch check:** NotMeter's next generation (`29087b479916fb24`, published Oct 14 14:32 UTC; week starting Oct 14 KST, so recorded on build 25926599) keeps the same class order: Chanter 114.08, Ranger 110.43, Gladiator 109.73, Sorcerer 103.69, Assassin 95.02, Templar 90.08, Spiritmaster 84.65, Cleric 66.98 (300–336 players per class) ([NM post-patch](https://notmeter.com/g/29087b479916fb24/data/notmeter-global-ranking.json)). A later generation (`fa55b4eec4719396`, Oct 14 19:39 UTC, [latest](https://notmeter.com/data/client/notmeter-ranking-latest.json)) gives the same order again: Chanter 116.12, Ranger 112.08, Gladiator 111.32, Sorcerer 102.59, Assassin 95.28, Templar 94.31, Spiritmaster 83.53, Cleric 69.03. The tier list below therefore holds after the patch.
- **Dead NotMeter links:** NotMeter keeps only its newest generation online, so the links to `7a95660ba62a7ef4` (and `29087b479916fb24`) now return 404. The numbers can be re-derived from the archived copy of that generation kept with this repo's working files (`.cache/notmeter/7a95660ba62a7ef4/`, not committed). The class files use the pre-patch week for detail; Sorcerer's file adds its post-patch numbers, because the Oct 13 patch changed Sorcerer.

**Written:** 2026-10-13; **updated for the Oct 13 patch:** 2026-10-14. **Region:** Global only. Korean and Taiwanese material appears only where the Global client shows the same skill, effect or number, tagged **[KR/TW-confirmed]**; anything else from KR/TW is labeled as KR/TW context.

**Global ≠ KR/TW.**
- **Skill balance:** the live Global client carries Korea/Taiwan's current skill balance, **including Korea's Sep 16 patch**. Global parses show Korea's Sep 16 changes are live: Templars show a second Noble Armor buff in 452 of 507 Templar fights longer than 130 s, and Chanters a second Guardian Blessing in 85 of 93 (buff applications; one cast never lasts past 120 s) (Sep 16 cut both cooldowns from 5 min to 2 min). Assassin Shadowstrike's option-2 buff lasts about 10 s (Sep 16 raised it from 5 s) ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [KR Sep 16 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6aa99cb8a279104f7d9d5c34)). The aion2.app "Global" database (client 18.09.2026) still shows the older values, so it is an older client snapshot (dated Sep 18). This guide uses the database for effect text and flags the values Sep 16 changed. Allyria's Global Ranger guide also says skill balance "carries over from the current TW patch". Korea's Sep 23 changes (Battlefield Might, Fracturing Rush direction) are UNVERIFIED on Global.
- **Buff durations scale with stigma level:** most stigma self-buffs listed as "for 10s" last 10 s at level 1, 14.5 s at 10, 17 s at 15 and 20 s at 20 (+0.5 s per level). Examples: Lunge Stance, Zikel's Blessing, Swift Contract, Illusive Clone, Vaizel's Authority, Bow of Blessing, Battlefield Banner, Element Enhancement, Power of the Storm, Prayer of Amplification, Flame Blessing. Exceptions: Spirit's Benediction stays 10 s, and buffs granted by specialty options (Savage Fang 15, Empyrean Lord's Punishment 15) stay 10 s ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)). The database text shows the level-1 value.
- **Global-only system changes:**
  - 4 stigma slots, capped at level 20;
  - about 19–21% maximum cooldown reduction;
  - Divine stats at half value;
  - no Heroic gear in Season 1;
  - Ariel board removed;
  - reworked Pet Genus;
  - Double Chance removed from titles;
  - a 50% stat crit cap.
  
  Sources: [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Kanon's Bible](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview).

---

## Classes and specs

**Classes (official):** NC's Global site lists eight: Gladiator, Templar, Assassin, Ranger, Chanter, Cleric, Sorcerer, Spiritmaster ([NC class list](https://aion2.plaync.com/en-us/about/index#classes)). There are no official subclasses. Brawler is a Korea-only class and isn't on Global.

**Specs (build paths, from Global party data):**
- A "spec" here is a **party role** that Global players actually fill.
- Each was confirmed from all 5,303 unique Global boss parses on NotMeter for the week of Oct 7–14 ([method](#method-notes)).
- Loadout swaps inside a role (PvE vs PvP vs solo; safety vs damage) are covered inside each spec file.

| Class | Spec | File | Global evidence for the spec |
|---|---|---|---|
| Gladiator | DPS | [gladiator-dps.md](gladiator-dps.md) | Default role |
| Gladiator | Tank (no Templar) | [gladiator-tank.md](gladiator-tank.md) | 36% of Global parses have no Templar. In 55% of those that have a Gladiator (908 of 1,644), the Gladiator receives the most healing. |
| Templar | Tank | [templar-tank.md](templar-tank.md) | In 64% of parses. No separate DPS Templar: two-Templar parties both run tank kits. |
| Assassin | DPS | [assassin-dps.md](assassin-dps.md) | — |
| Ranger | DPS | [ranger-dps.md](ranger-dps.md) | — |
| Sorcerer | DPS | [sorcerer-dps.md](sorcerer-dps.md) | — |
| Spiritmaster | DPS | [spiritmaster-dps.md](spiritmaster-dps.md) | — |
| Cleric | Healer | [cleric-healer.md](cleric-healer.md) | In 89% of fights (86% with exactly one). No separate DPS Cleric: in two-Cleric parties both heal (lower healer median 61%) with similar core stigmas. |
| Chanter | Support DPS | [chanter-dps.md](chanter-dps.md) | Default role |
| Chanter | Battle healer (no Cleric) | [chanter-battle-healer.md](chanter-battle-healer.md) | The Chanter is the top healer in 93% of the 565 Cleric-less parties that have one |

Every spec file has the same eight sections, in order: Overview · Max damage · Macros · Stigmas · Skills · Specializations · Tier list · Gear.

**Supporting files:**
- [sources.md](sources.md): every URL and what it was used for.
- [discrepancies.md](discrepancies.md): source conflicts and KR/TW-vs-Global differences, with the resolution.
- [unverified.md](unverified.md): what couldn't be confirmed, and what would confirm it.

---

## Overall tier list

### PvE (Global, measured)
Two independent measures, both from NotMeter's Global boss parses for the week of Oct 7–14 ([data](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)):

| Rank | Class | NotMeter class score (95% CI, grade) | Damage at equal CP vs the class average (this guide's regression) | Tier | Why |
|---|---|---|---|---|---|
| 1 | Chanter | 118.79 (111.2–126.3, B) | **+22.0%** (1st) | **S** | Top on both measures, plus the best party buffs |
| 2 | Ranger | 114.85 (109.3–120.4, B) | +0.7% (5th) | **A** | High score; top Rangers also have the highest median CP |
| 3 | Gladiator | 110.46 (106.4–114.5, A) | +5.3% (3rd) | **A** | Strong on both; can also tank |
| 4 | Sorcerer | 105.70 (101.7–109.7, A) | +9.8% (2nd) | **A** | 2nd at equal CP |
| 5 | Assassin | 96.66 (93.6–99.8, A) | −1.8% (6th) | **B** | Mid; big skill ceiling (top 10% about 83% above the CP trend line) |
| 6 | Templar | 92.92 (88.8–97.1, B) | +2.1% (4th) | **B** (as DPS) / **S** (as tank) | The only real tank. Taunt's Shrink and Fury raise the whole party's damage. |
| 7 | Spiritmaster | 82.54 (78.5–86.6, B) | −5.6% (7th) | **B−** | Global CDR caps the Ancient Spirit |
| 8 | Cleric | 69.41 (65.1–73.8, B) | −25.6% (8th) | **C** (as DPS) / **S** (as healer) | The healer; NotMeter measures damage only |

- **NotMeter score:** NotMeter's own weekly score: each player's best parse among the top 50 per boss, weighted equally across 16 content entries, with 100 = the median baseline ([rankingBasis field](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)).
- **Equal-CP column:** a class effect from regressing log(DPS) on log(CP) with boss fixed effects, over every player's best parse per boss in NotMeter's Global ranking. All ranked parses are used, not only the top 20 ([method](#method-notes), [tools/notmeter_snapshot.py](../tools/notmeter_snapshot.py)).
- **Sensitivity:** the figures depend on the method. On the top-20 set alone (independent re-check) they move a few points, for example Spiritmaster −9.0% instead of −5.6%, and Ranger and Assassin swap places. The top three (Chanter, Sorcerer, Gladiator) and the bottom two (Spiritmaster, Cleric) hold either way.
- **Tier letters:** this guide's judgment from these two measures.

### PvP (Global)
**UNVERIFIED.** No official or data-based Global PvP ranking exists yet. Launch-week opinion pieces put Assassin and Gladiator at the top for PvP ([ExitLag tier list](https://www.exitlag.com/news/aion-2-class-tier-list/), opinion; [timesaver.gg](https://timesaver.gg/blog/aion-2-tier-list-best-class-october-2026), opinion). Korean PvP rankings can't be assumed: Global has 4 stigma slots and different stats. Sirin, a Global SM guide author, writes that predicting Season 1 PvP "is impossible" ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).

### Solo / leveling (Global)
**Opinion, UNVERIFIED** (no Global leveling-speed data). These are this guide's reads from the class kits:
- **A:** Ranger (ranged, mobile, AoE), Gladiator (self-heal on hit), Chanter (heals and damage), Spiritmaster (tanky, spirits fight on their own).
- **B+:** Sorcerer (strong AoE but fragile).
- **B:** Assassin (squishy), Templar (slow kills), Cleric (slow kills).

Launch-week opinion pieces call Ranger the safe leveling pick ([ExitLag](https://www.exitlag.com/news/aion-2-class-tier-list/)).

### Easiest class for maximum damage (Global)
**Chanter.**
- It is 1st at equal CP.
- One in-game macro entry plus a held Onslaught covers the core rotation ([chanter-dps.md](chanter-dps.md)).
- Runner-up for ease: Spiritmaster. Sirin calls it a low skill floor class that "performs very well on high ping", but its Global damage is lower ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).

---

## Global systems (shared by all classes)

### Stigmas
- **Slots and cap:** 4 slots, capped at level 20. A fresh level 45 has 32 shards; the Abyss Point cap allows about 20 shards a week; resets are free ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). Global top players average about 4 stigmas each ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)).
- **Slot unlocks:** reported as character levels 22 / 27 / 32 / 37. Allyria writes that the 4th slot arrives only at 45. See [discrepancies](discrepancies.md).
- **Rarity:** stigmas have no rarity, only levels, and every effect up to your level is active ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)). Every "Settle rarity" cell for stigmas therefore says n/a.
- **Shard cost:** 75 shards per stigma to level 20 (1/2/4/8 per level for levels 1–5 / 6–10 / 11–15 / 16–20), confirmed in questlog's Global skill data ([questlog](https://questlog.gg/aion-2/en/db/skill/17410000); same as KR/TW). With that budget, top Global players this week sit at **one stigma at 20 and the rest at 5–15** ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)).

### Skills and specialties
- **Levels:** skill points take actives to 10. Levels 11–20 come from ring lines, blue Daevanion tiles and Arcana ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)). The Bible's general gear chapter also lists active-skill lines on weapon and guard, but none of the Global weapon/guard line lists (Bible ch.3, Sirin, Allyria) includes them, so skill lines on Global weapons are UNVERIFIED.
- **Effect numbers:** values quoted from the database are **level-1** values unless a level is given. Passives and stigma effects grow with level; for example, Templar's Fury is 5.5% at level 1 and about 13.5% at 17.
- **Specialties (pick 3 of 5):** options 1–3 unlock at **8** (one slot), option 4 at **12** (second slot), option 5 at **16**, and the third slot at **20**. Nothing else changes between those levels ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).
- **Option numbers:** they follow the in-game order. The guides' icon colors are 1 green, 2 blue, 3 yellow, 4 orange, 5 red.
- **Season 1:** only 5 Arcana cards and 4–5 gear lines, so few skills reach 20 ([Allyria ch.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).

### Daevanion boards
- **Points:** about 316 at 45 after Sealed Dungeons and side quests, plus 50 from the Shugo Festival shop and 50 from the Nightmare shop ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- **Global changes:**
  - Ariel (the PvE board) removed;
  - orange % tiles 2.5% → 1.5%;
  - Attack 5 → 3, Crit 10 → 5;
  - Azphel's PvP stats reduced;
  - about 200 fewer points ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- **Priority:** Orange > Blue > Green > White. Take a blue tile first when it lifts a key skill to 8 / 12 / 16 / 20. White tiles: Attack > Crit > HP. Resets cost Kinah ([Allyria ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).
- **Skip in PvE:** Multi-hit Resist and Crit Damage Tolerance oranges ([Bible ch.7](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

### Gear phases
The current Global endgame (bosses in this week's NotMeter data):
- **Vakron:** Tiere, Thamon, Vakron.
- **Transcendence / Deus 4:** Atiel, Gelcos, Nazmun.
- **Fire Temple (Kromede):** Kromede's Desire, Red Spark Ignus, Black Smoke Murute.
- **Ferocious Horn Den:** Watchdog Kwapo, Necromancer Duanka, Ferocious Horn Nuakum.
- **Arkanis 4:** Siliator of Deceit, Talisra of the Void, Ruthilis of Pain.

The **Ludra** raid (Sanctuary) isn't on Global yet; NC calls it upcoming ([Producer's Letter](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac95cd8d97eae18cc40e3d7)).

| Phase | Steps (in order) | Source |
|---|---|---|
| Leveling (1–45) | MSQ to 45. Along the way: Sealed Dungeons (Daevanion crystals, skill points), regional quests, feathers (only enough to reach Monolith level 30), strongholds (belt scrolls) and Rift runs | [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) (live, Oct 14) |
| Early endgame (to about 1,600 score) | <ol><li>At 45: Draupnir in Exploration (double-claim the first run for the pity).</li><li>Regional quests for accessory upgrades and Clash Runes. **Upgrade each Clash Rune only to +1 for now.**</li><li>Amulet to +10, then Substance Morph it to blue.</li><li>Spend Azphel (PvP board) points: they add item level.</li><li>Manastone everything once (about 1,000).</li><li>Side content and Abyss feathers (about 1,400).</li><li>Vakron in Exploration (save the pity chest), then Vakron in Conquest for Unique pieces (about 1,600).</li></ol> | [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) (live) |
| Endgame (now) | <ol><li>About 1,600: Uruguru for Unique accessories, while tapping earlier Unique pieces to +10 and running Transcendence level 1 for grey Arcana cards.</li><li>About 1,900: Transcendence level 2 for blue/green cards.</li><li>About 2,000: craft a gold Arcana card.</li><li>Then Ludra prep (below).</li></ol> Later dungeons named in the sheet's older (Oct 2) roadmap and by Allyria: Kromede (accessories, weapon), Ferocious Horn Den (armor, guard), Transcendence 3–4 (gold cards), crafted weapon / accessories. | [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) (live); older roadmap archived in [data/classes.json](../data/classes.json); [Allyria §0.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |

The sheet's author is moving this content to [daevaos.com](https://daevaos.com/guides/classes?author=Castform). On Oct 14 the sheet's Chanter, Ranger, Sorcerer and Templar tabs were replaced by links to daevaos.com; the Cleric, Spiritmaster, Gladiator and Assassin tabs, the Roadmap and Tips remain. Class-tab citations in this folder refer to the Oct 14 snapshot.

**Enhancement targets (Ludra prep):**
- weapon, guard and rings +17;
- earrings and necklace +16;
- armor and bracelets +15;
- Clash Runes about +5 ([Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview); the same sheet says to stop at +1 early on). Allyria says not past +6/7, because upgrades are RNG-heavy ([Allyria §6.1.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)), and failed rune upgrades destroy the rune ([Bible ch.2](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

Unique gear goes to +15 and then 5 Amp levels ([Bible ch.1](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

**Settle rarity:**
- **Unique, for every slot in Season 1.** There is no Heroic gear in S1 ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- Crafted gear (5 lines) is best in slot. Dungeon gear has 4 lines ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Allyria ch.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). F2P or sub-only players can stay in dungeon armor "without losing a lot" (Allyria).
- Belt and amulet: upgrade to Gold early, then stop for now ([Allyria §6.1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).
- Not on Global yet: Pendant, Brooch and Seals ([Allyria §6.1.2–6.1.5](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).

**Global gear changes:**
- PvE Damage Boost was removed from weapons, guards and accessories. Potential stats are PvP-only ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Bible ch.1](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).
- Perfect was removed from capes. Might, Precision and Combat Speed were added to necklaces.
- Wings can't be enhanced in S1. Talisra wings (Season Shop) are the cooldown-reduction goal ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- **Crit cap is 50%.** Top Global Gladiators, Rangers and Assassins already sit at it, so for them Crit stats are wasted ([Bible ch.3](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview), [genus audit](../docs/genus-audit.md)).

### Pet Genus
On Global, Double Chance rolls only on Special board line 4. On the other boards, line 4 is PvE Damage Boost. Lines 3/6/9 depend on class (Critical Hit if you're below the crit cap, Power Shard Damage Bonus at the cap). Full 45-line, per-class tables come from the Global client data in [docs/genus-audit.md](../docs/genus-audit.md) and on the [live site](https://265ada.github.io/aion2-macros/).

### Macros: allowed vs risky
- **In-game skill macro:** allowed (built in). Settings → Key Settings → General → Gameplay → Macro ([Allyria §3.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).
  - Each entry points to a hotbar slot that stacks up to 4 skills. In game the rows are numbered 0–3 from the **bottom** (row 0 sits directly above the key). This guide lists stacks row 0 first and treats row 0 as the highest priority, as the Korean setups it uses do. No cited source states the firing order outright, and it hasn't been tested on Global (UNVERIFIED).
  - **Charge skills fire uncharged:** Deadshot, Hellfire, Punishment and Bolt do about 35–45% of a Max cast. Keep them on their own keys.
- **External software or hardware macros** (Razer / G-Hub hold-to-run): **a risk.**
  - NC's Operation Policy bans "programs, devices, or equipment… enabling actions impossible for regular users" with an Integrated Account Ban ([NC Operation Policy](https://www.plaync.com/policy/operation/aion2global)).
  - NC's Oct 10 PDT notice restricted 4,996 accounts and named "use of macros, bots or other unauthorized programs" ([NC notice](https://aion2.plaync.com/en-us/board/notice/view?articleId=6acaa7506b722c561dc6aae9)). Further waves on Oct 12 PDT (10,000 accounts, [notice](https://store.steampowered.com/news/app/3393110/view/1846018067943055)) and Oct 14 (9,422, [notice](https://store.steampowered.com/news/app/3393110/view/1846651706673527)) gave the same reasons.
  - Allyria's FAQ says hold-to-run is "not bannable". That isn't an NC statement.
- **No Global patch has nerfed any class macro** as of the Oct 8 hotfix.

### Party buffs
Rules from the Global DB:

| Rule | Source |
|---|---|
| Chanter's **Undefeated Mantra** and Cleric's **Light of Protection** don't stack. The higher skill level applies; at equal level, Undefeated Mantra does. | [DB Undefeated Mantra](https://aion2.app/db/skills/18190000), [DB Light of Protection](https://aion2.app/db/skills/17410000) |
| Party members can't receive **Power of the Storm** while a Cleric's **Earth's Blessing** (from Earth Punishment) is active | [DB Power of the Storm](https://aion2.app/db/skills/18250000) |
| Chanter's **Earth's Promise** doesn't stack with Cleric's **Chain of Torment** (enemy tolerance shred) | [DB Earth's Promise](https://aion2.app/db/skills/18780000) |
| Gladiator's **Experienced Counterstrike** party buff doesn't stack with Templar's **Fury** | [DB Experienced Counterstrike](https://aion2.app/db/skills/11780000) |
| Gladiator's **Rage Burst** (Wounded) doesn't stack with Templar **Taunt**'s Shrink | [DB Rage Burst](https://aion2.app/db/skills/11390000) |
| Two Chanters' **Sprint Mantra** / **Undefeated Mantra** don't stack | [repo stigma notes](../data/stigma_db.json); Global buff uptimes agree: on third party members the two Chanters' uptimes sum to about one fight length (median 0.97–0.98) |
| Two Sorcerers' **Cold Storm** / **Fire Wall**: before Oct 13, a stronger Frostbite or Embers from another player removed yours. The Oct 13 patch fixed that, so each Sorcerer's damage over time now stays on the target. Whether the two *stack* their damage isn't stated. | [Oct 13 patch notes](https://store.steampowered.com/news/app/3393110/view/1846651706673374) |

---

## Method notes

All "Global data" numbers come from NotMeter's public Global cache, generation `7a95660ba62a7ef4`, published 2026-10-13 04:23 UTC. NotMeter labels it the week of Oct 7–14 (KST), but the retained parses are dated **Oct 11 00:31 to Oct 13 04:21 UTC**, on build 25800038. It holds 11,942 ranked parse rows and 5,303 unique boss fights. By region: EU 49%, Asia 23%, NA East 20%, NA West 6%, Latin America 2%, all on the same Global client ([latest.json](https://notmeter.com/data/client/notmeter-ranking-latest.json), [ranking file](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), [per-parse details, e.g. bucket 00](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/global-ranking-details/00.json)). The repo script that pulls them is [tools/notmeter_snapshot.py](../tools/notmeter_snapshot.py).

1. **Top-20 set.** For each class, take each player's best parse per boss, then the 20 highest-DPS parses per boss. That gives 300 parses per class over 15 bosses. Training-dummy parses are excluded.
2. **Damage share and uses per minute.** These come from each parse's per-skill damage percent and use count.
   - The "top 10%" is the top tenth of the set after adjusting for CP.
   - Some use counts exceed what a skill's cooldown allows, for example Ruinous Blow and Illusive Clone. These are probably hits or procs, so they're reported as "uses logged", not casts.
3. **Skill levels and specialty picks.** NotMeter's `rawSkillCode` minus `skillCode` gives the picked options. The level is inferred from the picks: any pick from options 1–3 means 8+, a second pick or option 4 means 12+, option 5 means 16+, and three picks means 20.
   - Stigma, passive and buff levels come from each player's own buffs (`skillLevel`), reported as medians.
4. **Stigma comparisons at equal CP.** Within the top-20 set, center log(DPS) and log(CP) per boss and fit one CP slope. For each pair of stigmas, compare the residuals of players who run A but not B against those who run B but not A.
   - Results are **averaged per player first** (one player can have up to 15 parses) and reported with a 95% range.
   - Parse-level figures are in [discrepancies.md](discrepancies.md).
   - These are **observational**. Player skill and party makeup can still confound them (for example, two-Chanter parties).
5. **Class equal-CP effect (tier table).** Over all ranked best-per-boss parses: log(DPS) = boss effect + class effect + slope × log(CP), with a common slope, fitted by alternating means ([tools/notmeter_snapshot.py](../tools/notmeter_snapshot.py)). The table shows exp(class effect) − 1, centered on the average class.
6. **Party roles.** For each unique fight, the record lists all 4–5 party members. The **tank** is the party member who received the most healing from others. The **healer** is whoever gave the most healing to others.
7. **Class scores.** NotMeter's `classPerformance` score and confidence interval are used as published.

### Global DB
Skill and stigma effects, cooldowns and specialty text come from [aion2.app](https://aion2.app/db/skills?class=Gladiator) (game client dated 18.09.2026, "Global" version). Korean level-25 effects are KR-only; Global caps stigmas at 20.

---

## Top 5 Global meta takeaways (Oct 13, 2026)

1. **Chanter is the best class on Global right now**, on both measures (NotMeter 118.79; +22% at equal CP), and the easiest to max: one macro entry. Get Dark Crush to 16 before anything else.
2. **The shard economy decides stigma levels.** Top Global players run one stigma at 20 and the rest at 5–15. Korean "everything at 20/25" plans don't apply. Prioritize each class's single key stigma (listed in each file).
3. **Global runs Korea/Taiwan's current skill balance (Sep 16 included) with Global-only systems on top.** Korean skill and rotation advice mostly transfers, including post-Sep-16 guides. Korean *system* advice (stigma slots and levels, CDR, Divine stats, Genus, gear lines) does not.
4. **The 50% crit cap and Global's low CDR (about 19–21%) reshape stats.**
   - Gladiator, Ranger and Assassin should stop adding crit.
   - Sorcerer and Spiritmaster lose the most from low CDR: Spiritmaster drops to 7th.
5. **Each party role has one class on Global.**
   - **Tank:** Templar (64% of parses). Gladiators tank the rest without changing their build.
   - **Healer:** Cleric (86%). Chanters cover the remainder with Recuperation.
   - **Not separate specs on Global:** "DPS Templar" and "DPS Cleric".

[NM]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
