from random import randint

board = []

# The boar
for x in range(7):
    board.append(["O"]*7)

def print_board(board):
    for row in board:
        print("".join(row))


# Initial board print
print ("Let's play Battleship!  There are 2 ships on the field.  Can you find one?")
print_board(board)                          

# Calculate random row
def random_row(board):
    return randint(0, len(board) -1)

def random_col(board):
     return randint(0, len(board) -1)

# Place and print ship 1 and 2.
ship_row = random_row(board)
ship_col = random_col(board)
ship_row2 = random_row(board)
ship_col2 = random_col(board)
shiplist1 = [ship_row, ship_col]
shiplist2 = [ship_row2, ship_col2]