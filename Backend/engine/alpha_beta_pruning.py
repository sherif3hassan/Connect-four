import math
import random

from engine.rules import is_game_over
from engine.evaluation import evaluate_board

from type_definitions import (
    COLUMN_COUNT,
    ROW_COUNT,
    Board,
    Player,
    Move
)


def alpha_beta_pruning(
        board: Board,
        depth: int,
        alpha: int,
        beta: int,
        player: Player
) -> Move:

    # list of possible moves
    available_columns = [
        col for col in range(COLUMN_COUNT) if not board[0][col]
    ]

    winner = is_game_over(board)

    if winner == Player.RED:
        return Move(None, math.inf)

    elif winner == Player.BLUE:
        return Move(None, -math.inf)

    elif winner == "draw":
        return Move(None, 0)

    # if the depth is reached, return the score of the board
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
                if not board[row][col]:
                    # if the row is empty, place the piece in that row
                    first_available_row = row
                    break

            # create a copy of the board and place the piece in the empty row
            new_board = [[cell for cell in row] for row in board]
            new_board[first_available_row][col] = Player.RED
            new_move = alpha_beta_pruning(
                new_board,
                depth - 1,
                alpha,
                beta,
                Player.BLUE
            )
            new_score = new_move.score

            if new_score > value:
                value = new_score
                actual_column = col

            alpha = max(alpha, value)

            # if alpha is greater than or equal to beta, break out of the loop
            # because there's no need to check the other moves
            if alpha >= beta:
                break

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
            new_move = alpha_beta_pruning(
                new_board,
                depth - 1,
                alpha,
                beta,
                Player.RED
            )

            new_score = new_move.score

            if new_score < value:
                value = new_score
                actual_column = col

            beta = min(beta, value)
            if alpha >= beta:
                break

        return Move(actual_column, value)
