import random

def menu():
    print("[1] Instructions")
    print("[2] Play Battleships")
    print("[0] Exit Game")

menu()
option = int(input("Enter your option:\n"))

while option != 0:
    if option == 1:
        #go to instructions
        print("Instructions has been called")
    elif option == 2:
        #Play Battleships
        print("Play Battleships has been called")
    else:
        print("Invalid option!")

    print()
    menu()
    option = int(input("Enter your option:\n"))

print("Thank you for playing Battleships! Goodbye!")