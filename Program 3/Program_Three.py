# CS101
# Program 3
# Gregory Gagnon
# gmg634@mail.umkc.edu
# 
# PROBLEM:  Play "Rock, Paper, Scissors" against the computer. The computer keeps track of
#           player's weapon choices, and selects the weapon that will beat the user's 
#           most frequent choice. 
#
# ALGORITHM:
#   1. Give user basic instructions and rules.
#   2. Setup a while loop to keep the game playing.
#   3. Get user input for version of game and/or help.
#   4. Initialize variables for:
#       a. Round Count
#       b. Weapon choice counts for each weapon type
#       c. Current computer weapon
#       d. Current user weapon
#       e. User wins
#       f. Computer wins
#       g. Ties
#   5. First round - computer makes random weapon selection
#   6. User inputs weapon choice (sanitize input, repeatedly prompt)
#   7. Compare computer and user weapon choices
#       a. Using if statements, determine winner of round
#       b. Increment all variables as necessary
#   8. Compare weapon choice counts, select weapon that defeats user's most common weapon choice.
#       If no most common weapon, make random selection. 
#   9. Repeat step 5 through 7 until user inputs "Quit." 
#   10. Print detailed summary of the game with:
#       a. rounds played
#       b. rounds won/lost/tied
#       c. weapons chosen how many times.
#
# ERROR HANDLING:
#   1. All user inputs reprompt until valid input is given. .lower method accepts upper and lower case.
#   2. User is prompted for possible valid entries after invalid input.
#
#
#
# OTHER COMMENTS: 
#

import random

print("ROCK. PAPER. SCISSORS.")
print("An ancient and well-known game.")
print()

version_str = ""
while True:
    version_str = input("Do you want to play the CLASSIC or FIVE WEAPON version of the game? ")
    if version_str.lower() == "classic" or version_str.lower() == "c":
        version_str = "classic"
        break
    elif version_str.lower() == "five weapon" or version_str.lower() == "five" or \
       version_str.lower() == "f" or version_str.lower() == "5":
        version_str = "five weapon"
        break
    else:
        print("I didn't understand your selection. Try typing 'classic' or 'five'")
        print()

# Classic Game
if version_str == "classic":

    help_str = ""
    help_str = input("Do you want HELP? If so, enter 'h' or 'H'. Otherwise, hit ENTER.")

    if help_str.lower() == "h":
        print()
        print("There are three weapons available...Rock, Paper or Scissors. You must choose.")
        print("Rock defeats scissors. Scissors defeats paper. Paper defeats rock.")
        print()
        print("To select your weapon, enter 'R' for rock, 'P' for paper, or 'S' for scissors. \n \
        To quit, enter 'Q'.")
        print()

    round_count_int = 0
    user_win_count_int = 0
    computer_win_count_int = 0
    ties_count_int = 0
    rock_count_int = 0
    paper_count_int = 0
    scissors_count_int = 0
    computer_weapon_int = 0
    user_weapon_str = ""
    user_weapon_int = 0
    random_weapon_int = 0
    weapon_list = ["","Rock","Paper","Scissors"]
    play_bool = True

    while play_bool == True:

        # Computer weapon selection
        if scissors_count_int < rock_count_int > paper_count_int:
            computer_weapon_int = 2
        elif rock_count_int < paper_count_int > scissors_count_int:
            computer_weapon_int = 3
        elif paper_count_int < scissors_count_int > rock_count_int:
            computer_weapon_int = 1
        else:
            random_weapon_int = random.randint(1,3)
            computer_weapon_int = random_weapon_int

        # User weapon selection
        while True:
            user_weapon_str = input("Choose Your Weapon: ")
            if user_weapon_str.lower() in "rps" and len(user_weapon_str) == 1:
                user_weapon_str = user_weapon_str.lower()
                break
            elif user_weapon_str.lower() == "h":
                print()
                print("There are three weapons available...Rock, Paper or Scissors. You must choose.")
                print("Rock defeats scissors. Scissors defeats paper. Paper defeats rock.")
                print()
                print("To select your weapon, enter 'R' for rock, 'P' for paper, or 'S' for scissors. \n \
                To quit, enter 'Q'.")
                print()
                continue
            elif user_weapon_str.lower() == "q":
                print()
                print("That was fun! We played {} rounds.".format(round_count_int))
                print()
                print("You won {} rounds, I won {} rounds, and we tied on {}.".format(user_win_count_int, computer_win_count_int, ties_count_int))
                print("You used rock {} times, paper {} times, and scissors {} times.".format(rock_count_int, paper_count_int, scissors_count_int))
                play_bool = False
                break
            else:
                print("I didn't understand your selection. Try typing:")
                print()
                print("'r' for rock\n'p' for paper\n's' for scissors\n'h' for help\n'q' to quit")
                print()

        # Quit 
        if play_bool == False:
             break
        
        if user_weapon_str == "r":
            user_weapon_int = 1           
        elif user_weapon_str == "p":
            user_weapon_int = 2           
        elif user_weapon_str == "s":
            user_weapon_int = 3
        round_count_int += 1
        
        # Compare user and computer weapons

        # Tie
        if user_weapon_int == computer_weapon_int:
            ties_count_int += 1
            if user_weapon_int == 1:
                rock_count_int += 1
            elif user_weapon_int == 2:
                paper_count_int += 1
            else:
                scissors_count_int += 1
            print("We tied. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))

        # User picks ROCK
        elif user_weapon_int == 1:
            rock_count_int += 1
            if computer_weapon_int == 2:
                computer_win_count_int += 1
                print("I won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
            if computer_weapon_int == 3:
                user_win_count_int += 1
                print("You won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))

        # User picks PAPER
        elif user_weapon_int == 2:
            paper_count_int += 1
            if computer_weapon_int == 3:
                computer_win_count_int += 1
                print("I won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
            if computer_weapon_int == 1:
                user_win_count_int += 1
                print("You won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
                
        # User picks SCISSORS
        elif user_weapon_int == 3:
            scissors_count_int += 1
            if computer_weapon_int == 1:
                computer_win_count_int += 1
                print("I won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
            if computer_weapon_int == 2:
                user_win_count_int += 1
                print("You won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))


# Five Weapon Game
else:
    print()
    print("This FIVE WEAPON version of the game is a bit trickier...")
    help_str = ""
    help_str = input("Do you want HELP? If so, enter 'h' or 'H'. Otherwise, hit ENTER.")

    if help_str.lower() == "h":
        print()
        print("There are five weapons available...Rock, Paper, Scissors, Lizard and Spock.")
        print("You must choose.")
        print()
        print("Rock breaks scissors, and crushes Lizard.")
        print("Paper covers rock, and disproves Spock.")
        print("Scissor cuts paper, and decapitates Lizard.")
        print("Lizard eats paper, and poisons Spock.")
        print("Spock breaks scissors, and vaporizes rock.")
        print()
        print("To select your weapon, enter 'R' for rock, 'P' for paper, 'SC' for scissors, \n'L' for lizard, or 'SP' for Spock. To quit, enter 'Q'.")
        print()

    round_count_int = 0
    user_win_count_int = 0
    computer_win_count_int = 0
    ties_count_int = 0
    rock_count_int = 0
    paper_count_int = 0
    scissors_count_int = 0
    lizard_count_int = 0
    spock_count_int = 0
    computer_weapon_int = 0
    user_weapon_str = ""
    user_weapon_int = 0
    random_weapon_int = 0
    random_choice_int = 0
    weapon_list = ["","Rock","Paper","Scissors","Lizard","Spock"]
    play_bool = True

    while play_bool == True:

        # Computer weapon selection - randomly selects between the two winning weapons
        if scissors_count_int < rock_count_int > paper_count_int and lizard_count_int < rock_count_int > spock_count_int:
            random_choice_int = random.randint(1,2)
            if random_choice_int == 1:               
                computer_weapon_int = 2
            else:
                computer_weapon_int = 5
                
        elif rock_count_int < paper_count_int > scissors_count_int and lizard_count_int < paper_count_int > spock_count_int:
            random_choice_int = random.randint(1,2)
            if random_choice_int == 1:               
                computer_weapon_int = 3
            else:
                computer_weapon_int = 4


        elif paper_count_int < scissors_count_int > rock_count_int and lizard_count_int < scissors_count_int > spock_count_int:
            random_choice_int = random.randint(1,2)
            if random_choice_int == 1:               
                computer_weapon_int = 1
            else:
                computer_weapon_int = 5

        elif scissors_count_int < lizard_count_int > rock_count_int and paper_count_int < lizard_count_int > spock_count_int:
            random_choice_int = random.randint(1,2)
            if random_choice_int == 1:               
                computer_weapon_int = 1
            else:
                computer_weapon_int = 3

        elif scissors_count_int < spock_count_int > rock_count_int and paper_count_int < spock_count_int > lizard_count_int:
            random_choice_int = random.randint(1,2)
            if random_choice_int == 1:               
                computer_weapon_int = 2
            else:
                computer_weapon_int = 4

        else:
            random_weapon_int = random.randint(1,5)
            computer_weapon_int = random_weapon_int

        # User weapon selection
        while True:
            user_weapon_str = input("Choose Your Weapon: ")
            if user_weapon_str.lower() in ["r","p","sc","l","sp"] and len(user_weapon_str) <= 2:
                user_weapon_str = user_weapon_str.lower()
                break
            elif user_weapon_str.lower() == "h":
                print()
                print("There are five weapons available...Rock, Paper, Scissors, Lizard and Spock.")
                print("You must choose.")
                print()
                print("Rock breaks scissors, and crushes Lizard.")
                print("Paper covers rock, and disproves Spock.")
                print("Scissor cuts paper, and decapitates Lizard.")
                print("Lizard eats paper, and poisons Spock.")
                print("Spock breaks scissors, and vaporizes rock.")
                print()
                print("To select your weapon, enter 'R' for rock, 'P' for paper, 'SC' for scissors, \n'L' for lizard, or 'SP' for Spock. To quit, enter 'Q'.")
                print()
                continue
            elif user_weapon_str.lower() == "q":
                print()
                print("That was fun! We played {} rounds.".format(round_count_int))
                print()
                print("You won {} rounds, I won {} rounds, and we tied on {}.".format(user_win_count_int, computer_win_count_int, ties_count_int))
                print("You used rock {} times, paper {} times, scissors {} times, \nlizard {} times, and Spock {} times.".format(rock_count_int, \
                paper_count_int, scissors_count_int, lizard_count_int, spock_count_int))
                play_bool = False
                break
            else:
                print("I didn't understand your selection. Try typing:")
                print()
                print("'r' for rock\n'p' for paper\n'sc' for scissors\n'l' for lizard\n'sp' for spock\n'h' for help\n'q' to quit")
                print()

        # Quit 
        if play_bool == False:
             break
        
        if user_weapon_str == "r":
            user_weapon_int = 1           
        elif user_weapon_str == "p":
            user_weapon_int = 2           
        elif user_weapon_str == "sc":
            user_weapon_int = 3
        elif user_weapon_str == "l":
            user_weapon_int = 4
        elif user_weapon_str == "sp":
            user_weapon_int = 5
        round_count_int += 1
        
        # Compare user and computer weapons

        # Tie
        if user_weapon_int == computer_weapon_int:
            ties_count_int += 1
            if user_weapon_int == 1:
                rock_count_int += 1
            elif user_weapon_int == 2:
                paper_count_int += 1
            elif user_weapon_int == 3:
                scissors_count_int += 1
            elif user_weapon_int == 4:
                lizard_count_int += 1
            elif user_weapon_int == 5:
                spock_count_int += 1
            print("We tied. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))

        # User picks ROCK
        elif user_weapon_int == 1:
            rock_count_int += 1
            if computer_weapon_int == 2 or computer_weapon_int == 5:
                computer_win_count_int += 1
                print("I won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
            if computer_weapon_int == 3 or computer_weapon_int == 4:
                user_win_count_int += 1
                print("You won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))

        # User picks PAPER
        elif user_weapon_int == 2:
            paper_count_int += 1
            if computer_weapon_int == 3 or computer_weapon_int == 4:
                computer_win_count_int += 1
                print("I won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
            if computer_weapon_int == 1 or computer_weapon_int == 5:
                user_win_count_int += 1
                print("You won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
                
        # User picks SCISSORS
        elif user_weapon_int == 3:
            scissors_count_int += 1
            if computer_weapon_int == 1 or computer_weapon_int == 5:
                computer_win_count_int += 1
                print("I won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
            if computer_weapon_int == 2 or computer_weapon_int == 4:
                user_win_count_int += 1
                print("You won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))

        # User picks LIZARD
        elif user_weapon_int == 4:
            lizard_count_int += 1
            if computer_weapon_int == 1 or computer_weapon_int == 3:
                computer_win_count_int += 1
                print("I won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
            if computer_weapon_int == 2 or computer_weapon_int == 5:
                user_win_count_int += 1
                print("You won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))

        # User picks SPOCK
        elif user_weapon_int == 5:
            spock_count_int += 1
            if computer_weapon_int == 2 or computer_weapon_int == 4:
                computer_win_count_int += 1
                print("I won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
            if computer_weapon_int == 1 or computer_weapon_int == 3:
                user_win_count_int += 1
                print("You won. You chose {}. I chose {}.".format(weapon_list[user_weapon_int],weapon_list[computer_weapon_int]))
