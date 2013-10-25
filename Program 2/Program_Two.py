# CS101
# Program 2
# Gregory Gagnon
# gmg634@mail.umkc.edu
#
# PROBLEM:   Play "Lucky Sevens" until the player loses all money in the pot. Then give user
#            a mathematical report detailing the futility in playing a game of chance such
#            as "Lucky Sevens" at a casino.
#
# ALGORITHM:
#      1. Import (or create) a random number generator.
#      2. Ask user for input to assign amount of money in pot.
#            a. If not positive integer, return error.
#            b. Assign integer to a variable representing the pot.
#      3. Ask user if they want a detailed report; assign Boolean to variable.
#      4. Initialize two variables representing two dice.
#      5. Initialize round count variable as zero.
#      6. Initialize variable representing the highest pot value, equal to current pot value.
#      7. Begin the game simulation:
#            a. Use while statement: while the value of the pot > 0:
#                  i.   Assign random whole number from 1 to 6 to each die.
#                  ii.  If the sum of the two dice == 7, add $4 to pot. Else, subtract $1.
#                  iii. Check the Boolean variable to see if the detailed report was requested.
#                           If so, print each die's value, the total roll, payoff (-1 or +4),
#                           and the amount remaining in the pot.
#                  iv.  Add one to the round count variable to count the number of games played.
#                  v.   If highest pot variable < current pot variable, assign current pot value
#                           to the highest pot variable.
#            b. When value of pot = $0, run else statement, listing round count variable and
#                  highest pot variable to show how many rounds it took to lose all money, and
#                  what maximum held was.
#      8. Ask user if they want to play another round. If so, continue from step 2.
#
#
# ERROR HANDLING:
#      1. User is reprompted to enter a whole integer for initial value in pot.
#      2. User input for detailed report boolean value is sanitized and/or user is reprompted.
#
# OTHER COMMENTS: I would have liked to use "try" and "except" for the error reporting. This would have
#                 corrected entries into pot_value_int that cannot be converted to integers.  
#                 However, I could not get it to catch both negative numbers, too, so I have omitted it.


import random

# Boolean to keep playing game or exit.
keep_playing_bool = True 
while keep_playing_bool == True:    

# User input for initial amount in pot, with error handling.
    pot_value_int = int(input("How much money is in the starting pot? "))

    while pot_value_int <= 0:
        print("Oops. Try entering a positive integer.")
        print ()
        pot_value_int = int(input("How much money is in the starting pot? "))

# User input for detailed report, with error handling.
    detailed_report_str = input(" Do you want a detailed report? ")
    detailed_report_bool = int(0)

    while type(detailed_report_bool) != bool:

        if str.lower(detailed_report_str) == "yes":
            detailed_report_bool = True
        elif str.lower(detailed_report_str) == "y":
            detailed_report_bool = True
        elif str.lower(detailed_report_str) == "no":
            detailed_report_bool = False
        elif str.lower(detailed_report_str) == "n":
            detailed_report_bool = False           
        else:
            print("I did not understand your input. Enter 'yes' or 'no'.")
            print ()
            detailed_report_str = input(" Do you want a detailed report? ")

# Initialize variables to represent two dice, round counter, payout, and highest pot value.

    die_a_int = 0
    die_b_int = 0
    round_count_int = 0
    payout_int = 0
    highest_pot_int = pot_value_int

# Begin the game simulation.

    while pot_value_int > 0:
        round_count_int += 1              
        die_a_int = random.randint(1,6)
        die_b_int = random.randint(1,6)
        
        if die_a_int + die_b_int == 7:
            pot_value_int += 4
            payout_int = 4        
        else:
            pot_value_int -= 1
            payout_int = -1
        if highest_pot_int < pot_value_int:
            highest_pot_int = pot_value_int
        if detailed_report_bool == True:
            print("Roll: ", die_a_int, " ", die_b_int, "Total: ", (die_a_int + die_b_int), " ", "Payout: ", payout_int, " ", \
                  "Pot: ", pot_value_int) 
    else:
        print()
        print("It took", round_count_int, "rounds, but you lost it all. Your maximum pot value was", highest_pot_int,".")
        print()

# User input to exit or play again.
    exit_str = input("Play again? ")
    exit_bool = int(0)

    while type(exit_bool) != bool:
    
        if str.lower(exit_str) == "yes":
            exit_bool = False
        elif str.lower(exit_str) == "y":
            exit_bool = False
        elif str.lower(exit_str) == "no":
            exit_bool = True
        elif str.lower(exit_str) == "n":
            exit_bool = True           
        else:
            print("I did not understand your input. Enter 'yes' or 'no'.")
            print ()
            exit_str = input("Play again? ")
        
    if exit_bool == True:
        keep_playing_bool = False
