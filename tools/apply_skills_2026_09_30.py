"""2026-09-30 review pass + new 'Skills to level' section.

- skills per class: active DPS / buff skills with target skill level, passive priority, first two skills to 20.
  Sources: Sep 2026 Korean optimizer guides (screenshots 'required level-20 actives' / 'required passives'),
  earlier Korean class guides, and Kanon's Aion 2 Bible (skill-level rules, stat values, wings).
- Fix: KR/TW Gladiator builds still treated Armor of Balance as a damage pick. A Jul 7-8 KR patch moved the
  Experienced Counterstrike x1.5 effect to Wave Armor (the Global DB shows the same), so Focused Block takes its slot.
- Global Season 1: 4 stigma slots confirmed on NC's official livestream (reported Sep 8).
"""
import json

ROOT = __file__.rsplit("tools", 1)[0]
P = ROOT + "data/stigmas.json"
M = json.load(open(P, encoding="utf-8"))
C = {c["id"]: c for c in M["classes"]}
INV = "https://www.inven.co.kr/board/aion2/"
VX = "https://vortexgaming.io/postdetail/"
KANON = ["Kanon's Aion 2 Bible (Sep 20)", "https://docs.google.com/document/d/11u4wLCG1WfL-xSka2Aze0rI9vYRa7mq3N3Gp1bt0AWY/preview"]

SK = {
 "templar": {
  "first": ["Judgment", "Pummel"],
  "act": [
   ["Judgment", "20", "DPS", "More than half of a Templar's damage comes from this one skill. First to 20; its no-cooldown option needs 16."],
   ["Pummel", "20", "DPS", "Your weave skill. 20 opens the third pick (extra Punishing Strike plus Punishment cooldown cuts)."],
   ["Vicious Strike", "20", "DPS", "Held basic attack. 16 is fine until you run the Vicious Strike-Judgment setup, which needs all three picks."],
   ["Punishment", "16-20", "Buff", "A full charge gives Executor: +200 Accuracy and +20% PvE damage for 20s. 12-16 as a buff, 20 if you also want its damage."],
   ["Annihilate", "16-20", "DPS", "Optional burst. 12 covers picks 3 and 4; 20 adds the multi-hit pick."],
   ["Warding Strike", "16", "Buff", "Warding (+20% PvE damage tolerance) and it re-opens Judgment. 16 unlocks the party tolerance share."],
   ["Debilitating Smash", "16", "Debuff", "Weaken: target Defense -25%."],
   ["Shield Smite", "12", "Utility", "Re-opens Judgment; pick 2 removes its MP cost."]],
  "pas": [
   ["Fury", "Front damage boost for you, plus PvE damage for the whole party for 20s whenever you block. Highest priority (KR endgame 35-36). Noble Armor 15 multiplies it x1.5."],
   ["Impact Hit (templar)", "Double Chance (KR 33)."],
   ["Insulting Roar", "+Attack on front attacks (KR 30). About the same value as Impact Hit."],
   ["Punishing Benediction", "+100 Crit and extra-damage procs."],
   ["Ironclad Defense", "Defense, which also feeds Battlefield Banner."]],
  "wings": "Eroded Wings 77%, Talisra 9%, Brawler 3.5%",
  "src": [["KR Sep 5 optimizer (screenshots)", INV + "6438/25862"], ["KR Templar skill guide (Jan, edited Apr)", INV + "6438/6625"], ["KR Mar 13 guide", VX + "696602"], KANON]},
 "gladiator": {
  "first": ["Overhead Slam", "Rending Blow"],
  "act": [
   ["Overhead Slam", "20", "DPS", "More than half of a Gladiator's damage. First to 20."],
   ["Rending Blow", "20", "DPS", "The other half of the Overhead Slam-Rending Blow cancel."],
   ["Ruinous Blow", "16", "Buff", "Opener: Prepare for Battle gives +20% PvE damage and +100 Crit for 20s. It no longer needs 20."],
   ["Aerial Snare", "12", "DPS", "Optional: one tester gained about 300k DPS using it in Sword Aura Rampage's spot, at the cost of some Overhead Slam hits."]],
  "pas": [
   ["Experienced Counterstrike", "Front damage boost, plus PvE damage for the party when you block. Highest priority (KR endgame 36). Wave Armor 10 multiplies it x1.5."],
   ["Murderous Burst", "Crit damage (KR 30). Wave Armor 15 multiplies it x1.5."],
   ["Attack Preparation", "PvE damage (KR 29)."],
   ["Identify Weakness", "Crit and Perfect (KR 22). Lunge Stance 15 multiplies it x1.5."],
   ["Impact Hit", "Double Chance (KR 21). The guide rates these last three about equal."]],
  "wings": "Eroded Wings 73%, Talisra 18.5%",
  "src": [["KR Sep 5 optimizer (screenshots)", INV + "6448/31551"], KANON]},
 "assassin": {
  "first": ["Heart Gore", "Quick Slice"],
  "act": [
   ["Heart Gore", "20", "DPS", "Your core: it resets on crits (pick 5, which needs 16)."],
   ["Quick Slice", "20", "DPS", "Held basic attack; pick 4 cuts Insignia Explosion's cooldown on every hit."],
   ["Insignia Explosion", "20", "DPS", "Detonates your Insignia stacks."],
   ["Savage Roar", "20", "DPS", "Filler that builds Insignias; pick 4 cuts Shadowstrike's cooldown."],
   ["Ambush", "20", "DPS", "Ranked just below the four above. Press it on its own key."],
   ["Shadowstrike", "16", "Buff", "Pick 2 gives +20% crit damage for 5s. 8 is the minimum."],
   ["Whirlwind Slice", "16", "DPS", "Multi-hit pick fixed; range or AoE by taste."],
   ["Storm Rampage", "16", "DPS", "Stagger-window skill held on its own key."]],
  "pas": [
   ["Rear Smite", "Back-attack damage boost plus PvE damage. Highest priority. Swift Contract 10 multiplies it x1.5."],
   ["Exploit Weakness", "+100 Crit and an Attack proc. Rated tier 1 since it gained the Attack bonus. Illusive Clone 15 multiplies it x1.5."],
   ["Impact Hit (assassin)", "Double Chance."],
   ["Assault Stance", "Crit damage. Swift Contract 15 multiplies it x1.5."]],
  "wings": "Talisra 58%, Awaken Pride 30% (newer, expected to overtake)",
  "src": [["KR Mar 31 specialization guide (20s and 16s)", VX + "726439"], ["KR May PvE guide (passive tiers)", VX + "854915"], KANON]},
 "ranger": {
  "first": ["Deadshot", "Gale Arrow"],
  "act": [
   ["Deadshot", "20", "DPS", "The guide calls it 'Ranger itself'. First to 20."],
   ["Gale Arrow", "20", "Buff", "Gale: +9-15% combat speed and PvE damage for 10s. 20 adds the -10s cooldown pick."],
   ["Snare Shot", "20", "DPS", "+2-3% DPS with the castable-while-moving pick and the Shackling Arrow chain."],
   ["Snipe", "16", "DPS", "Held basic attack. 16 opens picks 4 and 5."],
   ["Drill Dart", "16", "DPS", "16 opens its extra-activation pick."],
   ["Tempest Shot", "16", "DPS", "The cancel skill at the top of your macro line."]],
  "pas": [
   ["Focused Eye", "PvE damage, Accuracy and Double Chance. Highest priority (KR endgame 36). Vaizel's Authority 10 multiplies it x1.5."],
   ["Hunter's Resolve", "Crit damage (KR 33-34)."]],
  "wings": "Eroded Wings 54.5%, Talisra 25.5%, Illusory Echo 6.5%",
  "src": [["KR Sep 6 optimizer (screenshots)", INV + "6450/19498"], KANON]},
 "sorcerer": {
  "first": ["Hellfire", "Blaze"],
  "act": [
   ["Hellfire", "20", "DPS", "The guide calls it 'Sorcerer itself'. First to 20."],
   ["Blaze", "20", "DPS", "3rd-5th biggest damage source; its hits cut Wish of Concentration's cooldown."],
   ["Firestorm", "20", "DPS", "Each fireball cuts Hellfire's cooldown by 2s."],
   ["Wish of Concentration", "20", "Buff", "Your required buff: +20% Attack, +100 Accuracy for 20s, and at 20 also +10% combat speed and -10s on all cooldowns."],
   ["Bittercold Wind", "20", "DPS", "Semi-required. If only one more skill can reach 20, take this over Winter's Shackles (shorter cooldown)."],
   ["Winter's Shackles", "16-20", "Buff", "+20% PvE damage for 5s on hit."],
   ["Flame Arrow", "16", "DPS", "Held basic attack. Korea's Feb guide had it second to 20; the Sep guide no longer lists it."],
   ["Flame Scattershot", "16", "DPS", "Stagger-window skill on the Hellfire key."]],
  "pas": [
   ["Robe of Flame", "The only passive you need: Accuracy, PvE damage and Double Chance (KR endgame 36). Element Enhancement 10 multiplies it x1.5."],
   ["Fire Mark", "Extra fire damage procs. Second in the Feb guide's order."],
   ["Vitality Evaporation", "Extra damage above 70% target HP. Third."]],
  "wings": "Talisra 91.5% (Sorcerer's kit doesn't use front/back damage)",
  "src": [["KR Sep 22 optimizer (screenshots)", INV + "6453/17462"], ["KR Feb 4 guide", VX + "675679"], KANON]},
 "spiritmaster": {
  "first": ["Combustion", "Elemental Fusion"],
  "act": [
   ["Combustion", "20", "DPS", "Highest-priority skill, and even more important once you hit the Attack cap."],
   ["Elemental Fusion", "20", "DPS", "The guide calls it 'Spiritmaster itself'."],
   ["Summon: Fire Spirit", "20", "DPS", "Your main spirit; 20 opens the +20% stats pick."],
   ["Cold Shock", "16-20", "Buff", "Held basic attack; keeps your 5-stack Attack buff running. Worth 20 if you can."],
   ["Jointstrike: Curse", "16", "Debuff", "Curse on the target."],
   ["Rapid Scattershot", "16", "DPS", "Stagger-window skill."],
   ["Summon: Water Spirit", "16", "DPS", "Returns MP on hits."],
   ["Summon: Earth Spirit", "16", "DPS", ""],
   ["Dimensional Control", "16", "DPS", "Use it once it reaches 16."]],
  "pas": [
   ["Spirit Strike", "PvE damage and Perfect for you and your spirit. Highest priority (KR endgame 36). Spirit's Benediction 10 multiplies it x1.5."],
   ["Element Unification", "Stacking crit damage (KR 29). Slightly ahead of Mental Focus."],
   ["Mental Focus", "Double Chance (KR 32)."],
   ["Spirit Revitalization", "Third tier: cuts spirit summon cooldowns."]],
  "wings": "Eroded Wings 45%, Talisra 43.5%",
  "src": [["KR Sep 16 optimizer (screenshots)", INV + "6454/10286"], ["KR newbie guide (Jul)", INV + "6454/8165"], KANON]},
 "cleric": {
  "first": ["Condemnation", "Earth's Retribution"],
  "act": [
   ["Condemnation", "20", "DPS", "The guide calls it 'Cleric itself': resets on crits."],
   ["Earth's Retribution", "20", "DPS", "Held basic attack and the source of your cancels; pick 4 cuts Bolt's cooldown."],
   ["Bolt", "20", "DPS", "2nd biggest damage source."],
   ["Divine Aura", "20", "DPS", "4th-5th biggest damage source."],
   ["Radiant Recovery", "16", "Heal", "16 is enough for damage-focused play; 20 adds a cleanse. Older healer guides took it to 20 first, so do that if your party keeps dying."],
   ["Healing Light", "16", "Heal", "16 is enough; 20 adds a cleanse chance."],
   ["Chain of Torment", "12", "Debuff", "12 opens the pick that lowers the target's PvE damage tolerance."],
   ["Light of Regeneration", "16", "Buff", "Party damage tolerance. The Feb guide called 20 important for full healers."]],
  "pas": [
   ["Earth's Grace", "Crit damage and Accuracy. Highest priority (KR endgame 36; +0.29% per level). Prayer of Amplification 15 multiplies it x1.5."],
   ["Empyrean Lord's Grace", "Crit, Double Chance and extra damage (KR 34; +0.15% per level). Prayer of Amplification 10 multiplies it x1.5."],
   ["Healing Enhancement", "Heal boost. Second in the Mar healer order."]],
  "wings": "Eroded Wings 45%, Talisra 35%, Illusory Echo 9%",
  "src": [["KR Sep 24 optimizer (screenshots)", INV + "6452/29213"], ["KR Mar 4 guide", VX + "688137"], KANON]},
 "chanter": {
  "first": ["Dark Crush", "Onslaught"],
  "act": [
   ["Dark Crush", "20", "DPS", "The guide calls it 'Chanter itself'. First to 20."],
   ["Onslaught", "20", "DPS", "Held basic attack and the source of your cancels; pick 4 cuts Spinning Strike's cooldown."],
   ["Spinning Strike", "20", "Buff", "Semi-required: big hit, +15% crit damage for 30s (2 stacks), and it opens Dark Crush."],
   ["Recuperation", "16-20", "Heal", "Semi-required for care: 16 gives two casts and +5% heal; 20 adds a cleanse or cooldown pick."],
   ["Incandescent Blow", "16", "DPS", "Macro filler."],
   ["Wave Blow", "16", "DPS", ""],
   ["Gust Rampage", "16", "DPS", "Stagger-window skill; useful when fights run long."],
   ["Impactful Crush", "12", "DPS", "Opens Dark Crush; take the +30% skill speed pick."]],
  "pas": [
   ["Wind's Promise", "Crit damage plus extra damage on crits. Highest priority (KR endgame 36). Guardian Blessing 15 multiplies it x1.5."],
   ["Impact Hit (chanter)", "Double Chance (KR 30). Slightly ahead of Attack Preparation."],
   ["Attack Preparation (chanter)", "PvE damage (KR 30)."],
   ["Inspiring Spell", "Crit and Perfect; small effect."]],
  "wings": "Eroded Wings 45%, Talisra 23%, Awaken Pride 12.5%",
  "src": [["KR Sep 17 optimizer (screenshots)", INV + "6451/22932"], ["KR Sep 1 skill guide", VX + "1257410"], KANON]},
}
for cid, s in SK.items():
    C[cid]["skills"] = s

# ---------------------------------------------------------------- KR/TW Gladiator correction
g = C["gladiator"]
for b in g["builds"]:
    if b.get("main"):
        b["pick"] = [["Lunge Stance", 25], ["Zikel's Blessing", 25], ["Wave Armor", 25], ["Lifestealing Blade", 20], ["Rage Burst", 20], ["Focused Block", 20]]
        b["why"] = ("Lunge Stance and Zikel's Blessing are fixed 25s for PvE and PvP. Wave Armor is the third: since the Jul 8 patch it multiplies both "
                    "Experienced Counterstrike and Murderous Burst x1.5 (that boost used to sit on Armor of Balance), and at 25 it hits twice. "
                    "Lifestealing Blade is about 6% of your damage. Rage Burst is +10% PvE damage at 20. Focused Block is the usual 6th: parries keep "
                    "Experienced Counterstrike up and cover mistakes.")
        b["src"] = [["Jul 7: Counterstrike boost moved to Wave Armor", INV + "6448/23042"], ["Aug 26: 'Lunge, Zikel's, Wave Armor fixed'", INV + "6448/30214"],
                    ["Jul 8: 6-slot PvE list", INV + "6448/23595"], ["Lifestealing share (dummy test)", INV + "6448/22823"]]
    elif b["t"].startswith("Battle tank"):
        b["pick"] = [["Lunge Stance", 25], ["Zikel's Blessing", 25], ["Wave Armor", 25], ["Focused Block", 20], ["Armor of Balance", 20], ["Rage Burst", 20]]
        b["why"] = ("When you hold the boss, Focused Block parries keep Experienced Counterstrike's party buff up and restore HP at 20, and Wave Armor "
                    "multiplies that buff. Armor of Balance is now the survival pick: x1.5 Blood Absorption and Protection Armor plus CC resist. "
                    "Players are main-tanking Trial stage 16 and Sanctuary 4 on Gladiator. For progression pulls, trade Rage Burst for Tenaciousness.")
        b["src"] = [["Trial 16 main tank report", INV + "6448/32301"], ["Jul 7: what each armor boosts now", INV + "6448/23042"], ["Assembled from the current effects", ""]]
g["builds"] = [b for b in g["builds"] if not b["t"].startswith("With a Templar")]
g["builds"].insert(2, {"t": "Behind a Templar", "tag": "Swap",
    "pick": [["Lunge Stance", 25], ["Zikel's Blessing", 25], ["Wave Armor", 25], ["Lifestealing Blade", 20], ["Rage Burst", 20], ["Armor of Balance", 20]],
    "why": "The Templar takes the block mechanics, so Focused Block can go. Armor of Balance fills the slot for its CC resist and lifesteal boost; it no longer adds damage.",
    "src": [["Jul 7: Armor of Balance lost its damage boost", INV + "6448/23031"]]})
g["order"] = [
    {"s": [["Lunge Stance", 10], ["Zikel's Blessing", 10], ["Rage Burst", 5]], "n": "Rage Burst 5 = -15s cooldown. Zikel's 10 = +10% PvE damage."},
    {"s": [["Wave Armor", 10], ["Lifestealing Blade", 10], ["Focused Block", 5]], "n": "Wave Armor 10 = x1.5 Experienced Counterstrike. Focused Block 5 = a second parry."},
    {"s": [["Lunge Stance", 20], ["Zikel's Blessing", 20]], "n": "Lunge 20: 50% chance to cut all cooldowns 1s on crit."},
    {"s": [["Wave Armor", 20], ["Lifestealing Blade", 20]], "n": "Wave Armor 15 = x1.5 Murderous Burst. Lifestealing 15 = -30s cooldown."},
    {"s": [["Rage Burst", 20], ["Focused Block", 20]], "n": "Rage Burst 20: +10% PvE damage boost."},
    {"s": [["Lunge Stance", 25], ["Zikel's Blessing", 25], ["Wave Armor", 25]], "n": "Leftover 3 levels: Lifestealing Blade 23."}]
g["tiers"]["A"] = [["Wave Armor", "x1.5 Counterstrike and Murderous Burst since Jul 8"], ["Lifestealing Blade", "About 6% of damage plus party Predation"],
                   ["Rage Burst", "+10% PvE damage at 20; in the macro"], ["Focused Block", "Parries keep Counterstrike up; the usual 6th slot"]]
g["tiers"]["B"] = [["Armor of Balance", "Tank lifesteal and CC resist; lost its damage boost Jul 8"], ["Tenaciousness", "Invulnerability for progression and PvE wipes, PvP"]]
g["imageNote"] = "Same five Korean Gladiators run. The sixth is Wave Armor."
for b in g["gl"]["builds"]:
    if b.get("main"):
        b["src"] = [["KR Season 1 fixed four", VX + "725199"], ["Jul 7: Counterstrike boost moved to Wave Armor", INV + "6448/23042"]]

# ---------------------------------------------------------------- notices / changelog
M["meta"]["updated"] = "2026-09-30"
M["meta"]["notice"] = ("Default view = Global Season 1: 4 stigma slots (confirmed on NC's official livestream) with stigma levels capped at 20 "
                       "(reported by Global guides). Switch to KR/TW for the 6-slot, level-25 builds.")
M["changelog"].insert(0, {"date": "2026-09-30", "text": (
    "Review pass + new 'Skills to level' section for every class: which DPS and buff skills to take to 20 / 16 / 12, the first two to push, "
    "passive priority, and where skill levels come from (from the Sep 2026 Korean optimizer guides and Kanon's Aion 2 Bible). "
    "New 'Damage basics' panel (stat priority, crit cap, ping, raid accuracy/crit targets). "
    "Fixed: the KR/TW Gladiator cards treated Armor of Balance as a damage pick; a Jul 8 patch moved that boost to Wave Armor, "
    "so Focused Block takes the sixth slot. Global's 4 stigma slots are now confirmed (official livestream).")})
json.dump(M, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# macro page: notice + one stale level-25 reference
P2 = ROOT + "data/macros.json"
t = open(P2, encoding="utf-8").read()
a = "Global (NA/EU) early access opens Sep 30, 2026, with full free-to-play on Oct 5."
assert a in t
t = t.replace(a, "Global (NA/EU) early access opened Sep 30, 2026, with full free-to-play on Oct 5.")
a = "then Triniel's Dagger (+10% back damage at 25) and Assault Ambush."
assert a in t
t = t.replace(a, "then Triniel's Dagger (cuts all your cooldowns by 10% at stigma level 10) and Assault Ambush.")
mj = json.loads(t)
mj["changelog"].insert(0, {"date": "2026-09-30", "text": (
    "Accuracy pass: every skill name, icon, cooldown and MP cost re-checked against the game database (all match). "
    "Restored the level 5-20 effects in stigma hover cards (the database changed its page layout and the updater had stopped reading them). "
    "Stigmas page gained a 'Skills to level' section and a damage-basics panel; KR/TW Gladiator stigmas corrected.")})
json.dump(mj, open(P2, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
