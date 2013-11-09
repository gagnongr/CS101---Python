is_prime = 0

n = int(input("n? "))

if n == (1 or 2 or 3):
    is_prime = True

else:
    for m in range(2,(n)):
        if (n % m) == 0:
            is_prime = False
        else:
            is_prime = True

print("Prime? ", is_prime)
