from type_definitions import Player
from engine.minimax import (
    minimax,
)

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
    print(minimax(board, 10, Player.RED))
