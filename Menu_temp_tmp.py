
import sys
import time
import os
import menu


mainMenu = menu.Menu("Hangman2.0", update())


def menu():

    menu = {}
    menu['1']="Easy level with 7 lives"
    menu['2']="Medium level with 5 lives"
    menu['3']="Hard level with 3 lives"
    menu['4']="Exit"
    while True:
        options=menu.keys()
        options.sort()
        for entry in options:
            print(entry, menu[entry])

        selection=raw_input("Please Select:")
        if selection =='1':
          print("Selected: easy level with 7 lives!")
        elif selection == '2':
          print("Selected: medium level with 5 lives!")
        elif selection == '3':
          print("Selected: hard level with 3 lives!")
        elif selection == '4':
          break
        else:
          print("Unknown Option Selected!")
        return menu()

menu()


#import sys
# import time
# import string

"""def menu():

    def greating_the_user():
       user = input("Please enter your name: ")
       print("Hello " + user + "!" + "I am Hangman 2.0!")
    greating_the_user()


    def set_difficulty(value, difficulty):


        print("Please choose the difficulty level!")
        print("For easy level please select: 1")
        print("For medium level please select: 2")
        print("For hard please select: 3")
        print("For exit please type: quit")
        input("Please select difficulty level: ")

        if input(1) == "1":
            print("Welcome to easy level, you have 7 lives!")
            return get_random_word()
        elif input() == "2":
            print("Welcome to medium level, you have 5 lives!")
            return get_random_word()
        elif input() == "3":
            print("Welcome to hard level, you have 3 lives!")
            return get_random_word()
        else:
            print("Please select the correct number!")
            return menu()

    set_difficulty()


menu()"""
