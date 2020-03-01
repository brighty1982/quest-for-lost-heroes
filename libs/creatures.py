# Creatures library defining all possible creatures that can fought

import random
from . import util

#---Creatures base class---------------------------------------
class creature:
    name = "red shirt"
    type_ = "Unknown"
    # stats
    stats = {
        "wounds": 1,
        "weapon_skill": 1,
        "attacks": 1,
        "strength": 1,
        "toughness": 1,
        "armour_save": 7,
        "initiative": 1
        }
    
     # print stats
    def show_stats(self):
        util.spacer(1)
        print("Enemy Details")
        print ("-------------------------")
        print("Type: " + self.type_)
        util.spacer(1)
        for key in self.stats:
            print(key + " : " + str(self.stats[key]))
        print ("-------------------------")
        util.spacer(1)
#-------------------------------------------------------------------

# orc class
#-------------------------------------------------------------------
class orc(creature):
    type_ = "orc"
    stats = {
        "wounds": 1,
        "weapon_skill": 3,
        "attacks": 1,
        "strength": 3,
        "toughness": 4,
        "armour_save": 6,
        "initiative": 1
        }
#-------------------------------------------------------------------

# goblin class
#-------------------------------------------------------------------
class goblin(creature):
    type_ = "goblin"
    stats = {
        "wounds": 1,
        "weapon_skill": 2,
        "attacks": 1,
        "strength": 2,
        "toughness": 2,
        "armour_save": 7,
        "initiative": 1
        }
#-------------------------------------------------------------------

# black orc
#-------------------------------------------------------------------
class black_orc(creature):
    type_ = "black orc"
    stats = {
        "wounds": 2,
        "weapon_skill": 4,
        "attacks": 2,
        "strength": 4,
        "toughness": 5,
        "armour_save": 5,
        "initiative": 3
        }
#-------------------------------------------------------------------

#---End Creatures---------------------------------------

# return a list of creatures
#-------------------------------------------------------------------
def generate_foes():
    creature_list = [orc, goblin, black_orc]
    return creature_list
#-------------------------------------------------------------------

# select a random foe to fight
#-------------------------------------------------------------------
def select_random_foe():
    creatures = generate_foes()
    current_foe = random.choice(creatures)()
    current_foe.show_stats()
    util.spacer(1)
    print ("Get ready to fight!")
    return current_foe
#-------------------------------------------------------------------

# return a creature of the requested type
#-------------------------------------------------------------------
def get_foe(requested_creature):

    # all available creatures
    creatures = generate_foes()

    type_list = []
    # get list of creature types
    for creature in creatures: 
        type_list.append(creature.type_)

    if(requested_creature in type_list):
        # return the requested creature from the creature list
        selected_creature = creatures[type_list.index(requested_creature)]()
    else:   
        # default creature is goblin
        util.spacer(1)
        print(requested_creature + " is not recognised, so you get a goblin!")
        selected_creature = goblin()

    return selected_creature
#-------------------------------------------------------------------







    

    