
from . import util
from . import player

def begin_adventure(player):
    util.spacer(1)
    Intro = """
    Introduction
    ********************************************************************************

    Your name is """ + player.name + """ and you are 17 years old. You are the son of 
    the blacksmith Jacob Carlson. The Burger of Middelheim has recently invited 
    your father to come and be his personal blacksmith, an offer he couldn't refuse. 
    So your Mother, Father and younger sister Martha, along with all the family's
    belongings were hitched up to a wagon, the old forge closed as family set off
    on the 5 day journey to Middelheim.

    The journey was uneventful for the first 2 days. But on the third...

    ********************************************************************************
    """

    print(Intro)

    # Level 1 - Caravan attack aftermath
    level_1_caravan_aftermath(player)

def level_1_caravan_aftermath(player):
    util.spacer(3)
    print("*** Level 1: Caravan attack aftermath ***")
    util.spacer(1)
    


