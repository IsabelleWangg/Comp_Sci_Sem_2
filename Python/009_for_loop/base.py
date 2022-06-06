length = int(input("Please enter line length: "))
a = str(input("Do you want a horizontal or vertical line? "))
if a == "horizontal":
    for x in range(0,length):
        print("*", end =" ")
elif a == "vertical":
    for x in range(0,length):
        print("*")