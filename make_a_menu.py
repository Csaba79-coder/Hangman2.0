def menu():

    print("Welcome to Hangman2.0!")
    print("[1] Option - easy level with 7 lives")
    print("[2] Option - medium level with 5 lives")
    print("[3] Option - hard level with 3 lives")
    print("[0] Exit the program")

menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        print("Selected: easy level with 7 lives!")
        play(easy)
    elif option == 2:
        print("Selected: medium level with 5 lives!")
        play(medium)
    elif option == 3:
        print("Selected: hard level with 3 lives!")
        play(hard)
    else:
        print("Invalid option! Please select again!")

    print()
    menu()
    option = int(input("Enter your option: "))

print("Thanks for playing with Hangman2.0! Good bye!")

def play(easy):
    pass

def play(medium):
    pass
def play(hard):
    pass