from typing import List
import enum

# Types
Board = List[List]
Window = List[tuple[int, int]]
Score = int
COLUMN_COUNT = 7
ROW_COUNT = 6


class Player(enum.Enum):
    RED = 1
    BLUE = 2
