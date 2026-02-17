import math

def print_board(board):
    print("\n")
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print("\n")

def check_winner(board):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def is_draw(board):
    return " " not in board

# Minimax Algorithm
def minimax(board, depth, isMaximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_draw(board):
        return 0

    if isMaximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth+1, False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth+1, True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Game Loop
def tic_tac_toe():
    board = [" "] * 9
    print("Welcome to Tic Tac Toe (Human vs AI)")
    print("You are X | Computer is O")
    print("Positions:")
    print("1 | 2 | 3")
    print("---+---+---")
    print("4 | 5 | 6")
    print("---+---+---")
    print("7 | 8 | 9")

    while True:
        print_board(board)

        try:
            move = int(input("Enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input!")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move!")
            continue

        board[move] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        ai_move = best_move(board)
        board[ai_move] = "O"
        print(f"Computer chooses position {ai_move+1}")

        if check_winner(board) == "O":
            print_board(board)
            print("Computer wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

tic_tac_toe()