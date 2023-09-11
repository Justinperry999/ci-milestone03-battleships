import random


def menu():
    """
    Allows user to choose whether to read instructions, play game or exit.
    """
    print("[1] Instructions")
    print("[2] Play Battleships")
    print("[0] Exit Game")

menu()
option = int(input("Enter your option:\n"))

while option != 2:
    if option == 1:
        #go to instructions
        print("Instructions has been called")
    elif option == 0:
        #Exit Game
        print("Thank you for playing Battleships! Goodbye!")
    else:
        print("Invalid option!")

    print()
    menu()
    option = int(input("Enter your option:\n"))


ROWS = 5
COLUMNS = 5



print("Welcome to the Battleships!")
print(" ")
print("Lets sink some ships!")

print()
play_game = input("Would you like to play? (y/n):\n")

while play_game != "y":
    if play_game == "n":
        print("Thank you for playing Battleships! Goodbye!")
        menu()
    else:
        print("Invalid option!")

print("Initializing game...")
print()

def create_ships(board):
    return random.randrange(ROWS), random.randrange(COLUMNS)

def play_game():

    board = []

    for x in range(5):
        board.append(["0"] * 5)

    for row in board:
        print((" ").join(row))
    print()

    ship1 = create_ships(board)
    ship2 = create_ships(board)
    ship3 = create_ships(board)
    ship4 = create_ships(board)
    ships_left = 4
    ammo = 10

    
    while ammo:
        try:
            row = int(input(f"Enter a row number between 1-{ROWS} >: "))
            column = int(input(f"Enter a column number between 1-{COLUMNS} >: "))
        except ValueError:
            print("Only enter number!")
            continue

        if row not in range(1,6) or column not in range(1, 6):
            print("\nThe numbers must be between 1-6!")
            continue

        row = row - 1 # Reducing number to desired index.
        column = column - 1 # Reducing number to desired index.

        if board[row][column] == "-" or board[row][column] == "X":
            print("\nYou have already shoot there! Please choose another position.\n")
            continue
        elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3 or (row, column) == ship4:
            print("\nBoom! You hit! A ship has exploded! You were granted a new ammo!\n")
            board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("My my, i didn't know you were a sharpshooter! Congratz, you won!")
                play_again()
        else:
            print("\nYou missed!\n")
            board[row][column] = "-"
            ammo -= 1

play_game()