def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for y in range (2,x):
            if x % y ==0:
                return False
        return True

z = k = 0
list_var = []

n = int(input("What is n?"))

while sum(list_var) < n:
    z += 1
    if is_prime(z) == True:
        list_var.append(z)
else:
    k = len(list_var[:-1])
                
print(k)
