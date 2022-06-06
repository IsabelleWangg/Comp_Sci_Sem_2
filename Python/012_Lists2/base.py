x = int(input("How many random numbers would you like? "))
numlist = []
import random
for a in range(0,x):
    numlist.append(random.randrange(11))
print("Your numbers are: " + str(numlist))