import math

from engine.alpha_beta_pruning import alpha_beta_pruning
from engine.minimax import minimax
from engine.rules import is_game_over
from type_definitions import Player


class Difficulty:
    EASY = 1
    MEDIUM = 3
    HARD = 5


turn = Player.RED
difficulty = Difficulty.HARD


def print_board(board):
    for row in board:
        for cell in row:
            print("R" if cell == Player.RED else "B" if cell ==
                  Player.BLUE else "#", end=" ")
        print()
    print()


def human_move(board):
    column = int(input("Enter column: "))

    if board[0][column]:
        print("Invalid move")
        return human_move(board)

    for row in range(len(board) - 1, -1, -1):
        if not board[row][column]:
            board[row][column] = turn
            break

    return board


def computer_move(board, flag):
    global turn
    global difficulty
    if not flag:
        move = minimax(board, difficulty, turn)
    else:
        move = alpha_beta_pruning(board, difficulty, -math.inf, math.inf, turn)

    column = move.column

    for row in range(len(board) - 1, -1, -1):
        if not board[row][column]:
            board[row][column] = turn
            break

    return board


def play():
    global turn

    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]

    while not is_game_over(board):
        print_board(board)

        if turn == Player.RED:
            board = computer_move(board)
        elif turn == Player.BLUE:
            board = computer_move(board)

        turn = Player.RED if turn == Player.BLUE else Player.BLUE

    print_board(board)


if __name__ == "__main__":
    play()
