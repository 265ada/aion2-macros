"""One-off data update (2026-09-29): Full rotation tab, key stacks, Gladiator fix, cross-check alts."""
import json

ROOT = __file__.rsplit("tools", 1)[0]
S = json.load(open(ROOT + "data/skills.json", encoding="utf-8"))
S["Empyrean Lord's Punishment"]["mp"] = 200
open(ROOT + "data/skills.json", "w", encoding="utf-8").write(json.dumps(S, ensure_ascii=False, indent=0))

p = ROOT + "data/macros.json"
M = json.load(open(p, encoding="utf-8"))
C = {c["id"]: c for c in M["classes"]}
N = None
IV = "https://www.inven.co.kr/board/aion2/"

# ---- late-card corrections / held-key stacks ----
g = C["gladiator"]["late"]
g["keys"] = [
    {"label": "Overhead Slam key (mash)", "stack": ["Rage Burst", "Lifestealing Blade", "Overhead Slam", N]},
    {"label": "Buff key (press yourself)", "stack": ["Lunge Stance", "Zikel's Blessing", "Wave Armor", N]},
]
g["hold"] = ["Keen Strike", "Macro key", "Overhead Slam key (mash)"]
g["manual"] = ["Ruinous Blow", "Lunge Stance", "Zikel's Blessing", "Wave Armor", "Leaping Slam"]
g["tip"] = ("Opener: buffs → Ruinous Blow (Prepare for Battle) → start weaving. Rage Burst and Lifestealing Blade sit under "
            "Overhead Slam on the mashed key, so they fire the moment they're ready. Press Lunge Stance, Zikel's Blessing and "
            "Wave Armor yourself so they aren't wasted during mechanics or on trash (both the top-end and comfort layouts in the "
            "9/5 guide do this). Aerial Snare under Overhead Slam adds DPS. Aim for ~97–102 Upward Strike hits per minute. "
            "Rending Blow and Overhead Slam go to 20. Passives: Experienced Counterstrike and Murderous Burst first.")
g["src"] = "Inven 9/5 (image-verified) + 8/26, matches TW 5/27"

so = C["sorcerer"]["late"]
so["keys"] = [{"label": "Hellfire key (hold)", "stack": ["Delayed Explosion", "Hellfire", "Winter's Shackles", "Flame Scattershot"]}]
so["hold"] = ["Flame Arrow", "Macro key", "Hellfire key (hold)"]
so["why"] = ("Only one macro line: Sorcerer loses the most damage of any class from a second line. The held Hellfire key "
             "reproduces the manual timing. Delayed Explosion goes first, Hellfire follows fully charged, then Winter's Shackles, "
             "and Flame Scattershot sits at the top so its stagger cancel fires on its own. That key's stack is from the Aug 27 "
             "top-DPS post; the Sep 22 guide describes the same key.")
so["src"] = "Inven 9/22 + 8/27 (image-verified, identical main line)"

ch = C["chanter"]["late"]
ch["keys"] = [{"label": "Buff key (press yourself)", "stack": ["Power of the Storm", "Guardian Blessing", N, N]}]
ch["tip"] = ("Stack Guardian Blessing on top of Power of the Storm so it never gets forgotten. That frees keys for Undefeated "
             "Mantra and Sprint Mantra, which are toggle skills that must never go in a macro, because a second press switches "
             "them off. Marchutan's Wrath is no longer required, so swap in a utility stigma or Fracturing Blow. Dark Crush and "
             "Onslaught go to 20, and Spinning Strike and Recuperation are close behind. Passives: Wind's Promise, Impact Hit, "
             "Attack Preparation.")

C["ranger"]["late"]["queue"] = ("OFF in both 9/6 setups; a 9/3 tester prefers ON (buffs press instantly) and saw little DPS "
                                "difference.")

C["spiritmaster"]["late"]["alts"].insert(0, {
    "t": "Inven 8/13 alternative (skill queue OFF)",
    "s": ("A different tested approach: skill queue OFF so the macro skills always win, Elemental Fusion and the spirits in "
          "the in-game macro, Curse / Dimensional Control / Combustion mashed by mouse software, and Corrode kept out (it "
          "fires on trash and scrambles cooldowns). Opener: hold macro → Corrode → wait for party buffs (Power of the Storm, "
          "Fury, Earth Punishment) → Flame Blessing → Spirit's Benediction → Ancient Spirit → Destructive Attack → Corrode."),
    "macros": [["Elemental Fusion", N, N, N], ["Summon: Water Spirit", "Summon: Earth Spirit", "Summon: Fire Spirit", N]],
    "hold": ["Cold Shock", "Macro key"]})
C["assassin"]["late"]["alts"].append({
    "t": "Two more Assassin players, Sep 28",
    "s": ("Both use the same single macro slot: Insignia Explosion → Heart Gore → Savage Roar. One holds left click (Quick "
          "Slice) + the macro; the other also mashes Storm Rampage and Ambush on their own keys."),
    "macros": [["Insignia Explosion", "Heart Gore", "Savage Roar", N]], "hold": ["Quick Slice", "Macro key"]})
C["cleric"]["late"]["alts"].append({
    "t": "Inven 8/26 cross-check",
    "s": "A separate player: taking Debilitating Mark out of the Condemnation macro raised DPS, which matches the 9/24 guide.",
    "macros": [["Earth Punishment", "Divine Aura", "Condemnation", "Chain of Torment"]]})

# ---- NEW: full rotation macros ----
F = {}
F["assassin"] = {
    "src": "Built from the Inven 9/18 layout's buff keys (the macro line is the tested one)", "link": IV + "6449/23617",
    "macros": [["Insignia Explosion", "Heart Gore", "Savage Roar", N],
               ["Illusive Clone", "Savage Fang", "Triniel's Dagger", "Assault Ambush"]],
    "hold": ["Quick Slice", "Macro key"], "manual": ["Ambush", "Storm Slice", "Shadowstrike"],
    "why": ("Line 1 is the tested damage line. Line 2 fires your burst skills in the order that feeds it: Illusive Clone removes "
            "Heart Gore's cooldown for 10 s, Savage Fang engraves 5 Insignias so the next Insignia Explosion hits at full stacks, "
            "then Triniel's Dagger (+10% back damage at 25) and Assault Ambush."),
    "loss": ("Heart Gore is checked every other loop instead of every loop, and burst buffs also fire on trash or during "
             "mechanics. Expect a few percent lower DPS than the 1-line setup (for scale, a second line cost Gladiator 5–6% of "
             "its main hits)."),
    "tip": "Keep Ambush and Storm Slice out of the macro and press them yourself; the source found Ambush in any line lowers hits."}
F["cleric"] = {
    "src": "Inven 9/24 two-line option (rows 1–2 of each line are from the guide)", "link": IV + "6452/29213",
    "macros": [["Condemnation", "Chain of Torment", N, N],
               ["Earth Punishment", "Divine Aura", "Noble Aura", "Prayer of Amplification"]],
    "hold": ["Earth's Retribution", "Macro key", "Lightning Strike Scattershot"],
    "manual": ["Bolt", "Healing Light", "Radiant Recovery", "Debilitating Mark", "Judgment Thunder"],
    "why": ("The 9/24 guide splits Condemnation → Chain of Torment and Earth Punishment → Divine Aura into two lines and leaves "
            "the empty rows for 'skills you want automatic'. Noble Aura (a 5-minute summon) and Prayer of Amplification (party "
            "damage buff, stronger since Aug 26) fill them, so your whole damage kit plus two buffs run from one key."),
    "loss": ("Cleric loses almost nothing from a second line because its attack speed caps at 94.4%, so this is the cheapest "
             "full rotation of any class. Prayer of Amplification is best saved for burst windows, so it's the part you give up "
             "by automating."),
    "tip": "Keep Bolt manual so a charge never delays a heal, and keep heals on their own keys."}
F["sorcerer"] = {
    "src": "Inven 8/27 top-DPS post (image-verified: both lines exactly as shown)", "link": IV + "6453/16644",
    "macros": [["Bittercold Wind", "Blaze", "Firestorm", "Wish of Concentration"],
               ["Element Enhancement", "Fire Wall", "Cold Storm", N]],
    "keys": [{"label": "Hellfire key (hold)", "stack": ["Delayed Explosion", "Hellfire", "Winter's Shackles", "Flame Scattershot"]}],
    "hold": ["Flame Arrow", "Macro key", "Hellfire key (hold)"], "manual": ["Frost"],
    "why": ("The author's own setup: line 2 automates Element Enhancement and both ground AoEs. Since a patch shortened their "
            "animations, they say it's fine to keep the Element Enhancement line in the macro rather than pressing it."),
    "loss": ("Sorcerer is the class that loses the most per extra line. The AoE line can also fire before the Delayed Explosion "
             "and Winter's Shackles buffs are up (a 9/20 player saw exactly this), and ground AoEs are wasted when the boss moves."),
    "tip": ("Opener: Element Enhancement → Delayed Explosion → full-charge Hellfire → Fire Wall → Cold Storm → macro on. The "
            "author notes the Hellfire key sometimes gets stuck, so tap it again if it stops.")}
F["templar"] = {
    "src": "Inven 9/17 one-click setup (both stacks image-verified)", "link": IV + "6438/26762",
    "macros": [["Judgment", "Warding Strike", "Doom Shield", "Shield Smite"],
               ["Annihilate", "Noble Armor", "Battlefield Banner", "Empyrean Lord's Punishment"]],
    "hold": ["Vicious Strike", "Macro key"], "manual": ["Punishment", "Taunt", "Shield of Protection", "Poach", "Shield Rush"],
    "why": ("Line 1 is the Vicious Strike → Judgment damage line; Shield Smite and Doom Shield keep Judgment lit (Judgment now "
            "opens after any shield attack). Line 2 adds Annihilate plus your buffs: Noble Armor (2 min since Sep 16), "
            "Battlefield Banner and Empyrean Lord's Punishment. The author says line 2 works in the macro, but mashing it on its "
            "own key did slightly better."),
    "loss": ("Another Templar (Aug 28) notes that automating Banner and Empyrean Lord's Punishment costs speed and can overlap a "
             "Chanter's Power of the Storm. Press them yourself in groups if you want the top number."),
    "tip": "Skill queue ON for this setup. Charge Punishment yourself (or bind it to a mouse key)."}
F["chanter"] = {
    "src": "Inven 9/3 full-auto test (lines 1–2 image-verified) + 9/17 buff stack", "link": IV + "6451/22314",
    "macros": [["Dark Crush", "Spinning Strike", "Marchutan's Wrath", "Incandescent Blow"], ["Impactful Crush", N, N, N],
               ["Power of the Storm", "Guardian Blessing", N, N]],
    "hold": ["Onslaught", "Macro key", "Gust Rampage"], "manual": ["Undefeated Mantra", "Sprint Mantra", "Recuperation", "Rushing Smash"],
    "why": ("Lines 1–2 are the '100% in-game macro' setup a 900k Chanter built so nothing needs pressing: splitting Impactful "
            "Crush out stops the three Dark Crush openers from overlapping (+3–5 Dark Crush/min). Line 3 adds the 9/17 guide's "
            "buff stack so Power of the Storm and Guardian Blessing run themselves."),
    "loss": ("Three lines means each slot is checked a third of the time. Power of the Storm is a party burst buff, so "
             "automating it can waste it outside burst windows, and in the Abyss 'Battlefield Might' replaces it during boss fights."),
    "tip": "Never macro Undefeated or Sprint Mantra: they're toggles, and a second press switches them off."}
F["gladiator"] = {
    "src": "Inven 9/5 guide, 'comfort' layout (image-verified)", "link": IV + "6448/31551",
    "macros": [["Rage Burst", "Lifestealing Blade", "Sword Aura Rampage", "Rending Blow"]],
    "keys": [{"label": "Overhead Slam key (mash)", "stack": ["Lunge Stance", "Zikel's Blessing", "Wave Armor", "Overhead Slam"]}],
    "hold": ["Keen Strike", "Macro key", "Overhead Slam key (mash)"], "manual": ["Ruinous Blow", "Leaping Slam"],
    "why": ("The guide's own comfort setup: every stigma fires by itself. Rage Burst and Lifestealing Blade lead the macro line, "
            "and the buffs sit under Overhead Slam on the mashed key, which the guide says makes them turn on faster than a "
            "second macro line would."),
    "loss": ("The guide recommends pressing stigmas yourself for the top number, because automated buffs get wasted during "
             "mechanics and on trash. Adding the buffs as a second macro line instead costs even more (a second line cost 5–6% "
             "of Overhead Slam hits in an Aug 12 test)."),
    "tip": "Start fights with Ruinous Blow for Prepare for Battle, then hold."}
F["spiritmaster"] = {
    "src": "Inven 9/16 lines + the 9/06 player's buff stack", "link": IV + "6454/10286",
    "macros": [["Jointstrike: Corrode", "Jointstrike: Curse", "Dimensional Control", "Combustion"],
               ["Summon: Water Spirit", "Summon: Earth Spirit", "Summon: Wind Spirit", "Summon: Fire Spirit"],
               ["Elemental Fusion", N, N, N], ["Enhance: Spirit's Benediction", "Flame Blessing", N, N]],
    "hold": ["Cold Shock", "Macro key"], "manual": ["Summon: Ancient Spirit", "Jointstrike: Destructive Attack", "Rapid Scattershot"],
    "why": ("Everything except the timing-sensitive burst runs from one key: debuffs, all four spirits, Fusion and your two "
            "self-buffs. Ancient Spirit and Destructive Attack stay manual because the guide times them (Ancient Spirit after "
            "Earth Tremor 4–5 stacks, Destructive Attack 3–4 s later)."),
    "loss": ("Elemental Fusion in the macro tested lower than mashing it on its own key (9/16), and four lines spread the loop "
             "thin. Another tested guide (8/13) keeps Corrode out because it fires on trash and scrambles cooldowns."),
    "tip": "Fight from about 3 m. If Fusion stacks feel slow, pull line 3 back out and tap Fusion yourself; that recovers most of the loss."}
F["ranger"] = {
    "src": "Inven 9/6 lines (image-verified) + 8/30 buff line", "link": IV + "6450/19104",
    "macros": [["Griffon Arrow", "Explosive Arrow", "Arrow Scattershot", "Tempest Shot"],
               ["Gale Arrow", "Burst Arrow", "Drill Dart", "Snare Shot"],
               ["Vaizel's Authority", "Supporting Fire", "Bow of Blessing", N]],
    "hold": ["Snipe", "Macro key", "Deadshot"], "manual": ["Marking Shot"],
    "why": ("Lines 1–2 are the tested Tempest Shot cancel setup. Line 3 is the buff line an Aug 30 Ranger runs in their one-click "
            "setup (Vaizel's Authority → Supporting Fire → Bow of Blessing). They measured no real DPS difference against the "
            "tuned 28-Deadshot setup on the dummy."),
    "loss": ("A Sep 3 Ranger warns that buffs in the macro can drop Snipe below 16–18 hits/min. Check Snipe on the dummy, and if "
             "it drops, press the buffs yourself."),
    "tip": "Cast Marking Shot yourself while standing still, refreshing it with ~2 s left."}
for k, v in F.items():
    C[k]["full"] = v

M["meta"]["updated"] = "2026-09-29"
M["changelog"].insert(0, {"date": "2026-09-29", "text": (
    "New 'Full rotation' tab for all 8 classes: longer macros with buffs, each with its source and the DPS trade-off. Held/mashed "
    "key stacks are now drawn on cards. Gladiator corrected (Rage Burst and Lifestealing Blade sit under Overhead Slam). Level-25 "
    "augments corrected for 8 stigmas changed after July. KR/TW cooldowns for Warding Strike, Spinning Strike and Impactful "
    "Crush. Zikel's Blessing and Lunge Stance icons fixed (swapped in the database).")})
open(p, "w", encoding="utf-8").write(json.dumps(M, ensure_ascii=False, indent=1))

miss = set()
for c in M["classes"]:
    for m in ("late", "early", "full"):
        d = c.get(m) or {}
        stacks = d.get("macros", []) + [k["stack"] for k in d.get("keys", [])] + [s for a in d.get("alts", []) for s in a["macros"]]
        for st in stacks:
            for x in st:
                if x and x.rstrip("?") not in S:
                    miss.add(x)
print("missing:", miss or "none")
