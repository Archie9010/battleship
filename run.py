from random import randint

board = []

# The board
for x in range(5):
    board.append(["O"]*5)


def print_board(board):
    for row in board:
        print("".join(row))


# Initial board print
print("Let's play Battleship! There is a ship on the field. Can you find it?")
print_board(board)


# Calculate random row
def random_row(board):
    return randint(0, len(board)-1)


def random_col(board):
    return randint(0, len(board)-1)


# Place and print ship 1 .
ship_row = random_row(board)
ship_col = random_col(board)
ship_row2 = random_row(board)
ship_col2 = random_col(board)
shiplist1 = [ship_row, ship_col]
shiplist2 = [ship_row2, ship_col2]

# Take input for row and column
for turn in range(0, 10):
    print("Turn", turn+1)
    guess_row = int(input("Guess Row 1-5:"))-1
    guess_col = int(input("Guess Col 1-5:"))-1
# Win statement
    if (guess_row == ship_row and guess_col == ship_col) or (
          guess_row == ship_row2 and guess_col == ship_col2):
        print("Congratulation! You sunk my battleship!")
        break
# Out of boundaries and repeat guess
    else:
        if (guess_row < 0 or guess_row > 4) or (
              guess_col < 0 or guess_col > 4):
            print("That's not even in the water. Try again!")
        elif (board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
# Turncount/ Game over statemnet
        else:
            print("You missed Ship!")
            board[guess_row][guess_col] = "X"
        if turn == 9:
            print("Game Over")
# Print board with X's
    print_board(board)
