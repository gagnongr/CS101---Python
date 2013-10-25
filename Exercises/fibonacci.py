n = int(input("what is n: "))

result = int(0)
i = int(0)

#if n == 0:
    #result = 0
#elif n == 1:
    #result = 1
#elif n == 2:
    #result = 1
#else:

i = 0
j = 1
k = n
result = 0

while k > 1:
        i, j = j, (j+i)
        result = j
        k -= 1
        print ("i: ", i, ", j: ", j, ",n: ", n)


print("n is", n, " and ", "result is ", result)
