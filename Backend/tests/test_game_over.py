from test_utils import ensure

from type_definitions import Player
from engine.rules import is_game_over


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
    ensure(is_game_over, [board], "draw")
