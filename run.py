# install numpy to build up the matrix
# create board (6 rows by 7 columns)
import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

board = create_board()
print(board)
