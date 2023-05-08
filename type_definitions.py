from typing import List
import enum

# Types
Board = List[List]
Window = List[tuple[int, int]]
Score = int


class Player(enum.Enum):
    RED = 1
    BLUE = 2
