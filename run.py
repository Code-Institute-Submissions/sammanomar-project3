# install numpy
import numpy as np

ROW_COUNT = 6       #global variable
COLUMN_COUNT = 7    #global variable

# create board (6 rows by 7 columns matrix)
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

# drop piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board [ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):  # which row piece will fall on
    for r in range(ROW_COUNT):
        if board [r][col] == 0:
            return r

def print_board(board): #flip the board build up orientation from bottom to up at numpy
    print(np.flip(board,0))

def winning_move(board, piece): #win functionality
    #check horizontal locations for win
    for c in range (COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    

    #check vertical locations for win
    for c in range (COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    

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

            if winning_move(board, 1):
                print("PLAYER 1 WINS!!! Congrats!!!")
                game_over = True


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
