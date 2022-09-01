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
