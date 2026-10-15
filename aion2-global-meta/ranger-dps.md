# Ranger (弓星) — DPS spec · AION 2 Global

**Patch covered:** Global client build **25926599** (Steam public branch, updated 2026-10-14 06:40 UTC). That is the [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374) on top of the [Oct 6 PDT patch](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544) and the [Oct 8 PDT hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1). None of the three changed a Ranger skill. Build id: [SteamCMD](https://api.steamcmd.net/v1/info/3393110). NotMeter data (week of Oct 7–14) was recorded on the previous build 25800038. **Written:** 2026-10-13, **updated for the Oct 13 patch:** 2026-10-14.

**Tags:** [Global] · [KR/TW-confirmed] = Korean or Taiwanese source checked against the Global client · UNVERIFIED.

**Main data sources:**
- **ALLY:** [Allyria's Ranger Guide, Global Edition](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), updated 11.10.2026. This is the main Global source.
- **NM:** [NotMeter Global ranking](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), week of Oct 7–14. (NotMeter has since retired this generation, so the link returns 404; see the [README](README.md).) Top 20 Ranger parses on each of 15 bosses: 300 parses from 106 players, median CP 167,655, median DPS 75,538.
- **DB:** [aion2.app Global client DB](https://aion2.app/db/skills?class=Ranger), client dated 18.09.2026.
- **Sheet:** [Global class sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview).
- **Sheet snapshot:** citations of this class's sheet tab refer to the copy downloaded on Oct 14. Later that day the author replaced the tab with a link to [daevaos](https://daevaos.com/guides/ranger-class-guide), where the build is now maintained; differences found are noted where they matter.
- **Bible:** [Kanon's Bible](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview).

**How to read ALLY's specialty colors:** green = option 1, blue = 2, yellow = 3, orange = 4, red = 5. The game numbers specialties in DB order, and the colors match the in-game icons.

**A source conflict to know about:**
- Allyria writes that Ranger skill balance "carries over from the current TW patch". Global parse data supports this: Korea's Sep 16 changes are live on Global (see the [README](README.md)), even though the aion2.app database still shows older values.
- KR/TW Sep 16 gave every Ranger attack an element (Drill Dart, Griffon and Explosive Arrow became Fire). With Sep 16 live, this is likely on Global too (UNVERIFIED for this specific change).
- Ranger's damage skills show no difference between the Global DB and the KR/TW tooltips this guide uses.

---

## 1. Overview

| Item | Recommendation / finding | Why | Source |
|---|---|---|---|
| Role | Ranged physical DPS with a bow | NC: "A quiet hunter … with a single, decisive shot" | [NC class list](https://aion2.plaync.com/en-us/about/index#classes) |
| Playstyle | <ul><li>Deadshot (3-stage charge; +35% with Precision): 23.5% of damage.</li><li>Tempest Shot (the held-filler spam): 16.6%.</li><li>Drill Dart: 10.9%.</li><li>Hunter's Soul procs: 6.5%.</li><li>Snipe's option 4 cuts Deadshot's cooldown on every hit.</li></ul> | Global shares | [NM], [DB Deadshot](https://aion2.app/db/skills/14010000), [DB Snipe](https://aion2.app/db/skills/14020000) |
| Strengths | <ul><li>Safe range (20 m).</li><li>Lots of dashes; damage doesn't depend on distance.</li><li>Steady damage that "never really stops" once geared.</li></ul> | | [ALLY §0.3](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [DB range](https://aion2.app/db/skills?class=Ranger) |
| Weaknesses | <ul><li>Slow early: Combat Speed and CDR make the class.</li><li>Deadshot must be charged by hand. The in-game macro fires it uncharged: about one-third of a Max cast by tooltip (599 vs 1,798). Global macro-only parses land at roughly 40–90% of a Max cast per cast, but that's a small sample (4 players).</li></ul> | | [ALLY §0.3, FAQ](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM] |
| PvE standing (Global) | **2nd of 8.** NotMeter score 114.85; about even at equal CP (+0.7% on all ranked parses; +0.5% per player on the top-20 set, 95% range −3% to +4%), 5th–6th, not significant. Top Rangers also have the highest median CP. | | [NM classPerformance] |
| PvP standing (Global) | **UNVERIFIED.** ALLY: "reliable damage dealer in both PvE and PvP", but the guide has no PvP section. | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Difficulty | **Medium** (this guide's call). Manual Deadshot charging, Marking Shot upkeep, positioning for range. | | Mechanics: [ALLY ch.3](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Who should play it | Ranged players who want consistent damage and mobility, and are patient early | | [ALLY §0.3](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |

---

## 2. Max damage

### Single target

| Step | What to do | Why | Source |
|---|---|---|---|
| 1 | **Marking Shot**, standing still | Precision: +300 Crit for 10 s (15 s with option 3). Deadshot +35% while it's up. Keep it up yourself; don't spam it. | [DB](https://aion2.app/db/skills/14090000), [ALLY ch.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| 2 | **Gale Arrow** | Gale: +7% Combat Speed and +7% PvE Damage Boost for 10 s. At 16, option 5 = −10 s cooldown for full uptime. | [DB](https://aion2.app/db/skills/14110000), [ALLY ch.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| 3 | **Vaizel's Authority** + **Bow of Blessing** + **Supporting Fire** | <ul><li>Vaizel's: +20% Attack (10 s at level 1, 20 s at 20).</li><li>Bow of Blessing: +200 Crit and +100 Accuracy; 15: +20% Crit Damage Boost; 20: +7% Double Chance.</li><li>Supporting Fire: orb, 30 s at 10.</li></ul> | [DB Vaizel's](https://aion2.app/db/skills/14310000), [DB Bow](https://aion2.app/db/skills/14220000), [DB Supporting Fire](https://aion2.app/db/skills/14380000) |
| 4 | **Deadshot to charge stage 3** | 23.5% of damage. Top 10% of Global parses at equal CP: median 8.4 Deadshots a minute. | [NM], [ALLY FAQ](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| 5 | Hold **Snipe** + the macro | <ul><li>Snipe option 4: −1 s Deadshot per hit.</li><li>Snipe option 5: Tempest Arrow chain (3.3% of damage).</li><li>The macro lines fire Gale Arrow, Griffon Arrow, Snare Shot, Drill Dart, Tempest Shot, Burst Arrow and the three buffs (Macro A).</li></ul> | [DB Snipe](https://aion2.app/db/skills/14020000), [NM] |
| 6 | **Snare Shot** before **Burst Arrow** | Burst Arrow only hits Slowed or Rooted targets. Rooting Eye procs on them. | [DB Burst Arrow](https://aion2.app/db/skills/14080000), [DB Rooting Eye](https://aion2.app/db/skills/14770000) |
| 7 | **Griffon Arrow** on cooldown | Crimson Flames damage over time: 3.9% of damage | [DB](https://aion2.app/db/skills/14060000), [NM] |

**Line up:** Vaizel's (20 s at level 20), Bow of Blessing (17 s at 15), Gale (10 s) and Precision (10–15 s) on the same Deadshot. At Vaizel's 20, every crit has a 50% chance to cut all cooldowns by 1 s, so pack your crits inside it ([DB](https://aion2.app/db/skills/14310000)). Stigma buff durations measured in Global parses ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)); the DB's "10 s" is the level-1 value.

**Stagger:** Arrow Storm 50, Explosive Arrow 20, Griffon Arrow 20, Burst Arrow 15, Deadshot 10–16. Save these for stagger bars ([ALLY §1.3](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Arrow Scattershot is only for broken (staggered) bosses, as cooldown, HP and MP refill ([ALLY ch.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).

### AoE (packs)

| Tool | Targets | Source |
|---|---|---|
| Tempest Shot, Drill Dart, Gale Arrow, Snare Shot, Burst Arrow, Griffon Arrow | up to 4 within 4 m of the target | [DB](https://aion2.app/db/skills?class=Ranger) |
| Explosion Trap | up to 4 within 5 m; option 1 pulls enemies; "only used for pulling mobs together" in PvE | [DB](https://aion2.app/db/skills/14170000), [ALLY ch.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Arrow Storm (stigma) | up to 4; 50 stagger | [DB](https://aion2.app/db/skills/14270000) |

**AoE order:** Explosion Trap to group, then Snare Shot (Slow) → Burst Arrow and Griffon Arrow, then the held Snipe + macro ([ALLY ch.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). For farming, ALLY suggests holding only the in-game macro key without Deadshot ([ALLY FAQ](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).

---

## 3. Macros

The in-game macro: Settings → Key Settings → General → Gameplay → Macro ([ALLY §3.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Rows are numbered from the bottom (row 0 is next to the hotbar); this guide treats row 0 as the highest priority, which is UNVERIFIED on Global (see [README](README.md)).

**ALLY: keep these out of the macro**
- Marking Shot: spamming it wastes animations and forces jump movement, which can kill you.
- Arrow Scattershot.
- Suppressing Arrow.
- Explosion Trap.
- Mother Nature's Breath.

### Macro A: Global sheet layout (recommended in-game-only setup)

| Line (key) | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| Q | Gale Arrow | Griffon Arrow | Snare Shot | — | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Drill Dart slot | Drill Dart | Tempest Shot | — | — | same |
| 8 | Burst Arrow | Vaizel's Authority | Bow of Blessing | Supporting Fire | same |

The in-game Macro list fires those lines in the order Gale line → Drill line → Burst line → Drill line ([Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview); icons matched against the DB icons).

- **Delays:** 10 ms.
- **Hold:** Snipe (left click) + the macro key.
- **Press yourself:**
  - Deadshot, charged;
  - E: Marking Shot → Arrow Scattershot (one line);
  - key 1 Explosion Trap, key 2 Suppressing Arrow, key 3 Deadshot ([Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)).
- **Tempest Shot sits under Drill Dart** in the same line, in both the Global sheet and the Korean Aug 30 post ([Inven Aug 30](https://www.inven.co.kr/board/aion2/6450/19104), KR/TW).
- **Buffs in the macro:** ALLY says buffs in the macro are fine, because you run boss to boss. The Korean Aug 30 author also keeps buffs in the macro. He reports Deadshot at 24–28 hits ("타", a hit count, not casts) in a one-minute dummy run ([Inven Aug 30](https://www.inven.co.kr/board/aion2/6450/19104), KR/TW). Global parses record 2 hits per Deadshot cast ([NM]), so that is roughly 12–14 casts (this guide's inference).

### Macro B: Korean Aug 30 setup (alternative; uses a mouse macro)

| Entry | Row 0 | Row 1 | Row 2 | Row 3 | Source |
|---|---|---|---|---|---|
| 1 | Gale Arrow | Griffon Arrow | Snare Shot | Explosive Arrow* | [Inven Aug 30](https://www.inven.co.kr/board/aion2/6450/19104) (KR/TW, pre-Sep 16; same skills in the Global DB) |
| 2 | Vaizel's Authority | Supporting Fire | Bow of Blessing | Burst Arrow | same |
| 3 | Drill Dart | Tempest Shot | — | — | same |

- The post's in-game skill macro is Drill Dart, Drill Dart at 10 ms; Marking Shot, Mother Nature's Breath and Snipe sit on their own keys.
- The author runs the rest with a mouse macro ("마매"), which is external software (see the ban row below).
- An earlier version of this guide cited an "Inven Sep 6" post for a different layout; the link pointed to this Aug 30 post, and no Sep 6 source was found.

\*Explosive Arrow is only in 30% of Global top builds ([NM]). Without it the row stays empty.

### Charge-skill note
The in-game macro can't fire Deadshot at stage 3. Either charge it yourself while holding Snipe + the macro, or use external software. ALLY's setup uses Razer or Logitech to do this ([ALLY §3.3–3.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). See the ban row below before doing that.

### Banned or nerfed on Global

| Item | Status | Source |
|---|---|---|
| In-game macro | Allowed | [ALLY FAQ](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| External macro software (Razer / G-Hub hold-to-run) | **Disputed.** ALLY: "Is this bannable? No… as long as you aren't building a macro that can run automatically." NC's policy bans programs or devices "enabling actions impossible for regular users", and the Oct 10 ban wave named "use of macros". NC hasn't said hold-to-run mouse macros are allowed, so treat them as a risk. | [ALLY FAQ](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NC Operation Policy](https://www.plaync.com/policy/operation/aion2global), [Oct 10 notice](https://aion2.plaync.com/en-us/board/notice/view?articleId=6acaa7506b722c561dc6aae9), [Oct 14 notice](https://store.steampowered.com/news/app/3393110/view/1846651706673527) |
| Logitech with LMB/RMB as bound keys | Doesn't work; rebind to keyboard keys | [ALLY §3.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Ranger macro nerfs on Global | None (Oct 6, Oct 8 and [Oct 13](https://store.steampowered.com/news/app/3393110/view/1846651706673374) notes) | [Oct 6](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544), [Oct 8](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1) |

---

## 4. Stigmas

**Global rules:**
- 4 slots, cap 20; free resets ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- ALLY: the 4th slot only arrives at 45. Other Global sources say the slots open at character levels 22 / 27 / 32 / 37; see [discrepancies](discrepancies.md).
- No rarity, so "n/a" ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).
- AP farming in the Abyss is the main shard source ([ALLY ch.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).

**Global usage (top 20 per boss):** Vaizel's Authority 97% (median 20), Supporting Fire 96% (buff median 10, mode 15), Bow of Blessing 96% (15), Griffon Arrow 72% (15), Explosive Arrow 30% ([NM]).

### PvE

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Vaizel's Authority | Slot 1, "main buff" | **20** | n/a | <ul><li>10: ×1.5 Focused Eye.</li><li>15: ×1.5 Hunter's Soul.</li><li>20: 50% chance to cut all cooldowns 1 s on crit.</li><li>Global median 20.</li></ul> | [ALLY §2.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [DB](https://aion2.app/db/skills/14310000), [NM] |
| Bow of Blessing | Slot 2 | **15**, then 20 | n/a | 10: Attack from Crit. 15: +20% Crit Damage Boost. 20: +7% Double Chance. | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [DB](https://aion2.app/db/skills/14220000), [NM] |
| Supporting Fire | Slot 3 | **15**, then 20 | n/a | <ul><li>10: +15 s duration.</li><li>15: −30 s cooldown, so a 30 s orb every 60 s.</li><li>20: always crits.</li><li>4.4% of damage.</li></ul> | [DB](https://aion2.app/db/skills/14380000), [NM] |
| Griffon Arrow | Slot 4 (damage) | **15** | n/a | 15: Enhanced Crimson Flames. 20: damage-over-time interval halved. 72% use, median 15. | [DB](https://aion2.app/db/skills/14060000), [NM], [ALLY §2.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Arrow Storm | Slot 4 (stagger / AoE) | **10** | n/a | 50 stagger, the most of any Ranger skill. 10: Slow. 0 of 106 top Global Rangers run it. | [ALLY §1.3](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [DB](https://aion2.app/db/skills/14270000) |
| Mother Nature's Breath | Slot 4 (survival) | **5** (cleanses damage over time) | n/a | Tolerance and lifesteal. 0 of 106 top Global Rangers run it. | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [DB](https://aion2.app/db/skills/14350000) |
| Explosive Arrow | Not in the Global four | — | n/a | 30% use. At equal CP the two are even: Griffon Arrow users (72 players) vs Explosive Arrow users (29), +0.1% averaged per player, 95% range −6% to +6%. | [NM], [method](README.md#method-notes) |

**Shard order:** Vaizel's 10 → Bow 10 → Supporting Fire 10 → Griffon 5 → Supporting Fire 15 → Vaizel's 15 → Bow 15 → Vaizel's 20 → Griffon 15 → Bow 20 / Supporting Fire 20. This is this guide's own plan, from the Global medians and the DB breakpoints. A Korean 5-slot post says Bow and Vaizel's must reach 20 ([vortexgaming KR](https://vortexgaming.io/postdetail/722757), KR/TW).

### PvP

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Vaizel's Authority | Core | 20 | n/a | Burst | [DB](https://aion2.app/db/skills/14310000) |
| Mother Nature's Breath | Core | 20 | n/a | Cleanses damage over time; +10% PvP tolerance at 20 (20% total) | [DB](https://aion2.app/db/skills/14350000) |
| Ambush Kick | Core | 20 | n/a | Escape; stun at 15–20 | [DB](https://aion2.app/db/skills/14120000) |
| Bow of Blessing or Ensnaring Trap | 4th | 20 | n/a | Burst, or a buff strip (10) | [DB Trap](https://aion2.app/db/skills/14180000) |

This is **this guide's own pick, UNVERIFIED for Global**, built from the DB effects. The Korean post it was first tied to ([Inven 15518](https://www.inven.co.kr/board/aion2/6450/15518), KR/TW) is a PvE dummy test that suggests Mother Nature's Breath or Ambush Kick only as a 6th-slot utility. ALLY covers no PvP.

### Solo / survival

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Mother Nature's Breath | Replaces Griffon Arrow | 10 | n/a | ALLY's survival flex | [ALLY §2.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Ambush Kick | Alternative 4th | 10 | n/a | "Movement / survivability" flex | [ALLY §2.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |

---

## 5. Skills

**ALLY's tiers (Global):**
- **+20:** Gale Arrow > Deadshot > Drill Dart > Tempest Shot > Burst Arrow.
- **+16:** Snipe > Marking Shot.
- **+12:** Snare Shot > Explosion Trap > Arrow Scattershot.
- **No investment:** Defiance > Suppressing Arrow.

All of +20 is "difficult/impossible … in season 1" ([ALLY §1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Specialty breakpoints are 8 / 12 / 16 / 20 ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)). ALLY says to sometimes take a blue Daevanion tile over an orange one to reach a skill milestone.

### Actives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Gale Arrow | Tier 1 | **20** (16 = option 5) | n/a | Uptime buff. 69% of top Global players picked option 5 (so at least 16). | [ALLY §1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM] |
| Deadshot | Tier 1 | **20** (16 = option 5) | n/a | 23.5% of damage. 70–72% picked option 5 (so at least 16), 24–25% have three picks (20). | [NM], [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Drill Dart | Tier 1 | **20** (16 = option 5, fires twice) | n/a | 10.9%. 67% picked option 5 (so at least 16). | [NM], [DB](https://aion2.app/db/skills/14050000) |
| Tempest Shot | Tier 1 | **20** (16 = +20% skill speed) | n/a | 16.6%. 85% picked option 5 (so at least 16). | [NM], [DB](https://aion2.app/db/skills/14340000) |
| Burst Arrow | Tier 1 (last) | **20** (16 for option 5) | n/a | 4.1%. 21% picked option 5 (so at least 16). | [NM], [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Snipe | Tier 2 | **16** (12 is the big jump: option 4) | n/a | 69% picked option 5 (so at least 16). Options 4+5 for 64%. | [NM], [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Marking Shot | Tier 2 | **16** (12 is enough for 1+3) | n/a | 90% of top Global players run 1+3. Their level can't be inferred: 1+3 is available from 12. | [NM], [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Snare Shot | Tier 3 | **12** | n/a | Enables Burst Arrow; 2+3 (67%) | [NM], [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Explosion Trap | Tier 3 | **12** | n/a | Grouping | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Arrow Scattershot | Tier 3 | **12** | n/a | Stagger windows only | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Defiance | Tier 4 | skill-point level (≤10) | n/a | No investment | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Suppressing Arrow | Tier 4 | skill-point level (≤10) | n/a | "Not used at all" in PvE | [ALLY ch.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |

### Passives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Focused Eye | S | as high as possible (KR top 20: 35–36) | n/a | +100 Accuracy, +1% PvE Damage Boost, +0.2% Double Chance. ×1.5 under Vaizel's 10. | [ALLY §1.2](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [DB](https://aion2.app/db/skills/14740000), [NotMeter KR](https://notmeter.com/?view=setup-guide) (KR/TW) |
| Hunter's Resolve | S | as high as possible (KR top 20: 33) | n/a | +6% Crit Damage Boost | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [DB](https://aion2.app/db/skills/14750000), [NotMeter KR](https://notmeter.com/?view=setup-guide) (KR/TW) |
| Hunter's Soul | Tier 1 | 20 (KR top 20: 20) | n/a | 6.5% of Global damage | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM], [NotMeter KR](https://notmeter.com/?view=setup-guide) (KR/TW) |
| Rooting Eye / Concentrated Fire | Tier 2 | 15–17 (KR top 20: 16 / 17) | n/a | 2.4% / 2.8% of damage | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM], [NotMeter KR](https://notmeter.com/?view=setup-guide) (KR/TW) |
| Melee Fire, Vigilant Eye | Tier 2 | 15 (KR top 20) | n/a | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NotMeter KR](https://notmeter.com/?view=setup-guide) (KR/TW) |
| Revitalization Contract, Wind Vigor, Unyielding Resolve | Tier 3 | 10–15 (Wind Vigor Global median 13) | n/a | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM buffs] |

---

## 6. Specializations

ALLY's priority order is used throughout, with color = option number (see header). Most rows agree with what top Global Rangers pick. Exceptions: Deadshot at 16 (ALLY 2+3, Global's most common 2+5), Burst Arrow at 16 (ALLY 4+5, only 10% of top Global Rangers) and Arrow Scattershot (Global split 3+4 / 4+5).

| Item | Recommendation (ALLY order → picks at 8 / 12 / 16 / 20) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Deadshot | Blue > Yellow > Red: 2 / 2+3 / **2+3 (ALLY) or 2+5 (Global's most common at 16, 38%)** / 2+3+5 | 20 | n/a | <ul><li>2: +30% skill speed.</li><li>3: mobile.</li><li>5: extra damage on hit.</li><li>Option 4 (orange) is "total trash with a geared character" but may beat 5 early in S1.</li><li>Global: 2+5 38%, 2+3 24%, 2+3+5 15%; 2+4+5 about 9%.</li><li>Korea's Sep 16 patch (live on Global) fixed option 5's extra damage, which didn't multi-hit unless option 4 was also equipped, so the "orange may beat red early" note is weaker now ([KR Sep 16 notes](https://aion2.plaync.com/ko-kr/board/update/view?articleId=6aa99cb8a279104f7d9d5c34)).</li></ul> | [ALLY ch.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM] |
| Snipe | Orange > Red > Yellow: 3 / **3+4** / 4+5 / 3+4+5 | 16 | n/a | <ul><li>4: −1 s Deadshot per hit.</li><li>5: Tempest Arrow chain.</li><li>3 (multi-hit) early; ALLY: 0.7% HP regen instead if HP is short.</li><li>Global 4+5 64%.</li></ul> | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM], [DB](https://aion2.app/db/skills/14020000) |
| Tempest Shot | Red > Yellow > Blue: 3 / 2+3 / **3+5** / 2+3+5 | 20 | n/a | <ul><li>3: +12% on few targets.</li><li>5: +20% skill speed.</li><li>2: +10% crit, the last pick. ALLY gives no reason; the crit-cap reason (top Rangers sit at about 51%) is this guide's inference.</li><li>Global 3+5 55%.</li></ul> | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM] |
| Drill Dart | Red > Yellow > Orange: 3 / 3+4 / **3+5** / 3+4+5 | 20 | n/a | 5: fires 1 extra time. ALLY: 3% HP regen (option 1) instead of multi-hit early if HP is short. Global 3+5 44%. | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM] |
| Gale Arrow | Orange > Red > Yellow: 1 / 1+4 / **4+5** / 3+4+5 | 20 | n/a | Option 1 (+5 s) only early. At 16, switch to −10 s cooldown (5) + Combat Speed / damage when hitting few targets (4). Global 4+5 62%. | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM] |
| Burst Arrow | Red > Orange > Yellow: 3 / **3+4** / 4+5 / 3+4+5 | 20 | n/a | <ul><li>5: 25% chance to reset.</li><li>4: +20% on few targets.</li><li>3: mobile.</li><li>Option 1 (10% HP regen) if HP is short.</li><li>Global 3+4 52%.</li></ul> | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM] |
| Marking Shot | Green > Yellow > Red: 1 / **1+3** | 12–16 | n/a | 1: +5% Perfect. 3: +5 s Precision. Global 90%. | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM] |
| Snare Shot | Yellow > Blue > Orange: 3 / **2+3** (or 2+4) | 12 | n/a | Option 4 (Shackling Arrow) is "higher dmg overall" but clunky; ALLY: use orange instead of yellow, which gives 2+4. Global 2+3 66%, 3+4 14%, 2+4 9%. | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM] |
| Arrow Scattershot | Red > Orange > Green: 1 / 1+4 / 4+5 | 12 (16) | n/a | 5: −1 s all cooldowns per hit | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Explosion Trap | Green > Yellow > Red: 1 / 1+3 | 12 | n/a | 1: pull | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Suppressing Arrow | Yellow > Green: 3 / 1+3 | — | n/a | Unused in PvE | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Defiance | Red > Yellow > Blue: 3 / 2+3 / 3+5 | — | n/a | Global 3 64% | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [NM] |

**PvP changes:** Deadshot option 4 (ignores Block/Evasion) is "nice for PvP" ([ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)). Other PvP picks are UNVERIFIED.

### Daevanion boards (Global)

| Item | Recommendation | Target | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Priority | Orange > Blue > Green > White on all boards; blue before orange if it reaches an 8/12/16/20 milestone | — | n/a | | [ALLY ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| White tiles | Attack > Crit > HP > Defense > Crit Defense > MP | — | n/a | | [ALLY ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Rule | If you can't max a board, skip non-offensive tiles. Boards after the first four can be fully maxed. Resets cost Kinah. | — | n/a | | [ALLY ch.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Points / Global changes | About 316 at 45, +50 Shugo, +50 Nightmare. Ariel removed; orange % 2.5 → 1.5. | — | n/a | | [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

ALLY's Global board pictures are images. The tile-by-tile Ranger path is in the guide, but this text summary can't reproduce it, so it's UNVERIFIED here.

---

## 7. Tier list

| Content | Tier | Placement reason | Source |
|---|---|---|---|
| PvE | **A** (2nd of 8) | NotMeter score 114.85; +0.7% at equal CP | [NM classPerformance] |
| PvP | **UNVERIFIED** | No Global data. ALLY: reliable in PvE and PvP, without PvP testing. | [ALLY §0.3](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Solo / leveling | **A (opinion)** | Ranged, mobile, AoE filler. Launch-week guides call Ranger the safe leveling pick. | [ExitLag](https://www.exitlag.com/news/aion-2-class-tier-list/) (opinion) |

---

## 8. Gear

Global rules:
- **Unique is the settle rarity** for every slot in Season 1 ([Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- PvE crafted gear is best in slot. F2P or sub-only players can stay in dungeon armor "without losing a lot" ([ALLY ch.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).
- ALLY's progression: MSQ golden weapon → Vakron → Transcendence 2/3 → Kromede accessories and weapon → Transcendence 4 → Ferocious Horn Den armor → crafted accessories and bow → Ludra ([ALLY §0.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit)).

Enhancement targets (+17 / +16 / +15) come from the sheet roadmap's long-term "Ludra Preparations" list; Ludra isn't on Global yet ([Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview)).

| Item | Recommendation (ALLY line order) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Weapon (bow) | Weapon Damage Boost > Combat Speed > Might > Damage Boost > Multi-hit > Precision > Attack | **+17** (sheet) | Unique | | [ALLY §6.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Guard | Same as the weapon | **+17** | Unique | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Helmet | Incoming Heal > Focused Eye > Hunter's Resolve > Double Chance > Attack Increase > Crit > Attack | **+15** | Unique | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Pauldrons | Crit Damage Boost > Focused Eye > Hunter's Resolve > Double Chance > Crit > Attack > Accuracy | **+15** | Unique | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Breastplate | Damage Boost > Focused Eye > Hunter's Resolve > Perfect > Crit > Accuracy > Attack | **+15** | Unique | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Legs | Damage Tolerance > Focused Eye > Hunter's Resolve > Perfect > Attack Increase > Crit > Attack | **+15** | Unique | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Gloves | Combat Speed > Focused Eye > Hunter's Resolve > Perfect > Crit > Attack > Accuracy | **+15** | Unique | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Boots | Move Speed > Focused Eye > Hunter's Resolve > Perfect > Crit > Attack > Accuracy | **+15** | Unique | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Cape | Focused Eye > Hunter's Resolve > Double Chance > Attack Increase > Crit (PvP: Crit Damage Tolerance) > Accuracy > Attack | **+15** | Unique | No Perfect on capes on Global | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Necklace | Focused Eye > Hunter's Resolve > Combat Speed > Might > Precision > Accuracy > Crit | **+16** | Unique | Combat Speed / Might / Precision on necklaces are new on Global | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Earrings | Focused Eye > Hunter's Resolve > Might > Precision > Move Speed > Crit > Attack | **+16** | Unique | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Rings | Gale Arrow > Deadshot > Tempest Shot > Drill Dart > Might > Precision > Burst Arrow | **+17** | Unique | | [ALLY](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Bracelets | Wisdom > Destruction > Time > Illusion > Death > Justice > Life > Space > Freedom > Destiny | **+15** | Unique (slot 1); Epic / blue (slot 2) | From Sanctuary (Ludra); story/side-quest ones until then | [ALLY §6.1.3](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Belt / Amulet | Upgrade early, then stop (expensive in the first weeks); amulet to +10, then Substance Morph (live sheet) | to Unique (yellow / "gold") | **Unique** | | [ALLY §6.1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Clash Runes | Only +1 early on, about +5 later (sheet); ALLY: "not recommended to try to get higher than 6/7" | **~+5** (cap +6/7) | n/a | Upgrades are RNG-heavy (ALLY), and a failed upgrade destroys the rune (Bible) | [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview), [ALLY §6.1.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Bible ch.2](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview) |
| Pendant / Brooch / Seals | Not on Global yet (level-50 patch, Sanctuary 3, Sanctuary 4) | — | — | | [ALLY §6.1.2–6.1.5](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |

| Other | Recommendation | Source |
|---|---|---|
| Manastones / Soulstones | <ul><li>Early S1: Crit / Accuracy.</li><li>End gear: two gold +100 lines (Weapon or Front/Back Damage Boost best), or a +100 line plus Attack.</li><li>35 Attack ≈ one +100 line.</li></ul> | [ALLY §6.5](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Divine stats | Wisdom > Destruction > Time > Death > Illusion > Justice > Freedom > Space > Life > Destiny | [ALLY §6.3](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Arcana (5 at Global launch) | <ul><li>Chalice of Vigor (Time): Focused Eye, Hunter's Resolve, Gale Arrow, Deadshot.</li><li>Parchment of Vigor (Life/Destiny): Drill Dart, Snipe, Burst Arrow, Tempest Shot.</li><li>Compass of Magic (Death/Freedom): Burst Arrow, Scattershot, Deadshot, Gale Arrow.</li><li>Bell of Magic (Destruction): Hunter's Resolve, Revitalization, Vigilant Eye, Rooting Eye.</li><li>Mirror of Magic (Illusion/Wisdom): Focused Eye, Hunter's Soul, Concentrated Fire, Unyielding, Melee Fire.</li></ul> Upgrade cards to +1/+2 and check, rather than forcing +5. | [ALLY ch.7](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) (skills), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) (god stats) |
| Pet Genus | ALLY: slot 4 PvE Damage Boost (Fera: Weapon Damage Boost; Varian: PvE / Front / Back; Special: Double Chance); slots 1/5 Max Attack; 7 PvE Damage Tolerance (Special: Damage Tolerance); 3/6/9 Accuracy / Crit, balanced. **This guide's [audit](../docs/genus-audit.md):** top Global Rangers are crit-capped (51%), so 3/6/9 go to Power Shard Damage Bonus once Accuracy is covered. See discrepancies. | [ALLY ch.5](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Genus audit](../docs/genus-audit.md) |
| Pantheon | <ul><li>Artworks: Illusion + Wisdom (+ Life).</li><li>Statues: Freedom, Death, Space.</li><li>Colossus: Zikel/Kromede in S1. Sirin reports the Kromede colossus was removed on Global.</li></ul> | [ALLY ch.8](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit), [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Wings | Save Season coins for Talisra wings (end of S1). Wing enhancing isn't on Global. | [ALLY §0.4, §6.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Theostones | No PvE impact | [ALLY §6.4](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |

[NM]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM buffs]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM classPerformance]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
