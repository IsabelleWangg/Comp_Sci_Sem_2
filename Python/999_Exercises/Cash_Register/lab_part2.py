a = int(input("How many items would you like to buy? "))
sum = 0
itemlist = []
pricelist = []
for x in range(0,a):
    item = input("What item are you buying? ")
    itemlist.append(item)
    price = float(input("How much is the item? "))
    pricelist.append(price)
    print("Thanks for buying " + item)
    print("-----------------------------------------------------------" + "\n")
    sum = sum + price
for x in range(0,a):
    print(itemlist[x] + " - $" + str(pricelist[x]))
print("Your total for " + str(a) + " items is: $" + str(sum))