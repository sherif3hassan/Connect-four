import math
import random

from type_definitions import (
    COLUMN_COUNT,
    ROW_COUNT,
    Board,
    Player,
    Move
)


def minimax(
        board: Board,
        depth: int,
        player: Player
) -> Move:
    # list of possible moves
    available_columns = []
    for col in range(COLUMN_COUNT):
        if not board[0][col]:
            available_columns.append(col)

    winner = is_game_over(board)
    if winner == Player.RED:
        return Move(None, math.inf)
    elif winner == Player.BLUE:
        return Move(None, -math.inf)
    elif winner == "draw":
        return Move(None, 0)

    # if the depth is reached, evaluate the board and return the evaluation score
    if depth == 0:
        eval = evaluate_board(board, player)
        return Move(None, eval)

    if player == Player.RED:
        value = -math.inf

        first_available_row = None
        actual_column = random.choice(available_columns)

        # for each possible move, find the row where the piece will be placed
        for col in available_columns:
            for row in range(ROW_COUNT - 1, -1, -1):
                # if the row is empty, place the piece in that row
                if not board[row][col]:
                    first_available_row = row
                    break

            # create a copy of the board and place the piece in the empty row
            new_board = [[cell for cell in row] for row in board]
            new_board[first_available_row][col] = Player.RED
            # recursively call minimax with the new board, depth - 1, and the next player's turn
            new_move = minimax(new_board, depth - 1, Player.BLUE)
            new_score = new_move.score
            # if the new score is greater than the current value, set the value to the new score
            if new_score > value:
                value = new_score
                actual_column = col
        return Move(actual_column, value)
    else:
        # same as above, but for the blue player
        value = math.inf

        first_available_row = None
        actual_column = random.choice(available_columns)
        for col in available_columns:
            for row in range(ROW_COUNT - 1, -1, -1):
                if not board[row][col]:
                    first_available_row = row
                    break

            new_board = [[cell for cell in row] for row in board]
            new_board[first_available_row][col] = Player.BLUE
            new_move = minimax(new_board, depth - 1, Player.RED)
            new_score = new_move.score
            if new_score < value:
                value = new_score
                actual_column = col
        return Move(actual_column, value)
