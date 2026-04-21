N = 8

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    # check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve(board, row):
    if row == N:
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            if solve(board, row+1):
                return True
            board[row][col] = '.'  # backtrack

    return False

board = [['.' for _ in range(N)] for _ in range(N)]
solve(board, 0)