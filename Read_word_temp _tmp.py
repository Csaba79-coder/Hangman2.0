import random

def get_random_word():
    with open("countries-and-capitals.txt", "r") as file:
        lines = file.readlines()

        count = 1
        list = []

        for lines in file:
            count += 1

        new_lines = lines.strip("\n")

        new_lines_lines = new_lines.split(" | ")

        words = random.choice(new_lines_lines)

        # append akkor mehet tovább!

        countries = []
        capitals = []

