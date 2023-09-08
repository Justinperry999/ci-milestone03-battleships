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

board = []

for x in range(6):
  board.append(["_"] * 6)

def game_board(board):
  for row in board:
    print((" ").join(row))

print("Welcome to the Battleships!")
print(" ")
print("Lets sink some ships!")
game_board(board)

print()
play_game = input("Would you like to play? (y/n):\n")

while play_game != "y":
    if play_game == "n":
        print("Thank you for playing Battleships! Goodbye!")
        menu()
    else:
        print("Invalid option!")

print("Initializing game...")

def create_ships(board):
    return random.randint(0, 6), random.randint(0, 6)


ship1 = create_ships(board)
ship2 = create_ships(board)
ship3 = create_ships(board)
ship4 = create_ships(board)
ship5 = create_ships(board)
ships_left = 5
ammo = 15
