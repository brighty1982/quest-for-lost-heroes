# Defines the player character attributes

from . import util

#-------------------------------------------------------------------
class character:

    name = "Dave"
    wounds = 1
    weapon_skill = 1
    attacks = 1
    strength = 1
    toughness = 1
    armour_save = 1
    initiative = 1
        
    # set or change name
    def set_name(self, new_name):
        self.name = new_name
    # change wounds
    def change_wounds(self, number):
        self.wounds += number
    # change weapon skill
    def change_weapon_skill(self, number):
        self.weapon_skill += number
    # change attacks
    def change_attacks(self, number):
        self.attacks += number
    # change strength
    def change_strength(self, number):
        self.strength += number
    # change toughness
    def change_toughness(self, number):
        self.toughness += number
    # change armour_save
    def change_armour_save(self, number):
        self.armour_save += number
    # change initiative
    def change_initiative(self, number):
        self.initiative += number
    # print stats
    def print_stats(self):
        util.spacer(1)
        print("        Name : " + self.name)
        print("      Wounds : " + str(self.wounds))
        print("Weapon Skill : " + str(self.weapon_skill))
        print("     Attacks : " + str(self.attacks))
        print("    Strength : " + str(self.strength))
        print("   Toughness : " + str(self.toughness))
        print(" Armour Save : " + str(self.armour_save))
        print("  Initiative : " + str(self.initiative))
        util.spacer(1)
    

class human_warrior(character):
    type_ = "Human Warrior"
    wounds = 3
    weapon_skill = 4
    attacks = 1
    strength = 3
    toughness = 3
    armour_save = 5
    initiative = 7

class dwarven_smith(character):
    type_ = "Dwarven Smith"
    wounds = 4
    weapon_skill = 5
    attacks = 1
    strength = 3
    toughness = 4
    armour_save = 4
    initiative = 6

class elven_archer(character):
    type_ = "Elven Archer"
    wounds = 3
    weapon_skill = 5
    attacks = 1
    strength = 3
    toughness = 3
    armour_save = 6
    initiative = 8
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
    util.spacer(1)
    print("Your character name has been set to ** " + player.name + " **")
#-------------------------------------------------------------------



        
       



