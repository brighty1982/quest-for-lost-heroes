# useful utility functions

#-------------------------------------------------------------------
def get_clean_input(msg):
    spacer(1)
    input_ = input(msg)
    return input_.strip(" ")

#-------------------------------------------------------------------
def get_clean_input_lower(msg):
    spacer(1)
    input_ = input(msg)
    return input_.strip(" ").lower()
#-------------------------------------------------------------------

# line spacer
#-------------------------------------------------------------------
def spacer(lines):
    for x in range(int(lines)):
        print("")
        x=x
#-------------------------------------------------------------------

# check input for generic exit
#-------------------------------------------------------------------
def check_exit_game(txt):
    if(txt.lower().strip(" ") == "exit" ):
        spacer(1)
        if(input("Are you sure you wish to exit the game? [y|n] > ").strip(" ").lower() in ["y", "yes"]):
            print("Some people just don't have the stamina...bye!")
            exit()
#-------------------------------------------------------------------