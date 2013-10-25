
print("Rock, Paper, Scissors.")
print("An ancient and well-known game.")
print()

version_str = ""

version_str = input("Do you want to play the CLASSIC or FIVE WEAPON version of the game? ")
if version_str.lower() == "classic" or version_str.lower() == "c":
    version_str = "classic"
    
elif version_str.lower() == "five weapon" or version_str.lower() == "five" or \
   version_str.lower() == "f" or version_str.lower() == "5":
    version_str = "five weapon"
    
else:
    print("I didn't understand your selection. Try typing 'classic' or 'five'")
    print()
