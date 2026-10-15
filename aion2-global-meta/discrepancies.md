# Discrepancies and KR/TW-vs-Global differences

**Patch:** Global build 25926599 (Oct 6 PDT patch + Oct 8 hotfix). **Written:** 2026-10-13.

Every conflict between sources, and every place where Korean/Taiwanese material differs from Global, is listed with the resolution used and why. Pass-2 verification fixes are logged at the end (section "Pass 2 corrections").

## General / all classes

- **Patch version label.** NC publishes no version number for Global patches. → The Steam build id 25800038 ([SteamCMD](https://api.steamcmd.net/v1/info/3393110)) and the notice dates are used as the patch marker. **Superseded in Pass 2:** the current build is 25926599 (Oct 13 PDT / Oct 14 CEST patch).
- **What the Oct 6 patch contained.** aion2hub's English summary of the Global Oct 7 update lists extra items: Sorcerer Fire Wall / Cold Storm height fixes, an Abyss rematch, refining-stone odds, cheaper Auto-Loot Tickets, and presets 3 → 5 ([aion2hub](https://aion2hub.com/updates/aion-2-global-update-2026-10-05)). NC's official patch notes ([Steam](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544), [NC site](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac6a4c0fa34c1011d627a96)) don't list them. → Not applied (likely KR/TW items).
- **Oct 8 maintenance status.** Mein-MMO's live ticker says the Oct 8 maintenance was "postponed" ([Mein-MMO](https://mein-mmo.de/en/aion-2-server-down-problems-and-maintenance-on-october-8-2026-in-the-live-ticker,1591220/)). NC marks it "Completed" ([NC notice](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1)). → NC's notice is used.
- **Global balance date vs KR/TW.**
  - Allyria (Global Ranger guide) says skill balance "carries over from the current TW patch".
  - The Global client DB ([aion2.app](https://aion2.app/db/skills/12230000), client 18.09.2026) still shows pre-Sep 16 KR values: Noble Armor and Guardian Blessing 300 s, Fire Mark 20%. Questlog's Global skill text for Fire Mark ("Inflicts Fire Mark for 5s on landing a Fire attack", no chance) supports Korea's Sep 16 change to 100%, so the DB is out of date there; the application rate observed in logs stays UNVERIFIED.
  - It does show the Aug 26 rework: Judgment and Dark Crush open after any shield or ranged skill; Warding Strike 25 s; Spinning Strike 15 s.
  - → Global is treated as KR balance between Aug 26 and Sep 16. KR/TW Sep 16 and Sep 23 changes are not applied. **Superseded in Pass 2:** Global combat logs show Korea's **Sep 16 patch is live** (Noble Armor recast in 452/507 fights over 130 s; Guardian Blessing 85/93; Shadowstrike option 2 lasts 10 s; Sorcerer Pyroclasm gives +5% Fire for 10 s in 275/282 option-4 parses). The aion2.app "Global" DB is an older client snapshot (Sep 18). From Aug 26, Warding Strike's 25 s is **not** live (DB, questlog and use rates fit 30 s). Sep 23 changes stay UNVERIFIED.
- **Stigma slot count and cap.**
  - Kanon's Bible: "you can equip up to 6 (there's a chance this could be lower for global)".
  - Sirin: 4 slots, capped at 20.
  - NotMeter: top Global players average about 4 stigmas.
  - → 4 slots, cap 20.
- **Stigma slot unlock levels.**
  - The repo / Global sheet notes say character levels 22 / 27 / 32 / 37.
  - ExitLag: "four slots unlocking at level 22" ([ExitLag](https://www.exitlag.com/news/aion-2-templar-build/)).
  - Allyria: "4 Slots will only be available after reaching 45".
  - → Recorded as unresolved (see unverified.md). It doesn't change any endgame recommendation.
- **Stigma shard cost (1/2/4/8 per level, 75 to 20).** KR/TW data; no Global source confirms it. → Used for ordering only, marked UNVERIFIED. **Superseded in Pass 2:** confirmed in questlog's Global skill data ([questlog](https://questlog.gg/aion-2/en/db/skill/17410000)).
- **Cape stat lines.** Kanon's Bible ("for Global") lists Perfect Chance on Cloak. Sirin (Oct 12) says Perfect was removed from capes on Global, and Allyria's Global cape list has no Perfect. → Treated as removed (two newer Global sources).
- **Extendable weapon stat lines.** Kanon's Bible: 4 lines (Kromede, Ludra). Sirin: an extendable weapon drops to 3 lines. → Recorded; UNVERIFIED which is right on Global.
- **Kromede colossus.** The sheet and Allyria list Zikel/Kromede for S1. Sirin: the Kromede colossus was removed on Global. → Flagged in each Gear tab.
- **Pet Genus line-4 picks.** The Bible's Global section and the sheet put Crit Damage Boost on Cogni, Multi-hit/Perfect on Natura, and so on. This repo's audit of the Global client tables (two independent datamines, 45/45 identical) finds PvE Damage Boost out-rolls and out-values those. → The audit is followed ([docs/genus-audit.md](../docs/genus-audit.md)).
- **External macro software.** Allyria's FAQ says hold-to-run mouse macros are "not bannable". NC's Operation Policy bans programs or devices "enabling actions impossible for regular users", and the Oct 10 ban wave named "use of macros". → Treated as a risk; the in-game macro is the recommended setup. **Superseded in Pass 2:** ban waves on Oct 12 (10,000 accounts) and Oct 14 (9,422) used the same "macros, bots or other unauthorized programs" wording.
- **NotMeter use counts vs cooldowns.** Some logged use counts exceed what a cooldown allows (Gladiator Ruinous Blow 4.4/min on a 45 s cooldown; Assassin Illusive Clone 2.9/min on 90 s). → These are reported as "uses logged", probably hits or procs, not casts. **Superseded in Pass 2:** useCount and hitCount are separate fields, so these aren't hit counts. Assassin Illusive Clone counts are real casts (short fights inflate per-minute rates); Gladiator Rage Burst / Ruinous Blow are reported as "uses logged".


## Gladiator
- Global top players' 4th stigma: NotMeter Global (Oct 13) Focused Block 65% at Lv 5, Wave Armor 15%. The repo/site "Party DPS" Global build used Wave Armor 15 as the 4th (sheet order). → Went with Focused Block 5 (Global data); Wave Armor listed as the damage alternative behind a Templar. Sources: NM, Sheet.
- Rage Burst level: the site's Global build said 20; NotMeter Global median buff level 7 (most at 5). → Recommend 5 first, 20 after Lunge 20 / Zikel 15.
- Zikel's Blessing: site Global build 20; Global median 15; DB shows 20 only adds status chance. → 15.
- Ruinous Blow specialties: Global top 3+4 (32%) vs sheet/KR 1+4+5. → Both listed; 1+4+5 at 20, 1+4 or 3+4 at 12.
- Keen Strike: Global top 1+4 (39%) vs sheet 2+4. → 1+4 recommended (Global), 2+4 noted.
- Cloak Perfect Chance: Bible (Oct 4, "for Global") lists Perfect on Cloak; Sirin (Oct 12) says Perfect was removed from capes on Global; Allyria's Global cape list has no Perfect. → Treat as removed (2 newer sources).
- KR/TW Sep 16 "Leaping Slam / Ruinous Blow unusable while bound" and Sep 23 "Fracturing Rush follows key direction": KR/TW-only; Global client (18.09) predates; not applied. **Superseded in Pass 2:** with Sep 16 live, the bound restriction is likely live (UNVERIFIED by a Global test).
- NotMeter use counts for Ruinous Blow (3.0–4.4/min) exceed its 45 s cooldown: counts are likely hits, not casts. Cadence numbers are treated as "uses logged". **Superseded in Pass 2:** see the general entry; Ruinous Blow's target is now 16 (top Global median 16, 69% at 16+).
- Spec list: the site/KR data had a Gladiator "Battle tank (no Templar)" build with Armor of Balance/Tenaciousness. Global party analysis (NotMeter, 5,303 parses): Gladiators tank 55% of Templar-less parties but keep the DPS stigmas (Armor of Balance <2%, Tenaciousness ≤2%). → Tank spec kept as a role with the same loadout; KR battle-tank set marked "not used on Global".
- Spec list: KR "Templar natural-block DPS" and "DPS Cleric" not found on Global: in 85 two-Templar parties both run tank stigmas and receive similar healing; in 144 two-Cleric parties both run the same stigmas and both heal (median heal ratio ~0.6). → No separate Templar DPS or Cleric DPS spec on Global. **Superseded in Pass 2:** two-Templar parties: 35/85 had Taunt on both, 13/85 had one Templar with neither Taunt nor Noble Armor; two-Cleric parties: identical stigma sets in only 19/144 (both had Earth Punishment in 111), lower healer median 61%. The conclusion (no separate Global spec) stands.

## Templar
- KR/TW Sep 16 (Pummel/Punishing Strike/Judgment cancel delay up; Warding/Annihilate/Punishment +10%, Shield Smite +20%; Noble Armor 5→2 min; Taunt threat scales) is NOT in the Global client (aion2.app Global DB still shows Noble Armor 300 s). The site's Templar notes said "the Pummel→Judgment cancel is dead since Sep 16" — true for KR/TW, not for Global. → Global sheet layout with Pummel kept; KR post-Sep-16 advice flagged. **Superseded in Pass 2:** Sep 16 is live (Noble Armor 2-min recasts); the cancel delay, damage changes and Taunt threat are likely live, UNVERIFIED individually.
- Aug 26 rework (Judgment after any shield attack; Warding Strike 25 s) IS in the Global DB → KR Aug 26-based macro lines are usable [KR/TW-confirmed]. **Superseded in Pass 2:** Judgment-after-shield-attack is live; Warding Strike is 30 s on Global (DB, questlog, use rates), not 25 s.
- Noble Armor on Global: 300 s duration and 300 s cooldown → effectively permanent; KR 2-min note doesn't apply. **Superseded in Pass 2:** Noble Armor lasts 120 s and is recast about every 2 min on Global (logs).
- Pummel options 4/5: KR Sep 16 reworked them; Global DB shows the old text (5 = Punishing Strike 1 extra time). → Global text used. **Superseded in Pass 2:** with Sep 16 live, the reworked options are probably live (UNVERIFIED; logs can't separate the two texts).
- Stigma levels: site Global build "Battlefield Banner 20, Taunt 20, Noble Armor 20, Doom Shield 15" vs Global medians Banner 20, Noble Armor 15, Doom Shield 15. → Noble Armor 15 (20 later).
- Punishment specialties: sheet 3+4+5, KR optimizer 2+3+4, Global top 2+3 (42%) / 3+5 (28%). → 2+3 at 12, 3+5 at 16, 2+3+5 at 20 (Global + KR NotMeter 20 "35").
- Vicious Strike: Global top 4+5 (50%) vs sheet 3+4+5 at 20. → 4+5 at 16, 3+4+5 at 20.

## Assassin
- Global sheet Assassin armor rows list Spirit Strike / Mental Focus (Spiritmaster passives) and Wind's Promise (Chanter) — copy-paste error in the sheet. → Replaced with Assassin passives from the sheet's own accessory row.
- KR/TW Sep 16 (longer cancel delay on Savage Roar, Savage Smash, Heart Gore; +10% PvE on Insignia Explosion and slices) not on Global. KR Sep 18/30 macro tests were post-Sep-16. → Ambush-in-row-1 line kept as recommended, with the gain marked UNVERIFIED on Global. **Superseded in Pass 2:** Sep 16 is live (Shadowstrike 10 s). Ambush users trail at equal CP (per player −7%), so Macro A no longer uses Ambush; the Korean Sep 30 Ambush line is Macro B.
- Heart Gore specialties: sheet 2+4+5, KR top-20 1+4+5, Global top 4+5 (55%) / 3+4+5 (15%). → 4+5 at 16; third pick contested (2 per sheet).
- Savage Roar: sheet 2+3 vs Global 2+4 (68%). → 2+4 (Global; plans data showed 2+4 ahead).
- Ambush option 5: Korea's Sep 30 guide says don't take it; Korea's NotMeter top 20 run 4+5 at 16. → 1+2 (Global + sheet).
- Bracelet Death: Bible suggests Death for Assassin (pre-cap); Global crit cap 50% and top Global Assassins at cap. → Skip Death on Global.
- Triniel's Dagger: site Global build 10 (Korean guides) — Global usage 92% (level not logged). → 10.

## Ranger
- Allyria (Global guide, Oct 11) says Ranger skill balance "carries over from the current TW patch"; the Global client DB shows pre-Sep-16 KR values (e.g. Noble Armor 300 s). KR/TW Sep 16 "every Ranger attack has an element" is UNVERIFIED on Global. → Treated as not confirmed; no Ranger damage-skill text differs between the Global DB and the KR tooltips used. **Superseded in Pass 2:** Sep 16 is live on Global (logs); Ranger elements are likely live (NotMeter has no element field).
- Stigma slot timing: Allyria "4 slots only available after reaching 45"; repo/other Global guide note "slots open at 22/27/32/37"; ExitLag "four slots unlocking at level 22". → Recorded both; UNVERIFIED.
- Pet Genus lines 3/6/9: Allyria recommends Accuracy/Crit balanced; this repo's audit (Global client tables + NotMeter crit rates) recommends Power Shard Damage Bonus once crit-capped (top Global Rangers 51% crit on non-guaranteed skills). → Power Shard after Accuracy is covered; the value per point of Power Shard Damage Bonus is still unpublished (audit marks it UNVERIFIED).
- Deadshot at 16: Allyria order 2 > 3 > 5 implies 2+3 until 20; top Global Rangers run 2+5 (38%) more than 2+3 (24%). → Both listed.
- Kromede colossus: Allyria lists Zikel/Kromede for S1; Sirin says the Kromede colossus was removed on Global. → Flagged.
- Weapon line order: sheet WDB > CS > Might > Precision > DB...; Allyria WDB > CS > Might > DB > Multi > Precision. → Allyria (Global, newer, Ranger-specific).

## Sorcerer
- The Global sheet's Sorcerer page follows Est's guide, but Est states the guide is for TW/KR and may not work on Global. → Est used as [KR/TW] only where the Global DB shows the same skill text; Global-specific facts from Sirin/DB.
- Fire Mark: Global DB 20% proc; KR/TW Sep 16 100% and Blaze no longer consumes it. → Global needs Flame Arrow options 4/5 for Blaze uptime. **Superseded in Pass 2:** Flame Arrow option 4 is the Sep 16 version on Global (+5% Fire damage for 10 s, logs); Questlog's Global skill text for Fire Mark ("Inflicts Fire Mark for 5s on landing a Fire attack", no chance) supports Korea's Sep 16 100% change (the 20% that remains in that text is the extra-damage tick on a marked target), while the aion2.app DB (client 18.09.2026) still says 20%. The application rate observed in logs stays UNVERIFIED.
- CDR: Est's minimum 25.6% / ideal 37% (KR/TW) vs Global max ~19–21% (Sirin). → Est's own Global note (weave Ice Chain) kept, but top Global parses mostly skip Ice Chain (2/3 of top-10% don't cast it).
- Hellfire specialties: Est 5 > 3 > 1 (mobile), KR top-20 1+4+5, Global most common 1+5 (36%). → 1+5 at 16; third pick contested.
- Bittercold Wind: Est 1 > 2 > 4, Global 1+4 (61%). → 1+4 (Global) noted with Est alternative.
- Stigma levels: Global top players show Element Enhancement 20 with Fire Wall/Cold Storm logged at 5 — consistent with the Global shard budget (32 at 45 + ~20/week). Site's Global build had all four at 15–20. → "5 now → 20" targets. **Superseded in Pass 2:** logged medians are Fire Wall 11, Delayed Explosion 10, Cold Storm 5, EE 20 → Fire Wall "10–15 now → 20".
- aion2hub's Oct 7 Global summary lists "Sorcerer Fire Wall / Cold Storm height fixes" — not present in NC's official Oct 6 patch notes (Steam/official site). → Not applied; likely a KR/TW item. **Superseded in Pass 2:** NC's Oct 13 PDT notes contain these fixes officially (build 25926599).

## Cross-class: Global CP-adjusted stigma comparisons (NotMeter Oct 13, top 20 per boss; observational)
- Spiritmaster Flame Blessing (n=262) vs Jointstrike: Destructive Attack (n=32): −10.6% (±7.5%) → supports Sirin's Global guide (Destruction > Flame Blessing) against the 87% majority. **Superseded in Pass 2:** per-parse figures overstated certainty. Per player (README method): Destructive Attack vs Flame Blessing +4% (−2..+11).
- Gladiator Focused Block vs Wave Armor: −6.1% (±7.3%), n.s.; vs Lifestealing Blade −0.4% (±6.2%). **Superseded in Pass 2:** per player: Wave Armor vs Focused Block +2.6..+4% (−8..+15), n.s.; Lifestealing Blade vs Focused Block −1.5%.
- Assassin Savage Fang vs Evasion Stance: +6.1% (±7.2%), n.s. **Superseded in Pass 2:** per player: −5% (−11..+1), n.s.
- Templar Battlefield Banner vs Shield of Protection: +5.0% (±4.8%); Doom Shield vs SoP +3.9% (±5.0%); Taunt vs SoP +4.2% (±4.7%). **Superseded in Pass 2:** per player: Banner vs SoP +2..+3% (±5), n.s.
- Ranger Griffon Arrow vs Explosive Arrow: +1.7% (±3.9%), n.s. **Superseded in Pass 2:** per player: +0.1% (−6..+6).
- Cleric Noble Aura vs Light of Protection: +20.8% (±6.2%) on the Cleric's OWN damage (LoP's value is party-wide, not captured). **Superseded in Pass 2:** per player +12% (+4..+20), but confounded by Chanter presence (Noble Aura parses mostly with a Mantra Chanter); controlling for it +3% (−5..+11), n.s.
- Chanter Sprint Mantra vs Guardian Blessing: −17.1% (±7.9%) on the Chanter's own damage; Power of the Storm vs Guardian Blessing −0.3% (±6.8%). **Superseded in Pass 2:** per player: Guardian Blessing vs Sprint Mantra +8% (−1..+17), n.s.

## Spiritmaster
- 4th stigma: site/sheet/KR Flame Blessing (87% of top Global SMs) vs Sirin (Global guide) "Destruction performs a bit better". Global CP-adjusted: Destruction users +10.6% (±7.5%). → Destruction recommended; Flame Blessing as the common alternative. **Superseded in Pass 2:** per player, Destructive Attack vs Flame Blessing is +4% (−2..+11), not significant; both are listed.
- Ancient Spirit stigma level: site Global build 20 with no warning; Sirin reports a Global bug below Lv 15 (no skill every 7 attacks, no Elemental Fusion). → 15 ASAP. **Superseded in Pass 2:** NC's Oct 13 PDT patch fixes Ancient Spirit at level 15 or below; no post-patch parses confirm it yet.
- Corrode: KR advice "level Corrode first"; Sirin "5 then straight to 20 (all or nothing)". → Sirin.
- Wind Spirit: sheet calls it "kinda useless — mainly for mobbing"; Sirin (Oct 6) added it to the rotation. → Sirin (newer, Global).
- Weapon/guard lines: sheet "Weapon DB > Combat Speed > Might > Precision > DB..."; Sirin (Oct 12) "Combat Speed > Weapon DB > DB > Might > Precision > Multi-hit > Attack". → Sirin.
- Extendable weapons: Sirin says 3 lines; Kanon's Bible says 4 lines (Khromede, Ludra). → Recorded; UNVERIFIED which applies on Global.
- Sirin's specialty table rows are icons; row→skill mapping inferred by matching color orders to Global NotMeter picks (every row matched a distinct skill).

## Cleric
- Spec list: KR "DPS Cleric" not found on Global (144 two-Cleric parties: same stigmas, both heal). The sheet's "personal damage" set = a loadout of the healer. **Superseded in Pass 2:** the sheet has no "personal damage" set; two-Cleric parties share core stigmas (identical in 19/144), lower healer median 61%.
- Light of Protection: site Global "Party healer" build kept it (15); Global top-20 use 43%; CP-adjusted personal damage −20.8% (±6.2%) vs Noble Aura, but the meter can't see its party-wide +10.5%. → Keep without a Chanter; swap with a Chanter (DB: Mantra wins ties). **Superseded in Pass 2:** see the cross-class entry: +12% per player, +3% after controlling for Chanter presence; LoP is 17.5% at level 15 (10.5% is level 1).
- Earth's Retribution specialties: sheet 2+5 vs Global 2+4 (63%) and KR 2+3+4. → 2+4. **Superseded in Pass 2:** the sheet says 2/4 (matches Global 2+4); "sheet 2+5" was a misreading.
- Bolt/Divine Aura levels: sheet 20; Global 27%/25% at 16+. → 16/12 now, 20 later.
- Cleric attack-speed cap 94.4% (KR testing) — UNVERIFIED on Global.

## Chanter
- KR/TW Sep 16 (Guardian Blessing 5→2 min) and Sep 23 (Undefeated Mantra / Power of the Storm disabled under Battlefield Might) are NOT on Global (Global DB still shows Guardian Blessing 300 s). The site's Chanter opener ("stack Guardian Blessing on Power of the Storm, both 2 min since Sep 16") is KR-only. → Guardian Blessing treated as a 300 s buff on Global. **Superseded in Pass 2:** Guardian Blessing is recast in 85/93 long fights (2-min cooldown live). Sep 23 stays UNVERIFIED.
- Power of the Storm vs a Cleric: Global DB: party members can't receive Storm while a Cleric's Earth's Blessing is active. The repo's stigma note said "Doesn't stack with Cleric's Earth's Blessing (Storm applies)" — conflicting wording; the Global DB text is followed.
- Guardian Blessing vs Sprint Mantra: Global CP-adjusted, Guardian Blessing users +17.1% (±7.9%) personal damage; likely confounded (Sprint Mantra doesn't stack between two Chanters, so the 2nd Chanter in 407 two-Chanter parties tends to run Guardian Blessing). → Sprint Mantra kept (party value, 83% usage); Guardian Blessing noted as the damage swap. **Superseded in Pass 2:** per player +8% (−1..+17), n.s.
- Battle-healer build: site/KR "Healing Touch 20 + Impeding Authority 15" replacing two buffs; Global battle healers keep the buffer four (Healing Touch 14%, Impeding 9%) and heal with Recuperation. → Global practice as the default; KR picks as the hard-content swap.
- Spinning Strike: the sheet lists 1+2+3; Global 1+3 (50%) and Korea 1+3+5. → 1+3 → 1+3+5 (2 only for healing).

## Pass 2 corrections
Pass 2 re-checked every class file against Global data. Round 1 was an independent full check of all eight classes. Round 2 was a full re-check for Cleric and Templar and a light one for the other six, by request: the claims changed in round 1 plus 10 spot checks, fixing as it went. A third round was to be run only where round 2 found a high-severity error; only Templar's sheet-move finding qualified, and it was resolved by documenting the Oct 14 snapshot and the author's daevaos build. Counts are "claims checked / changed" as stated in each class's log (round 1 counts are approximate).

### Cross-class
- Korea's Sep 16 patch is live on Global: Noble Armor recast in 452/507 Templar fights over 130 s, Guardian Blessing in 85/93, Shadowstrike option 2 lasts 10 s, Pyroclasm +5% Fire in 275/282 option-4 parses. The aion2.app DB is an older client snapshot.
- Stigma buff durations scale with level (10 s at level 1 up to 20 s at 20; Power of the Storm is 10 / 12 / 14.5 / 17 / 20 s at levels 1 / 5 / 10 / 15 / 20 per questlog). Spirit's Benediction and option-granted buffs are exceptions.
- Stigma comparisons at equal CP are averaged per player (one player can supply up to 15 parses). No comparison stays significant: Cleric's Noble Aura +12% fell to +3% (−5..+11) after controlling for Chanter presence.
- NotMeter keeps only its newest generation online. Links to generations 7a95660ba62a7ef4 and 29087b479916fb24 now return 404; the numbers come from a local archive kept with the working files (not committed).
- On Oct 14 the sheet's Chanter, Ranger, Sorcerer and Templar tabs were replaced by links to daevaos.com. Citations to those tabs refer to the Oct 14 snapshot, and the author's daevaos builds are noted next to them.
- Bracelet slot 2 is blue / Epic in Season 1 (Sirin, Allyria); all Bracelet rows and the settle-rarity rule were updated.
- Stigma shard cost (1/2/4/8 per level, 75 to level 20) is confirmed in questlog's Global skill data.
- Newer NotMeter generations (29087b479916fb24, fa55b4eec4719396) keep the same class order as the one used for the class files.

### Spiritmaster
Round 1: ~235 claims checked, ~30 changed. Round 2 (light): 95 checked, 9 changed.
- Macro A rows were a KR/TW screenshot (Flame Blessing 25 / Corrode 23); replaced with SIRIN's own Option 1 rows, plus the 3-spirit version.
- Ancient Spirit level-15 bug was fixed on Oct 13. NC's notes say "Level 15 or below" (SIRIN: below 15); no post-patch parses exist to confirm it.
- Destructive Attack vs Flame Blessing recomputed per player: +4% (−2..+11), weak support; the pick rests on SIRIN's testing.
- Elemental Fusion / Dimensional Control pick shares recomputed on readable logs only (EF 3+5 46%, DC 2+3 95%); Siphon use 11% → 1%.
- Pet Genus: SIRIN's per-board line-4 lists restored next to the genus audit's ranking, with the conflict stated.
- Compass of Magic row follows SIRIN's Oct 14 fix (Combustion, Rapid Scattershot, Water Spirit, Wind Spirit).

### Assassin
Round 1: ~200 claims checked, ~27 changed. Round 2 (light): 70 checked, 14 changed.
- Macro A no longer puts Ambush in row 1: Ambush users trail at equal CP (per player −7.1% ±7.3%; 4 of the 30 top-10% parses). The recommended line is Insignia Explosion / Heart Gore / Savage Roar; Korea's Sep 30 Ambush line is the alternative.
- Buff durations by level (Clone / Swift 10–20 s); Shadowstrike option 2 is 10 s live, while the aion2.app DB says 5 s.
- Triniel's Dagger: the Korean Sep 30 post says the cut no longer reaches Savage Fang (not "only shortens running cooldowns"); the level-20 effect is enemy-side per questlog.
- Storm Rampage usage bases fixed: 69% of players use it, 56% of those at 16+.
- PvP table and shard order relabeled as this guide's picks; the Aug 29 Korean post wording corrected.
- Sheet copy errors noted (Savage Roar 16; cape row Wind's Promise).

### Gladiator
Round 1: ~260 claims checked, ~29 changed. Round 2 (light): 82 checked, 18 changed.
- Ruinous Blow target is 16, not 12 (top Global median 16, 69% at 16+), then 20.
- Added Tenyon's Global Gladiator guide; its stigma and passive order is shown next to the sheet's and Korea's.
- Tank file re-sourced: tanking count 908 of 1,644 (55%); the Inven 22575 set is Korea's no-Templar tank set, not a "battle tank" post; Tenaciousness equipped by 95% of Korea's top 20.
- Mis-cited sources fixed (Inven early guide, PvP four relabeled as this guide's pick, Wave Armor is the sheet's 2nd alternate).
- Usage bases fixed; Lifestealing Blade 4.3% of damage when slotted, equal-CP vs Focused Block −1.5% (sign flips under another grouping).
- Weapon and guard skill lines marked UNVERIFIED on Global; cloak line order and sheet lines corrected.

### Templar
Round 1: ~205 claims checked, 33 flagged. Round 2 (full): ~190 checked, 22 flagged.
- Noble Armor lasts 2 min on Global. Warding Strike stays 30 s (Korea's Aug 26 25 s cut isn't live).
- Macro A copied from the sheet's real layout; Macro B depends on an external mouse macro (ban risk).
- Level-1 values replaced by values at the target level (Fury 13.5% at 17, Block Pain 25% at 15, Noble Armor 11% at 15, Nezekan 55% at 15).
- Pummel options 4/5: questlog's Global text is the Sep 16 version and the logs agree, so they are Global-confirmed.
- The sheet's Templar tab moved to daevaos.com on Oct 14; the author's daevaos build is noted next to the snapshot.
- Banner vs Shield of Protection per player +2..+3%, not significant; PvP table re-sourced to Inven 7621.

### Ranger
Round 1: ~250 claims checked, 27 flagged. Round 2 (light): 60 checked, 5 changed.
- Macro A rebuilt from the sheet's images (icons pixel-matched); Tempest Shot sits under Drill Dart, not in its own entry.
- Macro B: the "Inven Sep 6" link was the Aug 30 post, now shown with its real layout and tagged as needing a mouse macro; its Deadshot "24–28" is hits in a one-minute dummy run, about 12–14 casts.
- Deadshot uncharged share is about one third (599 vs 1,798); "x% at 16+" became "picked option 5 (so at least 16)".
- Equal-CP +0.5..+0.7%, 5th–6th, not significant; PvP four and shard order relabeled as this guide's picks.
- Mother Nature's Breath is +10% PvP tolerance at 20 (20% total), not +20%; Focused Eye KR level 35–36.

### Sorcerer
Round 1: ~160 claims checked, 26 flagged. Round 2 (light): 120 checked, 8 changed.
- HIGH: Flame Arrow option 4 was described with its pre-Sep-16 text; the Sep 16 version (Pyroclasm +5% Fire for 10 s) is live (275/282 option-4 parses, none without).
- Fire Mark: questlog's Global skill text supports Korea's 100% change; the application rate in logs stays UNVERIFIED (see the Fire Mark entries above).
- Post-patch NotMeter generation added; same class order for all 8 classes.
- Stigma levels from logs (Fire Wall median 11, Delayed Explosion 10, Cold Storm 5, Element Enhancement 20); "% at 16+" are lower bounds from option picks.
- Crit on fire skills 42–44% (was 32%); Hellfire uncharged vs Max replaced with the DB 1:3 spread; Wish of Concentration 18 s at level 17.
- daevaos build (Castform, Oct 13) added: macro layout, shard order, skill plan, Arcana skill lines.

### Cleric
Round 1: ~210 claims checked, ~42 flagged. Round 2 (full): ~225 checked, ~35 flagged, none high.
- HIGH: Macro A entry 2 was misread; the sheet runs Divine Aura / Light of Regeneration / Judgment Thunder at 10 ms.
- HIGH: the main loadout is what top Global Clerics run, not "the sheet's pick"; the sheet's real priority is stated. Three quotes attributed to the sheet were not in it and were removed.
- Noble Aura vs Light of Protection: +12% per player was confounded by Chanter presence; controlled, +3% (−5..+11), not significant.
- Prayer of Amplification is self-only (0 of 11,573 other members); Light of Protection 10.5% is level 1 (17.5% at 15, 20% at 20).
- Uncharged Bolt is about one third of full damage (DB + logs); Earth's Retribution 2/4 in the sheet matches Global.
- Round 2: dead NotMeter links explained with the local archive; "Difficulty: Medium" is this guide's call; Korea's Oct 14 Cleric changes added as a watch note.

### Chanter
Round 1: ~150 claims checked, 18 findings (about 30 claims). Round 2 (light): 66 checked, 19 changed.
- HIGH: the Aug 26 rework (Spinning Strike 15 s, Impactful Crush 10 s) is not live; Korea's Sep 2 patch reverted them to 30 s and 15 s.
- Macro A delay 13 ms → 10 ms; two "sheet" claims (Marchutan's Wrath extend, Onslaught 2+4+5) were not in the sheet and were relabeled.
- Level-1 headline values replaced by level-20 values (Undefeated 20%, Earth's Promise −13%, Sprint move speed 20%).
- Guardian Blessing vs Sprint +9% (−1..+21), not significant; Sprint / Undefeated non-stacking backed by Global buff uptimes.
- Round 2: Power of the Storm durations from questlog; sheet, Inven 116 and daevaos picks added next to Global for Rushing Smash, Spinning Strike, Wave Blow, Onslaught and Recuperation; Arcana skill lines per card.
