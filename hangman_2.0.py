import random
from RandomWordGenerator import RandomWord
import string


def play(word, lives):
    pass


def choose_word():
    
    with open("countries-and-capitals.txt", "r") as file:
        alltext = file.read()
        variable1 = alltext.split(" | ")
        variable2 = random.randint(0, len(variable1)-1)
        variable3 = variable1[variable2]
        variable4 = variable3.split("\n") 

        print(variable4)

        

# play('Codecool', 6)