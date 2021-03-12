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



def hide_word():
    hide_word = []
    hide_word.append(guess_word())
    return hide_word

print(hide_word())



def hide():
    hide_word = guess_word()
    space = len(hide_word) # lekérjük a guess word hosszát
    print("Let's play Hangman!\n")
    print("_ " * space) # kicseréljük



"""def force_vaild_character(valid):
    letters = list(string.ascii_letters)
    if valid in letters or valid.lower() in letters:
        return True
    else:
        return False

force_vaild_character()"""


def ask_for_letter():
    guessed_word = guess_word()
    guess_letter = input("Please guess a letter: ")
    guessed_letter = []
    if guess_letter in guess_word():
        guess_letter = guessletter.replace(" ", guess_letter)
        guessed_letter.append(guess_letter) # ezzel felveszem a listába a tippelt betűt!
        print(guess_letter)
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
    print(user, " exit Python application")