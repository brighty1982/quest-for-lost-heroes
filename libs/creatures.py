# Creatures library defining all possible creatures that can fought

import random

#---Creatures---------------------------------------
# orc class
class orc:
    name = "orc"
    wounds = 1
    weapon_skill = 3
    attacks = 1
    strength = 4
    toughness = 4
    armour_save = 5
    inititiave = 3

# goblin class
class goblin:
    name = "goblin"
    wounds = 1
    weapon_skill = 2
    attacks = 1
    strength = 2
    toughness = 2
    armour_save = 6
    inititiave = 2

# black orc
class black_orc:
    name = "black orc"
    wounds = 2
    weapon_skill = 4
    attacks = 2
    strength = 4
    toughness = 5
    armour_save = 4
    inititiave = 3

#---End Creatures---------------------------------------

#---Helper functions------------------------------------
# return a list of creatures
def generate_creatures():
    creature_list = [orc, goblin, black_orc]
    return creature_list

# select a random foe to fight
def select_random_foe():
    creatures = generate_creatures()
    current_foe = random.choice(creatures)
    print ("******************************************")
    print ("************* Enemy Details **************")
    print ("******************************************")
    print ("Name: " + current_foe.name)
    print ("Wounds: " + str(current_foe.wounds))
    print ("Weapon skill: " + str(current_foe.weapon_skill))
    print ("Attacks: " + str(current_foe.attacks))
    print ("Strength: " + str(current_foe.strength))
    print ("Toughness: " + str(current_foe.toughness))
    print ("Armour Save: " + str(current_foe.armour_save))
    print ("Initiative: " + str(current_foe.inititiave))
    print ("******************************************")
    print ("")
    print ("Get ready to fight!")
    return current_foe

#---End Helper functions------------------------------------





    

    