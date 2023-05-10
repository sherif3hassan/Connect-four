from main import minimax, Player

Red_ = Player.RED
Blue = Player.BLUE

board = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None]
]

print(minimax(board, 10, Player.RED))


def play_move(board, column, player):
    ...


if __name__ == "__main__":
    # What is the best move right now?
    print(minimax(board, 10, Player.RED))
    turn = Player.RED

    # Game loop while game is not over
    while True:
        if turn == Player.RED:
            column = int(input("RED: "))
        else:
            # Get the best move
            column, value = minimax(board, 10, turn)

        # Make the move
        board = play_move(board, column, turn)

        # Print the board

        # Switch players
        turn = Player.RED if turn == Player.BLUE else Player.BLUE
