import random
def check_winner(board):
    ways_to_win = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
        (1, 5, 9), (3, 5, 7)              # Diagonal
    ]
    for a, b, c in ways_to_win:
        if board[a] == board[b] == board[c] and board[a] in {"X", "O"}:
            return board[a]
    return None
def is_board_full(board):
    for i in board:
        if board[i] not in {"X", "O"}:
            return False
    return True

def minimax(minimax_board, depth, is_maxxing):
    winner = check_winner(minimax_board)
    if winner == "X":
        return depth - 1000
    elif winner == "O":
        return 1000 - depth
    elif is_board_full(minimax_board):
        return 0
    
    if is_maxxing:
        best_score = -1000
        for i in minimax_board:
            if minimax_board[i] not in {"X", "O"}:
                minimax_board[i] = "O"
                score = minimax(minimax_board, depth+1, False)
                minimax_board[i] = f"{i}"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in minimax_board:
            if minimax_board[i] not in {"X","O"}:
                minimax_board[i] = "X"
                score = minimax(minimax_board, depth+1, True)
                minimax_board[i] = f"{i}"
                best_score = min(score,best_score)
        return best_score
    
def best_move(board):
    best_score = -1000
    move = -1
    for i in board:
            if board[i] not in {"X", "O"}:
                board[i] = "O"
                score = minimax(board, 0, False)
                board[i] = f"{i}"
                if score > best_score:
                    best_score = score
                    move = i
    if move != -1:
        return move

def roll():
    return random.randint(1,100)
def draw_board(board):
    board = (f"|{board[1]}|{board[2]}|{board[3]}|\n"
    f"|{board[4]}|{board[5]}|{board[6]}|\n"
    f"|{board[7]}|{board[8]}|{board[9]}|")
    print(board)

def rand_move(board):
    while True:
        c_choice = random.randint(1,9)
        if board[int(c_choice)] not in {"X","O"}: break
    return c_choice
    
def check_turn(turn):
    if turn % 2 == 0: 
        return "X"
    else: 
        return "O"

