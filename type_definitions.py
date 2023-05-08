import enum
from typing import List, Union

# Types
Board = List[List]

Score = int


class Player(enum.Enum):
    RED = 1
    BLUE = 2


Window = List[Union[Player, None]]
