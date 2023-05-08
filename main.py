import math
from random import random

from type_definitions import Player, Board, Score, Window, COLUMN_COUNT, ROW_COUNT
from typing import Union


def winning_move(board: Board, player: Player) -> bool:
    # Check horizontal locations for win
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and \
                    board[row][col + 3] == player:
                return True
    # Check vertical locations for win
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT - 4):
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and \
                    board[row + 3][col] == player:
                return True
    # Check positively sloped diagonals
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT - 4):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and \
                    board[row + 3][col + 3] == player:
                return True
    # Check negatively sloped diagonals
    for col in range(COLUMN_COUNT - 3):
        for row in range(2, ROW_COUNT):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and \
                    board[row - 3][col + 3] == player:
                return True


def minimax(
        board: Board,
        depth: int,
        player: Player
):
    places = []
    for col in range(COLUMN_COUNT):
        if board[0][col] == None:
            places.append(col)

    if winning_move(board, Player.RED):
        return 1
    elif winning_move(board, Player.BLUE):
        return 1
    elif (len(places) == 0):
        return 0
    if depth == 0:
        return evaluate_board(board, player)

    if player == Player.RED:
        value = -math.inf
        column = random.choice(places)
        openRow = None
        for col in places:
            for row in range(ROW_COUNT):
                if board[row][col] == 0:
                    openRow = row

            b_copy = board.copy()
            board[openRow][col] = Player.RED
            new_score = minimax(b_copy, depth - 1, Player.BLUE)
            if new_score > value:
                value = new_score
                column = col
        return value
    else:
        value = math.inf
        column = random.choice(places)
        openRow = None
        for col in places:
            for row in range(ROW_COUNT):
                if board[row][col] == 0:
                    openRow = row

            b_copy = board.copy()
            board[openRow][col] = Player.BLUE
            new_score = minimax(b_copy, depth - 1, Player.RED)
            if new_score < value:
                value = new_score
                column = col
        return value


def alphaBetapruning(
        board: Board,
        depth: int,
        alpha: int,
        beta: int,
        player: Player
):
    places = []
    for col in range(COLUMN_COUNT):
        if board[0][col] == None:
            places.append(col)

    if winning_move(board, Player.RED):
        return 1
    elif winning_move(board, Player.BLUE):
        return 1
    elif (len(places) == 0):
        return 0
    if depth == 0:
        return evaluate_board(board, player)

    if player == Player.RED:
        value = -math.inf
        column = random.choice(places)
        openRow = None
        for col in places:
            for row in range(ROW_COUNT):
                if board[row][col] == 0:
                    openRow = row

            b_copy = board.copy()
            board[openRow][col] = Player.RED
            new_score = minimax(b_copy, depth - 1, Player.BLUE)
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = math.inf
        column = random.choice(places)
        openRow = None
        for col in places:
            for row in range(ROW_COUNT):
                if board[row][col] == 0:
                    openRow = row

            b_copy = board.copy()
            board[openRow][col] = Player.BLUE
            new_score = minimax(b_copy, depth - 1, Player.RED)
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


# Evalute the board
def evaluate_board(board: Board, player: Player):
    ...


def is_game_over(board: Board) -> Union[Player, None]:
    ...


def evaluate_window(window: Window, player: Player) -> Score:
    ...
