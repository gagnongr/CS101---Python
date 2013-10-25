import random

number = random.randint(0,100) # get a number between 1-100 inclusive

print("Hi-Lo Number guessing Game: between 0 and 100 inclusive.")
print ()

# get an initial guess

guess_str = input("Guess a number: ")
guess = int(guess_str) # convert str to an int

#while guess is in range, keep asking

while 0 <= guess <= 100:
    if guess > number:
        print("guessed too high.")
    elif guess < number:
        print ("guessed too low.")

    else:
        print("you guessed it. the number was:", number)
        break
    #keep going, get the next guess

    guess_str = input("Guess a number: ")
    guess = int(guess_str)


else:
    print("You quit early. the number was:", number)

