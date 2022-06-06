symbol = str(input("What symbol would you like to use? "))
width = int(input("What's the width of your box? "))
height = int(input("What's the height of your box? "))
for x in range(0,height):
    for y in range(0,width):
        print(symbol, end="")
    print("")