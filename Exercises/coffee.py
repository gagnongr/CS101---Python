#       Calculate the amount of coffee grounds per oz. of water
#       To make perfect coffee

coffee_amt_int = input("How many ounces of coffee do you want to make? ")

grounds_amt_float = float(coffee_amt_int) / 3

print("You should use ", grounds_amt_float, " level tablespoons", "for ", coffee_amt_int, " ounces of coffee.")
