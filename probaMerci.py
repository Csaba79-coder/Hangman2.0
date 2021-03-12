import random

def words():

    file = open("countries-and-capitals.txt", "r")
    lines = file.readlines()
    list1 = []
    list2 = []
    for i in lines:
        spli = i.split(" | ")
        list1.append(spli[0])
    random.choice(list1)

    list2.append(random.choice(list1))

    sajt = random.choice(list1)
    print(sajt)
    return sajt

words()


