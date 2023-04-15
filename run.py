# install numpy
import numpy as np

ROW_COUNT = 6       #global variable
COLUMN_COUNT = 7    #global variable

# create board (6 rows by 7 columns matrix)
def create_board():
    board = np.zeros((6,7))
    return board

# drop piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board [5][col] == 0

def get_next_open_row(board, col):    # which row piece will fall on
    for r in range(ROW_COUNT):
        if board [r][col] == 0:
            return r

def print_board(board):     #flip the board build up orientation from bottom to up at numpy
    print(np.flip(board,0))
    

board = create_board()
print_board(board)   
game_over = False
turn = 0    #differnitate between player 1 and player 2 turn

# main game loop
while not game_over:
    # ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)


    # ask for player 2 input
    else: 
        col = int(input("Player 2 Make your Selection (0-6):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    print_board(board)        

    # switching between player 1 and player 2
    turn += 1
    turn = turn % 2
