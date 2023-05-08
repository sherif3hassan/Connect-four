from typing import Union

from type_definitions import Board, Player, Score, Window

DEBUG = False


def log(msg: str):
    if DEBUG:
        input(msg)


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
    ...


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
