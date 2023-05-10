from main import evaluate_board, Player

Red_ = Player.RED
Blue = Player.BLUE

board = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, Red_, None, None],
    [None, None, None, Red_, Blue, None, None],
    [None, None, Red_, Blue, Blue, Blue, None]
]

if __name__ == "__main__":
    print(evaluate_board(board, Player.RED))
