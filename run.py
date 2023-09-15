import random

ROWS = 5
COLUMNS = 5
board = []


def welcome():
    """
    Display a welcome message and the main menu.
    """
    print()
    print("                   __/___        ")
    print("             _____/______|        ")
    print("     _______/_____\\______\\_____   ")
    print("     \\              < < <       |    ")
    print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    ")
    print()
    print("----------------------------")
    print("Welcome to Battleships!")
    print(" ")
    print("Let's sink some ships!")
    print("----------------------------")
    print()
    menu()


def menu():
    """
    Allows user to choose whether to read instructions, play game or exit.
    """
    print("[1] Instructions")
    print("[2] Play Battleships")
    print("[0] Exit Game")
    print()
    menu_option()


def display_instructions():
    """
    Display game instructions for Battleships.

    This function provides a set of instructions to the player on how to play
    the Battleships game.
    """
    print("----------------------------")
    print(" ")
    print("Welcome to the Battleships game!")
    print(" ")
    print("Instructions:")
    print()
    print("1. You are the commander of a fleet of battleships.")
    print("2. Your goal is to sink all the enemy ships in the ocean grid.")
    print("3. The ocean grid is a 5x5 board with coordinates from.")
    print("   row 1, column 1 to row 5, column 5.")
    print("4. You will take turns to fire missiles at the enemies grid.")
    print("5. You will input the coordinates of your missile target.")
    print("   (e.g., row:1 column:1).")
    print("6. If your missile hits an enemy ship, you will see 'Hit!'")
    print("   and an 'X' will appear on the board.")
    print("7. If your missile misses, you will see 'Miss.' and a '-'")
    print("   will appear on the board.")
    print("8. Continue taking shots until all of the enemy ships are sunk")
    print("   and the enemy fleet is defeated!")
    print("9. You win the game if you sink all enemy ships. You have")
    print("   10 missiles, use them wisely!")
    print("10. Good luck, Commander!")
    print(" ")
    print("----------------------------")
    menu()


def menu_option():
    """
    Get a valid menu option from the user.

    This method prompts the user to enter a menu option (1, 2, or 0) and
    continues to do so until a valid option is provided.
    """
    option = input("Enter your option:\n")
    while option not in ["1", "2", "0"]:
        print("Invalid option!\n")
        option = input("Enter your option:\n")
    if option == "1":
        display_instructions()
    elif option == "2":
        play_game()
    else:
        print()
        print("Goodbye!")
        print()


def create_ships(board):
    """
    Create random ship coordinates on the board.
    """
    return random.randrange(ROWS), random.randrange(COLUMNS)


def create_board(board_to_print):
    """
    Create random ship coordinates on the board.
    """
    for row in board_to_print:
        print((" ").join(row))
    print()


def play_game():
    """
    Play the Battleships game.
    """

    board = []

    for x in range(5):
        board.append(["0"] * 5)
    print()
    print("ENEMY SHIP'S APPROACHING!")
    print("LET'S SINK SOME SHIPS!")
    print()
    create_board(board)

    ship1 = create_ships(board)
    ship2 = create_ships(board)
    ship3 = create_ships(board)
    ship4 = create_ships(board)
    ships_left = 4
    ammo = 10

    while ammo:
        try:
            row = int(input(f"Enter a row number between 1-{ROWS} >: "))
            column = int(
                input(
                    f"Enter a column number between 1-{COLUMNS} >: "
                )
            )
        except ValueError:
            print("Only enter number!\n")
            continue

        if row not in range(1, 6) or column not in range(1, 6):
            print("\nThe numbers must be between 1-5!\n")
            continue

        row = row - 1  # Reducing number to desired index.
        column = column - 1  # Reducing number to desired index.

        if board[row][column] == "-" or board[row][column] == "X":
            print(
                "\n{} {}\n".format(
                    "You have already shoot there!",
                    "Please choose another position.",
                )
            )
            continue
        elif (
            (row, column) == ship1 or
            (row, column) == ship2 or
            (row, column) == ship3 or
            (row, column) == ship4
        ):
            print(
                "\n{} {}\n".format(
                    "Boom! You hit! A ship has exploded!",
                    "You were granted another shot!",
                )
            )
            board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print(
                    "You sunk all the enemy ships! {}\n".format(
                        "Congratulations, you won!",
                    )
                )
                menu()
        else:
            print("\nYou missed!\n")
            board[row][column] = "-"
            ammo -= 1

        # After each guess, call create_board(board)
        # to print the updated board.
        create_board(board)

    # End of game message if the user doesn't sink all the ships.
    print(
        "{}{}{}".format(
            "Game over! You ran out of ammo, ",
            "and the enemy ships are still afloat. ",
            "Better luck next time!",
        )
    )
    print()
    menu()


welcome()