import enum
from typing import List, Union

# Type definitions

Score = int  # Score of a board
COLUMN_COUNT = 7  # Number of columns in the board
ROW_COUNT = 6  # Number of rows in the board


class Player(enum.Enum):
    RED = 1
    BLUE = 2

    def __repr__(self):
        return "RED " if self == Player.RED else "BLUE"


Board = List[List[Player]]  # Board is a 2D list of Player pieces
# The Window may contain Player pieces or is empty
Window = List[Union[Player, None]]


class Move:
    def __init__(self, column: int, score: Score):
        self.column = column
        self.score = score
