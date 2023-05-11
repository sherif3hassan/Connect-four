import math
from typing import Optional

from engine.alpha_beta_pruning import alpha_beta_pruning
from engine.minimax import minimax
from engine.rules import is_game_over
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
from type_definitions import COLUMN_COUNT, ROW_COUNT, Board, Player

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Game:
    board = [
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None],
    ]
    turn = Player.RED
    difficulty = 3
    game_over = False
    winner = None
    algorithm = "minimax"

    @classmethod
    def switch_turn(cls):
        cls.turn = Player.RED if cls.turn == Player.BLUE else Player.BLUE

    @classmethod
    def place_piece(cls, column: int):
        for row in range(ROW_COUNT - 1, -1, -1):
            if cls.board[row][column] is None:
                cls.board[row][column] = cls.turn
                break

    @classmethod
    def check_winner(cls):
        winner = is_game_over(Game.board)
        if winner:
            Game.game_over = True
            Game.winner = winner
            return True
        return False

    @classmethod
    def next_move(cls):
        if cls.game_over:
            raise Exception("Game is over")
        if cls.algorithm == "minimax":
            move = minimax(cls.board, cls.difficulty, cls.turn)
        else:
            move = alpha_beta_pruning(
                cls.board, cls.difficulty, -math.inf, math.inf, cls.turn)
        if move.column is not None:
            cls.place_piece(move.column)
            if not cls.check_winner():
                cls.switch_turn()

    @classmethod
    def play(cls, column: int):
        if cls.game_over:
            raise Exception("Game is over")
        if cls.board[0][column] is not None:
            raise Exception("Invalid move")
        cls.place_piece(column)
        if not cls.check_winner():
            cls.switch_turn()

    @classmethod
    def reset(cls):
        cls.board = [
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None],
        ]
        cls.turn = Player.RED
        cls.game_over = False
        cls.winner = None


def json_turn(turn: Player):
    return 1 if turn == Player.RED else 2


def json_board(board: Board):
    return [
        [0 if x is None else json_turn(x) for x in row]
        for row in board
    ]


@app.get("/board")
async def get_board():
    return {"board": json_board(Game.board)}


@app.get("/turn")
async def get_turn():
    return {"turn": json_turn(Game.turn)}


@app.get("/winner")
async def get_winner():
    return {"winner": json_turn(Game.winner) if Game.winner else None}


@app.post("/next")
async def next_move():
    try:
        Game.next_move()
        return {"board": json_board(Game.board)}
    except Exception as e:
        # return {"error": str(e)}
        pass


class AlgorithmBody(BaseModel):
    algorithm: str

    @validator("algorithm")
    def algorithm_must_be_in_range(cls, v):
        if v not in ["minimax", "alpha-beta"]:
            raise ValueError("Must be minimax or alpha_beta_pruning")
        return v


@app.post("/switchalgorithm")
async def switch_algorithm(body: AlgorithmBody):
    Game.algorithm = body.algorithm
    return {"algorithm": Game.algorithm}


class PlayBody(BaseModel):
    column: int

    @validator("column")
    def column_must_be_in_range(cls, v):
        if v < 0 or v > COLUMN_COUNT - 1:
            raise ValueError(f"Must be in range 0 to {COLUMN_COUNT - 1}")
        return v


@app.post("/play")
async def play(body: PlayBody):
    try:
        Game.play(body.column)
        return {"board": json_board(Game.board)}
    except Exception as e:
        # return {"error": str(e)}
        pass


@app.get("/difficulty")
async def get_difficulty():
    return {"difficulty": Game.difficulty}


class DifficultyBody(BaseModel):
    difficulty: int

    @validator("difficulty")
    def difficulty_must_be_in_range(cls, v):
        if v not in [1, 3, 5]:
            raise ValueError("Must be 1, 3, or 5")
        return v


@app.post("/difficulty")
async def set_difficulty(body: DifficultyBody):
    Game.difficulty = body.difficulty
    return {"difficulty": Game.difficulty}


@app.post("/reset")
async def reset():
    Game.reset()
    return {"board": json_board(Game.board)}
