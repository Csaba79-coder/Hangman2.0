# def play(word, lives):
#    pass

# play('Codecool', 6)

import random

def get_word():

    file = open("countries-and-capitals.txt", "r")
    countries = []
    capitals = []
    capandcount = []

    for line in file:
        splitline = line.split(" | ")
        countries.append(splitline[0].rstrip())
        capitals.append(splitline[1].rstrip())

    random.choice(countries)
    capandcount.append(random.choice(countries))

    random.choice(capitals)
    capandcount.append(random.choice(capitals))

    random.choice(capandcount)

    word = random.choice(capandcount)
    print(word)
    return word


get_word()

"""def change_hide_word():

    word = get_word()

    for _ in range(len(word)):
        displaylist.append("_ ")


change_hide_word()"""


