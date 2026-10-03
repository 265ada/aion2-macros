"""2026-10-02: apply the Global class sheet ('Personal Aion 2 Class Info', zxcastform) to macros, stigma builds and specs.

Macros: each class's Late game card becomes the sheet's Global-client layout (decoded from its screenshots, icon-matched
against the game database); the previous Korea/Taiwan card moves to Other versions. Early game cards no longer use stigmas
(slots open at 22 / 27 / 32 / 37). Gladiator gets a leveling line (Overhead Slam only hits knocked-down targets before
Rage Burst, so Mocking Blade sets it up). Stigmas: the Global main build follows the sheet's 4 picks and order.
Specs: picks from the sheet's skill priority; the Korean optimizer pick is kept in the note when it differs.
Run once (changelog).
"""
import json

SHEET = "https://docs.google.com/spreadsheets/d/1lbHaVairHaz26M8XGNF9CBWqiiHHBM6CylTwNKnlOug/htmlview"
SRC = "Global class sheet (zxcastform), Global-client screenshot"
M = json.load(open("data/macros.json", encoding="utf-8"))
ST = json.load(open("data/stigmas.json", encoding="utf-8"))
CL = json.load(open("data/classes.json", encoding="utf-8"))
MC = {c["id"]: c for c in M["classes"]}
SC = {c["id"]: c for c in ST["classes"]}

def demote(cid, title):
    """Move the current late card into alts (first) and return the alts list."""
    old = MC[cid]["late"]
    alt = {"t": title, "s": (old.get("why") or "") + (" " + old["tip"] if old.get("tip") else ""), "macros": old["macros"],
           "delays": old.get("delays"), "hold": old.get("hold"), "extra": old.get("keys") or []}
    alt = {k: v for k, v in alt.items() if v}
    return [alt] + old.get("alts", [])

def late(cid, **kw):
    alts = kw.pop("alts")
    MC[cid]["late"] = {"src": SRC, "link": SHEET, **kw, "alts": alts}

# ---------- Sorcerer ----------
late("sorcerer",
     macros=[["Blaze", "Firestorm", "Winter's Shackles", "Frost Burst"]], delays=[10],
     hold=["Flame Arrow", "Macro key"],
     manual=["Element Enhancement", "Delayed Explosion", "Hellfire", "Fire Wall", "Cold Storm", "Bittercold Wind", "Wish of Concentration", "Frost"],
     keys=[{"label": "Key 1 (press yourself)", "stack": ["Element Enhancement", "Delayed Explosion", None, None]},
           {"label": "Key 3 (press yourself)", "stack": ["Fire Wall", "Cold Storm", None, None]},
           {"label": "Key 4 (press yourself)", "stack": ["Bittercold Wind", "Wish of Concentration", None, None]}],
     queue="Not stated in the sheet, so test both",
     why="The Global sheet's layout, taken from Est's Sorcerer guide (updated Oct 2). The macro on right click only handles the filler. Blaze and Firestorm go on cooldown, and every Firestorm fireball cuts Hellfire's cooldown by 2 s. Winter's Shackles and Frost Burst fire when they're ready. Flame Arrow, held on left click, fills every gap and gives back MP. Everything that decides your burst stays on keys you press, so it lines up: Element Enhancement + Delayed Explosion on key 1, Hellfire on key 2, Fire Wall + Cold Storm on key 3, and Bittercold Wind + Wish of Concentration on key 4.",
     tip="Opener (Est): Element Enhancement → Delayed Explosion → fully charged Hellfire → Fire Wall + Cold Storm → Bittercold Wind → Firestorm → Wish of Concentration (−10 s on every cooldown) → Bittercold Wind → Delayed Explosion → Winter's Shackles → Hellfire → Firestorm. After that, hold left click + the macro and press everything else as it comes up. Hellfire is always fully charged. Blaze needs option 5 (skill level 16) for the rotation to work. Global: cooldown reduction is very low at launch, so Est recommends weaving Ice Chain into the rotation for now.",
     patch=MC["sorcerer"]["late"].get("patch", ""),
     alts=demote("sorcerer", "In-game only, 6 entries (Korea, Sep 4): automates the AoEs, needs all 4 stigmas"))

# ---------- Gladiator ----------
late("gladiator",
     macros=[["Zikel's Blessing", None, None, None], ["Lifestealing Blade", "Lunge Stance", "Rending Blow", None], ["Rage Burst", "Overhead Slam", None, None]],
     delays=[10, 10, 10], hold=["Keen Strike", "Macro key"],
     manual=["Ruinous Blow", "Mocking Blade", "Crushing Wave", "Ankle Slice", "Sword Aura Rampage"],
     keys=[{"label": "Q key (press yourself)", "stack": ["Leaping Slam", "Rush Strike", "Aerial Snare", None]}],
     queue="Not stated in the sheet, so test both",
     why="The Global sheet's layout: three entries, all in the in-game macro. Entry 1 keeps Zikel's Blessing on cooldown. Entry 2 casts Lifestealing Blade and Lunge Stance, with Rending Blow as the filler. Entry 3 has Rage Burst with Overhead Slam right above it. Rage Burst makes Overhead Slam usable on the target for 10 s (game database), so Overhead Slam fires from that entry during each Rage Burst window. Hold Keen Strike (left click) with the macro: it's your MP source.",
     tip="Mana: the sheet warns you'll run short on MP until Rending Blow reaches skill level 16, so keep left click held. The screenshot slots Lifestealing Blade. The sheet's stigma order is Lunge Stance, Zikel's Blessing, Wave Armor, Rage Burst, so if you run Wave Armor instead, press it yourself and that row stays empty. Korean top players mash Overhead Slam on its own key for more hits (Other versions).",
     patch=MC["gladiator"]["late"].get("patch", ""),
     alts=demote("gladiator", "Korea/Taiwan top setup: mash an Overhead Slam key (Sep 5 + Aug 26)"))

# ---------- Templar ----------
late("templar",
     macros=[["Battlefield Banner", "Taunt", "Debilitating Smash", None], ["Judgment", "Warding Strike", "Shield Smite", "Pummel"], ["Annihilate", None, None, None]],
     delays=[10, 10, 10], hold=["Vicious Strike", "Macro key"],
     manual=["Noble Armor", "Punishment", "Poach"],
     keys=[{"label": "Q key (press yourself)", "stack": ["Doom Shield", "Shield Rush", None, None]}],
     queue="Not stated in the sheet, so test both",
     why="The Global sheet's layout. The Judgment line is the same as Korea's: Shield Smite and Warding Strike are shield attacks, so they keep opening Judgment, and Pummel fills. The sheet adds a first entry that keeps Battlefield Banner and Taunt on cooldown, with Debilitating Smash under them. Annihilate gets its own entry.",
     tip="Press Noble Armor yourself on cooldown. Doom Shield (also a shield attack, and it resets Annihilate) and Shield Rush sit on Q. Fully charge Punishment yourself for Executor (+20% PvE damage).",
     patch=MC["templar"]["late"].get("patch", ""),
     alts=demote("templar", "Korea/Taiwan top setup (Inven Sep 5 optimizer guide)"))

# ---------- Ranger ----------
late("ranger",
     macros=[["Gale Arrow", "Drill Dart", "Burst Arrow", None], ["Griffon Arrow", "Snare Shot", "Tempest Shot", None], ["Vaizel's Authority", "Bow of Blessing", "Supporting Fire", None]],
     delays=[10, 10, 10], hold=["Snipe", "Macro key"],
     manual=["Deadshot", "Explosion Trap"],
     keys=[{"label": "E key (press yourself)", "stack": ["Marking Shot", "Suppressing Arrow", None, None]}],
     queue="Not stated in the sheet, so test both",
     why="The Global sheet's layout. Tempest Shot sits at the top of the Griffon line, away from Drill Dart, which is the same rule Korean Rangers use for the Tempest Shot cancel. Snare Shot slows the target, and that's what lets Burst Arrow (on the Gale line) fire. The third entry keeps Vaizel's Authority, Bow of Blessing and Supporting Fire rolling.",
     tip="Keep Marking Shot's debuff up yourself (E). You can also take the 3 buffs out of the macro and press them before the pull (sheet). The Global Ranger guide (Allyria) leaves Marking Shot, Arrow Scattershot, Suppressing Arrow and Explosion Trap out of the macro. Charge Deadshot yourself.",
     patch=MC["ranger"]["late"].get("patch", ""),
     alts=demote("ranger", "Korea/Taiwan top setup (Inven Sep 6)"))

# ---------- Cleric ----------
late("cleric",
     macros=[["Earth Punishment", "Chain of Torment", "Debilitating Mark", "Condemnation"], ["Judgment Thunder", "Divine Aura", None, None]],
     delays=[10, 10], hold=["Earth's Retribution", "Macro key"],
     manual=["Bolt", "Noble Aura", "Prayer of Amplification", "Light of Protection", "Healing Light", "Radiant Recovery", "Light of Regeneration"],
     queue="Not stated in the sheet, so test both",
     why="The Global sheet's offensive layout. Earth Punishment leads, because with it on the target Condemnation always crits. Chain of Torment marks targets so Condemnation can hit them, and Debilitating Mark lowers their Defense. Condemnation (3 s) fills. The second entry adds Judgment Thunder.",
     tip="Before the pull: Prayer of Amplification (your biggest self-buff), then summon Noble Aura (your 2nd-biggest damage skill). Then hold the macro. Charge Bolt yourself, and heal by hand. Early on, weave in left click (Earth's Retribution), because holding the macro alone drains your MP. Judgment Thunder has no cooldown, so as row 0 it fires almost every time its entry comes up and Divine Aura above it rarely gets a turn. Press Divine Aura yourself if you want it.",
     patch=MC["cleric"]["late"].get("patch", ""),
     alts=demote("cleric", "Korea/Taiwan top setup (Inven Sep 24 optimizer guide)"))

# ---------- Spiritmaster ----------
late("spiritmaster",
     macros=[["Summon: Water Spirit", "Summon: Earth Spirit", "Summon: Fire Spirit", None], ["Jointstrike: Curse", "Elemental Fusion", "Dimensional Control", "Combustion"]],
     delays=[10, 10], hold=["Cold Shock", "Macro key"],
     manual=["Jointstrike: Corrode", "Summon: Ancient Spirit", "Summon: Wind Spirit", "Soul's Cry"],
     keys=[{"label": "Key 1 (press yourself)", "stack": ["Flame Blessing", "Enhance: Spirit's Benediction", None, None]}],
     queue="Sirin's Global guide has two versions: skill queue OFF (with mouse software) or ON (relies more on the in-game macro)",
     why="The Global sheet's layout: a spirit line and a Curse line. Elemental Fusion sits in the macro here (row 1 of the Curse line), so it fires whenever you have Four Elements. Korea keeps it on a separate mashed key.",
     tip="Press keys 1–3 yourself (Flame Blessing + Benediction, Corrode, Ancient Spirit), then hold left click + the macro. Wind Spirit (key 4) is mainly for mobbing. You can summon the spirits by hand a few seconds before the pull. Global: Sirin's Global guide measured only ~19–21% cooldown reduction with the best Global gear (Korea reaches 34–40%), so Ancient Spirit (90 s) will have real downtime.",
     patch=MC["spiritmaster"]["late"].get("patch", ""),
     alts=demote("spiritmaster", "Korea/Taiwan top setup: 4 spirits, Fusion mashed (Inven Sep 16)"))

# ---------- Assassin ----------
late("assassin",
     macros=[["Insignia Explosion", None, "Heart Gore", "Savage Roar"]], delays=[10],
     hold=["Quick Slice", "Macro key"],
     manual=["Illusive Clone", "Swift Contract", "Triniel's Dagger", "Savage Fang", "Flash Slice", "Shadowstrike"],
     keys=[{"label": "Q key (press yourself)", "stack": ["Infiltrate", "Shadow Fall", None, None]},
           {"label": "E key (press yourself)", "stack": ["Whirlwind Slice", "Storm Rampage", None, None]}],
     queue=MC["assassin"]["late"].get("queue", ""),
     why="The Global sheet's layout: one line, as in Korea. In the screenshot, row 1 holds Smoke Bomb, a 6th stigma Global doesn't have, so leave it empty. Or put Ambush there: Korea's Sep 30 guide found that slightly better on real bosses (Other versions).",
     tip="Press your buffs and the other actives yourself, hold left click + the macro, and dash when needed. " + MC["assassin"]["late"].get("tip", ""),
     patch=MC["assassin"]["late"].get("patch", ""),
     alts=demote("assassin", "Korea Sep 30 optimizer line: Ambush in row 1"))

# ---------- Chanter (already the same stack; adopt the sheet's delay, keys and Marchutan) ----------
ch = MC["chanter"]["late"]
ch["src"] = "Global class sheet (Global-client screenshot) + Inven Sep 17 optimizer guide (same stack)"
ch["link"] = SHEET
ch["delays"] = [13]
ch["hold"] = ["Onslaught", "Macro key"]
ch["manual"] = ["Marchutan's Wrath", "Power of the Storm", "Undefeated Mantra", "Sprint Mantra", "Recuperation", "Rushing Smash", "Gust Rampage"]
ch["keys"] = [{"label": "Q key (press yourself)", "stack": ["Tremor Crush", "Wave Blow", None, None]}]
ch["why"] = ch["why"].replace("(Marchutan's Wrath gives 3 s, but it isn't in the Global 4)", "(Marchutan's Wrath, your 4th Global stigma, gives 3 s; press it yourself when the macro runs out of Dark Crush windows)")
ch["tip"] = ch["tip"].replace("Settings: one entry, delay 10 ms (raise it to 30–50 ms only if skills get skipped)", "Settings: one entry, delay 13 ms in the Global sheet's screenshot (Korean setups use 10 ms; raise it only if skills get skipped)").replace("Hold Onslaught + the macro key, and Gust Rampage too for its stagger cancel.", "Hold Onslaught (left click) + the macro key. Korean players also hold Gust Rampage for its stagger cancel.").replace(" Stack Guardian Blessing on top of Power of the Storm.", "")

# ---------- Early cards: no stigmas before 22 ----------
SLOTS = "Stigma slots open at character level 22, 27, 32 and 37 (Global)."
e = MC["templar"]["early"]
e["manual"] = ["Punishment", "Annihilate", "Debilitating Smash", "Shield Rush", "Poach"]
e["why"] = "The same Judgment line the late-game layouts use, and every skill in it is a regular skill: Pummel (Lv 1), Shield Smite (Lv 3), Judgment (Lv 4) and Warding Strike (Lv 8). Shield Smite and Warding Strike are shield attacks, so they keep opening Judgment, and Pummel in the same line lets your held Vicious Strike cancel into it."
e["tip"] = "Hold Vicious Strike (left click) with the macro. Shield Smite stuns normal mobs, which is what Annihilate (Lv 12) needs. Charge Punishment (Lv 14) yourself. " + SLOTS + " The sheet's order: Battlefield Banner, Taunt, Noble Armor, Doom Shield. When you have Doom Shield, press it to open pulls (it's a shield attack too)."
e = MC["assassin"]["early"]
e["manual"] = ["Shadowstrike", "Flash Slice", "Whirlwind Slice"]
e["tip"] = "While leveling, hold Quick Slice with the macro, because it restores MP. " + SLOTS + " The sheet's order: Illusive Clone, Swift Contract, Triniel's Dagger, Savage Fang."
e = MC["ranger"]["early"]
e.update({"macros": [["Gale Arrow", "Drill Dart", "Burst Arrow", None], ["Snare Shot", "Tempest Shot", None, None]], "delays": [10, 10],
          "hold": ["Snipe", "Macro key"], "manual": ["Marking Shot", "Deadshot", "Explosion Trap", "Suppressing Arrow"],
          "why": "The Global layout without its stigma rows (Griffon Arrow and the buffs come at 22+). Drill Dart (Lv 4), Gale Arrow (Lv 7) and Burst Arrow (Lv 10) share a line. Snare Shot and Tempest Shot (Lv 1) get their own, which keeps Tempest Shot away from Drill Dart. Snare Shot's slow is what lets Burst Arrow fire.",
          "tip": "The launch-week Korean leveling guides put left and right click (Snipe and Tempest Shot) first for skill points, then Marking Shot. Explosion Trap (Lv 8) groups packs. " + SLOTS + " The sheet's order: Vaizel's Authority, Bow of Blessing, Supporting Fire, Griffon Arrow."})
e["alts"] = [a for a in e.get("alts", [])]
for a in e["alts"]:
    if a["t"] == "Video version":
        a["s"] = (a.get("s", "") + " Griffon Arrow and Explosive Arrow are stigmas (level 22+), so those rows are empty while leveling.").strip()
e = MC["spiritmaster"]["early"]
e.update({"macros": [["Summon: Water Spirit", "Summon: Earth Spirit", "Summon: Fire Spirit", None], ["Jointstrike: Curse", "Elemental Fusion", "Dimensional Control", "Combustion"]],
          "delays": [10, 10], "hold": ["Cold Shock", "Macro key"], "manual": ["Summon: Wind Spirit", "Soul's Cry"],
          "why": "The Global layout uses no stigmas in the macro, so it works while leveling. Fire Spirit (Lv 1), Water Spirit (Lv 3) and Earth Spirit (Lv 7) share the spirit line. Curse (Lv 4), Dimensional Control (Lv 8), Elemental Fusion (Lv 14) and Combustion (Lv 1) share the second line. Rows you haven't learned are skipped.",
          "tip": "Wind Spirit (Lv 10) is mainly for mobbing; summon it yourself. The launch-week Korean guide says to spread skill points evenly across the spirits, because Fusion needs all four elements. " + SLOTS + " The sheet's order: Ancient Spirit, Spirit's Benediction, Corrode, Flame Blessing."})
e = MC["cleric"]["early"]
e.update({"macros": [["Chain of Torment", "Debilitating Mark", "Condemnation", None], ["Judgment Thunder", "Divine Aura", None, None]],
          "delays": [10, 10], "hold": ["Earth's Retribution", "Macro key"], "manual": ["Bolt", "Healing Light", "Radiant Recovery", "Light of Regeneration"],
          "why": "The Global layout without Earth Punishment, which is a stigma (level 22+). Chain of Torment (Lv 4) marks targets so Condemnation (Lv 8) can hit them, and Debilitating Mark (Lv 1) lowers their Defense. Judgment Thunder (Lv 1) is the second line.",
          "tip": "Weave left click (Earth's Retribution) while leveling: holding the macro alone drains MP (sheet). Korean launch-week players called Condemnation at skill level 12 the key leveling skill. Charge Bolt (Lv 14) yourself. " + SLOTS + " The sheet's order: Light of Protection, Earth Punishment, Noble Aura, Prayer of Amplification."})
g = MC["gladiator"]
old_early = g["early"]
g["early"] = {
    "src": "Built from the Korean launch-week leveling guides (Inven Nov 19–21, 2025) + the Global sheet's key layout",
    "link": "https://www.inven.co.kr/board/aion2/6448/40",
    "macros": [["Overhead Slam", "Mocking Blade", "Crushing Wave", "Rending Blow"]], "delays": [10],
    "hold": ["Keen Strike", "Macro key"],
    "manual": ["Ankle Slice", "Ruinous Blow", "Leaping Slam", "Rush Strike", "Aerial Snare", "Sword Aura Rampage"],
    "why": "No stigmas until 22, and in the game database Overhead Slam only hits a knocked-down target (or procs 7% of the time on bosses that can't be knocked down). So while leveling, the macro knocks targets down for it: Mocking Blade (Lv 3) knocks down for 3 s, and Overhead Slam (Lv 4) sits above it to fire right after. Crushing Wave (Lv 8) hits everything within 5 m. Rending Blow (Lv 1) is the filler. Korean launch-week players called Crushing Wave the best leveling skill: at skill level 8–12 it heals on hit and resets on crits.",
    "tip": "Hold Keen Strike (left click): it's your MP source until Rending Blow reaches skill level 16 (sheet). Ankle Slice (Lv 7) roots packs. Rush Strike after a dodge also knocks down. Aerial Snare (Lv 12) hits knocked-down targets. Ruinous Blow (Lv 14) opens boss fights. " + SLOTS + " Rage Burst is what makes Overhead Slam usable on bosses for 10 s, so it's the stigma that changes the macro. The sheet's order is Lunge Stance, Zikel's Blessing, Wave Armor, Rage Burst.",
    "alts": [{"t": "One-key layout (this sheet's previous early card, uses stigma rows from 22)", "s": old_early.get("why", ""), "macros": old_early["macros"], "hold": old_early.get("hold")}] + [a for a in old_early.get("alts", [])],
}

# ---------- Stigmas: Global main build = the sheet's 4, in the sheet's order ----------
def setmain(cid, picks, title=None, tag="Most used", why=None, src=True):
    g = SC[cid]["gl"]
    names = [p[0] for p in picks]
    target = None
    for b in g["builds"]:
        if sorted(p[0] for p in b["pick"]) == sorted(names):
            target = b
    for b in g["builds"]:
        if b.get("main"):
            b.pop("main", None)
            if b is not target and b.get("tag") == "Most used":
                b["tag"] = "Swap"
    if target is None:
        target = {"t": title or "Global sheet pick", "why": why or "", "src": []}
        g["builds"].insert(0, target)
    else:
        g["builds"].remove(target)
        g["builds"].insert(0, target)
    target["pick"] = picks
    target["main"] = True
    target["tag"] = tag
    if title:
        target["t"] = title
    if why:
        target["why"] = why
    if src:
        target["src"] = [["Global class sheet (zxcastform)", SHEET]] + [s for s in target.get("src", []) if s[1] != SHEET]

def lv(cid, name):
    for l in SC[cid]["gl"]["levels"]:
        if l[0] == name:
            return l[1]
    return 20

for cid, order in {"sorcerer": ["Element Enhancement", "Fire Wall", "Delayed Explosion", "Cold Storm"],
                   "gladiator": ["Lunge Stance", "Zikel's Blessing", "Wave Armor", "Rage Burst"],
                   "ranger": ["Vaizel's Authority", "Bow of Blessing", "Supporting Fire", "Griffon Arrow"],
                   "spiritmaster": ["Summon: Ancient Spirit", "Enhance: Spirit's Benediction", "Jointstrike: Corrode", "Flame Blessing"],
                   "assassin": ["Illusive Clone", "Swift Contract", "Triniel's Dagger", "Savage Fang"]}.items():
    setmain(cid, [[n, lv(cid, n)] for n in order])
setmain("templar", [["Battlefield Banner", 20], ["Taunt", 20], ["Noble Armor", 20], ["Doom Shield", 15]],
        title="Global sheet pick (damage tank)",
        why="The Global sheet's order: Battlefield Banner, Taunt, Noble Armor, Doom Shield. Banner turns Defense into Attack. Taunt's Shrink makes the boss take more damage from the whole party. Noble Armor 15 multiplies Fury by 1.5. Doom Shield is a shield attack, so it opens Judgment (Aug 26 rework), and at 5 it resets Annihilate. For hard bosses, the Party tank and Hard content versions trade damage for Shield of Protection and party saves.")
setmain("chanter", [["Undefeated Mantra", 20], ["Power of the Storm", 20], ["Sprint Mantra", 10], ["Marchutan's Wrath", 5]],
        title="Global sheet pick (= your image)",
        why="The Global sheet's order, which is also the list from your image: Undefeated Mantra, Power of the Storm, Sprint Mantra, Marchutan's Wrath. Marchutan's Wrath gives the longest Dark Crush window (3 s), so it adds Dark Crush casts on top of Impactful Crush and Spinning Strike. The sheet's next picks are Guardian Blessing, then Focused Defense or Impeding Authority.")
setmain("cleric", [["Light of Protection", 15], ["Earth Punishment", 20], ["Noble Aura", 15], ["Prayer of Amplification", 20]],
        title="Global sheet pick (damage, content on farm)",
        why="The Global sheet's order: Light of Protection, Earth Punishment, Noble Aura, Prayer of Amplification. The sheet calls it a personal-damage setup once content is on farm. While learning a fight, swap #3 or #4 for Benevolence or Summon Resurrection. With a Chanter in the party, swap Light of Protection out, because Undefeated Mantra replaces it.")
lvls = SC["chanter"]["gl"]["levels"]
if not any(l[0] == "Marchutan's Wrath" for l in lvls):
    lvls.insert(3, ["Marchutan's Wrath", 5, "The 3 s Dark Crush window works from level 1. 5: up to +20% damage on fewer targets. 10–20 add stun and anti-heal (PvP)."])
for b in SC["chanter"]["gl"]["builds"]:
    if b.get("t", "").startswith("Your image"):
        pass

# ---------- Specs from the sheet ----------
for cid, c in CL["classes"].items():
    sheet = c.get("sheet")
    if not sheet:
        continue
    old = {sp["n"]: sp for sp in SC[cid].get("specs", [])}
    new = []
    for name, lvl, picks in sheet["skills"]:
        if not picks:
            continue
        o = old.get(name, {})
        note = []
        if o and sorted(o["pick"]) != sorted(picks):
            note.append(f"Korea's Sep optimizer: {' · '.join(map(str, o['pick']))}.")
        if o.get("note") and o.get("note") != "Fixed.":
            note.append(o["note"])
        sp = {"n": name, "pick": picks, "lvl": lvl, "note": " ".join(note), "src": ["Global class sheet (zxcastform)", SHEET]}
        if o.get("u20") and sorted(o["pick"]) == sorted(picks):
            sp["u20"] = o["u20"]
        new.append(sp)
    SC[cid]["specs"] = new

M["meta"]["updated"] = ST["meta"]["updated"] = "2026-10-02"
M["changelog"].insert(0, {"date": "2026-10-02", "text": "Every class updated from the shared Global class sheet. Late game cards are now each class's Global-client layout (the previous Korea/Taiwan setups are under Other versions). Early game cards no longer use stigmas, and Gladiator gets a leveling line built around Mocking Blade → Overhead Slam. Global stigma picks follow the sheet (Templar: Banner / Taunt / Noble Armor / Doom Shield, Chanter: Marchutan's Wrath as the 4th, Cleric: Light of Protection / Earth Punishment / Noble Aura / Prayer). Specialization picks and skill target levels now come from the sheet for every skill, with Korea's pick noted where it differs. New per-class gear tables: soul binding per piece, accessories, Arcana, Pet Genus, Pantheon."})
json.dump(M, open("data/macros.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(ST, open("data/stigmas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
