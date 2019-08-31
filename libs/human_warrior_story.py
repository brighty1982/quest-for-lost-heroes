
from . import util
from . import player
import time

# Intro to human warrior story line
#-------------------------------------------------------------------
def begin_adventure(player):
    util.spacer(1)
    Intro = """
    Introduction
    ********************************************************************************

    Your name is """ + player.name + """ and you are 17 years old. You are the son of 
    the blacksmith Jacob Carlson. The Burger of Middelheim has recently invited 
    your father to come and be his personal blacksmith, an offer he couldn't refuse. 
    So your Mother, Father and younger sister Martha, along with all the family's
    belongings were hitched up to a wagon and the old forge closed as family set off
    on the 5 day journey to Middelheim.

    The journey was uneventful for the first 2 days. But on the third...

    ********************************************************************************
    """
    
    print(Intro)

    input("Continue [enter] >")

    # Level 1 - Caravan attack aftermath
    level_1_caravan_aftermath(player)
#-------------------------------------------------------------------

# Level 1 code
#-------------------------------------------------------------------
def level_1_caravan_aftermath(player):
    util.spacer(3)
    print("*** Level 1: Caravan attack aftermath ***")
    util.spacer(2)
    print("You slowly open your eyes. Your vision is blurry, your memory hazy...")
    print("Why am I laying in the dirt? Why does my head hurt so much? You gently ")
    print("touch head and your hand comes away covered in sticky blood...and you start ")
    print("to remember. Goblins! As the wagon caravan was passing through a narrow lane ")
    print("throught the Craven Forest. But Goblins? Here? They were pushed out of human lands ")
    print("and into the Misty Mountains generations ago.")
    util.spacer(1)
    input("Continue [enter] >")
    util.spacer(1)
    print("You lift you head and look to the left. The bodies of you parents lay sprawled ")
    print("alongside the wagon. Four dead Goblins lay around your father's corpse where he ")
    print("killed the with his forge hammer. Dead caarvan guards are spread around the wagons ")
    print("alongside the occasional dead goblin. Up ahead you see a goblin searching corpses ")
    print("for coins and weapons. Next to you lays a discarded caravan guard's sword... ")
    util.spacer(1)
    input("Continue [enter] >")
    util.spacer(1)

    s = util.get_clean_input_lower("Do you pick up the sword? [y|n] > ")
    util.check_exit_game(s)
    if(s in ["y","yes"]):
        util.spacer(1)
        print("Great! 'Guard Sword' will be added to you inventory and equipped.")

        player.set_hand_weapon("Guard Sword")

        util.spacer(1)

        if(util.get_clean_input_lower("View your equipment? [y|n] > ") in ["y","yes"]):
            player.show_equipment()
        
        
    else:
        util.spacer(1)
        print("Really? You sir, are a coward! Start again and be a man!")
        util.spacer(1)
        input("Continue [enter] >")
        level_1_caravan_aftermath(player)
    


#-------------------------------------------------------------------


