import random
import string
import sys

def guess_word():
    with open('countries-and-capitals.txt', 'r') as file:
        text = file.read()
        coupital = text.split(' | ')
        position = random.randint(0, len(coupital)-1)
        randword = coupital[position]
        final = randword.split('\n')
        return final[random.randint(0, 1)]

"""
def force_vaild_character(valid):
    letters = list(string.ascii_letters)
    if valid in letters or valid.lower() in letters:
        return True
    else:
        return False

force_vaild_character()

def ask_for_letter(i):
    guessed_word = guess_word()
    guessed_letter = []
    
"""

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
    while True:
        guess_letter = input("Please guess a letter: ")
        if guess_letter in printed_unknown_word:
#            correct_letter = guess_letter.replace("_", 'guess_letter')
            printed_unknown_word.append(correct_letter) # ezzel felveszem a listába a tippelt betűt!
            return printed_unknown_word
        
        elif guess_letter == "quit":
            print("Good bye!")
            sys.exit()
        


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
                print("Invalid option! Please select again!")
        if option == 0:
            print('Thanks for playing with Hangman2.0! Good bye!')
            sys.exit()


def tries(lives):
    if lives >= 7:
        with open('Hanging(7)', 'r') as seven:
            se = seven.read()    
        print(se)
    elif lives == 6:
        with open('Hanging(6)', 'r') as six:
            si = six.read()
        print(si)
    elif lives == 5:
        with open('Hanging(5)', 'r') as five:
            fi = five.read()
        print(fi)
    elif lives == 4:
        with open('Hanging(4)', 'r') as four:
            fo = four.read()
        print(fo)
    elif lives == 3:
        with open('Hanging(3)', 'r') as three:
            th = three.read()
        print(th)
    elif lives == 2:
        with open('Hanging(2)', 'r') as two:
            tw = two.read()
        print(tw)
    elif lives == 1:
        with open('Hanging(1)', 'r') as one:
            on = one.read()
        print(on)
    else:
        with open('Hanging(0)', 'r') as game_over:
            lose = game_over.read()
        print(lose)
        while True:
            play = input('Would you give it another try?')
            if play == 'y' or 'yes':
                main()
            elif play == 'n' or 'no':
                sys.exit()
            else:
                print('Please choose yes or no as an answer')


def main():
    lives = 7
    word = guess_word()
    play(word, lives)


if __name__ == '__main__':
    print('Welcome to Hangman 2.0')
    name = input('What is your name? ')
    print('Good luck '+ name + '!')
    main()