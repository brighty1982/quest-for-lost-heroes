from libs import combat
from libs import creatures
from libs import player
from libs import util

# character stype adventures
from libs import human_warrior_story


# Begin your adventure
#-------------------------------------------------------------------
def start_adventure(player):

    if(player.type_.lower() != "human warrior"):
        print("Sorry, only the Human Warrior story line is ready.")
        exit()
    else:
        human_warrior_story.begin_adventure(player)
#-------------------------------------------------------------------

# main
#-------------------------------------------------------------------
def main():
    util.spacer(1)
    print("Type 'exit' at any time to quit")
    util.spacer(1)
    print("*********************************************")
    print("********* The Quest For Lost Heroes *********")
    print("*********************************************")

    player_character = player.select_character_type() # set the players character

    util.spacer(1)

    player.set_player_name(player_character)

    player_character.show_stats()

    input("Continue [enter]>")

    start_adventure(player_character)   # begin your quest!
#-------------------------------------------------------------------
     
# entry point
#-------------------------------------------------------------------
if __name__ == "__main__":
    main()
#-------------------------------------------------------------------

