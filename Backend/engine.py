import math
from main import is_game_over, alpha_beta_pruning, Player


turn = Player.RED
difficulty = 5


def print_board(board):
    for row in board:
        for cell in row:
            print("R" if cell == Player.RED else "B" if cell == Player.BLUE else "#", end=" ")
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


def computer_move(board):
    global turn

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
            board = human_move(board)
        elif turn == Player.BLUE:
            board = computer_move(board)

        turn = Player.RED if turn == Player.BLUE else Player.BLUE

    print_board(board)


if __name__ == "__main__":
    play()
