"""Stigmas page, 2026-09-30: add the Global Season 1 view (4 slots, stigma max 20) for all 8 classes,
per-stigma level targets with the reason to stop there, and the skill-specialization picks (3 of 5).

Sources are in each entry. Korean Season 1 (Nov 2025 - Mar 24 2026) is the closest real 4-slot / level-20
data; the Global client DB matches KR balance of roughly late August 2026 (it has the Aug 26 rework, not Sep 16).
"""
import json

ROOT = __file__.rsplit("tools", 1)[0]
P = ROOT + "data/stigmas.json"
M = json.load(open(P, encoding="utf-8"))
C = {c["id"]: c for c in M["classes"]}

INV = "https://www.inven.co.kr/board/aion2/"
VX = "https://vortexgaming.io/postdetail/"

# ---------------------------------------------------------------- Global Season 1: 4 slots, max level 20
GL = {
 "gladiator": {
  "builds": [
   {"t": "Party DPS", "tag": "Most used", "main": True,
    "pick": [["Lunge Stance", 20], ["Zikel's Blessing", 20], ["Rage Burst", 20], ["Wave Armor", 15]],
    "why": "Lunge Stance, Zikel's Blessing and Rage Burst were Korea's fixed Season 1 picks, and all three are still the core. Korea's 4th was Focused Block while Wave Armor was bugged (March). On the balance Global launched with, Wave Armor 10/15 multiplies Experienced Counterstrike and Murderous Burst by 1.5, so it's the better 4th when someone else holds the boss.",
    "src": [["KR Season 1 fixed four", VX + "725199"], ["Wave Armor vs Armor of Balance math", INV + "6448/22705"]]},
   {"t": "Battle tank (no Templar)", "tag": "Battle tank",
    "pick": [["Lunge Stance", 20], ["Rage Burst", 20], ["Focused Block", 20], ["Armor of Balance", 15]],
    "why": "Rage Burst 10 lowers the boss's Attack by 20% (Wounded), the best tank tool you have. Focused Block gives 2 parries from level 5 and heals 10% HP per parry at 20, and parrying keeps Experienced Counterstrike's frontal buff up. Armor of Balance 10/15 boosts your lifesteal and Protection Armor and adds CC resist. Short on threat or damage? Swap Armor of Balance for Zikel's Blessing.",
    "src": [["KR tank combo (no Templar)", INV + "6448/22575"], ["Built from those effects, trimmed to 4", ""]]},
   {"t": "Korea's Season 1 four", "tag": "Swap",
    "pick": [["Lunge Stance", 20], ["Rage Burst", 20], ["Zikel's Blessing", 20], ["Focused Block", 10]],
    "why": "What Korean Gladiators ran with 4 slots (Nov 2025 - Mar 2026). A safe start: Focused Block covers mistakes while you learn fights.",
    "src": [["KR Season 1 fixed four", VX + "725199"]]},
   {"t": "Solo / leveling", "tag": "Solo",
    "pick": [["Lunge Stance", 15], ["Rage Burst", 20], ["Lifestealing Blade", 15], ["Zikel's Blessing", 15]],
    "why": "Lifestealing Blade heals 10% of the damage it deals to up to 4 targets, and 15 cuts its cooldown by 30s. Rage Burst 5 alone brings its cooldown from 45s to 30s.",
    "src": [["Assembled from the stigma effects; not a single source", ""]]}],
  "levels": [
   ["Lunge Stance", 20, "15: x1.5 Identify Weakness. 20: 50% chance to cut all cooldowns by 1s on crits. Worth the full 75."],
   ["Zikel's Blessing", 20, "10: +10% PvE damage. 15: +50% multi-hit. 20 only adds status-effect chance, so stop at 15 if shards are tight."],
   ["Rage Burst", 20, "5: -15s cooldown. 10: Wounded lowers enemy Attack by 20%. 15: always crits. 20: +10% PvE damage."],
   ["Wave Armor", 15, "10: x1.5 Experienced Counterstrike. 15: x1.5 Murderous Burst. 20 only reflects 10% of damage taken, so skip it."],
   ["Focused Block", 10, "5: second parry. 10: castable while moving. Go to 20 only if you tank (10% HP per parry)."]],
  "order": [
   {"s": [["Lunge Stance", 10], ["Zikel's Blessing", 10], ["Rage Burst", 10]], "n": "Rage Burst 5 = -15s cooldown; 10 = boss -20% Attack."},
   {"s": [["Wave Armor", 10]], "n": "x1.5 Experienced Counterstrike."},
   {"s": [["Lunge Stance", 20], ["Zikel's Blessing", 15]]},
   {"s": [["Rage Burst", 20], ["Wave Armor", 15], ["Zikel's Blessing", 20]], "n": "Rage Burst 20: +10% PvE damage."}]},

 "templar": {
  "builds": [
   {"t": "Party tank", "tag": "Most used", "main": True,
    "pick": [["Taunt", 20], ["Noble Armor", 20], ["Shield of Protection", 10], ["Empyrean Lord's Punishment", 15]],
    "why": "Korea's 4-slot Templars fixed Taunt, Shield of Protection and Empyrean Lord's Punishment, and filled the 4th with Noble Armor. Taunt's Shrink makes the boss take more damage from the whole party. Noble Armor 15 multiplies Fury (your damage passive) by 1.5 and it never drops. Shield of Protection blocks stuns. Empyrean Lord's Punishment adds +10% PvE damage and stagger.",
    "src": [["KR Dec 24: Block, Punishment, Taunt fixed", INV + "6438/2684"], ["KR Feb 6 stigma guide (4 slots)", INV + "6438/7621"]]},
   {"t": "Geared DPS Templar", "tag": "Swap",
    "pick": [["Taunt", 20], ["Battlefield Banner", 20], ["Noble Armor", 20], ["Doom Shield", 15]],
    "why": "Battlefield Banner turns Defense into Attack, so it only pays off once your armor is upgraded; early on, Korean players called it poor value for the shards. Doom Shield opens Judgment (Aug 26 rework) and resets Annihilate at 5, which is what the sheet's late-game macro uses.",
    "src": [["Templar skill/stigma test (Banner value)", INV + "6438/12045"], ["KR current top picks", INV + "6438/27186"]]},
   {"t": "Hard content / party saver", "tag": "Raid",
    "pick": [["Taunt", 20], ["Shield of Protection", 15], ["Comrade in Arms", 20], ["Nezekan's Shield", 15]],
    "why": "Comrade in Arms redirects party damage to you and restores 50% of your HP at 20 ('the 4th effect is mandatory'). Nezekan's Shield puts a party shield up for unavoidable hits. Use this for learning hard bosses.",
    "src": [["KR Apr: Taunt, SoP, Comrade, Nezekan", INV + "6438/12045"], ["KR Feb: Comrade needs level 20", INV + "6438/7621"]]},
   {"t": "Solo / open world", "tag": "Solo",
    "pick": [["Doom Shield", 15], ["Noble Armor", 20], ["Second Skin", 20], ["Empyrean Lord's Punishment", 15]],
    "why": "Taunt does nothing solo. Korean players recommend Second Skin at 20 for solo play (the jump from 15 to 20 adds +20% PvE damage tolerance). Doom Shield opens each pull, resets on kills at 15, and resets Annihilate.",
    "src": [["KR Feb: 'solo = Second Skin 20'", INV + "6438/7621"]]}],
  "levels": [
   ["Taunt", 20, "5: Shrink cuts the boss's PvE damage tolerance by 10% for the party. 15: -5s cooldown. Korean players say you need 20 to keep it up permanently."],
   ["Noble Armor", 20, "15: x1.5 Fury, a big damage gain. 20: +10% healing received."],
   ["Shield of Protection", 10, "5: second block. 10: castable while moving. 15 and 20 (speed, 10% HP per block) are extras; one Korean tank says a single block is enough once you know the fight."],
   ["Empyrean Lord's Punishment", 15, "10: +50 stagger. 15: +10% PvE damage for 10s on hit. 20 is just +25% stun chance."],
   ["Battlefield Banner", 20, "Only once your Defense is high: 10: +10% weapon damage. 20: -30s cooldown."],
   ["Doom Shield", 15, "5: resets Annihilate. 10: +200 Block. 15: resets on kill. 20 is only knockdown chance."]],
  "order": [
   {"s": [["Taunt", 5], ["Shield of Protection", 5], ["Empyrean Lord's Punishment", 10]], "n": "The 3 fixed picks at their cheap unlocks first."},
   {"s": [["Taunt", 15], ["Noble Armor", 15]], "n": "Noble Armor 15 = x1.5 Fury."},
   {"s": [["Taunt", 20], ["Shield of Protection", 10], ["Empyrean Lord's Punishment", 15]]},
   {"s": [["Noble Armor", 20]]}]},

 "assassin": {
  "builds": [
   {"t": "PvE DPS", "tag": "Most used", "main": True,
    "pick": [["Illusive Clone", 20], ["Swift Contract", 20], ["Savage Fang", 15], ["Triniel's Dagger", 10]],
    "why": "Illusive Clone and Swift Contract are your burst window. Savage Fang is in the macro and gives +10% PvE damage at 15. Triniel's Dagger 10 cuts all your cooldowns by 10% on hit, and Korean guides stop it at 10.",
    "src": [["KR May: levelling priority", VX + "854915"], ["KR Nov: Triniel 10 + Clone 10 core", VX + "601044"]]},
   {"t": "Solo / farming", "tag": "Solo",
    "pick": [["Illusive Clone", 10], ["Swift Contract", 15], ["Throw Shadowblade", 20], ["Savage Fang", 15]],
    "why": "Throw Shadowblade resets on kills at 10 and becomes an AoE at 20, so packs die fast. Korean guides call it essential for field and Abyss hunting.",
    "src": [["KR May: Shadowblade for field hunting", VX + "854915"]]}],
  "levels": [
   ["Illusive Clone", 20, "10: +20% crit damage in the window (the must-have level). 15: x1.5 Exploit Weakness. 20: extra damage on crits."],
   ["Swift Contract", 20, "10: x1.5 Rear Smite. 15: x1.5 Assault Stance. 20: +10% more combat speed."],
   ["Savage Fang", 15, "10: +50 stagger. 15: +10% PvE damage for 10s. 20 (always crit) is last."],
   ["Triniel's Dagger", 10, "10: -10% all cooldowns on hit. 15 and 20 barely matter in PvE."],
   ["Throw Shadowblade", 10, "10: resets on kill. 20: AoE, for farming only."]],
  "order": [
   {"s": [["Illusive Clone", 10], ["Swift Contract", 10], ["Savage Fang", 10], ["Triniel's Dagger", 10]], "n": "Korean advice: if levels are 'awkwardly high' on one, drop it to 10 and spread shards."},
   {"s": [["Savage Fang", 15], ["Illusive Clone", 15], ["Swift Contract", 15]]},
   {"s": [["Illusive Clone", 20], ["Swift Contract", 20]]}]},

 "ranger": {
  "builds": [
   {"t": "PvE DPS", "tag": "Most used", "main": True,
    "pick": [["Vaizel's Authority", 20], ["Bow of Blessing", 20], ["Supporting Fire", 20], ["Griffon Arrow", 15]],
    "why": "Exactly the list in your image. Korean Rangers call these four the essential damage stigmas: Bow of Blessing and Vaizel's Authority need 20 to work properly, Supporting Fire always crits at 20, and Griffon Arrow is about 10% of your damage.",
    "src": [["KR: 'four essential' Ranger stigmas", VX + "722757"], ["Dummy test", INV + "6450/15518"]]},
   {"t": "Korea's Season 1 four", "tag": "Swap",
    "pick": [["Vaizel's Authority", 20], ["Bow of Blessing", 20], ["Arrow Storm", 10], ["Explosive Arrow", 10]],
    "why": "What Korean Rangers ran in Dec 2025, before Supporting Fire became the pick: both buffs, Arrow Storm for stagger, and Explosive Arrow (or Ambush Kick).",
    "src": [["KR Dec 24 thread", INV + "6450/1736"]]},
   {"t": "Solo / survival", "tag": "Solo",
    "pick": [["Vaizel's Authority", 20], ["Bow of Blessing", 20], ["Supporting Fire", 20], ["Mother Nature's Breath", 10]],
    "why": "Mother Nature's Breath is Korea's 6th-slot pick: damage tolerance, crit resist and a heal chance. It cleanses damage-over-time at 5.",
    "src": [["25 and 6th slot summary", INV + "6450/15571"]]}],
  "levels": [
   ["Vaizel's Authority", 20, "10: x1.5 Focused Eye. 15: x1.5 Hunter's Soul. 20: 50% chance to cut all cooldowns 1s on crits."],
   ["Bow of Blessing", 20, "10: Attack from Crit. 15: +20% crit damage. 20: +7% Double Chance."],
   ["Supporting Fire", 20, "5: +25% fire chance. 10: +15s duration. 15: -30s cooldown. 20: always crits."],
   ["Griffon Arrow", 15, "5: castable while moving. 10: +5s burn. 15: Enhanced Crimson Flames. 20 (burn ticks twice as fast) when shards allow."]],
  "order": [
   {"s": [["Vaizel's Authority", 10], ["Bow of Blessing", 10], ["Supporting Fire", 10], ["Griffon Arrow", 5]]},
   {"s": [["Supporting Fire", 15], ["Vaizel's Authority", 15], ["Bow of Blessing", 15]], "n": "Bow 15 = +20% crit damage."},
   {"s": [["Vaizel's Authority", 20], ["Bow of Blessing", 20], ["Supporting Fire", 20]]},
   {"s": [["Griffon Arrow", 15]]}]},

 "sorcerer": {
  "builds": [
   {"t": "PvE DPS", "tag": "Most used", "main": True,
    "pick": [["Element Enhancement", 20], ["Fire Wall", 20], ["Delayed Explosion", 20], ["Cold Storm", 15]],
    "why": "Element Enhancement, Fire Wall and Delayed Explosion were Korea's top three with 4 slots and still are. For the 4th, your image and current Korean damage players take Cold Storm. Korea's Feb 4-slot guide took Steel Barrier for safety (see the swap). With two Sorcerers in a party, only one Cold Storm counts.",
    "src": [["KR Feb 4: 4-slot priority", VX + "675679"], ["KR Sep: 'we're DPS, Cold Storm first'", INV + "6453/17196"]]},
   {"t": "Korea's Season 1 four (safer)", "tag": "Swap",
    "pick": [["Element Enhancement", 20], ["Fire Wall", 20], ["Delayed Explosion", 20], ["Steel Barrier", 10]],
    "why": "The Feb 4 guide's order: Element Enhancement, Fire Wall, Delayed Explosion, Steel Barrier. Beginner path: Element Enhancement 5, Delayed Explosion 10, Element Enhancement 15, Fire Wall 20, then Steel Barrier 5-10.",
    "src": [["KR Feb 4 Sorcerer guide", VX + "675679"]]},
   {"t": "Hard content", "tag": "Raid",
    "pick": [["Element Enhancement", 20], ["Fire Wall", 20], ["Arctic Armor", 20], ["Delayed Explosion", 15]],
    "why": "Arctic Armor adds 20% PvE damage tolerance (40% at 20) and turns part of the damage you take into MP loss, so you can stand in mechanics and keep casting.",
    "src": [["KR: Arctic Armor for raids", INV + "6453/17368"]]}],
  "levels": [
   ["Element Enhancement", 20, "10: x1.5 Robe of Flame. 15: x1.5 Grace of Enhancement. 20: another +10% Fire and Water Attack."],
   ["Fire Wall", 20, "5: Embers deal extra damage. 15: +2s wall. 20: +10s Embers (near-permanent burn)."],
   ["Delayed Explosion", 20, "10: -10s cooldown. 15: becomes AoE. 20: +10% damage taken from you (on top of 15%)."],
   ["Cold Storm", 15, "5: Frostbite deals extra damage. 15: +3s storm. 20: +10s Frostbite when shards allow."],
   ["Steel Barrier", 10, "5: +10% move speed. 10: HP regen. 15: +10% PvE tolerance if you want it tankier."]],
  "order": [
   {"s": [["Element Enhancement", 5], ["Delayed Explosion", 10], ["Element Enhancement", 15], ["Fire Wall", 20]], "n": "The Korean Feb beginner path, step for step."},
   {"s": [["Element Enhancement", 20], ["Cold Storm", 10]]},
   {"s": [["Delayed Explosion", 20], ["Cold Storm", 15]]}]},

 "spiritmaster": {
  "builds": [
   {"t": "PvE DPS", "tag": "Most used", "main": True,
    "pick": [["Jointstrike: Corrode", 20], ["Summon: Ancient Spirit", 20], ["Flame Blessing", 20], ["Enhance: Spirit's Benediction", 20]],
    "why": "Exactly your image. Korean Spiritmasters call these four the only real PvE stigmas; everything else costs damage.",
    "src": [["'Only 4 usable PvE stigmas'", INV + "6454/8922"], ["Newbie guide stigma table", INV + "6454/8165"]]},
   {"t": "Survival / solo", "tag": "Solo",
    "pick": [["Jointstrike: Corrode", 20], ["Summon: Ancient Spirit", 20], ["Enhance: Spirit's Benediction", 20], ["Siphon", 15]],
    "why": "Siphon heals, restores MP, and from 15 shields you for 30% of max HP for 30s.",
    "src": [["Siphon for survival", INV + "6454/10248"]]}],
  "levels": [
   ["Jointstrike: Corrode", 20, "5: +15% spirit damage on the target. 20: +10s, so it barely drops. Level it first."],
   ["Summon: Ancient Spirit", 20, "10: x1.5 Spirit's Descent. 15: skill after 5 basic attacks. 20: +20% spirit stats."],
   ["Flame Blessing", 20, "15: +10% crit damage. 20: extra-damage proc cooldown halved. 20 is the big one."],
   ["Enhance: Spirit's Benediction", 20, "10: x1.5 Spirit Strike. 15: x1.5 Spirit Communion. 20: +25% PvE damage and tolerance for you and the spirit."]],
  "order": [
   {"s": [["Jointstrike: Corrode", 10], ["Summon: Ancient Spirit", 10], ["Flame Blessing", 10], ["Enhance: Spirit's Benediction", 10]]},
   {"s": [["Jointstrike: Corrode", 20]], "n": "Korean advice: if you can only push one, push Corrode."},
   {"s": [["Summon: Ancient Spirit", 20], ["Enhance: Spirit's Benediction", 20]]},
   {"s": [["Flame Blessing", 20]]}]},

 "cleric": {
  "builds": [
   {"t": "Party healer", "tag": "Most used", "main": True,
    "pick": [["Earth Punishment", 20], ["Prayer of Amplification", 20], ["Light of Protection", 15], ["Benevolence", 20]],
    "why": "Korea's 4-slot Clerics always ran Light of Protection 15 and Earth Punishment 20, and by March added Prayer of Amplification 15 as the third. For the 4th, Benevolence (group heal-over-time, cleanse every 5s at 20) is what Korean Clerics bring for care now; it isn't in their Season 1 lists, so it likely arrived in March. Take Prayer to 20 only if you're not already at the Attack cap.",
    "src": [["KR Mar 4: fixed three + levels", VX + "688137"], ["KR Feb 4: LoP 15 + Earth Punishment 20 fixed", INV + "6452/7695"], ["KR Sep: Benevolence in care presets", INV + "6452/28978"]]},
   {"t": "With a Chanter in the party", "tag": "Swap",
    "pick": [["Earth Punishment", 20], ["Prayer of Amplification", 20], ["Noble Aura", 15], ["Benevolence", 20]],
    "why": "Chanter's Undefeated Mantra overrides your Light of Protection (higher level wins), so the slot goes to Noble Aura: +30% damage to bosses (Incapacitated Immunity) at 15.",
    "src": [["Presets with / without Chanter", INV + "6452/28978"]]},
   {"t": "Korea's Season 1 four", "tag": "Swap",
    "pick": [["Light of Protection", 15], ["Earth Punishment", 20], ["Prayer of Amplification", 15], ["Salvation", 15]],
    "why": "The Mar 4 guide's PvE set. The 4th is situational: Salvation 15 (party lowest-HP gets it too), Voice of Doom 15, or Summon Resurrection 5 for learning runs.",
    "src": [["KR Mar 4 Cleric guide", VX + "688137"]]},
   {"t": "Solo DPS", "tag": "Solo",
    "pick": [["Earth Punishment", 20], ["Prayer of Amplification", 20], ["Noble Aura", 15], ["Light of Protection", 15]],
    "why": "Korea's Feb solo/damage set was Light of Protection, Earth Punishment, an aura pet and Prayer of Amplification. Noble Aura is that pet: it follows you for 5 minutes and hits your target.",
    "src": [["KR Feb 27 Cleric guide", VX + "684217"]]}],
  "levels": [
   ["Earth Punishment", 20, "5: Condemnation always crits on the target. 10: party Double Chance. 15: party Attack and Defense. 20: +10s. The one to push first."],
   ["Prayer of Amplification", 20, "5: +20% PvE damage boost (huge for 5 shards). 10/15: x1.5 two passives. 20: +15% Attack, useless if you're at the Attack cap."],
   ["Light of Protection", 15, "5: +10% healing received. 15: +10% max HP. Korea's 4-slot level was 15."],
   ["Benevolence", 20, "5: +10s duration. 15: 2% HP every 5s. 20: cleanses every 5s."],
   ["Noble Aura", 15, "15: +30% damage to bosses. 20: attacks 1s faster."],
   ["Salvation", 15, "10: heals 20% at the end. 15: also protects your lowest-HP party member."]],
  "order": [
   {"s": [["Earth Punishment", 10], ["Prayer of Amplification", 5], ["Light of Protection", 5], ["Benevolence", 5]], "n": "Korean advice: get every pick to its first level, then push Earth Punishment to 20."},
   {"s": [["Earth Punishment", 20]]},
   {"s": [["Prayer of Amplification", 15], ["Light of Protection", 15], ["Benevolence", 15]]},
   {"s": [["Benevolence", 20], ["Prayer of Amplification", 20]]}]},

 "chanter": {
  "builds": [
   {"t": "Buffer", "tag": "Most used", "main": True,
    "pick": [["Undefeated Mantra", 20], ["Power of the Storm", 20], ["Guardian Blessing", 15], ["Sprint Mantra", 10]],
    "why": "Korea's 4-slot Chanters put Undefeated Mantra at 20 first and called Power of the Storm mandatory. Guardian Blessing 15 multiplies Wind's Promise by 1.5, and Korean players call 15 the minimum. Sprint Mantra's low levels are cheap and strong. Marchutan's Wrath is optional now: Dark Crush opens after any ranged skill since the Aug 26 rework.",
    "src": [["KR Mar 4 Chanter guide", VX + "688518"], ["Chanter PvE guide (level order)", INV + "6451/116"], ["KR Sep 17: Marchutan's no longer required", INV + "6451/22932"]]},
   {"t": "Battle healer (no Cleric)", "tag": "Battle healer",
    "pick": [["Undefeated Mantra", 20], ["Power of the Storm", 15], ["Healing Touch", 20], ["Impeding Authority", 15]],
    "why": "Healing Touch heals the party and removes 5 debuffs at 15 (+5% heal at 20). Impeding Authority shields the party for 16% of max HP and adds 10% PvE tolerance at 15. Korea's Mar guide lists both as the care picks.",
    "src": [["KR Mar 4: care picks", VX + "688518"], ["No-Cleric party run", INV + "6451/116"]]},
   {"t": "Your image (5) trimmed to 4", "tag": "Swap",
    "pick": [["Undefeated Mantra", 20], ["Power of the Storm", 20], ["Sprint Mantra", 10], ["Marchutan's Wrath", 15]],
    "why": "If you like pressing Marchutan's Wrath: it hits 4 targets and opens Dark Crush for 3s. 10 adds a stun chance.",
    "src": [["Chanter PvE guide", INV + "6451/116"]]}],
  "levels": [
   ["Undefeated Mantra", 20, "5: +100 Crit. 10: +100 Accuracy. 15: +5% crit damage. 20: +5% Double Chance. First to 20."],
   ["Power of the Storm", 20, "5: -30s cooldown (120s to 90s). 20: +20% Attack for you, +10% for the party."],
   ["Guardian Blessing", 15, "10: x1.5 Crossguard. 15: x1.5 Wind's Promise, the reason to take it. 20 only adds healing received."],
   ["Sprint Mantra", 10, "5: +10% healing received. 10: +30% stamina regen. The guide says low levels are the value; 15-20 later."],
   ["Healing Touch", 15, "15: removes 5 debuffs. 20: +5% heal."]],
  "order": [
   {"s": [["Undefeated Mantra", 5], ["Power of the Storm", 5], ["Sprint Mantra", 5], ["Guardian Blessing", 5]], "n": "The Korean guide's opening order (Marchutan's replaced by Guardian Blessing)."},
   {"s": [["Undefeated Mantra", 20]]},
   {"s": [["Sprint Mantra", 10], ["Power of the Storm", 20]]},
   {"s": [["Guardian Blessing", 15]]}]},
}

GTIERS = {
 "templar": {
  "S": [["Taunt", "Party-wide boss debuff; the reason DPS want a Templar"], ["Noble Armor", "x1.5 Fury at 15 plus always-on HP"]],
  "A": [["Shield of Protection", "Blocks stuns (2 uses at 5)"], ["Empyrean Lord's Punishment", "+10% PvE damage and stagger"], ["Battlefield Banner", "Strong once Defense is high; weak early"], ["Doom Shield", "Engage, opens Judgment, resets Annihilate"]],
  "B": [["Comrade in Arms", "Party saver for hard bosses (needs 20)"], ["Nezekan's Shield", "Party shield for hard raids"], ["Second Skin", "Solo survival at 20"], ["Assault Fury", "Natural-block DPS setups"]],
  "C": [["Grapple", "Pulls, PvP"], ["Armor of Balance", "PvP CC resist"], ["Executing Blade", "Korean players call it a design miss"]]},
 "gladiator": {
  "S": [["Lunge Stance", "Combat speed plus cooldown cuts on crit"], ["Zikel's Blessing", "+20% Attack, +10% PvE damage"], ["Rage Burst", "-20% boss Attack, +10% PvE damage"]],
  "A": [["Wave Armor", "x1.5 two damage passives at 10/15"], ["Focused Block", "Parries for tanking and pugs"], ["Lifestealing Blade", "Sustain and party Predation"]],
  "B": [["Armor of Balance", "Tank lifesteal and CC resist"], ["Tenaciousness", "Invulnerability for progression and PvP"]],
  "C": [["Blade Toss", "PvP heal cut"], ["Forced Restraint", "PvP Seal"], ["Fracturing Rush", "PvP gap-closer"], ["Wrath Wave", "AoE knockdown"], ["Assault Strike", "Shared Assault skill"]]},
 "sorcerer": {
  "S": [["Element Enhancement", "+Fire and Water Attack; x1.5 two passives"], ["Fire Wall", "Embers damage-over-time"], ["Delayed Explosion", "Boss takes +15-25% damage from you"]],
  "A": [["Cold Storm", "Frostbite damage-over-time; one per party"], ["Steel Barrier", "Korea's Season 1 4th pick"], ["Arctic Armor", "Tolerance and Mana Conversion"]],
  "B": [["Hibernation", "Invulnerability for raids and PvP"], ["Divine Burst", "Burst plus lifesteal, clunky"]],
  "C": [["Glacial Smite", "PvP single-target"], ["Soul Freeze", "PvP Seal"], ["Lumiel's Space", "PvP Aerial Bind"], ["Curse: Tree", "PvP polymorph"], ["Assault Bombardment", "Shared Assault skill"]]},
}

# tier text that assumed level 25 -> cap-neutral wording (KR/TW view keeps the same ranks)
RETIER = {
 ("assassin", "Smoke Bomb"): "Blind; Weakness at 25 (KR/TW); mostly PvP",
 ("cleric", "Prayer of Amplification"): "+20% PvE damage at 5; top damage pick",
 ("cleric", "Noble Aura"): "5-minute pet; +30% vs bosses at 15",
 ("cleric", "Salvation"): "Invulnerability; also covers lowest-HP ally at 15",
 ("sorcerer", "Fire Wall"): "Embers damage-over-time",
 ("sorcerer", "Delayed Explosion"): "Boss takes +15-25% damage from you",
 ("templar", "Second Skin"): "Personal tolerance; solo pick at 20",
 ("gladiator", "Lunge Stance"): "Combat speed plus crit procs",
 ("gladiator", "Zikel's Blessing"): "+20% Attack, +10% PvE damage",
 ("spiritmaster", "Flame Blessing"): "Extra damage procs; proc cooldown halved at 20",
 ("spiritmaster", "Siphon"): "Heal and 30% HP shield at 15",
 ("ranger", "Vaizel's Authority"): "+20% Attack; strongest buff",
}

# ---------------------------------------------------------------- skill specializations (3 of 5)
# pick = options at skill level 20 (numbers = in-game order, same as the DB), u20 = the 2 to run before 20.
SPECS = {
 "templar": [
  {"n": "Judgment", "pick": [3, 4, 5], "u20": [5, 3], "note": "Swap 3 for 1 (30% lifesteal) when you need sustain.", "src": "sep5"},
  {"n": "Pummel", "pick": [3, 4, 5], "u20": [3, 4], "note": "The core of the Pummel-Judgment weave.", "src": "sep5"},
  {"n": "Vicious Strike", "pick": [3, 4, 5], "u20": [4, 5], "note": "Required for the Vicious Strike-Judgment setup.", "src": "sep5"},
  {"n": "Punishment", "pick": [2, 3, 4], "note": "2 and 3 fixed. Third: 4 (castable while moving) for comfort, or 5 (ignores block/evasion, crits) for a little more damage.", "src": "sep5"},
  {"n": "Annihilate", "pick": [3, 4, 1], "u20": [3, 4], "note": "1 (+50% multi-hit) nudges the ceiling at 20.", "src": "sep5"},
  {"n": "Warding Strike", "pick": [1, 5], "note": "Level 16 is enough: -5s cooldown and the party damage-tolerance share.", "src": "jan"},
  {"n": "Shield Smite", "pick": [2, 3], "note": "Level 12: no MP cost, and a 50% chance to trigger Debilitating Smash.", "src": "mar_te"}],
 "gladiator": [
  {"n": "Overhead Slam", "pick": [3, 4, 5], "note": "Upward Strike chain, guaranteed crit, no cooldown.", "src": "sep5g"},
  {"n": "Rending Blow", "pick": [3, 4, 5], "note": "The Overhead Slam-Rending Blow cancel skill.", "src": "sep5g"},
  {"n": "Ruinous Blow", "pick": [1, 4, 2], "note": "1 and 4 fixed. Third: 2 (+12.5m range) for comfort, or 5 for a little more damage. No longer needs level 20.", "src": "sep5g"}],
 "assassin": [
  {"n": "Quick Slice", "pick": [3, 4, 5], "note": "From a 6.9M-DPS setup (Sep 18). Use 2, 4, 5 if you need lifesteal.", "src": "sep18"},
  {"n": "Heart Gore", "pick": [2, 4, 5], "note": "1 instead of 2 for sustain; 3, 4, 5 if your crit is low.", "src": "mar_as"},
  {"n": "Savage Roar", "pick": [2, 3, 4], "note": "4 (-1s Shadowstrike cooldown) is the key one.", "src": "mar_as"},
  {"n": "Insignia Explosion", "pick": [2, 3, 5], "note": "Fixed for PvE.", "src": "may_as"},
  {"n": "Ambush", "pick": [1, 2, 4], "note": "Sep 18: drop 5 (extra uses) for 1 and 4. Press it on its own key, not in the macro.", "src": "sep18"},
  {"n": "Shadowstrike", "pick": [2, 5], "note": "2 (+20% crit damage) from level 8.", "src": "may_as"}],
 "ranger": [
  {"n": "Deadshot", "pick": [2, 3, 5], "note": "3 (castable while moving) in real fights; 4 (multi-hit) instead on a training dummy.", "src": "sep6"},
  {"n": "Gale Arrow", "pick": [3, 4, 5], "note": "A small damage gain, worth 20.", "src": "sep6"},
  {"n": "Snare Shot", "pick": [2, 3, 4], "note": "+2-3% DPS; take it to 20 for the mobile specialty.", "src": "sep6"},
  {"n": "Snipe", "pick": [4, 5], "note": "Skip 2 and 3: Ranger multi-hit is already 87-94%.", "src": "sep6"},
  {"n": "Drill Dart", "pick": [1, 5], "note": "The multi-hit option is wasted for the same reason.", "src": "sep6"},
  {"n": "Tempest Shot", "pick": [3, 5], "note": "Skip 2 (+10% crit) once your crit is capped.", "src": "sep6"}],
 "sorcerer": [
  {"n": "Hellfire", "pick": [1, 4, 5], "note": "Level 20 required.", "src": "sep22"},
  {"n": "Blaze", "pick": [3, 4, 5], "note": "3rd-5th biggest damage source.", "src": "sep22"},
  {"n": "Firestorm", "pick": [2, 4, 5], "u20": [2, 5], "src": "sep22"},
  {"n": "Wish of Concentration", "pick": [2, 4, 5], "u20": [4, 5], "note": "Your required buff.", "src": "sep22"},
  {"n": "Bittercold Wind", "pick": [1, 2, 4], "u20": [1, 2], "note": "2 frees you from standing still.", "src": "sep22"},
  {"n": "Winter's Shackles", "pick": [3, 5, 1], "u20": [3, 5], "note": "If you can only take one of these two to 20, take Bittercold Wind.", "src": "sep22"},
  {"n": "Flame Arrow", "pick": [3, 4, 5], "src": "feb_so"},
  {"n": "Flame Scattershot", "pick": [4, 5], "note": "Level 16.", "src": "feb_so"}],
 "spiritmaster": [
  {"n": "Elemental Fusion", "pick": [2, 3, 5], "note": "The charge option (4) tested worse.", "src": "sep16"},
  {"n": "Combustion", "pick": [2, 4, 5], "note": "Even more important once you hit the Attack cap.", "src": "sep16"},
  {"n": "Summon: Fire Spirit", "pick": [2, 3, 5], "src": "sep16"}],
 "cleric": [
  {"n": "Condemnation", "pick": [2, 4, 5], "note": "Level 20 required.", "src": "sep24"},
  {"n": "Earth's Retribution", "pick": [2, 3, 4], "note": "Your basic-attack cancel skill.", "src": "sep24"},
  {"n": "Bolt", "pick": [3, 4, 5], "note": "2nd biggest damage source.", "src": "sep24"},
  {"n": "Divine Aura", "pick": [3, 4, 5], "src": "sep24"},
  {"n": "Healing Light", "pick": [1, 4, 3], "u20": [1, 4], "note": "16 is enough; 3 adds a cleanse at 20.", "src": "sep24"},
  {"n": "Radiant Recovery", "pick": [2, 5, 1], "u20": [2, 5], "note": "16 is enough; 1 (removes 2 debuffs) at 20.", "src": "sep24"},
  {"n": "Chain of Torment", "pick": [2, 4, 5], "u20": [2, 4], "src": "feb_cl"}],
 "chanter": [
  {"n": "Dark Crush", "pick": [3, 4, 5], "note": "Fixed.", "src": "sep17"},
  {"n": "Onslaught", "pick": [3, 4, 5], "note": "Use 2, 4, 5 for more stable lifesteal.", "src": "sep17"},
  {"n": "Spinning Strike", "pick": [1, 3, 5], "note": "Use 2, 3, 5 for more healing when there's no Cleric.", "src": "sep17"},
  {"n": "Recuperation", "pick": [1, 4, 2], "u20": [1, 4], "note": "Third: 2 if the fight has debuffs to cleanse, otherwise 5.", "src": "sep17"},
  {"n": "Impactful Crush", "pick": [4], "note": "+30% skill speed; no other option is worth much.", "src": "sep9"}],
}
SPSRC = {
 "sep5": ["KR Sep 5 Templar optimizer (screenshots)", INV + "6438/25862"],
 "jan": ["KR Templar skill guide (Jan, edited Apr)", INV + "6438/6625"],
 "mar_te": ["KR Mar 13 Templar guide", VX + "696602"],
 "sep5g": ["KR Sep 5 Gladiator optimizer (screenshots)", INV + "6448/31551"],
 "sep18": ["KR Sep 18 Assassin setup (screenshot)", INV + "6449/23617"],
 "mar_as": ["KR Mar 31 Assassin specialization guide", VX + "726439"],
 "may_as": ["KR May Assassin PvE guide", VX + "854915"],
 "sep6": ["KR Sep 6 Ranger optimizer (screenshots)", INV + "6450/19498"],
 "sep22": ["KR Sep 22 Sorcerer optimizer (screenshots)", INV + "6453/17462"],
 "feb_so": ["KR Feb 4 Sorcerer guide", VX + "675679"],
 "sep16": ["KR Sep 16 Spiritmaster optimizer (screenshots)", INV + "6454/10286"],
 "sep24": ["KR Sep 24 Cleric optimizer (screenshots)", INV + "6452/29213"],
 "feb_cl": ["KR Feb 27 Cleric guide", VX + "684217"],
 "sep17": ["KR Sep 17 Chanter optimizer (screenshots)", INV + "6451/22932"],
 "sep9": ["KR Sep 9 Chanter setup", VX + "1264072"],
}

IMAGE_NOTES = {
 "assassin": "3 of 4 match. Throw Shadowblade is the farming pick (resets on kills). For bosses, Korean guides take Triniel's Dagger at 10 instead.",
 "cleric": "Your list has 6; with 4 slots keep Earth Punishment, Prayer of Amplification, Light of Protection and Benevolence. Noble Aura replaces Light of Protection when a Chanter is with you. Summon Resurrection is for learning runs only.",
 "sorcerer": "Exactly the Global main build.",
 "templar": "Your list is the damage-leaning version: Battlefield Banner and Doom Shield pay off once your armor is upgraded (see Geared DPS Templar). Korea's 4-slot tanks took Noble Armor and Empyrean Lord's Punishment first.",
 "chanter": "Your list has 5; with 4 slots, Marchutan's Wrath is the one to cut, since Dark Crush opens after any ranged skill since the Aug 26 rework. Guardian Blessing stays for its level-15 effect.",
 "gladiator": "Your list has 5. Lunge Stance, Zikel's Blessing and Rage Burst are the core. For the 4th: Focused Block if you're tanking or learning a fight, Wave Armor for damage behind a Templar. Lifestealing Blade is the solo pick.",
 "spiritmaster": "Exactly the Global main build.",
 "ranger": "Exactly the Global main build."
}

for cid, g in GL.items():
    c = C[cid]
    c["gl"] = dict(g, imageNote=IMAGE_NOTES[cid])
    if cid in GTIERS:
        c["gtiers"] = GTIERS[cid]
    c["specs"] = [dict(s, src=SPSRC[s["src"]]) for s in SPECS[cid]]
    for tier in c["tiers"].values():
        for row in tier:
            if (cid, row[0]) in RETIER:
                row[1] = RETIER[(cid, row[0])]

M["meta"]["updated"] = "2026-09-30"
M["meta"]["notice"] = ("Default view = Global Season 1: 4 stigma slots, stigma level capped at 20. That's what Global-focused guides "
                       "report (NCSOFT hasn't published it). Switch to KR/TW for the 6-slot, level-25 builds.")
M["changelog"].insert(0, {"date": "2026-09-30", "text": (
    "Global Season 1 view (now the default): 4-slot builds capped at level 20 for all 8 classes, a 'how high to level each' list "
    "with the reason to stop there, Season 1 level-up orders, and Korea's own 4-slot builds (Nov 2025 - Mar 2026) for comparison. "
    "New skill-specialization section: the 3 of 5 specialties to pick for each class's core skills, read from the Sep 2026 Korean "
    "optimizer screenshots and matched to the Global database's English options.")})
json.dump(M, open(P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
