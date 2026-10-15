# Cleric (治癒星) — Healer spec · AION 2 Global

**Patch covered:** Global client build **25926599** (Steam public branch, updated 2026-10-14 06:40 UTC). That is the [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374) on top of the [Oct 6 PDT patch](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544) and the [Oct 8 PDT hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1). None of the three changed a Cleric skill. Build id: [SteamCMD](https://api.steamcmd.net/v1/info/3393110). NotMeter data (week of Oct 7–14) was recorded on the previous build 25800038. **Written:** 2026-10-13, **updated for the Oct 13 patch:** 2026-10-14.

**Tags:** [Global] · [KR/TW-confirmed] = Korean or Taiwanese source checked against the Global client · UNVERIFIED.

**Main data sources:**
- **NM:** [NotMeter Global ranking](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), week of Oct 7–14. (NotMeter has since retired this generation, so the link returns 404; see the [README](README.md).) Top 20 Cleric parses on each of 15 bosses: 300 parses from 109 players, median CP 144,378, median DPS 44,111. NotMeter ranks **damage only**; there's no Global healing ranking, but each parse logs the healing every member received, which the party checks below use.
- **DB:** [aion2.app Global client DB](https://aion2.app/db/skills?class=Cleric), client dated 18.09.2026.
- **Sheet:** [Global class sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview). Its Cleric page credits twitch.tv/youmadsin.

**Why there is one Cleric spec on Global.** Korea talks about a damage Cleric, but no separate Global build was found. In the 144 Global parties with two Clerics, both healed and ran similar core stigmas (both had Earth Punishment in 111; identical detected sets in only 19): the lower healer still did a median 61% of the other's healing ([NM]; method in [README](README.md#method-notes)).

**Watch (Korea only, not on Global):** Korea's Oct 14 update changed Cleric: attack skills gain elements (Lightning Strike Scattershot Wind; Noble Aura and Empyrean Lord's Grace Earth), level-25 stigma options, an Assault Mark change and lower PvP damage (questlog's KR/TW records; [aion2hub summary](https://aion2hub.com/updates/aion-2-update-2026-10-14), secondary). Global's Oct 13 notes have none of it.

---

## 1. Overview

| Item | Recommendation / finding | Why | Source |
|---|---|---|---|
| Role | Healer (mace) with real damage | NC: "preserves life with the gentle touch of light" | [NC class list](https://aion2.plaync.com/en-us/about/index#classes) |
| Playstyle | <ul><li>**Damage:** Condemnation is 35.6%. It only hits targets with Chain of Torment, always crits on targets with Earth Punishment (stigma 5), and resets on crit (option 4).</li><li>**Judgment Thunder** + its Divine Punishment chain: 23.4%.</li><li>**Healing** is manual: Healing Light and Radiant Recovery; Light of Regeneration sits on the macro early (sheet) and goes by hand later.</li></ul> | | [NM], [DB Condemnation](https://aion2.app/db/skills/17350000), [DB Earth Punishment](https://aion2.app/db/skills/17400000) |
| Strengths | <ul><li>**Party buffs:** Earth Punishment (+5% Double Chance and +5% Attack/Defense to the party), Light of Protection (party PvE damage and tolerance: 10.5% at level 1, 17.5% at 15, 20% at 20).</li><li>Prayer of Amplification is **self-only**: in Global logs it never shows on other party members.</li><li>Chain of Torment option 4 lowers the boss's PvE Damage Tolerance by 15% total (a Chanter's Earth's Promise doesn't apply on top of it).</li><li>Resurrection and cleanses.</li></ul> | | [DB Earth Punishment](https://aion2.app/db/skills/17400000), [DB LoP](https://aion2.app/db/skills/17410000), [DB Chain](https://aion2.app/db/skills/17070000) |
| Weaknesses | <ul><li>Lowest personal damage (NotMeter 69.41, 8th).</li><li>Light of Protection doesn't stack with a Chanter's Undefeated Mantra (higher level wins; Mantra wins ties).</li><li>A Korean guide author reports Cleric's attack-speed cap at 94.4% vs about 121.6% for others (KR/TW; UNVERIFIED on Global).</li></ul> | | [NM classPerformance], [DB LoP](https://aion2.app/db/skills/17410000), [Inven Sep 24](https://www.inven.co.kr/board/aion2/6452/29213) |
| PvE standing (Global) | **Essential healer.** 4,562 of 5,303 Global boss parses (86%) have exactly one Cleric. | Party presence | [NM] |
| PvP standing | **UNVERIFIED** (no Global data) | | — |
| Difficulty | **Medium** (this guide's call): you split attention between healing and the damage macro | | — |
| Who should play it | Players who like keeping a party alive. Every Global party wants one. | | [NM] |

---

## 2. Max damage (while healing)

### Single target

| Step | What to do | Why | Source |
|---|---|---|---|
| Pre-pull | **Prayer of Amplification**, then summon **Noble Aura** | <ul><li>Prayer (self only): +20% Attack (10 s at level 1, 17 s at 15). 5: +20% PvE Damage Boost. 10/15: ×1.5 Empyrean Lord's Grace / Earth's Grace.</li><li>Noble Aura: a 300 s companion attack, 6.3% of damage. Level 10: +20% damage to targets with Debilitating Mark ([questlog](https://questlog.gg/aion-2/en/db/skill/17440000)).</li></ul> | [DB Prayer](https://aion2.app/db/skills/17430000), [DB Noble Aura](https://aion2.app/db/skills/17440000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NM] |
| Toggle | **Light of Protection** on, unless a Chanter runs Undefeated Mantra | Party PvE damage and tolerance: 10.5% at level 1, 17.5% at 15, 20% at 20 | [DB](https://aion2.app/db/skills/17410000), [questlog levels](https://questlog.gg/aion-2/en/db/skill/17410000) |
| Core | Hold **Earth's Retribution** + the macro: Earth Punishment → Chain of Torment → Debilitating Mark → Condemnation, plus a Judgment Thunder entry | Condemnation 35.6%; top 10% Global: about 42 logged uses a minute (3 s cooldown, resets on crit) | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Burst | **Bolt** charged to Max, by hand | <ul><li>8.6% of damage.</li><li>Uncharged (macro) Bolt does about one third of a Max cast (DB 987 vs 2,963; Global parses 31–35%).</li><li>Earth's Retribution option 4: −7 s Bolt per Discharge proc.</li></ul> | [NM], [DB Bolt](https://aion2.app/db/skills/17060000), [DB Earth's Retribution](https://aion2.app/db/skills/17010000) |
| Heal | Healing Light / Radiant Recovery by hand; Light of Regeneration on the macro early, by hand later | Heals stay off the macro so you pick Healing Light or Radiant Recovery for the situation; Bolt stays manual because a charge can delay care (KR guide). The sheet puts Light of Regeneration in macro entry 2 early on (see Macros). | [Inven Sep 24](https://www.inven.co.kr/board/aion2/6452/29213) [KR/TW] |

**Line up:** Prayer of Amplification (17 s at level 15; the DB's 10 s is level 1) + Earth Punishment's Earth's Blessing (10 s; 20 s at 20) + a Max Bolt. Derived from the DB durations; stigma buff durations measured in Global parses ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)).

### AoE

| Tool | Targets | Source |
|---|---|---|
| Condemnation, Judgment Thunder, Bolt, Chain of Torment, Debilitating Mark | up to 4 within 4 m | [DB](https://aion2.app/db/skills?class=Cleric) |
| Divine Aura option 2 | becomes AoE | [DB](https://aion2.app/db/skills/17150000) |

Korea's guide: Judgment Thunder is for trash ([Inven Sep 24](https://www.inven.co.kr/board/aion2/6452/29213), KR/TW). Global AoE order is UNVERIFIED.

---

## 3. Macros

The in-game macro: Settings → Key Settings → General → Gameplay → Macro ([Allyria §3.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Rows are numbered from the bottom (row 0 is next to the hotbar); this guide treats row 0 as the highest priority, which is UNVERIFIED on Global (see [README](README.md)).

### Macro A: Global sheet layout (recommended)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Earth Punishment | Chain of Torment | Debilitating Mark | Condemnation | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| 2 | Divine Aura | Light of Regeneration | Judgment Thunder | — | same |

- **Hold:** Earth's Retribution (left click) + the macro. The sheet says to hold the macro and weave left click early on; holding the basic attack with the macro is from the Korean guide ([Inven Sep 24](https://www.inven.co.kr/board/aion2/6452/29213), KR/TW).
- **Press yourself:**
  - Bolt, charged;
  - Noble Aura, Prayer of Amplification, Light of Protection;
  - Healing Light and Radiant Recovery.
- **MP early:** the sheet says to weave left click early on, because holding the macro alone drains MP.
- **Entry 2 (sheet):** Divine Aura on row 0, Light of Regeneration on row 1 and Judgment Thunder (no cooldown) as the filler on row 2; 10 ms delay. The sheet runs Light of Regeneration (30 s cooldown) in the macro "when starting out" and swaps it out later ([Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview); icons matched against the Global DB). Global logs agree that Divine Aura fires constantly: it's in 99% of long top parses. Top Clerics also cast Light of Regeneration 1.85 times a minute (cap 2), Debilitating Mark 5.5 (cap 6) and Earth Punishment 2.2 (cap 2) ([NM]).

### Macro B: Korean top setup (alternative)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Earth Punishment | Divine Aura | Condemnation | Chain of Torment | [Inven Sep 24 optimizer](https://www.inven.co.kr/board/aion2/6452/29213) [KR/TW-confirmed: same skills in the Global DB] |

Hold Earth's Retribution, the macro and Lightning Strike Scattershot (stagger cancel). Use Debilitating Mark only when the party is hurting; the Korean guide found it loses damage on cooldown.

### Banned or nerfed on Global

| Item | Status | Source |
|---|---|---|
| In-game macro | Allowed | Built-in setting ([Allyria §3.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)) |
| External software | **Risk.** NC's unauthorized-program rule; macros named in the Oct 10, Oct 12 and Oct 14 ban waves. | [NC Operation Policy](https://www.plaync.com/policy/operation/aion2global), [Oct 10 notice](https://aion2.plaync.com/en-us/board/notice/view?articleId=6acaa7506b722c561dc6aae9), [Oct 14 notice](https://store.steampowered.com/news/app/3393110/view/1846651706673527) |
| Cleric nerfs on Global | None (Oct 6, Oct 8 and [Oct 13](https://store.steampowered.com/news/app/3393110/view/1846651706673374) notes) | [Oct 6](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544), [Oct 8](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1) |

---

## 4. Stigmas

**Global rules:** 4 slots, cap 20, free resets ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). No rarity, so "n/a" ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

**Global usage:**
- **All parties (per Cleric appearance in a fight):** Earth Punishment 85–87%, Prayer of Amplification 65–66%, Noble Aura 58–59%, Light of Protection 33–35%, Yustiel's Power 17%, Benevolence 14–17%, Absolution 12–14%, Salvation 11–12%.
- **Top 20 per boss:** Earth Punishment 100% (median 20), Prayer 94% (15), Noble Aura 85% (median 10; 15 is the most common level), Light of Protection 43% (15), Salvation 30% (level unreadable).

([NM])

### PvE: Global main loadout (damage-leaning healer; what top Global Clerics run)

This is what top Global Clerics run (per player: Earth Punishment 100%, Prayer 94%, Noble Aura 85%, Light of Protection 43%; [NM]) and what Korea's top 20 run ([NotMeter KR](https://notmeter.com/?view=setup-guide)). **The sheet's own priority is different:** 1. Light of Protection, 2. Earth Punishment, 3. Absolution, 4. Summon Resurrection, swapping Light of Protection for Prayer or Resurrection with a Chanter ([Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)).

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Earth Punishment | Slot 1 | **20** | n/a | <ul><li>5: Condemnation crits.</li><li>10: +10% Double Chance (party +5%).</li><li>15: Attack/Defense (party +5%).</li><li>20: +10 s.</li><li>Global median 20.</li></ul> | [DB](https://aion2.app/db/skills/17400000), [NM] |
| Prayer of Amplification | Slot 2 | **15** (5 is the big step) | n/a | <ul><li>5: +20% PvE Damage Boost.</li><li>10/15: ×1.5 Grace passives.</li><li>20 only adds +15% Attack. A Korean March post says 20 is fine if you aren't Attack-capped (KR/TW, written before Global's 4-slot rules).</li><li>Self only: it doesn't buff the party.</li></ul> | [DB](https://aion2.app/db/skills/17430000), [NM], [vortexgaming KR Mar](https://vortexgaming.io/postdetail/688137) |
| Noble Aura | Slot 3 | **15** | n/a | 15: +30% damage to Incapacitated-immune bosses. 20: attacks 1 s faster. | [DB](https://aion2.app/db/skills/17440000), [NM] |
| Light of Protection | Slot 4 (no Chanter) | **15** | n/a | Party PvE damage and tolerance: 10.5% at level 1, **17.5% at 15**, 20% at 20. 5: +10% Incoming Heal. 15: +10% max HP. | [DB](https://aion2.app/db/skills/17410000), [questlog levels](https://questlog.gg/aion-2/en/db/skill/17410000), [NM] |

**With a Chanter:** the sheet says a Chanter lets the Cleric swap Light of Protection "for another heal / shield / self buff-dmg Stigma", and names Prayer of Amplification or Resurrection; it adds that Yustiel's Power "during certain mechs can be really strong" ([Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)). This guide's suggestions are **Benevolence 20** (group heal over time; cleanses every 5 s at 20) or **Yustiel's Power** (party PvE Damage Tolerance: 20% at level 1, 30% at 20) ([DB Benevolence](https://aion2.app/db/skills/17160000), [DB Yustiel's](https://aion2.app/db/skills/17420000)). Global logs can't settle it: in Mantra-Chanter parties the most common visible extra stigma is Salvation (15%), Benevolence 9%, Yustiel's 6%, and in 104 of 240 parses the fourth stigma isn't visible ([NM]).

**What the parse data shows:** averaged per player, Clerics with Noble Aura in the slot (70 players) deal about 12% more personal damage than those with Light of Protection (8 players). That gap is mostly the party: 177 of the 186 Noble Aura parses had an Undefeated Mantra Chanter, and 14 of the 19 Light of Protection parses had no Chanter. Controlling for that, the gap is +3% (95% range −5% to +11%), not significant. The meter also can't see Light of Protection's party-wide buff ([NM], [method](README.md#method-notes)). Keep Light of Protection when no Chanter covers it.

**Party composition:**
- 81% of single-Cleric Global parties have a Mantra Chanter; there, Clerics run Light of Protection only 20% of the time, against 94% in parties with no Chanter at all ([NM]). With both, only the higher-level Damage Boost applies, and Undefeated Mantra wins a tie (the DB names the Damage Boost part; the sheet says the Chanter's buff takes priority) ([DB](https://aion2.app/db/skills/17410000)).
- Earth Punishment's Earth's Blessing and a Chanter's Power of the Storm can't both be on a party member. In Global logs, Earth's Blessing covers 27% of the fight with a Storm Chanter against 37% without ([DB Earth's Promise / party rules](README.md#party-buffs), [NM]).
- A Chanter's Earth's Promise doesn't apply together with Chain of Torment ([DB](https://aion2.app/db/skills/18780000)).
- With two Clerics, the higher-level Chain of Torment overrides the other's ([Inven Sep 24](https://www.inven.co.kr/board/aion2/6452/29213), KR/TW).

### PvE: progression / care loadout (learning fights)

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Earth Punishment | Keep | 20 | n/a | | [DB](https://aion2.app/db/skills/17400000) |
| Prayer of Amplification | Keep | 15 | n/a | | [DB](https://aion2.app/db/skills/17430000) |
| Benevolence | Care | **20** | n/a | Cleanse every 5 s at 20 | [DB](https://aion2.app/db/skills/17160000), [questlog](https://questlog.gg/aion-2/en/db/skill/17160000) |
| Salvation or Summon Resurrection | Safety | Salvation **15** / Summon Resurrection **10** | n/a | <ul><li>Salvation 15 also protects the lowest-HP party member.</li><li>Resurrection 10: 3 s invincibility after the raise.</li><li>The sheet's own priority list has Summon Resurrection 4th.</li></ul> | [DB Salvation](https://aion2.app/db/skills/17270000), [DB Res](https://aion2.app/db/skills/17390000), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

**Shard order (damage loadout):** derived from the DB breakpoints and Korean advice (a Korean video: levels first, then Earth Punishment 20; [vortexgaming KR](https://vortexgaming.io/postdetail/688137), KR/TW). The loadout at its target levels (Earth Punishment 20, the others 15) costs 180 shards; a fresh 45 has 32, plus about 20 a week. Per-level costs (1/2/4/8, 75 to level 20) are in questlog's Global data.

| Step | Stigma levels |
|---|---|
| 1 | Earth Punishment 10 → Prayer 5 → Light of Protection 5 → Noble Aura 5 |
| 2 | Earth Punishment 20 |
| 3 | Prayer 15 → Noble Aura 15 → Light of Protection 15 |

### PvP

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Salvation | Core | 20 | n/a | 3 s immunity; 20 triggers on Impact-type CC | [DB](https://aion2.app/db/skills/17270000) |
| Earth Punishment | Core | 20 | n/a | | [DB](https://aion2.app/db/skills/17400000) |
| Absolution | Core | 20 | n/a | Removes all debuffs at 10 | [DB](https://aion2.app/db/skills/17290000) |
| Yustiel's Power | Party PvP | 20 | n/a | Party tolerance | [DB](https://aion2.app/db/skills/17420000) |

**UNVERIFIED for Global.** Derived from the DB effects; no Global Cleric PvP source.

### Solo
Earth Punishment, Prayer, Noble Aura and Benevolence. Korean Clerics found Root and Voice of Doom barely help (this repo's KR notes, no primary source linked; KR/TW). Solo target levels: the main loadout's (UNVERIFIED).

**Shard totals:** the main loadout costs 180 shards; the care loadout (Earth Punishment 20, Prayer 15, Benevolence 20, Salvation 15) 220; the PvP four at 20, 300. With 32 at 45 plus about 20 a week, the care and PvP sets are 9–14 weeks out.

---

## 5. Skills

Specialty breakpoints are 8 / 12 / 16 / 20 ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

### Actives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Condemnation | 1st damage | **20** (12 = reset on crit) | n/a | 35.6% of damage. 51% of top Global at 16+, 17% at 20. The sheet lists Condemnation (20) among the skills to push to 20 while leveling. | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Judgment Thunder | 2nd damage | **16** (option 5: Divine Punishment twice) | n/a | 8.3% + Divine Punishment 15.1%. 76% picked option 5 (at least 16). The sheet says 20. | [NM], [DB](https://aion2.app/db/skills/17040000) |
| Bolt | 3rd | **16** (option 5 always crits) | n/a | 8.6%. 27% at 16+. Sheet and Korea: 20. | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Divine Aura | 4th | **12** (16 for −10 s) | n/a | 6.1%. 25% at 16+. Sheet: 20. | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Earth's Retribution | Held | **12** (option 4: −7 s Bolt) | n/a | Korea runs it at 20 (2+3+4) | [NM], [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Chain of Torment | Debuff | **12** | n/a | Option 4: −10% more enemy PvE Damage Tolerance. 90% run 2+4. | [NM], [DB](https://aion2.app/db/skills/17070000) |
| Debilitating Mark | Debuff | **12** | n/a | Lowers the boss's PvE Damage Boost by 5% (15% with option 4): damage mitigation. 2+4 (88%). Top Clerics cast it 5.5 times a minute (cap 6). | [NM] |
| Radiant Recovery | Heal + cleanse | **16** (it already removes 1 debuff; option 1 makes it 2; the sheet says 20) | n/a | 37% picked option 5 (at least 16) | [NM], [repo KR](../data/stigmas.json) |
| Healing Light | Single heal | **16** | n/a | 1+4 (59%). The sheet says 20. | [NM] |
| Light of Regeneration | Party heal over time | **16** | n/a | Option 5: party tolerance. 40% picked option 5 (at least 16), buff median 15. | [NM], [DB](https://aion2.app/db/skills/17090000) |
| Lightning Strike Scattershot | Stagger | **12** | n/a | Korea 16 (4+5). Global: 3+4 32%, 4+5 23% (47 parses). | [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Defiance | CC break | **16** (sheet) | n/a | 0 of 20 Global players with a readable level are at 16 | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

### Passives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Earth's Grace | 1st (Korea) / 2nd (sheet) | as high as possible (Korea's top 20: 35) | n/a | +Crit Damage Boost (10.5% at level 1, 17.5% at 15, 20% at 20), +100 Accuracy; ×1.5 at Prayer 15 | [DB](https://aion2.app/db/skills/17780000), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Empyrean Lord's Grace | 2nd (Korea) / **1st (sheet)** | as high as possible (Korea's top 20: 33) | n/a | 5.5% of Global damage. ×1.5 at Prayer 10. A Korean guide puts Earth's Grace ahead, "not a big difference" (KR/TW). The Global sheet ranks Empyrean Lord's Grace 1st and lists it first on every gear line. | [DB](https://aion2.app/db/skills/17730000), [NM], [Inven Sep 24](https://www.inven.co.kr/board/aion2/6452/29213), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Healing Enhancement | Healer 3rd | Korea's top 20: 18 (no Global level data) | n/a | Heal Boost scales with Attack | [DB](https://aion2.app/db/skills/17740000) |
| Warm Benediction, Prayer of Concentration (Global median 10), Immortal Veil | Filler | 10–15 | n/a | | [NM buffs], [NotMeter KR](https://notmeter.com/?view=setup-guide) |

---

## 6. Specializations

| Item | Recommendation (picks at 8 / 12 / 16 / 20) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Condemnation | 2 / **2+4** / 4+5 / 2+4+5 | 20 | n/a | <ul><li>4: reset on crit.</li><li>5: multi-hit.</li><li>Global 2+4 47%, 4+5 35%.</li><li>Sheet and Korea: 2+4+5.</li></ul> | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Judgment Thunder | 2 / 1+2 / **2+5** / 1+2+5 | 16–20 | n/a | Global 2+5 69% | [NM] |
| Bolt | 3 / **3+4** / 3+5 / 3+4+5 | 16–20 | n/a | Global 3+4 64% | [NM] |
| Divine Aura | 3 / **3+4** / 3+5 / 3+4+5 | 12–20 | n/a | Global 3+4 about 65% | [NM] |
| Earth's Retribution | 2 / **2+4** / — / 2+3+4 | 12–20 | n/a | Global 63–66%; the sheet also says 2/4. Korea's top 20: 2+3+4. | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Chain of Torment | 2 / **2+4** (Korea's top 20 too) | 12 | n/a | Global 90% | [NM] |
| Debilitating Mark | 2 / **2+4** | 12 | n/a | Global 88% | [NM] |
| Radiant Recovery | 2 / 2+3 / **2+5** / 1+2+5 or 2+3+5 | 16–20 | n/a | Global split: 2+3 about 35%, 2+5 about 25%. Option 2: aion2.app says +20% skill speed, but questlog's Global data and KR say +1 consecutive use, and Global logs agree (about 3.4–3.9 uses a minute with option 2 vs 2.7–2.8 without). | [NM], [questlog](https://questlog.gg/aion-2/en/db/skill/17120000) |
| Healing Light | 1 / **1+4** / 1+5 / 1+4+5 | 16 | n/a | Global 59%; sheet 1+4+5 | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Light of Regeneration | — / 3+4 or 1+4 / **4+5** | 16 | n/a | Global split: 4+5 21%, 3+4 18% | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Defiance | 3 / 3+5 | 16 | n/a | Sheet. No Global player with a readable level reaches 16 | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

**PvP (UNVERIFIED):** Chain of Torment option 5 (ignores Block/Evasion), and Bolt option 1 (stun on a full charge).

### Daevanion boards (Global)

| Item | Recommendation | Target | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Priority | <ul><li>Orange > Blue > Green > White.</li><li>Condemnation / Judgment Thunder blue tiles at milestones (this guide's application of the 8/12/16/20 rule).</li><li>Earth's Grace / Empyrean Lord's Grace green tiles (derived).</li></ul> | — | n/a | | [Allyria ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Bible ch.7](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Global changes | About 316 points at 45 (+100 from shops); orange % 2.5 → 1.5; Ariel removed | — | n/a | | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

Korea has a Cleric node guide ([Inven](https://www.inven.co.kr/board/aion2/6452/27247), KR/TW). The Global path is UNVERIFIED.

---

## 7. Tier list

| Content | Tier | Placement reason | Source |
|---|---|---|---|
| PvE healer | **S** (the healer of record) | In 86% of Global boss parses; party buffs plus a boss debuff | [NM] |
| PvE personal damage | **C** (8th of 8) | NotMeter score 69.41; −25.6% at equal CP ([README method](README.md#method-notes)). Post-patch week: 66.98, still 8th | [NM classPerformance], [NM post-patch](https://notmeter.com/g/29087b479916fb24/data/notmeter-global-ranking.json) |
| PvP | **UNVERIFIED** | | — |
| Solo | **B (opinion)** | Self-heals and solid damage skills; slow kills | [DB](https://aion2.app/db/skills?class=Cleric) |

---

## 8. Gear

Global rules: **Unique is the settle rarity** for every slot in Season 1 ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). Phases: [README](README.md#gear-phases).

Enhancement targets (+17 / +16 / +15) come from the sheet roadmap's long-term "Ludra Preparations" list; Ludra isn't on Global yet ([Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)).

| Item | Recommendation (stat lines in order) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Weapon (mace) | Weapon Damage Boost > Combat Speed > Might > Precision > Damage Boost > Multi-hit > Attack | **+17** | Unique | Korean testing: Cleric attack speed caps at 94.4% (KR/TW, UNVERIFIED on Global) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Guard | Same, Damage Boost 3rd | **+17** | Unique | | same |
| Helmet | Incoming Heal > Empyrean Lord's Grace > Earth's Grace > Double Chance > Attack Increase > Crit > Attack | **+15** | Unique | | same |
| Shoulders | Crit Damage Boost > Empyrean Lord's Grace > Earth's Grace > Accuracy > Crit > Attack | **+15** | Unique | | same |
| Chest | Damage Boost > Empyrean Lord's Grace > Earth's Grace > Crit > Accuracy > Attack | **+15** | Unique | | same |
| Legs | Damage Tolerance > Empyrean Lord's Grace > Earth's Grace > Perfect > Attack Increase > Crit > Attack | **+15** | Unique | | same |
| Gloves / Boots | Combat Speed / Move Speed > Empyrean Lord's Grace > Earth's Grace > Perfect > Crit > Attack | **+15** | Unique | | same |
| Cloak | Empyrean Lord's Grace > Earth's Grace > Double Chance (the sheet also lists "Smite", the same stat) > Attack Increase > Crit > Attack | **+15** | Unique | No Perfect on capes on Global per Sirin; the Bible's Global list still has it (see discrepancies) | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Bible ch.3](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Earrings / Necklace | Empyrean Lord's Grace > Earth's Grace > Might > Precision > Healing Enhancement > Accuracy > Crit > Attack | **+16** | Unique | | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Rings | Condemnation > Bolt > Radiant Recovery > Might > Precision > Divine Aura > Judgment Thunder > Healing Light > Attack | **+17** | Unique | | same |
| Bracelets | Wisdom > Destruction > Time > Illusion > Death | **+15** | Unique (slot 1); Epic / blue (slot 2) | | same, [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Belt / Amulet | Upgrade early, then stop; amulet to +10, then Substance Morph (live sheet) | to Unique (yellow / "gold") | **Unique** | Allyria's "Gold" is the Unique tier (Sirin) | [Allyria §6.1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Clash Runes | Only +1 early on, about +5 later (sheet); Allyria: not past +6/7 | **~+5** (cap +6/7) | n/a | Upgrades are RNG-heavy (Allyria), and a failed upgrade destroys the rune (Bible) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [Allyria §6.1.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Bible ch.2](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |

| Other | Recommendation | Source |
|---|---|---|
| Manastones | Weapon Damage Boost ≈ Crit Damage Boost > Damage Boost > Attack | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Arcana | Chalice Time · Parchment Life/Destiny · Compass Death/Freedom · Bell Destruction · Mirror Illusion/Wisdom. Skill lines: Earth's Grace first (Korea's top 20 all run it at +11). | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Pet Genus | <ul><li>Special line 4: Double Chance.</li><li>Line 4 on other boards: PvE Damage Boost.</li><li>Lines 1/5: Max Attack.</li><li>**Lines 3/6/9: Critical Hit** (top Global Clerics at about 38%).</li><li>Line 7: PvE Damage Tolerance.</li><li>No Genus line boosts healing directly; whether heals scale with Attack is UNVERIFIED.</li></ul> | [Genus audit](../docs/genus-audit.md) |
| Wings | Talisra (Season Shop) for CDR. Korea notes Talisra for a lower Salvation cooldown. | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [repo KR](../data/classes.json) |

[NM]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM buffs]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM classPerformance]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
