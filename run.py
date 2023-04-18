ROW_COUNT = 8       # global variable
COLUMN_COUNT = 12   # global variable

# create board (8 rows by 12 columns matrix)
Class Board():
    
    # store state of the game and handle users input until there is a winner
    # instance variable
    def __init__(self):
        # create board array
        self.board = [[' ' for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
        # track turns that have been played and last move input
        self.turns = 0
        self.last_move = [-1, -1] # row, col (invalid move because we haven't played anything yet)

    #reusable function to display the board to the terminal as the game goes on
    def print_board(self):
        # number the columns
        print("\n")
        for c in range(COLUMN_COUNT):
            #display what number this column is and start counting at 1
            print(f" ({c + 1})", end="")
        print("\n")

# drop piece
def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board [ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):  # which row piece will fall on
    for r in range(ROW_COUNT):
        if board [r][col] == 0:
            return r

def print_board(board): # flip the board build up orientation from bottom to up at numpy
    print(np.flip(board,0))

def winning_move(board, piece): # win functionality

    # check horizontal locations for win
    for c in range (COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    # check vertical locations for win
    for c in range (COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    # check positively sloped diaganols for win
    for c in range (COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    
    # check negatively sloped diaganols for win
    
    for c in range (COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

board = create_board()
print_board(board)   
game_over = False
turn = 0    # differnitate between player 1 and player 2 turn

# main game loop
while not game_over:
    print("----------------------------------------------------------------------------")
    print("Welcome to DROP PIECES TO CONNECT FOUR GAME!!")
    print("Entries should be numbers from 0 to 11 only")
    print("First left column is column: 0")
    print("Pick column number to drop piece at first empty spot from bottom")
    print("Connect four vertically or horizontally or diagonally to win")
    print("----------------------------------------------------------------------------")

    # ask for player 1 input
    if turn == 0:
        # which column to drop piece
        # check whether data is valid
        col = int(input("Player 2 Make your Column Selection (0-11):"))       
        
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

            if winning_move(board, 1):
                print("PLAYER 1 WINS!!! Congrats!!!")
                game_over = True


    # ask for player 2 input
    else:
        # which column to drop piece  
        col = int(input("Player 2 Make your Column Selection (0-11):"))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                print("PLAYER 2 WINS!!! Congrats!!!")
                game_over = True     

    print_board(board)        

    # switching between player 1 and player 2
    turn += 1
    turn = turn % 2
    
