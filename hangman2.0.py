import random
import string
import atexit
import sys


def guess_word():
    with open('countries-and-capitals.txt', 'r') as file:
        text = file.read()
        coupital = text.split(' | ')
        position = random.randint(0, len(coupital)-1)
        randword = coupital[position]
        final = randword.split('\n')
        return final[random.randint(0, 1)]


guess_word()


def hide_word():
    hided_word = []
    for _ in len(guess_word):
        hided_word.append("_ ")
        return hided_word

hide_word()

def print_hide_word(hide_word):
    output = ""
    space = len(guess_word) # lekérjük a guess word hosszát
    print("Let's play Hangman!\n")
    print("_ " * space) # kicseréljük

print_hide_word()


"""def force_vaild_character(valid):
    letters = list(string.ascii_letters)
    if valid in letters or valid.lower() in letters:
        return True
    else:
        return False

force_vaild_character()"""

def play():
    guessed_word = guess_word()
    hided_word = hide_word(guess_word)



"""def ask_for_letter():
    guessed_word = guess_word()
    guessed_letter = []

    while guess_letter live > 0 and guess_letter:
        guess_letter = input("Please guess a letter: ")
        if guess_letter in guess_word():
            guess_letter = guess_letter.replace("_ ", guess_letter)
            guessed_letter.append(guess_letter) # ezzel felveszem a listába a tippelt betűt!
            return guess_letter
        elif guess_letter == guessed_letter:
            print("You already guessed this letter!")
            return(guess_letter)
        elif guess_letter == "quit":
            print("Good bye!")
            sys.exit()
        elif guess_letter not in guess_word:
            guess_letter = print("Wrong guess!")


ask_for_letter()

def exit(user):
    print(user, " exit Python application")"""








