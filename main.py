from type_definitions import Player, Board, Score, Window
from typing import Union


def minimax(
        board: Board,
        depth: int,
        alpha: int,
        beta: int,
        player: Player
) -> Score:
    return 0


# Evalute the board
def evaluate_board(board: Board, player: Player):
    value = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if col + 3 < len(board[0]):
                value += evaluate_window([
                    board[row][col + 0],
                    board[row][col + 1],
                    board[row][col + 2],
                    board[row][col + 3]
                ], player)
            if row + 3 < len(board):
                value += evaluate_window([
                    board[row + 0][col],
                    board[row + 1][col],
                    board[row + 2][col],
                    board[row + 3][col]
                ], player)
            if row + 3 < len(board) and col + 3 < len(board[0]):
                value += evaluate_window([
                    board[row + 0][col + 0],
                    board[row + 1][col + 1],
                    board[row + 2][col + 2],
                    board[row + 3][col + 3]
                ], player)
            if row + 3 < len(board) and col - 3 >= 0:
                value += evaluate_window([
                    board[row + 0][col - 0],
                    board[row + 1][col - 1],
                    board[row + 2][col - 2],
                    board[row + 3][col - 3]
                ], player)

        return value


def is_game_over(board: Board) -> Union[Player, None]:
    ...


def evaluate_window(window: Window, player: Player) -> Score:
    ...
