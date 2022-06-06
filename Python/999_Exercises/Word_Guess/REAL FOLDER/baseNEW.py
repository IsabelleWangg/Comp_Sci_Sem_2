list_words = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        list_words.append(l)

a=0
w=0
b=0
import random
num = random.randrange(12972)
answer = list_words[num]

while(w<6):
    guess = input("Give me a word: ")
    if guess == answer:
        print("You guessed it!")
        b=1
        break
    else:
        for words in list_words:
            if guess == words:
                a = 1
        if a == 1:
            print("Wrong word!")
            w=w+1
        else:
            print("Invalid entry, guess again!")
        a=0

if b=0:
    print("You lost! The word was: " + answer)

f.close