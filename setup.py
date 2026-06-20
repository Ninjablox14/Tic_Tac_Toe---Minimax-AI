import os, random,time
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
def win_conditions(board):
    ways_to_win = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
        (1, 5, 9), (3, 5, 7)              # Diagonal
    ]
    for a, b, c in ways_to_win:
        if board[a] == board[b] == board[c] and board[a] in {"X", "O"}:
            return True
            
    return False

def main_menu():
    while True:
        print("Welcome to Tic-Tac-Toe!")
        print("1. Play vs a Friend (PvP)")
        print("2. Play vs Computer (Easy)")
        print("3. Play vs Computer (Normal)")
        print("4. Play vs Computer (Hard)")
        print("5. Play vs Computer (Impossible)")
        print("6.  Pess q to quit")
        choice = input("Select an option: ")
        
        if choice == "1":
            game(mode="pvp") 
        elif choice == "2":
            game(mode="very easy") 
        elif choice == "3":
            game(mode="normal")
        elif choice == "4":
            game(mode="hard")
        elif choice == "5":
            game(mode="minimax")
        elif choice == "q":
            print("Thanks for playing!")
            break
        else:
            print("Invalid Input! Please select from the options above.\n")

def game(mode = "N/A"):
    board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    draw_board(board)
    turn = 0
    
    playing = True
    winner = None

    while playing:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(board)
        current_turn = turn % 2 + 1
        if mode == "very easy" and current_turn == 2:
            time.sleep(0.2)
            board[rand_move(board)] = check_turn(turn)
            
            if win_conditions(board):
                playing = False
                winner = current_turn
            else: 
                turn +=1
        elif mode == "normal" and current_turn == 2:
            chance = roll()
            if chance <= 50:
                time.sleep(0.2)
                board[rand_move(board)] = check_turn(turn)
            else:
                time.sleep(0.2)
                board[best_move(board)] = check_turn(turn)
            if win_conditions(board):
                playing = False
                winner = current_turn
            else: 
                turn +=1
        elif mode == "hard" and current_turn == 2:
            chance = roll()
            if chance <= 40:
                time.sleep(0.2)
                board[rand_move(board)] = check_turn(turn)
            else:
                time.sleep(0.2)
                board[best_move(board)] = check_turn(turn)
            if win_conditions(board):
                playing = False
                winner = current_turn
            else: 
                turn +=1
        elif mode == "minimax" and current_turn ==2:
            time.sleep(0.2)
            board[best_move(board)] = check_turn(turn)
            
            if win_conditions(board):
                playing = False
                winner = current_turn
            else: 
                turn +=1
        else:
            print(f"Player {current_turn}'s turn: (Pick a spot or enter q to exit)")
            choice = input('>')
            if choice == 'q':
                playing = False
                break
            elif str.isdigit(choice) and int(choice) in board:
                if board[int(choice)] not in {"X","O"}:
                    board[int(choice)] = check_turn(turn)
                
                    if win_conditions(board): 
                        playing = False
                        winner = current_turn
                    else:
                        turn +=1   
                else:
                    print("Spot was taken! Press Enter...")
                    input()
            else: 
                print("Invalid spot! Press Enter...")
                input()
        if turn > 8 and playing:
            playing = False    

    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(board)

    if winner: 
        if mode != "pvp" and winner == 2:
            print("Computer wins!")
        else:
            print(f"Player {winner} wins!")
    else: print("It's a tie!")
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
