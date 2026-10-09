"""Run-once (Oct 9, 2026): macro and text changes from the top-player data pass (data/topplayers.json, data/plans.json).

- Assassin Late: the Korea Sep 30 optimizer line (Ambush in row 1) becomes the main card; the Global sheet's line with an
  empty row 1 moves to Other versions. Ambush is in 70% of top Global parses.
- Gladiator Late: Ruinous Blow (Prepare for Battle, +20% PvE damage) joins Zikel's Blessing in entry 1 so it stays on
  cooldown; top Global Gladiators cast it 2.9 times a minute.
- Templar Late: Debilitating Smash leaves entry 1 (0.8% of damage; two thirds of the top 10% never cast it).
- Chanter: Dark Crush spec path by skill level, Marchutan's Wrath wording (it IS the Global 4th stigma), stigma
  level-up order now matches the main build.
- Sorcerer / Ranger tips: Ice Chain and Snipe option 4 findings.
- classes.json "hits": Global top-10% boss-fight numbers next to the Korean dummy targets.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda f: os.path.join(ROOT, 'data', f)
mac = json.load(open(P('macros.json'), encoding='utf-8'))
stg = json.load(open(P('stigmas.json'), encoding='utf-8'))
ov = json.load(open(P('classes.json'), encoding='utf-8'))
C = {c['id']: c for c in mac['classes']}


def sub(obj, key, old, new):
    assert old in obj[key], (key, old[:60])
    obj[key] = obj[key].replace(old, new)


# ---- Assassin
a = C['assassin']['late']
sheet_alt = {"t": "Global sheet layout (row 1 empty)", "s": "The Global class sheet's screenshot: one line with Smoke Bomb in row 1, a stigma Global doesn't have, so the row stays empty. Same skills otherwise. The Ambush line above is ahead on real bosses.",
             "macros": [list(a['macros'][0])], "hold": ["Quick Slice", "Macro key"]}
sep30 = a['alts'].pop(0)
assert sep30['t'].startswith('Korea Sep 30')
a['macros'] = [["Insignia Explosion", "Ambush", "Heart Gore", "Savage Roar"]]
a['src'] = "Korea Sep 30 optimizer guide line, checked against top Global players (NotMeter, week of Oct 7)"
a['link'] = "https://www.inven.co.kr/board/aion2/6449/24247"
a['why'] = ("One line. Insignia Explosion fires first whenever it's ready, then Ambush, then Heart Gore, which triggers off your crits, "
            "with Savage Roar as the filler when nothing else is up. Ambush in row 1 costs a few Heart Gore hits but raised total damage "
            "on real bosses (Korea's Sep 30 guide), and it's in 70% of top Global Assassin parses: its option 1 engraves 2 Insignias on a "
            "back attack, which makes the next Insignia Explosion hit harder. With Ambush taking over the lifesteal, Heart Gore needs its "
            "Insignia option (2).")
a['tip'] = ("Stand behind the boss: top Global Assassins land 85% of their hits from behind. Press Swift Contract, then Illusive Clone "
            "(the attack-speed buff shortens Clone's animation); the top 10% cast Clone about once a minute, while most median players never do. "
            "Press Savage Fang before Triniel's Dagger: the Dagger only cuts cooldowns that are already running. Hold the E key during stagger "
            "bars for Storm Rampage's cancel. Don't take Ambush's option 5 (+2 uses); it made the motion worse. Level order and picks: see "
            "Max damage plan.")
a['alts'].insert(0, sheet_alt)

# ---- Gladiator
g = C['gladiator']['late']
assert g['macros'][0] == ["Zikel's Blessing", None, None, None]
g['macros'][0] = ["Zikel's Blessing", "Ruinous Blow", None, None]
g['manual'] = [x for x in g['manual'] if x != 'Ruinous Blow']
sub(g, 'why', "Entry 1 keeps Zikel's Blessing on cooldown.",
    "Entry 1 keeps Zikel's Blessing and Ruinous Blow on cooldown (Ruinous Blow's Prepare for Battle is +20% PvE damage for 20 s; top Global Gladiators recast it every ~21 s, so this page moved it from your hands into the macro).")
sub(g, 'why', "Hold Keen Strike (left click) with the macro: it's your MP source.",
    "The macro alternates Rending Blow (entry 2) and Overhead Slam (entry 3), which is the Overhead Slam → Rending Blow cancel: the top 10% of Global Gladiators cast ~59 Overhead Slams and ~52 Rending Blows a minute. Hold Keen Strike (left click) only while MP runs short.")

# ---- Templar
t = C['templar']['late']
assert t['macros'][0] == ["Battlefield Banner", "Taunt", "Debilitating Smash", None]
t['macros'][0] = ["Battlefield Banner", "Taunt", None, None]
sub(t, 'why', "The sheet adds a first entry that keeps Battlefield Banner and Taunt on cooldown, with Debilitating Smash under them.",
    "The sheet adds a first entry that keeps Battlefield Banner and Taunt on cooldown. Its Debilitating Smash row is now empty: it's 0.8% of damage, its −25% Defense barely matters on bosses (Defense only removes 10% of its value in PvE), and two thirds of the top-10% Global Templars never cast it.")

# ---- Chanter
ch = C['chanter']
sub(ch['late'], 'tip', "and Dark Crush options 3 · 4 · 5 (crit on hit, Piercing Strike chain, no cooldown).",
    "and Dark Crush picks by skill level: 3 at 8 (crit), 3 + 4 at 12 (Piercing Strike chain), 3 + 5 at 16 (no cooldown; this beat 4 + 5 by ~5% in Global data), 3 + 4 + 5 at 20.")
sub(ch['full'], 'loss', "Global: Marchutan's Wrath isn't in the Global 4 stigma build, so its row is skipped unless you slot it.",
    "Global: Marchutan's Wrath is your 4th stigma (slot 4 opens at level 37), so its row is skipped until then.")
alt = ch['late']['alts'][0]
sub(alt, 's', "Global: Marchutan's Wrath isn't in your 4 stigmas, so its row is skipped. What's left is Dark Crush / Spinning Strike / Incandescent Blow plus Impactful Crush on its own entry.",
    "Global: Marchutan's Wrath is your 4th stigma from level 37; before that its row is skipped.")
sub(ch['early'], 'tip', "Slot them in this order: 22 Undefeated Mantra (toggle it on), 27 Power of the Storm, 32 Guardian Blessing (stack it on Power of the Storm's key), 37 Sprint Mantra (toggle).",
    "Slot them in this order: 22 Undefeated Mantra (toggle it on), 27 Power of the Storm, 32 Sprint Mantra (toggle), 37 Marchutan's Wrath (the Global sheet's order and what 98% of top Global Chanters slot).")
cg = [c for c in stg['classes'] if c['id'] == 'chanter'][0]['gl']
cg['order'] = [
    {"s": [["Undefeated Mantra", 5], ["Power of the Storm", 5], ["Sprint Mantra", 5], ["Marchutan's Wrath", 5]],
     "n": "Cheap unlocks first. Marchutan's Wrath's 3 s Dark Crush window works from level 1."},
    {"s": [["Undefeated Mantra", 20]], "n": "Top Global Chanters this week: Undefeated Mantra at 20, everything else at 5–10."},
    {"s": [["Sprint Mantra", 10], ["Power of the Storm", 20]]},
]
cg['imageNote'] = ("Your list has 5; with 4 slots, keep Marchutan's Wrath and drop Guardian Blessing. That's the Global sheet's pick, and 98% of "
                   "top Global Chanters slot Marchutan's Wrath vs 28% for Guardian Blessing.")

# ---- Sorcerer / Ranger tips
so = C['sorcerer']['late']
sub(so, 'tip', "Global: cooldown reduction is very low at launch, so Est recommends weaving Ice Chain into the rotation for now.",
    "Est recommends weaving Ice Chain while Global cooldowns are long, but two thirds of top-10% Global Sorcerer parses never cast it and it measured ±0, so skip it unless you're short on MP.")
ra = C['ranger']['late']
ra['tip'] = ra['tip'] + (" Get Snipe (left click) to skill level 12 early for option 4: −1 s Deadshot cooldown per hit, which gave Global Rangers "
                         "2.3x as many Deadshots.")

# ---- hits lines: add Global top-10% boss-fight numbers
G = {
 'gladiator': "Global top 10% in boss fights (this week): Overhead Slam ~59, Upward Strike ~49, Rending Blow ~52 casts a minute",
 'templar': "Global top 10% in boss fights (this week): Judgment ~45 casts a minute (median top player 38)",
 'assassin': "Global top 10% in boss fights (this week): Heart Gore ~52, Insignia Explosion ~17 casts a minute",
 'ranger': "Global top 10% in boss fights (this week): Deadshot ~7, Tempest Shot ~107, Drill Dart ~18, Gale Arrow ~9 casts a minute",
 'sorcerer': "Global top 10% in boss fights (this week): Hellfire ~6, Blaze ~34, Firestorm ~13 casts a minute",
 'spiritmaster': "Global top 10% in boss fights (this week): Elemental Fusion ~20, Combustion ~39 casts a minute",
 'cleric': "Global top 10% in boss fights (this week): Condemnation ~40 casts a minute",
 'chanter': "Global top 10% in boss fights (this week, downtime included): Dark Crush ~30, Spinning Strike ~7 casts a minute",
}
for k, v in G.items():
    h = ov['classes'][k].get('hits') or ''
    ov['classes'][k]['hits'] = (h + '. ' + v) if h else v

mac['meta']['updated'] = '2026-10-09'
mac['changelog'].insert(0, {"date": "2026-10-09", "text": (
    "New on every class page: Max damage plan. It shows which skill to level first and which specialty to slot at skill level 8 / 12 / 16 / 20, "
    "with estimated DPS for each step, where top Global players' damage comes from, and what a macro costs vs pressing by hand. Built from "
    "this week's top Global boss parses and Korea's top-20 builds (NotMeter). Macro changes: Assassin's Late card is now the Ambush line; "
    "Gladiator fires Ruinous Blow from the macro; Templar drops Debilitating Smash. Fixed Chanter text that said Marchutan's Wrath isn't a "
    "Global stigma. New home panels: DPS tier list, easiest class to max, and the Bible's Oct 4 Global changes.")})
stg['meta']['updated'] = '2026-10-09'

json.dump(mac, open(P('macros.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
json.dump(stg, open(P('stigmas.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
json.dump(ov, open(P('classes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('done')
