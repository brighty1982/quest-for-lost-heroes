# contains data tables to resolve combat

# To hit table shows the values required to 'hit' between any two weapon_skills
# Weapon skill ranges from 1-10
# using the table below oponent A with weapon_skill 6 will 'hit' openent 2
# with weapon_skill 3 with a score of 2 or more
weapon_skill_hit_table = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                         [1, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6],
                         [2, 3, 4, 5, 5, 6, 6, 6, 6, 6, 6],
                         [3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 6],
                         [4, 2, 3, 3, 4, 5, 5, 6, 6, 6, 6],
                         [5, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6],
                         [6, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6],
                         [7, 2, 2, 2, 2, 3, 3, 4, 5, 5, 6],
                         [8, 2, 2, 2, 2, 2, 3, 3, 4, 5, 5],
                         [9, 2, 2, 2, 2, 2, 2, 3, 3, 4, 5],
                         [10, 2, 2, 2, 5, 2, 2, 2, 3, 3, 4]]

# Armour save table defines the value needed to save a an attack that hits
# The strength of the attacker modifies the armour save
# using the table below an defender with an armour save of 3+ would save
# a hit from an attacker with strength 5 with a score of 4 or higher
# this is because the strength 5 has modifed the 3+ save by -1
armour_save_table = [[0, 1, 2, 3, 4, 5, 6],
                    [1, 1, 2, 3, 4, 5, 6],
                    [2, 1, 2, 3, 4, 5, 6],
                    [3, 1, 2, 3, 4, 5, 6],
                    [4, 1, 2, 3, 4, 5, 6],
                    [5, 2, 3, 4, 5, 6, 0],
                    [6, 3, 4, 5, 6, 0, 0],
                    [7, 4, 5, 6, 0, 0, 0],
                    [8, 5, 6, 0, 0, 0, 0],
                    [9, 6, 0, 0, 0, 0, 0],
                    [10, 0, 0, 0, 0, 0, 0]]
                    
# To wound table shows the values required to 'wound' between an oponents
# when an attack has hit and the armour save has failed
# strength and a defenders toughness 
# Strength and Toughness ranges from 1-10
# using the table below an attacker with strength 6 will 'wound' a defender
# with toughness 3 with a score of 2 or more
strength_toughness_wound_table = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                                 [1, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6],
                                 [2, 3, 4, 5, 5, 6, 6, 6, 6, 6, 6],
                                 [3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 6],
                                 [4, 2, 3, 3, 4, 5, 5, 6, 6, 6, 6],
                                 [5, 2, 2, 3, 3, 4, 5, 5, 6, 6, 6],
                                 [6, 2, 2, 2, 3, 3, 4, 5, 5, 6, 6],
                                 [7, 2, 2, 2, 2, 3, 3, 4, 5, 5, 6],
                                 [8, 2, 2, 2, 2, 2, 3, 3, 4, 5, 5],
                                 [9, 2, 2, 2, 2, 2, 2, 3, 3, 4, 5],
                                 [10, 2, 2, 2, 5, 2, 2, 2, 3, 3, 4]]