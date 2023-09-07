import random

def create_board(board):
    hidden_board = [[' '] * 8 for x in range[8]]
    guess_board = [[' '] * 8 for x in range[8]]
    letters_to_numbers = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
    print('     A B C D E F G H')
    print('     ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def menu():
    """
    Allows user to choose whether to read instructions, play game or exit.
    """
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



