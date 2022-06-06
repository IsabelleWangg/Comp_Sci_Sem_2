name = input("What is your name? ")
for x in range(0,len(name)):
    a = name[x:x+1]
    print(a)

for x in range(0,len(name)):
    a = name[x:x+1]
    if a == " ":
        print(name[x+1:len(name)], end=" ")
        print(name[0:x])