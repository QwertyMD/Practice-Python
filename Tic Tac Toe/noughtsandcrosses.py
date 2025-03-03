"""
Imports necessary modules for the game.

Modules:
    random: Provides functions to generate random numbers.
    os.path: Provides functions for interacting with the OS's file system.
    json: Provides functions for working with JSON data.
"""

import random
import os.path
import json

random.seed()


def draw_board(board):
    """
    Draws the Noughts and Crosses board.

    Args:
        board (list): A list of list representing the game board.
    """
    for row in board:
        print(("-" * 11).center(30))
        print(("| " + " | ".join(row) + " |").center(30))
    print(("-" * 11).center(30))


def welcome(board):
    """
    Prints the welcome message and displays the initial game board.

    Args:
        board (list): A list of list representing the current state of the game board.
    """
    print('Welcome to the "Unbeatable Noughts and Crosses" game.')
    print("The board layout is shown below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the sqaure you want.")


def initialise_board(board):
    """
    Initializes the game board by setting all elements to a single space character ' '.

    Args:
        board (list): A list of list representing the game board.

    Returns:
        board (list): The initialized game board with all elements set to ' '.
    """
    print()
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            board[i][j] = " "
    return board


def get_player_move(board):
    """
    Prompts the user to place their 'X' on the board and returns the corresponding row, col.

    User is asked to input a number corresponding to the desired square.
    Checks if the move is valid (within range 1-9 and chosen square is not already taken).
    If move is valid, it returns the row and col of the chosen square.
    If move is invalid or the square is already taken, user is prompted to try again.

    Args:
        board (list): The current state of the board, where each cell is either 'X', 'O', or ' '.

    Returns:
        row, col (tuple): A tuple (row, col) representing row and col of chosen square.
    """
    print("1 2 3".center(46))
    print("4 5 6".center(46))
    player_move = input("Choose your square: 7 8 9 : ")
    moves = {
        "1": (0, 0),
        "2": (0, 1),
        "3": (0, 2),
        "4": (1, 0),
        "5": (1, 1),
        "6": (1, 2),
        "7": (2, 0),
        "8": (2, 1),
        "9": (2, 2),
    }
    if player_move in moves:
        row, col = moves[player_move]
        if board[row][col] == " ":
            return row, col
        print()
        print("Square already taken. Try again.")
        draw_board(board)
        return get_player_move(board)
    print()
    print("Invalid move. Try again.")
    draw_board(board)
    return get_player_move(board)


def choose_computer_move(board):
    """
    Determines the computer's move to choose the square.

    Scans the provided game board for empty cells, randomly selects one of them,
    and returns the row and col of the chosen cell.

    Args:
        board (list): A list of list representing the game board, where each square
                      contains either 'X', 'O', or ' '.

    Returns:
        row, col (tuple): A tuple (row, col) representing row and col of chosen square.
    """
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))
    row, col = random.choice(empty_cells)
    return row, col


def check_for_win(board, mark):
    """
    Check if either 'X' or '0' has won the game on the board.
    Checks all rows, cols, and both diagonals to determine a winning line.

    Args:
        board (list): A list of list representing the game board.
        mark (str): The mark to check for a win ('X' or 'O').

    Returns:
        bool: True if the given mark has won, False otherwise.

    """
    for row in board:
        if row[0] == row[1] == row[2] == mark:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False


def check_for_draw(board):
    """
    Check if the game board is in a draw state.

    This function checks if all cells on the game board are occupied.
    If all cells are occupied, it returns True indicating a draw.
    If there is at least one empty cell, it returns False.

    Args:
        board (list): A list of list representing the game board.

    Returns:
        bool: True if all cells are occupied (draw), False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True


def play_game(board):
    """
    Plays a game of Noughts and Crosses on the given board.

    Alternates between the player and the computer moves until win or draw.
    The player plays with "X" and the computer plays with "0".

    Args:
        board (list): The game board, a list of list representing the
                      current state of the game.

    Returns:
        int: The result of the game. Returns 1 if the player wins, -1 if the
             computer wins, and 0 if the game is a draw.
    """
    board = initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = "X"
        print()
        draw_board(board)
        if check_for_win(board, "X"):
            print("Congratulations! You Won.")
            return 1
        if check_for_draw(board):
            print("It's a Draw.")
            return 0
        row, col = choose_computer_move(board)
        board[row][col] = "0"
        print(f"Computer chose {row * 3 + col + 1}")
        draw_board(board)
        if check_for_win(board, "0"):
            print("Computer Won.")
            return -1
        if check_for_draw(board):
            print("It's a Draw.")
            return 0


def menu():
    """
    Displays a menu with options for user to select and return the user's choice.

    Returns:
        str: The user's choice ('1', '2', '3', or 'q').
    """
    print()
    print("Enter one of the following options: ")
    print("1 - Play the Game")
    print("2 - Save your score in the leaderboard")
    print("3 - Load and display the leaderboard")
    print("q - End the program")
    choice = input("1, 2, 3 or q? ")
    return choice


def load_scores():
    """
    Loads the leaderboard scores from the file 'leaderboard.txt'.

    Checks if the file 'leaderboard.txt' exists in the current directory.
    If it exists, it reads the content of the file, and loads it into a dictionary.
    If it exists but is empty, it returns an empty dictionary.
    If it doesn't exist, it returns an empty dictionary.

    Returns:
        leaders (dict): A dictionary containing the leaderboard scores.
    """
    print()
    leaders = {}
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r", encoding="utf-8") as file:
            data = file.read() or "{}"
        leaders = json.loads(data)
    else:
        print("leaderboard.txt doesn't exist")
    return leaders


def save_score(score):
    """
    Prompts the player for name and saves the current score to 'leaderboard.txt'.

    If 'leaderboard.txt' exists, it reads the existing data, updates it with the new score,
    and writes the updated data back to the file.
    If the file does not exist, it prints an error message.

    Args:
        score (int): The score to be saved.
    """
    print()
    name = input("Enter name: ")
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r", encoding="utf-8") as file:
            data = file.read() or "{}"
            data = json.loads(data)
        data[name] = score
        with open("leaderboard.txt", "w", encoding="utf-8") as file:
            file.write(json.dumps(data))
        print("Saved to leaderboard.txt")
    else:
        print("Couldn't save, leaderboard.txt doesn't exist.")


def display_leaderboard(leaders):
    """
    Displays the leaderboard scores.

    Args:
        leaders (dict): A dictionary where keys are player names and values are their scores.
    """
    for key, val in leaders.items():
        print(f"{key}: {val}")
