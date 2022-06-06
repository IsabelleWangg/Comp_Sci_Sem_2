a = int(input("How many items would you like to buy? "))
sum = 0
for x in range(0,a):
    item = input("What item are you buying? ")
    price = float(input("How much is the item? "))
    print("Thanks for buying " + item)
    print("-----------------------------------------------------------" + "\n")
    sum = sum + price
print("Your total for " + str(a) + " items is: $" + str(sum))