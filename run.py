ROW_COUNT = 6      # global variable
COLUMN_COUNT = 8   # global variable

# create board object (8 rows by 12 columns)
class Board():
    # store state of the game and handle users input until there is a winner
    def __init__(self):
        """
        Instance variable
        Create board array
        """
        self.board = [[' ' for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
        self.turns = 0 # track turns that have been played and last move input
        self.last_move = [-1, -1] # [r, c] # [r, c] (invalid move because we haven't played anything yet)


    def print_board(self):
        """
        Reusable function to display the board 
        to the terminal as the game goes on
        """
        # number the columns
        print("\n") # new line
        # display what number this column is and start counting at 1
        for r in range(COLUMN_COUNT):
            print(f"  ({r+1}) ", end="")
        print("\n")

        # print slots of game board
        for r in range(ROW_COUNT):
            print('|', end="")
            for c in range(COLUMN_COUNT):
                print(f"  {self.board[r][c]}  |", end="")
            print("\n")
        # python trick to print 50 dashes all next to each other  
        print(f"{'-' * 50}\n")

    
    def which_turn(self):
        """
        Switching between player X and player O
        """
        players = ['X', 'O']
        return players[self.turns % 2]

    
    def in_bounds(self, r, c):
        """
        Test row column coordinates is within our 2D array
        """
        return (r >= 0 and r < ROW_COUNT and c >= 0 and c < COLUMN_COUNT)

    
    def turn(self, column):
        """
        Turn function
        """
        # Search bottom up for an open slot
        for i in range(ROW_COUNT-1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.which_turn() # execute this turn and put X or O here
                self.last_move = [i, column] # save this last move to the spot

                self.turns += 1 # increment the turn that has been played
                return True # to indicate that was a valid move

        return False


    def check_winner(self):
        """
        Check winner function
        """
        last_row = self.last_move[0] # tracking
        last_col = self.last_move[1] # tracking
        last_letter = self.board[last_row][last_col] # tracking

        # [r, c] direction, matching letter count, locked bool
        directions = [[[-1, 0], 0, True], # check upward
                      [[1, 0], 0, True],  # check upward
                      [[0, -1], 0, True], # check downard
                      [[0, 1], 0, True],  # check downard
                      [[-1, -1], 0, True],# check left
                      [[1, 1], 0, True],  # check right
                      [[-1, 1], 0, True], # check diagonally
                      [[1, -1], 0, True]] # check diagonally
        
        # Search outwards looking for matching pieces
        for a in range(4):
            for d in directions:
                r = last_row + (d[0][0] * (a+1))
                c = last_col + (d[0][1] * (a+1))

                if d[2] and self.in_bounds(r, c) and self.board[r][c] == last_letter:
                    d[1] += 1
                else:
                    # Stop searching in this direction
                    d[2] = False

        # Check possible direction pairs for '4 pieces in a row'
        for i in range(0, 7, 2):
            if (directions[i][1] + directions[i+1][1] >= 3):
                self.print_board()
                print(f"{last_letter} is the winner!")
                return last_letter   

        # Did not find any winners
        return False


def play():
    """
    Create an instance of the board
    """
    # Initialize the game board
    game = Board()

    game_over = False
    while not game_over:
        print("  Welcome to DROP PIECES TO CONNECT FOUR GAME!!!")
        print("        2 Players Game Without Computer")
        print("--------------------------------------------------")
        game.print_board()


        # Ask the user for input, but only accept valid turns
        valid_move = False
        while not valid_move:
            try:
                user_move = int(input(f"{game.which_turn()}'s Turn - pick a column (1-{COLUMN_COUNT}): "))
                if user_move <= 0 or user_move > 8:
                    print(f"Please choose a number from 1 and {COLUMN_COUNT}")
                else:    
                    valid_move = (game.turn(int(user_move)-1))    
            except ValueError:
                print(f"Please choose a number from 1 and {COLUMN_COUNT}")

                            
        # End the game if there is a winner
        game_over = game.check_winner()
        
        # End the game if there is a tie
        if not any(' ' in x for x in game.board):
            print("The game is a draw..")
            return

#set up game loop with python trick that execute play function when file is run
if __name__ == '__main__':
    play()

