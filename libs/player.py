# Defines the player character attributes

from . import util

# main character class
#-------------------------------------------------------------------
class character:
    name = "Dave"

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

    # inventory - dictionary of arrays that items can added/removed from
    inventory = {
        "hand-weapon": [],
        "arnour": [],
        "shield": [],
        "special": []
        }

    # currently equipement you are armed with - dictionary of string as only one item at a time
    equiped = {
        "hand-weapon": "",
        "armour": "",
        "shield": "",
        "special": ""
        }

    # helper functions
    #-------------------------------------------------------------------

    # handweapon inventory
    def add_hand_weapon_inventory(self, weapon):
        self.inventory["hand-weapon"].append(weapon)
    
    def remove_hand_weapon_inventory(self, weapon):
        self.inventory["hand-weapon"].remove(weapon)

    # armour inventory
    def add_armour_inventory(self, armour):
        self.inventory["armour"].append(armour)

    def remove_armour_inventory(self, armour):
        self.inventory["armour"].remove(armour)

    # shield inventory
    def add_shield_inventory(self, shield):
        self.inventory["shield"].append(shield)
    
    def remove_shield_inventory(self, shield):
        self.inventory["shield"].remove(shield)

    # special inventory
    def add_special_inventory(self, special):
        self.inventory["special"].append(special)

    def remove_special_inventory(self, special):
        self.inventory["special"].remove(special)
    

    # equip/unequip handweapon
    def set_hand_weapon(self, weapon):
        self.equiped["hand-weapon"] = weapon
    
     # equip/unequip shield
    def set_shield(self, shield):
        self.equiped["shield"] = shield

    # equip/unequip special
    def set_special(self, special):
        self.equiped["special"] = special

    # show current equipment
    def show_equipment(self):
        util.spacer(1)
        print("Currently Equipped")
        util.spacer(1)
        for key in self.equiped:
            print(key + " : " + self.equiped[key])
        util.spacer(1)
        
    # set or change name
    def set_name(self, new_name):
        self.name = new_name
    # change wounds
    def change_wounds(self, number):
        self.stats["wounds"] += number
    # change weapon skill
    def change_weapon_skill(self, number):
        self.stats["weapon_skill"] += number
    # change attacks
    def change_attacks(self, number):
        self.stats["attacks"] += number
    # change strength
    def change_strength(self, number):
        self.stats["strength"] += number
    # change toughness
    def change_toughness(self, number):
        self.stats["toughness"] += number
    # change armour_save
    def change_armour_save(self, number):
        self.stats["armour_save"] += number
    # change initiative
    def change_initiative(self, number):
        self.stats["initiative"] += number

    # print stats
    def show_stats(self):
        util.spacer(1)
        print("Your stats")
        util.spacer(1)
        for key in self.stats:
            print(key + " : " + str(self.stats[key]))
        util.spacer(1)
    #-------------------------------------------------------------------
#-------------------------------------------------------------------
    
# human warrior sub class
#-------------------------------------------------------------------
class human_warrior(character):
    type_ = "Human Warrior"
    stats = {
        "wounds": 3,
        "weapon_skill": 3,
        "attacks": 1,
        "strength": 3,
        "toughness": 3,
        "armour_save": 6,
        "initiative": 7
    }
#-------------------------------------------------------------------

# dwarven smith sub class
#-------------------------------------------------------------------
class dwarven_smith(character):
    type_ = "Dwarven Smith"
    stats = {
        "wounds": 4,
        "weapon_skill": 4,
        "attacks": 1,
        "strength": 3,
        "toughness": 4,
        "armour_save": 5,
        "initiative": 6
    }
#-------------------------------------------------------------------

# elven_archer sub class
#-------------------------------------------------------------------
class elven_archer(character):
    type_ = "Elven Archer"
    stats = {
        "wounds": 3,
        "weapon_skill": 4,
        "attacks": 1,
        "strength": 3,
        "toughness": 3,
        "armour_save": 6,
        "initiative": 8
    }
#-------------------------------------------------------------------

# return a list of available characters
#-------------------------------------------------------------------
def generate_character_list():
    character_list = [human_warrior, dwarven_smith, elven_archer]
    return character_list
#-------------------------------------------------------------------

# Choose a character type
#-------------------------------------------------------------------
def select_character_type():
    while True:
        characters = generate_character_list()
        n = 0
        for character in characters: 
            print(n, ") " + character.type_) 
            n += 1

        util.spacer(1)
        selection = str(input("Choose your character > "))
        util.check_exit_game(selection)
        if(selection.isdigit()):            # make sure user entered a number
            selection = int(selection)      # convert string to int
            if (selection in range(0,n)):   # check int is in range for list size
                util.spacer(1)
                print("You have chosen *** " + characters[selection].type_ + " ***")
                util.spacer(1)
                continue_ = input("Continue? [y|n] > ").strip(" ").lower()
                util.check_exit_game(continue_)
                if(continue_ in ["y","yes"]):
                    return characters[selection]()
#-------------------------------------------------------------------

# Set or change the players name
#-------------------------------------------------------------------
def set_player_name(player):
    util.spacer(1)
    name = input("What is your characters name? > ")
    util.check_exit_game(name)
    player.set_name(name)
    if(player.name.lower() == "exit"): set_player_name(player)
    util.spacer(1)
    print("Your character name has been set to ** " + player.name + " **")
#-------------------------------------------------------------------



        
       



