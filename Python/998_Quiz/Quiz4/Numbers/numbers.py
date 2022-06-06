mynumbers = [6,9,32,28,15,22,3,18]
sum  = mynumbers[0]
for x in range(0,len(mynumbers)-1):
    sum = sum + mynumbers[x+1]
average = sum/len(mynumbers)
print("average: " + str(average))

a = 0
for x in range(0,len(mynumbers)):
    if mynumbers[x]>a:
        a=mynumbers[x]
    elif mynumbers[x]<a:
        if x==len(mynumbers):
            break
print("max: " + str(a))

b = mynumbers[1]
for x in range(0,len(mynumbers)):
    if mynumbers[x]<b:
        b = mynumbers[x]
    elif mynumbers[x]>b:
        if x==len(mynumbers):
            break
print("min: " + str(b))

