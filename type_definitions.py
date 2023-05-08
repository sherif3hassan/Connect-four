from typing import List, Union
import enum

Score = int


class Player(enum.Enum):
    RED = 1
    BLUE = 2


Board = List[List[Player]]
Window = List[Union[Player, None]]
