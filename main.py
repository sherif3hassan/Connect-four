from type_definitions import Player, Board, Score, Window
from types import Union


def minimax(
        board: Board,
        depth: int,
        alpha: int,
        beta: int,
        player: Player
) -> Score:
    return 0


# Evalute the board
def evaluate_board(board: Board, player: Player):
    ...


def is_game_over(board: Board) -> Union[Player, None]:
    ...


def evaluate_window(window: Window, player: Player) -> Score:
    ...
