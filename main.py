from typing import Union

from type_definitions import Board, Player, Score, Window


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



    if Window.count(Player.RED) == 4:
        return Player.RED
    elif Window.count(Player.BLUE) == 4:
        return Player.BLUE
    else:
        return None
    



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
