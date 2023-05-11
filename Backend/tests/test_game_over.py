from engine.rules import (
    is_game_over,
)
from type_definitions import Player

Red_ = Player.RED
Blue = Player.BLUE

# Full board (draw)
board = [
    [Red_, Blue, Red_, Blue, Red_, Blue, Red_],
    [Red_, Blue, Red_, Blue, Red_, Blue, Red_],
    [Red_, Blue, Red_, Blue, Red_, Blue, Red_],
    [Blue, Red_, Blue, Red_, Blue, Red_, Blue],
    [Red_, Blue, Red_, Blue, Red_, Blue, Red_],
    [Red_, Blue, Red_, Blue, Red_, Blue, Red_],
]

if __name__ == "__main__":
    print(is_game_over(board))
