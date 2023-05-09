import math
import random

from type_definitions import Player, Board, Score, Window, COLUMN_COUNT, ROW_COUNT
from typing import Union

DEBUG = True


def log(msg: str):
    if DEBUG:
        input(msg)


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


# Returns the score and the move that got that score (i.e. column)
def minimax(
        board: Board,
        depth: int,
        player: Player
):
    turn = "RED" if player == Player.RED else "BLUE"
    log(f"depth: {depth}, player: {turn}")

    places = []
    for col in range(COLUMN_COUNT):
        if not board[0][col]:
            places.append(col)

    NL = "\n"
    log(f"{turn}, board:\n{NL.join([str(row) for row in board])}\n")
    log(f"{turn}, places: {places}")

    if winning_move(board, Player.RED):
        log("RED won")
        return 1
    elif winning_move(board, Player.BLUE):
        log("BLUE won")
        return -1
    elif (len(places) == 0):
        log("tie")
        return 0

    if depth == 0:
        log(f"{turn}, depth reached")
        eval = evaluate_board(board, player)
        log(f"{turn}, eval: {eval}")
        return eval

    if player == Player.RED:
        value = -math.inf
        log(f"{turn}, value: {value}")

        openRow = None
        for col in places:
            for row in range(ROW_COUNT - 1, -1, -1):
                log(f"{turn}, row: {row}, col: {col}")
                if not board[row][col]:
                    log(f"{turn}, found empty spot")
                    openRow = row
                    break

            b_copy = [[cell for cell in row] for row in board]
            b_copy[openRow][col] = Player.RED
            log(f"{turn}, b_copy:\n{NL.join([str(row) for row in b_copy])}\n")
            new_score = minimax(b_copy, depth - 1, Player.BLUE)
            log(f"{turn}, new_score: {new_score}")
            if new_score > value:
                value = new_score
                log(f"{turn}, new value: {value}")
        return value
    else:
        value = math.inf
        log(f"{turn}, turn, value: {value}")

        openRow = None
        for col in places:
            for row in range(ROW_COUNT - 1, -1, -1):
                log(f"{turn}, row: {row}, col: {col}")
                if not board[row][col]:
                    log(f"{turn}, found empty spot")
                    openRow = row
                    break

            b_copy = [[cell for cell in row] for row in board]
            b_copy[openRow][col] = Player.BLUE
            new_score = minimax(b_copy, depth - 1, Player.RED)
            log(f"{turn}, new_score: {new_score}")
            if new_score < value:
                value = new_score
                log(f"{turn}, new value: {value}")
        return value


# Returns the score and the move that got that score (i.e. column)
def alpha_beta_pruning(
        board: Board,
        depth: int,
        alpha: int,
        beta: int,
        player: Player
):
    turn = "RED" if player == Player.RED else "BLUE"
    log(f"depth: {depth}, player: {turn}")

    places = []
    for col in range(COLUMN_COUNT):
        if not board[0][col]:
            places.append(col)

    NL = "\n"
    log(f"{turn}, board:\n{NL.join([str(row) for row in board])}\n")
    log(f"{turn}, places: {places}")

    if winning_move(board, Player.RED):
        log("RED won")
        return 1
    elif winning_move(board, Player.BLUE):
        log("BLUE won")
        return -1
    elif (len(places) == 0):
        log("tie")
        return 0

    if depth == 0:
        log(f"{turn}, depth reached")
        eval = evaluate_board(board, player)
        log(f"{turn}, eval: {eval}")
        return eval

    if player == Player.RED:
        value = -math.inf
        log(f"{turn}, value: {value}")

        openRow = None
        for col in places:
            for row in range(ROW_COUNT - 1, -1, -1):
                log(f"{turn}, row: {row}, col: {col}")
                if not board[row][col]:
                    log(f"{turn}, found empty spot")
                    openRow = row
                    break

            b_copy = [[cell for cell in row] for row in board]
            b_copy[openRow][col] = Player.RED
            log(f"{turn}, b_copy:\n{NL.join([str(row) for row in b_copy])}\n")
            new_score = alpha_beta_pruning(b_copy, depth - 1, alpha, beta, Player.BLUE)
            log(f"{turn}, new_score: {new_score}")
            if new_score > value:
                value = new_score
                log(f"{turn}, new value: {value}")
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = math.inf
        log(f"{turn}, turn, value: {value}")

        openRow = None
        for col in places:
            for row in range(ROW_COUNT - 1, -1, -1):
                log(f"{turn}, row: {row}, col: {col}")
                if not board[row][col]:
                    log(f"{turn}, found empty spot")
                    openRow = row
                    break

            b_copy = [[cell for cell in row] for row in board]
            b_copy[openRow][col] = Player.BLUE
            new_score = alpha_beta_pruning(b_copy, depth - 1, alpha, beta, Player.RED)
            log(f"{turn}, new_score: {new_score}")
            if new_score < value:
                value = new_score
                log(f"{turn}, new value: {value}")
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


# Evalute the board
def evaluate_board(board: Board, player: Player):
    value = 0

    log(f"board rows: {len(board)}")
    log(f"board cols: {len(board[0])}")

    for row in range(len(board)):
        for col in range(len(board[0])):
            log(f"row: {row}, col: {col}")

            # Horizontal
            if col + 3 < len(board[0]):
                window = [
                    board[row][col + 0],
                    board[row][col + 1],
                    board[row][col + 2],
                    board[row][col + 3]
                ]
                log(f"horizontal window: {window}")
                value += evaluate_window(window, player)

            # Vertical
            if row + 3 < len(board):
                window = [
                    board[row + 0][col],
                    board[row + 1][col],
                    board[row + 2][col],
                    board[row + 3][col]
                ]
                log(f"vertical window: {window}")
                value += evaluate_window(window, player)

            # Diagonal down-right
            if row + 3 < len(board) and col + 3 < len(board[0]):
                window = [
                    board[row + 0][col + 0],
                    board[row + 1][col + 1],
                    board[row + 2][col + 2],
                    board[row + 3][col + 3]
                ]
                log(f"diagonal down-right window: {window}")
                value += evaluate_window(window, player)

            # Diagonal down-left
            if row + 3 < len(board) and col - 3 >= 0:
                window = [
                    board[row + 0][col - 0],
                    board[row + 1][col - 1],
                    board[row + 2][col - 2],
                    board[row + 3][col - 3]
                ]
                log(f"diagonal down-left window: {window}")
                value += evaluate_window(window, player)

    return value


def is_game_over(board: Board) -> Union[Player, None]:

#Horizontal Window Check
    for row in range(len(board)):
        for col in range(len(board[0])):
            if col + 3 < len(board[0]):
                Window = [
                    board[row][col + 0],
                    board[row][col + 1],
                    board[row][col + 2],
                    board[row][col + 3]
                ]

                if Window.count(Player.RED) == 4:
                    return Player.RED
                elif Window.count(Player.BLUE) == 4:
                    return Player.BLUE
                else:
                    return None
                
#Vertical Window Check
    for row in range(len(board)):
        for col in range(len(board[0])):
            if row + 3 < len(board):
                Window = [
                    board[row + 0][col],
                    board[row + 1][col],
                    board[row + 2][col],
                    board[row + 3][col]
                ]

                if Window.count(Player.RED) == 4:
                    return Player.RED
                elif Window.count(Player.BLUE) == 4:
                    return Player.BLUE
                else:
                    return None
                
#Diagonal Window Check
    for row in range(len(board)):
        for col in range(len(board[0])):
            if row + 3 < len(board) and col + 3 < len(board[0]):
                Window = [
                    board[row + 0][col + 0],
                    board[row + 1][col + 1],
                    board[row + 2][col + 2],
                    board[row + 3][col + 3]
                ]

                if Window.count(Player.RED) == 4:
                    return Player.RED
                elif Window.count(Player.BLUE) == 4:
                    return Player.BLUE
                else:
                    return None
                
#Diagonal Window Check
    for row in range(len(board)):
        for col in range(len(board[0])):
            if row + 3 < len(board) and col - 3 >= 0:
                Window = [
                    board[row + 0][col - 0],
                    board[row + 1][col - 1],
                    board[row + 2][col - 2],
                    board[row + 3][col - 3]
                ]

                if Window.count(Player.RED) == 4:
                    return Player.RED
                elif Window.count(Player.BLUE) == 4:
                    return Player.BLUE
                else:
                    return None
                
#Check for Draw
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == None:
                return None
            else:
                return "Draw"

            
    



def evaluate_window(window: Window, player: Player) -> Score:
    score = 0

    # switch player based on the current player's color
    opponent_piece = Player.RED if player == Player.BLUE else Player.BLUE

    # if there are 4 pieces in a window, the player wins
    if window.count(player) == 4:
        score += 100
    # if there are 3 pieces in a window, the player gets 5 points
    elif window.count(player) == 3 and window.count(None) == 1:
        score += 5
    # if there are 2 pieces in a window, the player gets 2 points
    elif window.count(player) == 2 and window.count(None) == 2:
        score += 2

    # if there are 3 pieces of the opponent in a window, the player loses 4 points
    if window.count(opponent_piece) == 3 and window.count(None) == 1:
        score -= 4

    return score
