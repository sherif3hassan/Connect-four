from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QComboBox
from type_definitions import Player, ROW_COUNT, COLUMN_COUNT
from engine.minimax import minimax
from engine.alpha_beta_pruning import alpha_beta_pruning
from engine.rules import is_game_over
import sys
import math
import pyautogui
from PIL import ImageGrab
import time


ALGORITHMS_GUI = ["Minimax", "Alpha-Beta Pruning"]
DIFFICULTIES_GUI = ["Easy", "Medium", "Hard"]

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

BOARD_WIDTH = 514
BOARD_HEIGHT = 441

LEFT = 426
TOP = 202
RIGHT = LEFT + BOARD_WIDTH
BOTTOM = TOP + BOARD_HEIGHT

OFFSET_X = 73
OFFSET_Y = 73
RELATIVE_START_X = 36
RELATIVE_START_Y = 20

EMPTY = None
RED = Player.RED
BLUE = Player.BLUE


class View(QWidget):
    def __init__(self, start_game_callback):
        super().__init__()
        self.callback = start_game_callback

        self.setWindowTitle("Hello World")
        self.resize(300, 300)

        self.setLayout(QVBoxLayout())

        self.algorithm_combobox = QComboBox()
        self.algorithm_combobox.addItems(ALGORITHMS_GUI)

        self.difficulty_combobox = QComboBox()
        self.difficulty_combobox.addItems(DIFFICULTIES_GUI)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_button_clicked)

        self.layout().addWidget(self.algorithm_combobox)
        self.layout().addWidget(self.difficulty_combobox)
        self.layout().addWidget(self.start_button)

    def start_button_clicked(self):
        self.callback(
            self.algorithm_combobox.currentText(),
            self.difficulty_combobox.currentText(),
        )
        self.close()


class GameUtils:
    def __init__(self):
        self.board = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]

    def print_board(self):
        print("Board:")
        for row in self.board:
            # if red R else if blue B else if empty *
            print(
                "".join(
                    [
                        "R" if cell == Player.RED else "B" if cell == Player.BLUE else "*"
                        for cell in row
                    ]
                )
            )
        print("")

    def get_game_grid(self):
        # Read board from screen
        img = ImageGrab.grab().crop((LEFT, TOP, RIGHT, BOTTOM))
        for row in range(ROW_COUNT):
            for col in range(COLUMN_COUNT):
                # Get pixel color
                pixel_color = img.getpixel(
                    (RELATIVE_START_X + col * OFFSET_X,
                     RELATIVE_START_Y + row * OFFSET_Y)
                )
                # Check if pixel is empty
                if pixel_color[0] > 200 and pixel_color[1] > 200 and pixel_color[2] > 200:
                    self.board[row][col] = EMPTY
                # Check if pixel is red
                elif pixel_color[0] > 200:
                    self.board[row][col] = RED
                # Check if pixel is blue
                elif pixel_color[2] > 200:
                    self.board[row][col] = BLUE

    def select_column(self, column):
        # Click on column
        pyautogui.click(
            LEFT + RELATIVE_START_X + column * OFFSET_X,
            TOP + RELATIVE_START_Y
        )


class Game:
    def __init__(self):
        self.utils = GameUtils()
        self.turn = Player.RED
        self.difficulty = 1
        self.game_over = False
        self.winner = None
        self.algorithm = "minimax"

    def switch_turn(self):
        self.turn = Player.RED if self.turn == Player.BLUE else Player.BLUE

    def place_piece(self, column: int):
        for row in range(ROW_COUNT - 1, -1, -1):
            if self.utils.board[row][column] is None:
                self.utils.board[row][column] = self.turn
                break

    def check_winner(self):
        winner = is_game_over(self.utils.board)
        if winner:
            self.game_over = True
            self.winner = winner
            return True
        return False

    def next_move(self):
        if self.game_over:
            raise Exception("Game is over")
        if self.algorithm == "minimax":
            move = minimax(self.utils.board, self.difficulty, Player.RED)
        else:
            move = alpha_beta_pruning(
                self.utils.board,
                self.difficulty,
                -math.inf,
                math.inf,
                Player.RED,
            )
        if move.column is not None:
            print("AI move:", move.column)
            return move
        else:
            print("Game is over")
            return None

    def play(self, column: int):
        if self.game_over:
            raise Exception("Game is over")
        if self.utils.board[0][column] is not None:
            raise Exception("Invalid move")
        self.place_piece(column)
        if not self.check_winner():
            self.switch_turn()

    def reset(self):
        self.utils.board = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        self.turn = Player.RED
        self.game_over = False
        self.winner = None

    def start_game(self, algorithm, difficulty):
        if algorithm == "Minimax":
            self.algorithm = "minimax"
        else:
            self.algorithm = "alpha-beta"

        if difficulty == "Easy":
            self.difficulty = 2
        elif difficulty == "Medium":
            self.difficulty = 5
        else:
            self.difficulty = 7

        self.reset()

        while not self.game_over:
            self.utils.get_game_grid()

            self.utils.print_board()

            # YOUR CODE GOES HERE
            move = self.next_move()

            if move is not None:
                self.utils.select_column(move.column)
            else:
                self.game_over = True

            time.sleep(5)


def main():
    app = QApplication(sys.argv)
    game = Game()
    window = View(game.start_game)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
