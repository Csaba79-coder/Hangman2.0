import random
import string
import sys


def main():
    print('Welcome to Hangman 2.0')
    name = input('What is your name? ')
    print('Good luck ' + name.capitalize() + '!')
    lives = 7
    word = guess_word()
    play(word, lives)
    guess_letters(word)


def difficulty(i):
    lives = 7
    while True:
        print('Choose a difficulty')
        print("[1] Easy level with 7 lives")
        print("[2] Medium level with 5 lives")
        print("[3] Hard level with 3 lives")
        print("[0] Exit the program")
        option = int(input("Enter your option: "))
        while option != 0:
            if option == 1:
                print("Selected: easy level with 7 lives!")
                return lives
            elif option == 2:
                print("Selected: medium level with 5 lives!")
                return (lives)-2
            elif option == 3:
                print("Selected: hard level with 3 lives!")
                return (lives)-4
            else:
                print("Unknown Option Selected!")
                break
            return menu()
        if option == 0:
            print('Thanks for playing with Hangman2.0! Good bye!')
            sys.exit()


def guess_word():
    with open('countries-and-capitals.txt', 'r') as file:
        text = file.read()
        coupital = text.split(' | ')
        position = random.randint(0, len(coupital)-1)
        randword = coupital[position]
        final = randword.split('\n')
        return final[random.randint(0, 1)]


def play(word, lives):
    lives = difficulty(i=True)
    print('Starting game now!')
    print('Here\'s the word to guess!')
    guess_letter = []
    unknown_word = []
    printed_unknown_word = ""
    for char in word:
        if char == ' ':
            unknown_word.append(char)
        else:
            unknown_word.append("_ ")
    for x in unknown_word:
        printed_unknown_word += x
    print(printed_unknown_word+"\n")
    print(word)


def guess_letters(word):
    guesses = 0
    wordlist = list(word)
    blanks = "" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []
    print("Let's play Hangman!\n")
    print("\n" + ' '.join(blanks_list))
    print("\n")
    print("Please guess a letter: ")
    while guesses < 6:
        guess = input("Guess letter: -> ")
        guess = guess.lower()
        if len(guess) > 1:
            print("Please enter only one letter!")
        elif guess == "":
            print("Please enter a letter!")
        elif guess in guess_list:
            print("Already guessed! Here are the letters what you have guessed:")
            print(' '.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = wordlist[i]
                i = i + 1
            if new_blanks_list == blanks_list:
                print("\nYou have guessed a wrong letter.")
                # print_design(guesses, word)

                if guesses < 6:
                    print("Please guess again.")
                    print(' '.join(blanks_list))

            elif wordlist != blanks_list:
                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))
                if wordlist == blanks_list:
                    print("\nYOU WIN!")
                    print("Would you like to play again? Type 1 for Yes and 2 for No")
                    again = input("-> ")
                    if again == "1":
                        return guess_letters()
                    else:
                        print("Good bye!")
                        exit()

                else:
                    print("\nGreat guess! Guess the next!")


if __name__ == '__main__':

