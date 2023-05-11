# from test_utils import ensure
# import math

from type_definitions import Player
from engine.minimax import minimax
# from engine.alpha_beta_pruning import alpha_beta_pruning

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
    # What is the best move right now?
    print(minimax(board, 1, Red_))
