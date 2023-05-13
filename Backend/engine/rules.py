from typing import Union

from type_definitions import Board, Player


def is_game_over(board: Board) -> Union[Player, None, str]:
    # check if there are 4 pieces horizontally, vertically, or diagonally
    # if there are, return the winning player

    if board[0].count(None) == 0:
        return "draw"

    for row in range(len(board)):
        for col in range(len(board[0])):
            # Horizontal Window Check
            if col + 3 < len(board[0]):
                window = [
                    board[row][col + 0],
                    board[row][col + 1],
                    board[row][col + 2],
                    board[row][col + 3]
                ]

                if window.count(Player.RED) == 4:
                    return Player.RED
                elif window.count(Player.BLUE) == 4:
                    return Player.BLUE

            # Vertical Window Check
            if row + 3 < len(board):
                window = [
                    board[row + 0][col],
                    board[row + 1][col],
                    board[row + 2][col],
                    board[row + 3][col]
                ]

                if window.count(Player.RED) == 4:
                    return Player.RED
                elif window.count(Player.BLUE) == 4:
                    return Player.BLUE

            # Diagonal Window Check
            if row + 3 < len(board) and col + 3 < len(board[0]):
                window = [
                    board[row + 0][col + 0],
                    board[row + 1][col + 1],
                    board[row + 2][col + 2],
                    board[row + 3][col + 3]
                ]

                if window.count(Player.RED) == 4:
                    return Player.RED
                elif window.count(Player.BLUE) == 4:
                    return Player.BLUE

            # Diagonal Window Check
            if row + 3 < len(board) and col - 3 >= 0:
                window = [
                    board[row + 0][col - 0],
                    board[row + 1][col - 1],
                    board[row + 2][col - 2],
                    board[row + 3][col - 3]
                ]

                if window.count(Player.RED) == 4:
                    return Player.RED
                elif window.count(Player.BLUE) == 4:
                    return Player.BLUE
