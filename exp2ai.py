def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i < 8 and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True
def solve_queens(board, col):
    if col >= 8:
        return True
    for row in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1  

            if solve_queens(board, col + 1):
                return True
            board[row][col] = 0  
    return False 
board = [[0 for _ in range(8)] for _ in range(8)]

if solve_queens(board, 0):
    print("8-Queen Solution:\n")
    for row in board:
        print(row)
else:
    print("No solution exists")
