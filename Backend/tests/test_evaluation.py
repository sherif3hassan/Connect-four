from type_definitions import Player
from test_utils import ensure
from engine.evaluation import evaluate_board


Red_ = Player.RED
Blue = Player.BLUE

if __name__ == "__main__":
    ensure(evaluate_board, (
        [[None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, Blue, Blue, Blue, Blue, None]],
        Blue
    ), 2 + 5 + 100 + 5)

    ensure(evaluate_board, (
        [[None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None],
         [None, Blue, Blue, Blue, Blue, None, None]],
        Red_
    ), -4 + -4)
