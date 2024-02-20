import random

# Constants
EMPTY = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'
WIN = 1
DRAW = 0.5
BOARD_WIDTH = 7
BOARD_HEIGHT = 6

# Function to initialize an empty game board
def init_board():
    return [[EMPTY for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# Function to print the game board
def print_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')
    print(' 0 1 2 3 4 5 6')

# Function to get all legal moves in the current position
def moves(board):
    legal_moves = []
    for col in range(BOARD_WIDTH):
        if board[0][col] == EMPTY:
            legal_moves.append(col)
    return legal_moves

# Function to make a move and return the new position
def make_move(board, col, player):
    new_board = [row[:] for row in board]
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if new_board[row][col] == EMPTY:
            new_board[row][col] = player
            break
    return new_board

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check columns
    for col in range(BOARD_WIDTH):
        for row in range(BOARD_HEIGHT - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonals (top-left to bottom-right)
    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    # Check diagonals (bottom-left to top-right)
    for row in range(3, BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False

# Function to simulate a game from a given position
def simulate(board, move, player):
    sim_board = make_move(board, move, player)
    temp_player = player
    legal_moves = 0
    # Randomly simulate the rest of the game
    while not is_over(sim_board):
        legal_moves = moves(sim_board)
        if not legal_moves:
            break
        random_move = random.choice(legal_moves)
        sim_board = make_move(sim_board, random_move, PLAYER_X if temp_player == PLAYER_O else PLAYER_O)
        temp_player = PLAYER_X if temp_player == PLAYER_O else PLAYER_O
    
    if check_win(sim_board, PLAYER_O if player == PLAYER_O else PLAYER_X):
        return WIN  # The opponent wins
    elif not legal_moves:
        return DRAW  # Game is a draw
    return 0

# Function to perform a pure Monte Carlo search
def pure_mc(board, player, N=200):
    my_side = player
    initial_moves = moves(board)
    win_counts = {move: 0 for move in initial_moves}

    for move in initial_moves:
        for _ in range(N):
            result = simulate(board, move, my_side)
            if result == WIN:
                win_counts[move] += WIN
            elif result == DRAW:
                win_counts[move] += DRAW

    # Calculate the best move based on winning percentages (picks the one with the least amount of wins)
    best_move = max(win_counts, key=lambda move: win_counts[move] / N)
    for k, v in win_counts.items():
      print(f"Column: {k}: {v / N * 100}%")
      
    return best_move


# Function to check if the game is over
def is_over(board):
    return check_win(board, PLAYER_X) or check_win(board, PLAYER_O) or not moves(board)

# Function to play the game with a text-based UI
def play_game():
    board = init_board()
    player_turn = True

    while True:
        print_board(board)
        player = PLAYER_X if player_turn else PLAYER_O

        if player_turn:
            move = int(input(f'To move: {player}\nYour move? '))
        else:
            move = pure_mc(board, player)

        if move in moves(board):
            board = make_move(board, move, player)
            if is_over(board):
                print_board(board)
                if check_win(board, player):
                    print(f'{player} wins!')
                else:
                    print('It\'s a draw!')
                break
            player_turn = not player_turn
        else:
            print('Invalid move. Try again.')

if __name__ == "__main__":
    play_game()