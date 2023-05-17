from timing import time_it
import math
from engine.minimax import minimax
from engine.alpha_beta_pruning import alpha_beta_pruning
from type_definitions import Player

Red_ = Player.RED
Blue = Player.BLUE

board = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]


if __name__ == "__main__":
    for difficulty in range(1, 5 + 1):
        print("Difficulty: ", difficulty)

        minimix_result = time_it(
            minimax,
            board, difficulty, Red_
        )

        alpha_beta_result = time_it(
            alpha_beta_pruning,
            board, difficulty, -math.inf, math.inf, Red_
        )

        print()
