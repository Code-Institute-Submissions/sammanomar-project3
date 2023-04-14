# install numpy
import numpy as np

# create board (6 rows by 7 columns matrix)
def create_board():
    board = np.zeros((6,7))
    return board

# drop piece
def drop_piece():
    pass

def is_valid_location(board, col):
    return board [5][col] == 0

def get_next_open_row():
    pass

board = create_board()
print(board)   
game_over = False
turn = 0    #differnitate between player 1 and player 2 turn

# main game loop
while not game_over:
    # ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6):"))

    # ask for player 2 input
    else: 
        col = int(input("Player 2 Make your Selection (0-6):"))

    # switching between player 1 and player 2
    turn += 1
    turn = turn % 2
