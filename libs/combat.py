# Combat library containing all combat 
# note that all values are based on scores from a 6 sided dice (like a board game)

from . import combat_tables
import random
from . import constants

# decide whether one oponent hits the other
#-------------------------------------------------------------------
def Check_To_Hit(attacker_weapon_skill, defender_weapon_skill):
    score_needed = combat_tables.weapon_skill_hit_table[(attacker_weapon_skill + 1)][(defender_weapon_skill + 1)]
    score = random.randint(constants.LOWER_ROLL, constants.UPPER_ROLL)
    if (score >= score_needed):
        success = True
    else:
        success = False
    return success
#-------------------------------------------------------------------

# decide whether the oponents armour saves a hit
#-------------------------------------------------------------------
def Check_armour_save(attacker_strength, defender_armour_save):
    score_needed = combat_tables.armour_save_table[attacker_strength + 1][(defender_armour_save + 1)]
    score = random.randint(constants.LOWER_ROLL, constants.UPPER_ROLL)
    if (score >= score_needed):
        success = True
    else:
        success = False
    return success
#-------------------------------------------------------------------

# decide whether a successful hit causes a wound
#-------------------------------------------------------------------
def Check_To_Wound(attacker_strength, defender_toughness ):
    score_needed = combat_tables.strength_toughness_wound_table[(attacker_strength + 1)][(defender_toughness + 1)]
    score = random.randint(constants.LOWER_ROLL, constants.UPPER_ROLL)
    if (score >= score_needed):
        success = True
    else:
        success = False
    return success
#-------------------------------------------------------------------

# resolve a fight between the player and an enemy combatent
#-------------------------------------------------------------------
def resolve_combat(player, enemy, ambush):
    
    success = False

    # max +1 enemy initiative if it's an ambush to ensure they attack first
    if(ambush): enemy.initiative = 11

    # who attacks first
    if(player.initiative >= enemy.initiative):
        attacker = player
        defender = enemy
    else:
        attacker = enemy
        defender = player

    # resolve combat - fight until one oponent has 0 wounds remaining
    while True:
        
        print(attacker.name + " attacks!")

        if(Check_To_Hit(attacker.weapon_skill,defender.weapon_skill)):
            print("Successful hit!")
            if(Check_armour_save(attacker.strength, defender.armour_save)):
                print("Armour blocks the blow!")
            else:
                if(Check_To_Wound(attacker.strength, defender.toughness)):
                    defender.change_wounds(-1)
                    print("The hit has caused a wound!")
        else:
            print("The attack misses!")

        if(defender.wounds <= 0):
            if attacker == player: success = True
            break
        else: # swap attacker and defender and continue fight
            temp = attacker 
            attacker = defender
            defender = temp

    return success
#-------------------------------------------------------------------



