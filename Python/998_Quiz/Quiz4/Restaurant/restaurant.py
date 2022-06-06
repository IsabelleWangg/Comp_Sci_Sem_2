restaurants = ["souplantation", "in_n_out", "dominos"]
souplantation = ["minestrone", "chowder", "noodle"]
in_n_out = ["hamburger", "cheeseburger", "doubledouble"]
dominos = ["cheese", "pepperoni", "veggie"]
import random
pick = input("pick a restaurant: 0. souplantation, 1. in-n-out, 2. dominos ")
if pick == '0':
    print(souplantation)
    print(souplantation[random.randrange(3)])
elif pick == '1':
    print(in_n_out)
    print(in_n_out[random.randrange(3)])
elif pick == '2':
    print(dominos)
    print(dominos[random.randrange(3)])