from typing import List, Union
import enum

Score = int
COLUMN_COUNT = 7
ROW_COUNT = 6


class Player(enum.Enum):
    RED = 1
    BLUE = 2

    def __repr__(self):
        return "RED " if self == Player.RED else "BLUE"


Board = List[List[Player]]
Window = List[Union[Player, None]]
