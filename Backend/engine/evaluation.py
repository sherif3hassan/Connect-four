from type_definitions import (
    Board,
    Player,
    Score,
    Window
)


def evaluate_window(window: Window, player: Player) -> Score:
    score = 0

    opponent_piece = Player.RED if player == Player.BLUE else Player.BLUE

    # 4 pieces = +100 pts (winning move)
    if window.count(player) == 4:
        score += 100

    # 3 pieces = +5 pts
    elif window.count(player) == 3 and window.count(None) == 1:
        score += 5

    # 2 pieces = +2 pts
    elif window.count(player) == 2 and window.count(None) == 2:
        score += 2

    # 3 pieces of the opponent = -4 pts
    if window.count(opponent_piece) == 3 and window.count(None) == 1:
        score -= 4

    return score


def evaluate_board(board: Board, player: Player):
    value = 0
    # evaluate the board horizontally, vertically, and diagonally
    # each window is of 4 pieces or cells
    for row in range(len(board)):
        for col in range(len(board[0])):
            # if the window is within the board
            # add the score of the window to the value and return the value

            # check for horizontal window
            if col + 3 < len(board[0]):
                window = [
                    board[row][col + 0],
                    board[row][col + 1],
                    board[row][col + 2],
                    board[row][col + 3]
                ]
                value += evaluate_window(window, player)

            # check for vertical window
            if row + 3 < len(board):
                window = [
                    board[row + 0][col],
                    board[row + 1][col],
                    board[row + 2][col],
                    board[row + 3][col]
                ]
                value += evaluate_window(window, player)

            # check for diagonal up-right window
            if row + 3 < len(board) and col + 3 < len(board[0]):
                window = [
                    board[row + 0][col + 0],
                    board[row + 1][col + 1],
                    board[row + 2][col + 2],
                    board[row + 3][col + 3]
                ]
                value += evaluate_window(window, player)

            # check for diagonal up-left window
            if row + 3 < len(board) and col - 3 >= 0:
                window = [
                    board[row + 0][col - 0],
                    board[row + 1][col - 1],
                    board[row + 2][col - 2],
                    board[row + 3][col - 3]
                ]
                value += evaluate_window(window, player)

    return value
