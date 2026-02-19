# Tic Tac Toe Game in Python

board = [' ' for _ in range(9)]

def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print("--+---+--")
    print(board[3], '|', board[4], '|', board[5])
    print("--+---+--")
    print(board[6], '|', board[7], '|', board[8])
    print()

def check_win(symbol):
    # Win conditions (rows, columns, diagonals)
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(board[a] == board[b] == board[c] == symbol for a,b,c in win_conditions)

def check_draw():
    return all(cell != ' ' for cell in board)

def play_game():
    current_player = "X"

    while True:
        print_board()
        move = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

        # Check valid move
        if board[move] != ' ':
            print("Invalid move! Try again.")
            continue

        board[move] = current_player

        # Check win
        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        # Check draw
        if check_draw():
            print_board()
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# MAIN PROGRAM
play_game()
