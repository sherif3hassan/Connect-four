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
import random


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

PIECE_SIZE_X = 74
PIECE_SIZE_Y = 73
RELATIVE_START_X = 0
RELATIVE_START_Y = 0

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

    def print_grid(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY:
                    print("*", end=" ")
                elif grid[i][j] == RED:
                    print("R", end=" ")
                elif grid[i][j] == BLUE:
                    print("B", end=" ")
            print("\n")

    def _convert_grid_to_color(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == (255, 255, 255):
                    grid[i][j] = EMPTY
                elif grid[i][j][0] > 200:
                    grid[i][j] = RED
                elif grid[i][j][0] > 50:
                    grid[i][j] = BLUE
        return grid

    def _get_grid_cordinates(self):
        startCord = (RELATIVE_START_X, RELATIVE_START_Y)
        cordArr = []
        for i in range(0, COLUMN_COUNT):
            for j in range(0, ROW_COUNT):
                x = startCord[0] + i * PIECE_SIZE_X
                y = startCord[1] + j * PIECE_SIZE_Y
                cordArr.append((x, y))
        return cordArr

    def _transpose_grid(self, grid):
        return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    def _capture_image(self):
        image = ImageGrab.grab()
        cropedImage = image.crop((LEFT, TOP, RIGHT, BOTTOM))
        return cropedImage

    def _convert_image_to_grid(self, image):
        pixels = [[] for i in range(7)]
        i = 0
        for index, cord in enumerate(self._get_grid_cordinates()):
            pixel = image.getpixel(cord)
            if index % 6 == 0 and index != 0:
                i += 1
            pixels[i].append(pixel)
        return pixels

    def _get_grid(self):
        cropedImage = self._capture_image()
        pixels = self._convert_image_to_grid(cropedImage)
        # cropedImage.show()
        # exit()
        grid = self._transpose_grid(pixels)
        return grid

    def _check_if_game_end(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY and self.board[i][j] != EMPTY:
                    return True
        return False

    def get_game_grid(self):
        game_grid = self._get_grid()
        new_grid = self._convert_grid_to_color(game_grid)
        is_game_end = self._check_if_game_end(new_grid)
        self.board = new_grid
        return (self.board, is_game_end)

    def select_column(self, column):
        pyautogui.click(
            self._get_grid_cordinates()[column][0] + LEFT,
            self._get_grid_cordinates()[column][1] + TOP,
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
            move = minimax(self.utils.board, self.difficulty, self.turn)
        else:
            move = alpha_beta_pruning(
                self.utils.board,
                self.difficulty,
                -math.inf,
                math.inf,
                self.turn
            )
        if move.column is not None:
            self.place_piece(move.column)
            if not self.check_winner():
                self.switch_turn()

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

    def read_board(self):
        # use pyautogui to read the board
        board, is_game_end = self.utils.get_game_grid()

    def start_game(self, algorithm, difficulty):
        if algorithm == "Minimax":
            self.algorithm = "minimax"
        else:
            self.algorithm = "alpha-beta"

        if difficulty == "Easy":
            self.difficulty = 1
        elif difficulty == "Medium":
            self.difficulty = 3
        else:
            self.difficulty = 5

        self.reset()

        while not self.game_over:
            (game_board, game_end) = self.utils.get_game_grid()

            # FOR DEBUG PURPOSES
            self.utils.print_grid(game_board)

            # YOUR CODE GOES HERE
            self.next_move()

            # Insert here the action you want to perform based on the output of the algorithm
            # You can use the following function to select a column
            random_column = random.randint(0, COLUMN_COUNT - 1)
            self.utils.select_column(random_column)

            time.sleep(2)


def main():
    app = QApplication(sys.argv)
    game = Game()
    window = View(game.start_game)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
