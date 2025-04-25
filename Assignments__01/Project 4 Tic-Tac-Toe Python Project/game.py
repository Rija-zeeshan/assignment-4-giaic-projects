# Tic Tac Toe Game in Python
# This is a simple implementation of the Tic Tac Toe game in Python.

board = [" "]*9  # 9 empty spots on board

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_win(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for line in wins:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False

def tic_tac_toe():
    player = "X"
    for turn in range(9):
        print_board()
        move = int(input(f"Player {player}, enter position (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move, try again.")
            continue

        board[move] = player

        if check_win(player):
            print_board()
            print(f"Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board()
    print("It's a tie!")

tic_tac_toe()
