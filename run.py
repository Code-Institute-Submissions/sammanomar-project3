ROW_COUNT = 8      # global variable
COLUMN_COUNT = 10   # global variable

# create board (8 rows by 12 columns matrix)
class Board():

    # store state of the game and handle users input until there is a winner
    # instance variable
    def __init__(self):
        # create board array
        self.board = [[' ' for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
        self.turns = 0 # track turns that have been played and last move input
        self.last_move = [-1, -1] # [r, c] (invalid move because we haven't played anything yet)

    # reusable function to display the board to the terminal as the game goes on
    def print_board(self):
        # number the columns
        print("\n") #new line
        for r in range(COLUMN_COUNT):
            # display what number this column is and start counting at 1
            print(f"  ({r+1}) ", end="")
        print("\n")
        # print slots of game board
        for r in range(ROW_COUNT):
            print('|', end="")
            for c in range(COLUMN_COUNT):
                print(f"  {self.board[r][c]}  |", end="")
            print("\n")
        #python trick to print 64 dashes all next to each other    
        print(f"{'-' * 64}\n")

    # switching between player X and player O
    def which_turn(self):
        players = ['X', 'O']
        return players[self.turns % 2]    

#create an instance of the board
def play():
    game = Board()

    game_over = False
    while not game_over:
        #continue playing

        game.print_board()

        # Ask the user for input, but only accept valid turns
        valid_move = False
        while not valid_move:
            user_move = input(f"{game.which_turn()}'s Turn - pick a column (1-{COLUMN_COUNT}): ")

        try:
            valid_move = game.turn(int(user_move)-1)
        except:
            print(f"Please choose a number between 1 and {COLUMN_COUNT}")   

#set up game loop with python trick that execute play function when file is run
if __name__ == '__main__':
    play()
