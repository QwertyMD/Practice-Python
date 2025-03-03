"""
This module contains the main function to play "Unbeatable Noughts and Crosses" game.
"""

from noughtsandcrosses import (
    welcome,
    menu,
    play_game,
    save_score,
    load_scores,
    display_leaderboard,
)


def main():
    """
    The main function to run the "Unbeatable Noughts and Crosses" game.

    Initializes game board, displays welcome message, and enters loop to present the menu.
    User can choose to play the game, save their score, view the leaderboard, or quit the game.

    The function keeps track of the total score and updates it after each game.
    """
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == "1":
            score = play_game(board)
            total_score += score
            print("Your current score is:", total_score)
        if choice == "2":
            save_score(total_score)
        if choice == "3":
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == "q":
            print()
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print("Good Bye!")
            return


if __name__ == "__main__":
    main()
