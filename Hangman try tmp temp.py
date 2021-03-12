def get_word():
    with open("countries-and-capitals.txt", "r") as file:
        all_text = file.read()
        part_line = all_text.split(" | ")
        word_position = random.randint(0, len(all_text)-1)
        whole_word = all_text[word_position]
        word_list = whole_word.split("\n")
        x = input("Choose a category! \n1 - Countries\n2 - Capitals\n3 - Both\n")
        if x == 1:
            word = word_list[0]
        elif x == 2:
            word = word_list[1]
        elif x == 3:
            word = word_list[random.randint(0, 1)]
        return(word)

print(get_word())


with open("countries-and-capitals.txt", "r") as file:

    lines = file.readline()

    list = lines
    word_list  = []

    for lines in list:
      word_list.append(lines)

    new_lines = lines.strip("\n")

    new_lines_lines = new_lines.split(" | ")

    words = random.choice(new_lines_lines)

    print(words)
    # append akkor mehet tovább!

    countries = []
    capitals = []

with open("countries-and-capitals.txt", "r") as file:

    lines = file.readline()

    count = 1

    for lines in file:
      count += 1

    new_lines = lines.strip("\n")

    new_lines_lines = new_lines.split(" | ")

    words = random.choice(new_lines_lines)

    print(words)
    # append akkor mehet tovább!

    countries = []
    capitals = []

with open("countries-and-capitals.txt", "r") as file:

    lines = file.readline()

    count = 1
    list = []

    for lines in file:
        count += 1
        new_lines = list.append(lines)


    new_lines = lines.strip("\n")

    new_lines_lines = new_lines.split(" | ")

    words = random.choice(new_lines_lines)

    print(words)
    # append akkor mehet tovább!

    countries = []
    capitals = []
