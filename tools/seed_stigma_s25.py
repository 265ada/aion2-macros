"""One-off seed (2026-09-29): level-25 specialties and KR/TW notes for all 104 stigmas.

Level-25 text: skills.json s25 (already patch-corrected) where it exists, otherwise the Jul 1, 2026 KR in-game
tooltips posted on the Inven class boards. Run before tools/fetch_stigmas.py (which keeps these fields).
"""
import json, os

ROOT = __file__.rsplit("tools", 1)[0]
S = json.load(open(ROOT + "data/skills.json", encoding="utf-8"))

S25 = {
 "gladiator": {
  "Wrath Wave": "Becomes a ranged skill", "Focused Block": "+1s block duration",
  "Armor of Balance": "+30% Ailment Resist for the duration", "Blade Toss": "Chains up to 2 extra hits",
  "Tenaciousness": "+2s duration", "Forced Restraint": "Ignores Block and Evasion",
  "Assault Strike": "-1 min cooldown", "Fracturing Rush": "Adds a 3rd chain skill"},
 "templar": {
  "Empyrean Lord's Punishment": "+200% damage to targets with Incapacitated Immunity",
  "Nezekan's Shield": "+100% shield amount", "Armor of Balance": "+30% Ailment Resist for the duration",
  "Second Skin": "Enrage effect x1.5 and -30s cooldown (Jul 8)",
  "Executing Blade": "Target's skill cooldowns +3%", "Comrade in Arms": "+20% Ailment Resist for the duration",
  "Grapple": "+2 targets", "Assault Fury": "-1 min cooldown",
  "Battlefield Banner": "+10% Combat Speed for the duration"},
 "assassin": {
  "Swift Contract": "+10% Attack for the duration", "Smoke Bomb": "Applies Weakness for 5s on hit",
  "Evasion Stance": "+1s duration", "Spiral Slice": "Ignores Block and Evasion",
  "Shadow Walk": "Attacking from behind while stealthed stuns for 3s", "Aerial Bind": "Ignores Block and Evasion",
  "Evasion Contract": "Removes damage-over-time effects and grants immunity to them",
  "Shadowstep": "+2s stealth duration"},
 "ranger": {
  "Arrow Storm": "Up to -30s cooldown, more the more targets it hits", "Ambush Kick": "2s stealth on use",
  "Ensnaring Trap": "Ignores Block and Evasion", "Illusory Arrow": "Applies Weakness for 5s on hit",
  "Stealth": "Attacking from stealth grants +1000 Crit for 5s",
  "Sealing Arrow": "Ignores Block and Evasion",
  "Mother Nature's Breath": "+15% Mother Nature proc chance", "Assault Smite": "-1 min cooldown"},
 "sorcerer": {
  "Divine Burst": "+100% damage to targets with Incapacitated Immunity",
  "Steel Barrier": "No extra damage from rear attacks", "Curse: Tree": "+50% Transformation hit chance",
  "Arctic Armor": "Stronger Mana Conversion (less HP and MP lost)",
  "Soul Freeze": "Ignores Block and Evasion",
  "Lumiel's Space": "Double Aerial Bind chance on Frozen or Slowed targets",
  "Hibernation": "Breaking Hibernation has a 75% chance to Freeze up to 4 nearby enemies for 3s",
  "Assault Bombardment": "-1 min cooldown"},
 "spiritmaster": {
  "Flame Blessing": "+100% damage to targets with Incapacitated Immunity (raised from 50%)",
  "Kaisinel's Power": "+30% duration", "Siphon": "+30% shield amount",
  "Cry of Terror": "-30s cooldown", "Cursed Cloud": "Damage-over-time ticks 50% faster",
  "Seize Magic": "Ignores Block and Evasion", "Magic Block": "Ignores Block and Evasion",
  "Assault Terror": "-50% cooldown",
  "Command: Proxy": "Spirits can't drop below 50% HP while Proxy is active"},
 "cleric": {
  "Power Burst": "+200% damage to targets with Incapacitated Immunity",
  "Absolution": "+10% instant heal and +3% heal over time",
  "Benevolence": "Action Points, HP and cleanse ticks come 1s faster",
  "Prayer of Amplification": "+10% PvE and +5% PvP Damage Boost",
  "Summon Resurrection": "On cast, grants an in-place resurrection for 1 min",
  "Salvation": "Gives the whole party Salvation's base effect",
  "Root": "Ignores Block and Evasion", "Light of Protection": "+5% Double Chance",
  "Yustiel's Power": "Shield gains another 20% of max HP",
  "Voice of Doom": "-20% target Ailment Resist for the duration", "Assault Mark": "-1 min cooldown"},
 "chanter": {
  "Obliterate": "+200% damage to targets with Incapacitated Immunity",
  "Focused Defense": "+1s Weapon Block duration",
  "Impeding Authority": "+10% PvE and +5% PvP Damage Tolerance",
  "Healing Touch": "-5s cooldown", "Assault Shock": "-1 min cooldown",
  "Barrier Spell": "Removes all debuffs when it ends naturally"},
}

NOTES = {
 "gladiator:Zikel's Blessing": "KR/TW Jul 8: self only (no longer party-wide); base effect adds +100 Accuracy.",
 "gladiator:Lunge Stance": "KR/TW Aug 12: the 20% MP-cost reduction was removed.",
 "templar:Noble Armor": "KR/TW Sep 16: cooldown 5 min to 2 min. The Global DB still shows 300 s.",
 "templar:Taunt": "Its level-25 crit-damage-resist shred helps every party member, which is why Taunt is a top 25 pick even for DPS parties.",
 "chanter:Guardian Blessing": "KR/TW Sep 16: cooldown 5 min to 2 min. The Global DB still shows 300 s.",
 "chanter:Undefeated Mantra": "Toggle. Two Chanters don't stack: only the higher level applies. Doesn't stack with Cleric's Light of Protection (higher level wins; a tie goes to Undefeated). KR/TW Sep 23: disabled during Abyss boss fights, Rifts and Time-Space battles (Battlefield Authority buff replaces party synergies).",
 "chanter:Power of the Storm": "Doesn't stack with Cleric's Earth's Blessing (Storm applies). KR/TW Sep 23: disabled during Abyss boss fights, Rifts and Time-Space battles.",
 "chanter:Sprint Mantra": "Toggle. Two Chanters don't stack: only the higher level applies.",
 "cleric:Light of Protection": "Toggle. Doesn't stack with Chanter's Undefeated Mantra (higher level wins; a tie goes to Undefeated), so drop it when a Chanter is in the party. KR/TW Sep 23: disabled in Abyss boss fights, Rifts and Time-Space battles.",
 "sorcerer:Cold Storm": "With two Sorcerers in one party only the stronger Cold Storm debuff counts (Sep 17 player test), so only one of you needs it high.",
 "spiritmaster:Jointstrike: Destructive Attack": "KR/TW Sep 10: the Jointstrike no longer overwrites the previous one, so it can be used on cooldown (full charge).",
}

db = {"_about": ("All Stigma skills (13 per class) from the aion2.app Global client DB: names, icons, level-1 "
                 "description, specialties at 5/10/15/20. s25 = level-25 specialty from the KR/TW client (not in the "
                 "Global DB yet). note = KR/TW patch differences. Regenerate with tools/fetch_stigmas.py (keeps s25/note).")}
for cls, m in S25.items():
    for en, txt in m.items():
        db[f"{cls}:{en}"] = {"s25": txt}
for en, s in S.items():
    if isinstance(s, dict) and s.get("s25"):
        db.setdefault(f"{s['cls']}:{en}", {})["s25"] = s["s25"]
for k, n in NOTES.items():
    db.setdefault(k, {})["note"] = n
json.dump(db, open(ROOT + "data/stigma_db.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(db) - 1, "seeded")
