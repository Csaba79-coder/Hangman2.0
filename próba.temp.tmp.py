import random


def hide_character():
    for i in range(0, len(word)):
        if ord(word[i]) != 32:
            new_word = word
            new_word = new_word.replace(word[i], "_ ")



hide_character()

guesses = 0
    words = word()
    blanks = "_ " * len(words)
    blanks_list = list(blanks)
    print("Let's play Hangman!\n")
    print("\n" + ''.join(blanks_list))


with open("countries-and-capitals.txt", "r") as file:

    with open("countries-and-capitals.txt", "r") as file:
        lines_list = []

        lines = file.read()

        for lines in lines_list:
            lines_list.append(lines)
            capitals.append(lines)
            lines_list.append(lines)
        print(lines_list)

        new_lines = lines.strip("\n")

        new_lines_lines = lines.split(" | ")

        words = random.choice(new_lines_lines)
        print(words)

        # countries = []
        # capitals = []