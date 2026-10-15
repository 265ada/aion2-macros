# Spiritmaster (精靈星) — DPS spec · AION 2 Global

**Patch covered:** Global client build **25926599** (Steam public branch, updated 2026-10-14 06:40 UTC). That is the [Oct 13 PDT / Oct 14 CEST patch](https://store.steampowered.com/news/app/3393110/view/1846651706673374) on top of the [Oct 6 PDT patch](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544) and the [Oct 8 PDT hotfix](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1). The Oct 13 notes list one Spiritmaster change: Summon: Ancient Spirit summons at "Level 15 or below" "did not activate skills properly", fixed in this patch. Nothing else changed for Spiritmaster. Build id: [SteamCMD](https://api.steamcmd.net/v1/info/3393110). NotMeter data (week of Oct 7–14) was recorded on the previous build 25800038. **Written:** 2026-10-13, **updated for the Oct 13 patch:** 2026-10-14.

**Tags:** [Global] · [KR/TW-confirmed] = Korean or Taiwanese source checked against the Global client · UNVERIFIED.

**Main data sources:**
- **SIRIN:** [Sirin's Spiritmaster Guide, written for Global](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), updated 14.10.2026. This is the main source.
- **NM:** [NotMeter Global ranking](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json), week of Oct 7–14. (NotMeter has since retired this generation, so the link returns 404; see the [README](README.md).) Top 20 Spiritmaster parses on each of 15 bosses: 300 parses from 133 players, median CP 141,212, median DPS 53,493.
- **DB:** [aion2.app Global client DB](https://aion2.app/db/skills?class=Elementalist), client dated 18.09.2026. In the DB, Spiritmaster is "Elementalist".
- **Sheet:** [Global class sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview).

**About SIRIN's specialty table.** Its skill names are icons, which the text export drops. Each row was first matched to a skill by its color order, then confirmed by an independent re-check against the doc's images: all 12 rows and all 6 stigma paragraphs match. Colors: green 1, blue 2, yellow 3, orange 4, red 5.

**Skill name:** SIRIN's "Destruction" is the stigma **Jointstrike: Destructive Attack** (its Global client name). It is not the Divine stat Destruction.

---

## 1. Overview

| Item | Recommendation / finding | Why | Source |
|---|---|---|---|
| Role | Ranged magic DPS that summons elemental spirits | NC: "commands the battlefield with elemental power" | [NC class list](https://aion2.plaync.com/en-us/about/index#classes) |
| Playstyle | <ul><li>Summon spirits to build elements, and fire **Elemental Fusion** at 4 stacks: 17.0% of damage.</li><li>Combustion 7.6% plus its Ashy Call chain 6.8%; Dimensional Control 7.5%.</li><li>The Ancient Spirit's attacks are about 15%.</li><li>A large share of damage comes from the spirits on their own.</li></ul> | | [NM], [SIRIN Rotation](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB Elemental Fusion](https://aion2.app/db/skills/16300000) |
| Strengths | <ul><li>"Fairly tanky", with heals and shields.</li><li>"Performs very well on high ping".</li><li>Low skill floor.</li></ul> | | [SIRIN About](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Weaknesses | <ul><li>**Ancient Spirit:** most damage hangs on it (90 s cooldown), and Global CDR (about 19–21% with best-in-slot gear) means "substantial downtime".</li><li>**Mana:** "mana intensive", so on Global use a mana pot at all times.</li><li>**Fixed Oct 13:** SIRIN reported Ancient Spirit below stigma level 15 not using its skill every 7 attacks and giving no Elemental Fusion. NC's Oct 13 notes list the fix for level 15 or below, one level wider than SIRIN's range. No parses after the patch exist yet to confirm it.</li></ul> | | [SIRIN Rotation, Stigmas](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Oct 13 patch notes](https://store.steampowered.com/news/app/3393110/view/1846651706673374) |
| PvE standing (Global) | **7th of 8.** NotMeter score 82.54; −5.6% at equal CP (7th; about −9% on the top-20 set alone, see the [README](README.md#overall-tier-list)). This data predates the Oct 13 Ancient Spirit fix. | Global CDR limits the Ancient Spirit | [NM classPerformance], [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| PvP standing | **UNVERIFIED.** SIRIN: "fairly middle of the pack in PvP though this could be different in season 1 on global". | | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Difficulty | **Low to medium.** "Fairly easy to play… low skill floor and a medium/average skill ceiling". | | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Who should play it | High-ping players; players who want a durable ranged class with simple inputs | | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

---

## 2. Max damage

### Single target (SIRIN's rules)

| Step | What to do | Why | Source |
|---|---|---|---|
| 1 | **Enhance: Spirit's Benediction** (+ Flame Blessing if slotted) **before** summoning the Ancient Spirit | Stats are snapshotted onto spirits when they're summoned. Benediction: +20% PvE Damage Boost and Tolerance for you and the spirit; +25% more at 20. | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16190000) |
| 2 | **Summon: Ancient Spirit** (90 s cooldown, lasts 30 s) | Each Ancient skill grants Four Elements, which means an Elemental Fusion | [DB](https://aion2.app/db/skills/16250000) |
| 3 | **Jointstrike: Corrode** | The target takes +10% damage from the spirit (+15% more at 5) for 20 s (+10 s at 20) | [DB](https://aion2.app/db/skills/16150000) |
| 4 | **Jointstrike: Destructive Attack**, max charge (if slotted) | Charge skill at 5 (up to +200%). 20 resets Curse and Corrode. | [DB](https://aion2.app/db/skills/16240000), [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| 5 | Cycle **Water → Earth → Wind → Fire** spirits | Builds element stacks for Fusion. Each summon enables Dimensional Control. | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB Dimensional Control](https://aion2.app/db/skills/16330000) |
| 6 | Weave **Cold Shock** (held), **Combustion**, **Dimensional Control**, **Jointstrike: Curse** | With specialty option 4, Cold Shock's Earth Tremor chain stacks +2% Attack up to 5 times. Element Unification stacks Crit Damage up to 5 times on landed spirit-skill hits. | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB Cold Shock](https://aion2.app/db/skills/16010000), [DB Element Unification](https://aion2.app/db/skills/16780000) |
| 7 | **Rapid Scattershot** at 16 during boss stagger | −1 s all cooldowns per hit, the way to shorten the Ancient Spirit's downtime on Global | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16340000) |

**Line up:** Benediction (10 s at every level) and Flame Blessing (10 s at level 1, 17 s at 15) cast right before the Ancient Spirit (30 s). On Global, Ancient Spirit and Benediction drift out of sync, because CDR is low ([SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). Stigma buff durations measured in Global parses ([NM](https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json)).

### AoE

| Tool | Targets | Source |
|---|---|---|
| Combustion, Curse, Corrode, Dimensional Control | up to 4 within 4 m | [DB](https://aion2.app/db/skills?class=Elementalist) |
| Fire / Wind Spirit skills | up to 4 within 5 m | [DB Fire](https://aion2.app/db/skills/16100000), [DB Wind](https://aion2.app/db/skills/16120000) |
| Elemental Fusion option 1 | becomes AoE | [DB](https://aion2.app/db/skills/16300000) |
| Wind Spirit | up to 4 within 5 m; in SIRIN's rotation since Oct 6 (the sheet calls it "mainly used for mobbing") | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |

**AoE order:** UNVERIFIED (no Global AoE test).

---

## 3. Macros

SIRIN gives three setups: Option 1 (in-game macro only), Option 2 (external software), and a 3-spirit version added Oct 10 for mana. She says Options 1 and 2 "perform similarly", with Option 2 slightly ahead ([SIRIN Rotation & Macros](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)). Her rows below are read from the doc's screenshots.

### Macro A: SIRIN Option 1, in-game macro only, 4 spirits (recommended)

**Hotbar stacks (row 0 is the face skill, fired first):**

| Hotbar key | Row 0 | Row 1 | Row 2 | Row 3 |
|---|---|---|---|---|
| Macro stack | Jointstrike: Corrode | Jointstrike: Curse | Dimensional Control | Combustion |
| Fusion key | Elemental Fusion | — | — | — |
| Spirit key | Summon: Water Spirit | Summon: Earth Spirit | Summon: Wind Spirit | Summon: Fire Spirit |
| Key 5 (buffs) | Enhance: Spirit's Benediction | Summon: Ancient Spirit | — | — |

**The in-game macro (held on right click)** has three entries, in order:
1. the Corrode / Curse / Dimensional Control / Combustion stack;
2. Elemental Fusion;
3. the spirit stack.

**Keys you press:**
- Left click: Cold Shock (held).
- Q: Jointstrike: Destructive Attack, charged by hand.
- E: Rapid Scattershot (stagger, at 16).
- R: Soul's Cry.
- Key 5: the buff stack. SIRIN's own key 5 repeat-press is a Razer macro, which is external software (see the ban row below). Pressing key 5 yourself works the same.

**Notes:**
- "Buffs are not part of the macro and cannot be." Hold Benediction until the Ancient Spirit is back up.
- Skill queue: on or off, your choice; test both.
- **3-spirit version** (less mana): Fire, Water and Earth plus Elemental Fusion on one key, and Wind on a second key.

**Global sheet rows (KR/TW):** the sheet's Spiritmaster screenshot shows Flame Blessing at level 25 and Corrode at 23, which a Global client can't show. Its rows are Korean/Taiwanese, so they aren't used here.

### Macro B: SIRIN Option 2, external software, skill queue OFF
Mouse software (Razer / G-Hub) fires Destructive Attack at max charge automatically. SIRIN warns it misfires when the frame rate drops. **Risk:** see below.

### Banned or nerfed on Global

| Item | Status | Source |
|---|---|---|
| In-game macro | Allowed | [SIRIN Disclaimer](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| External software (Option 2, the Razer key-5 repeat) | **Risk.** NC's unauthorized-program rule. The Oct 10, Oct 12 and Oct 14 ban waves listed "use of macros, bots or other unauthorized programs" under botting and gold farming. | [NC Operation Policy](https://www.plaync.com/policy/operation/aion2global), [Oct 10 notice](https://aion2.plaync.com/en-us/board/notice/view?articleId=6acaa7506b722c561dc6aae9), [Oct 12 notice](https://store.steampowered.com/news/app/3393110/view/1846018067943055) |
| Spiritmaster nerfs on Global | None. The Oct 13 patch only fixed the Ancient Spirit bug. | [Oct 13](https://store.steampowered.com/news/app/3393110/view/1846651706673374), [Oct 6](https://steamcommunity.com/games/3393110/announcements/detail/712288859283521544), [Oct 8](https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac7475738eb0528f90021b1) |

---

## 4. Stigmas

**Global rules:**
- 4 slots, cap 20; a fresh 45 has 32 shards, the AP cap allows about 20 shards a week, and resets are free ([SIRIN Stigmas](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).
- No rarity, so "n/a" ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

**Global usage (top 20 per boss):** Ancient Spirit 100%, Corrode 98%, Benediction 98% (median 10), Flame Blessing 87% (median 14, mode 15; level logged on 55 parses), Destructive Attack 11%, Siphon 1% ([NM]).

**4th slot: Destructive Attack vs Flame Blessing**
- **SIRIN:** "from early testing, Destruction [Destructive Attack] performs a bit better" than Flame Blessing.
- **Global parses, at equal CP:** Destructive Attack users (32 parses from only 14 players) were about 4% ahead of Flame Blessing users (116 players), averaged per player. The 95% range is −2% to +11%, so this is weak support ([NM], [method](README.md#method-notes)). Two of the 14 players provide 15 of the 32 parses.
- **Recommendation:** **Destructive Attack** (Sirin's testing is the main basis), with Flame Blessing as the alternative most players still run.

### PvE

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Summon: Ancient Spirit | Slot 1 | **15**, then 20 | n/a | <ul><li>"The biggest source of your damage."</li><li>SIRIN's "15 ASAP" was a workaround for a Global bug that the Oct 13 patch fixed. 15 is still the first big step.</li><li>15: skill after 5 attacks.</li><li>20: +20% spirit stats.</li></ul> | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16250000) |
| Enhance: Spirit's Benediction | Slot 2 | **10**, then 20 (the first to 20 late) | n/a | <ul><li>"Your main buff… never take off your hotbar."</li><li>10: ×1.5 Spirit Strike.</li><li>20: +25% PvE Damage Boost and Tolerance.</li><li>Global median 10.</li></ul> | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16190000), [NM] |
| Jointstrike: Corrode | Slot 3 | **5**, then **20** | n/a | "All or nothing": 5 (+15% spirit damage taken), then straight to 20 (+10 s duration) | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16150000) |
| Jointstrike: Destructive Attack (SIRIN: "Destruction") | Slot 4 (damage) | **10** early, **19** late | n/a | <ul><li>Charged at 5; "number 1 stagger skill".</li><li>SIRIN stops at 19, to avoid cancelling a bugged double hit seen in KR/TW, "if it gets fixed" otherwise.</li></ul> | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16240000) |
| Flame Blessing | Slot 4 alternative | **15** (minimum if used) | n/a | <ul><li>"If you are going to use this it needs to be at least lvl 15."</li><li>15: +10% Crit Damage Boost.</li><li>20: −50% proc cooldown.</li></ul> | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16370000) |
| Siphon | Survival option | **15** | n/a | 30% max-HP shield at 15. "You won't really have space for this." | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16060000) |

**Shard order (SIRIN):**

| Stage | Stigma levels |
|---|---|
| Early | Ancient Spirit 15, Corrode 5, Benediction 5, Destructive Attack 5–10. SIRIN's reason for Ancient 15, a Global bug, was fixed on Oct 13. |
| Mid | Ancient Spirit 15–20, Corrode 5, Benediction 10, Destructive Attack 15 |
| Late (all to 20) | Benediction 20 → Ancient Spirit 20 → Corrode 20 → Destructive Attack (19) |

Source: [SIRIN Leveling Priority](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit).

### PvP (SIRIN's Global suggestions; Benediction and Ancient Spirit are fixed)

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Enhance: Spirit's Benediction | Fixed | 20 | n/a | "Non-negotiable" | [SIRIN PvP](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Summon: Ancient Spirit | Fixed | 20 | n/a | "Non-negotiable" | same |
| Kaisinel's Power + Command: Proxy | General option | 20 | n/a | Status effect chance and resist, plus survival | same |
| Corrode + Destructive Attack | Burst option | 20 | n/a | "Corrode into Destruction into Corrode can be really deadly" | same |
| Siphon + Proxy | Defensive option | 20 | n/a | Self-heal and shield | same |
| Seize Magic + Command: Proxy | Buff removal / CC | 10+ | n/a | Strips buffs; seals from 10 | same, [DB](https://aion2.app/db/skills/16230000) |
| Flame Blessing | **Not recommended** for PvP (SIRIN) | — | n/a | Listed in SIRIN's "not recommended" row | same |

SIRIN: "Predicting how PvP will play out during season 1 on global is impossible", so all PvP picks are low confidence.

### Solo
Siphon (15) in place of the 4th slot, for survival ([SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)).

---

## 5. Skills

**SIRIN:**
- Spiritmaster "only really needs 2 skills at level 20". Season 1 limits are 4–5 gear lines and 5 Arcana.
- 16 priority with Arcana and rings: **Combustion, Elemental Fusion, Rapid Scattershot**.
- Cold Shock 20 and Fire Spirit 20 are optional.

Specialty breakpoints are 8 / 12 / 16 / 20 ([Bible ch.4](https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview)).

### Actives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Combustion | 1st | **20** (16 = Ashy Call chain) | n/a | 7.6% + 6.8% Ashy Call. 70% of top Global at 16+. | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NM] |
| Elemental Fusion | 1st | **20** (16 first) | n/a | 17.0%. 50% at 16+. | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NM] |
| Rapid Scattershot | 16 priority | **16** | n/a | −1 s all cooldowns per hit, "crucial early" | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Summon: Fire Spirit | 16–20 | **16** (20 optional) | n/a | Fire Spirit skill + basic attacks ≈ 10.8%. 34% at 16+. | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NM] |
| Cold Shock | 16–20 | **16** (20 for its passive healing) | n/a | Held; Attack stacks | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Summon: Water / Earth / Wind Spirit | 14–16 | **16** for option 5 (+20% stats) | n/a | Wind Spirit is now in the rotation (SIRIN, Oct 6). 14–25% of top Global players who run them have 16+. | [SIRIN changelog](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NM] |
| Jointstrike: Curse | 12–14 | **12** | n/a | 3.0% + Curse. 3+4 (49% Global). The sheet says 16–20. | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NM] |
| Dimensional Control | 12–14 | **12** (sheet 16) | n/a | 7.5%. 0% of top Global past 12. | [NM], [Sheet](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Soul's Cry | 12–14 | **12** | n/a | In SIRIN's 12–14 group, and on her R key in all three layouts. 53 of 300 top Global parses use it. | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NM] |
| Defiance | CC break | **12** (SIRIN 12–14; the sheet says 16) | n/a | | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

### Passives

| Item | Recommendation | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Spirit Strike | S | as high as possible (KR top-20 median 36, [NotMeter KR](https://notmeter.com/?view=setup-guide), KR/TW context) | n/a | PvE Damage Boost and Perfect for you and the spirit; ×1.5 at Benediction 10 | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16710000) |
| Mental Focus | S | as high as possible (KR 32, KR/TW context) | n/a | Double Chance | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16760000) |
| Element Unification | A | **16+** (Global median 16; KR 29, KR/TW context) | n/a | Stacking Crit Damage Boost | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NM buffs] |
| Spirit Revitalization | A | as gear allows (KR 22, KR/TW context) | n/a | Faster summon cooldowns | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [DB](https://aion2.app/db/skills/16750000) |
| Corrode (passive) | Arcana line on the Mirror | as gear allows | n/a | +100 Crit and a 50% proc on crits. 3.9% of top Global damage, more than the Jointstrike: Corrode stigma's 0.7%. | [DB](https://aion2.app/db/skills/16740000), [NM] |
| Others | B–C | **14–16** | n/a | "Will most likely sit at level 14-16" | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

---

## 6. Specializations

SIRIN's color priorities (matched to skills as described in the header), checked against Global picks:

| Item | Recommendation (SIRIN → picks at 8 / 12 / 16 / 20) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Cold Shock | Orange > Yellow > Blue (if 20 or for survival): 3 / **3+4** / 3+4 / 2+3+4 | 16 | n/a | 4: +2% Attack per Earth Tremor (5 stacks). Global 3+4 74%. | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NM] |
| Combustion | Red > Orange > Blue: 2 / 2+4 / **4+5** / 2+4+5 | 20 | n/a | 5: Ashy Call chain. 4: +20% skill speed. Global 4+5 52%. | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NM] |
| Summon: Fire Spirit | Blue > Red > Yellow (if 20 or under 16): 2 / **2+3** / 2+5 / 2+3+5 | 16–20 | n/a | Global 2+3 62%, 2+5 26% | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NM] |
| Summon: Water Spirit | Blue > Red > Yellow (if under 16): 2 / 2+3 / **2+5** | 16 | n/a | Global 2+3 58%, 2+5 20% | same |
| Summon: Earth Spirit | Red > Yellow > Blue (if under 16): 3 / 2+3 / **3+5** | 16 | n/a | Global 2+3 34%, 3+5 20% | same |
| Summon: Wind Spirit | Blue > Red > Yellow (if under 16): 2 / 2+3 / **2+5** | 16 | n/a | Global 2+3 57% | same |
| Elemental Fusion | Red > Blue > Yellow: 2 / 2+3 / **2+5** / 2+3+5 | 20 | n/a | <ul><li>5: 25% chance to keep Four Elements.</li><li>SIRIN leaves option 4 (charge skill) out. This guide's reading: a macro would fire it uncharged.</li><li>Global, among parses where the picks are readable (175): 3+5 46%, 2+3 24%, 2+5 14%, 2+3+5 12%.</li></ul> | same, [DB](https://aion2.app/db/skills/16300000) |
| Dimensional Control | Blue > Yellow: 2 / **2+3** | 12 | n/a | Global 2+3 95% where both picks are readable (61 of 64 players). Many logs only show option 2. | same |
| Jointstrike: Curse | Orange > Yellow: 3 / **3+4** | 12 | n/a | Global 49% | same |
| Rapid Scattershot | Red > Orange: — / 4 / **4+5** | 16 | n/a | 5: −1 s all cooldowns | same |
| Soul's Cry | Orange > Yellow: 3 / 3+4 | — | n/a | Korea 3+4 | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [NotMeter KR](https://notmeter.com/?view=setup-guide) |
| Defiance | Yellow > Orange: 3 / **3+4** | 12 | n/a | | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

PvP specialty changes are UNVERIFIED; SIRIN gives none.

### Daevanion boards (Global; SIRIN)

| Item | Recommendation | Target | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Points | About 316 at 45 after the Monolith, Sealed Dungeons and side quests; +50 Shugo Festival, +50 Nightmare (416) | — | n/a | | [SIRIN Daevanion](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Order | <ol><li>All blue and green nodes first.</li><li>Then orange damage nodes: Combat Speed, CDR, Damage Boost, Crit Damage Boost, Multi-hit.</li><li>Then white Attack and Crit.</li></ol> | — | n/a | | same |
| Azphel (PvP) | 36 points from the Abyss Monolith feathers; more from the Abyss Trade Shop | — | n/a | | same |
| Global changes | <ul><li>Orange % 2.5 → 1.5; Attack 5 → 3; Crit 10 → 5; Defense 50 → 30.</li><li>Ariel removed; Azphel reduced.</li><li>About 200 fewer points.</li></ul> | — | n/a | | same |

SIRIN's example Global boards (Nezekan, Zikel, Vaizel, Triniel, Azphel) are images; open the doc for the tile layout.

---

## 7. Tier list

| Content | Tier | Placement reason | Source |
|---|---|---|---|
| PvE | **B−** (7th of 8) | NotMeter score 82.54; −5.6% at equal CP. Held back by Global CDR on the Ancient Spirit. | [NM classPerformance], [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| PvP | **UNVERIFIED** (SIRIN: middle of the pack) | | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Solo / leveling | **A (opinion)** | Tanky, heals and shields, spirits deal damage while you move | [SIRIN About](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

---

## 8. Gear (SIRIN's Global soulbind priorities, updated Oct 12)

Global gear rules ([SIRIN Equipment](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit)):
- **No Heroic gear in Season 1**, so **Unique is the settle rarity** for every slot.
- PvE crafted gear is best in slot at 5 lines. Dungeon gear has 4; an extendable weapon has 3.
- Only T1 crafted gear is directly craftable on Global; it's bound and upgrades by Transfer Crafting.
- PvE Damage Boost was removed from weapons, guards and accessories.
- Some soulbind values were lowered, and base stats were raised.

| Item | Recommendation (stat lines in order) | Target level | Settle rarity | Why | Source |
|---|---|---|---|---|---|
| Weapon (orb) | Combat Speed > Weapon Damage Boost > Damage Boost > Might > Precision > Multi-hit > Attack (PvP: Status Effect Chance) | **+17** (the sheet's Ludra-prep target) | Unique | Enhance levels come from the sheet's roadmap; SIRIN gives none | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Sheet roadmap](https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview) |
| Guard | Same as the weapon | **+17** | Unique | | same |
| Head | Double Chance > Attack Increase > Attack > Spirit Strike > Mental Focus > Element Unification > Spirit Revitalization | **+15** | Unique | | [SIRIN](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Chest | Damage Boost > Perfect > Attack > Spirit Strike > Mental Focus > Element Unification > Spirit Revitalization | **+15** | Unique | | same |
| Pants | Attack Increase > Damage Tolerance > Perfect > Attack > Spirit Strike > Mental Focus > Element Unification | **+15** | Unique | | same |
| Cloak | Double Chance > Attack Increase > Attack > Spirit Strike > Mental Focus > Element Unification > Spirit Revitalization | **+15** | Unique | Perfect was removed from capes on Global | same |
| Shoulders | Double Chance > Crit Damage Boost > Attack > Spirit Strike > Mental Focus > Element Unification > Spirit Revitalization | **+15** | Unique | | same |
| Gloves | Combat Speed > Perfect > Attack > Spirit Strike > … | **+15** | Unique | | same |
| Shoes | Move Speed > Perfect > Attack > Spirit Strike > … | **+15** | Unique | | same |
| Earring | Move Speed > Might > Precision > Spirit Strike > Mental Focus > Element Unification > Spirit Revitalization | **+16** | Unique | | same |
| Necklace | Combat Speed > Spirit Strike > Mental Focus > Element Unification > Spirit Revitalization > Attack | **+16** | Unique | Combat Speed / Might / Precision on necklaces are new on Global | same |
| Ring | Might > Precision > active skills (whichever levels you're missing; drop Precision first if short on space) | **+17** | Unique | | same |
| Bracelets | Story Unique + side-quest blue for now, Sanctuary later. Wisdom > Destruction > Time > Illusion > Justice > Death/Freedom. | **+15** | Unique (slot 1); Epic / blue (slot 2) | Sanctuary bracelets can be amplified for +5% Attack | same, [Sirin](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Belt / Amulet | To Gold | Gold | Gold | | [Allyria §6.1.1](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |
| Clash Runes | | **+5 to +7** | n/a | They can break | [Allyria §6.1.6](https://docs.google.com/document/d/1GwcOMFMMJj9eHrsYp-OVtddBxfQhNOjAzmV1eOkmiAk/edit) |

| Other | Recommendation | Source |
|---|---|---|
| Arcana (5 cards) | <ul><li>Chalice of Vigor (Time): Combustion, Elemental Fusion, Cold Shock / Fire Spirit, Spirit Strike.</li><li>Parchment of Vigor (Life): Elemental Fusion, Cold Shock, Fire Spirit, Earth Spirit.</li><li>Compass of Magic (Death): Combustion, Rapid Scattershot, Water Spirit, Wind Spirit (SIRIN corrected this row on Oct 14; it used to read Fire Spirit and Earth Spirit).</li><li>Bell of Magic (Destruction): Spirit Strike, Element Unification, Spirit Revitalization.</li><li>Mirror (Wisdom, or **Illusion in S1** for Ancient Spirit's cooldown): Mental Focus, Corrode (the passive).</li></ul> | [SIRIN Arcana](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Divine stats | 10 Divine = 1% on Global (halved) | [SIRIN Stats](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Wings | <ul><li>Early: Vakron Sky Garden cube drop.</li><li>Mid: Nightmare Trade Shop.</li><li>Late: **Talisra** from the Season Shop (CDR, "very important").</li><li>Wings can't be enhanced in S1.</li></ul> | [SIRIN Wings](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Pet Genus | <ul><li>**SIRIN, line 4 by board:** Cogni Crit Damage Boost > Damage Boost > PvE Damage Boost; Fera Weapon Damage Boost > Damage Boost > PvE Damage Boost; Natura PvE Damage Boost > Perfect > Multi-hit; Varian Back Damage Boost > PvE Damage Boost; Special Double Chance.</li><li>**This guide's [genus audit](../docs/genus-audit.md)** (Global client tables) ranks PvE Damage Boost first on Cogni, Fera, Natura and Varian. See [discrepancies](discrepancies.md).</li><li>**Lines 3/6/9 (SIRIN):** Accuracy > Critical Hit > Power Shard Damage Bonus once capped.</li><li>**Other lines:** 1/5 Max Attack > Attack Bonus; 2/8 HP increase; 7 Damage Tolerance > PvE Damage Tolerance.</li><li>Aim for 2.5%+ rolls on Double Chance / Damage Boost, and don't min-max the first preset.</li></ul> | [SIRIN Genus](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit), [Genus audit](../docs/genus-audit.md) |
| Pantheon | <ul><li>Divine stats halved.</li><li>Kromede colossus removed; use the Nightmare Trade Shop colossus.</li><li>Statues: 10 Draupnir clears, all Kibelisks.</li><li>Paintings: 5 Sanctuary clears, dungeons, world bosses.</li></ul> | [SIRIN Pantheon](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |
| Titles | Global removed Double Chance from titles and cut Combat Speed / CDR about 30%. Late offensive title: Mastered Genus Insight (level 10 on all boards). | [SIRIN Titles](https://docs.google.com/document/d/16RBdqrTCKJ4TZJNEkYri9hLYcMv-Hle2pW6HXSNCX7c/edit) |

[NM]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM buffs]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
[NM classPerformance]: https://not4you-dev.github.io/NotMeter-Cache/g/7a95660ba62a7ef4/data/notmeter-global-ranking.json
