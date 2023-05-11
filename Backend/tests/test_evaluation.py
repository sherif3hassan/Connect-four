from type_definitions import Player
from engine.evaluation import (
    evaluate_board,
)

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
