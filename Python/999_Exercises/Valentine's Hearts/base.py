import datetime

list_people = []
with open('People.txt') as f:
    for line in f:
        l = line.strip()
        list_people.append(l)

list_compliments = []
with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        list_compliments.append(l)

import random
x = datetime.datetime.now()

while(x.minute != 58):
    x = datetime.datetime.now()
    a = random.randrange(0, len(list_people))
    b = random.randrange(0, len(list_compliments))
    print(list_people[a] + " " + list_compliments[b])

f.close()
