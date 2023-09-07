from random import randint


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

cpu_board = []
user_board = []

for x in range(6):
  cpu_board.append(["_"] * 6)
  user_board.append(["_"] * 6)

def cpu_game_board(cpu_board):
  for row in cpu_board:
    print((" ").join(row))

def user_game_board(user_board):
  for row in user_board:
    print((" ").join(row))

print("Welcome to the Battleships!")
print(" ")
print("Computer's Board")
cpu_game_board(cpu_board)
print(" ")
print("Your Board")
user_game_board(user_board)










"""
def create_board(board):
    hidden_board = [[' '] * 6 for x in range[6]]
    guess_board = [[' '] * 6 for x in range[6]]
    letters_to_numbers = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5}
    print('     A B C D E F')
    print('     -----------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_cpu_ships(board):
    ship_row = randint(0,len(board)-1)
    ship_col = randint(0, len(board[0])-1)
    ship_position = ship_row,ship_col

def rungame():
    print("Welcome to Battleships!")    
    create_board(board)
    create_cpu_ships(board)
"""