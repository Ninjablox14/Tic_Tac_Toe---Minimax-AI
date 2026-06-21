import os,time
from helpers import *

def main_menu():
    while True:
        print("Welcome to Tic-Tac-Toe!")
        print("1. Play vs a Friend (PvP)")
        print("2. Play vs Computer (Easy)")
        print("3. Play vs Computer (Normal)")
        print("4. Play vs Computer (Hard)")
        print("5. Play vs Computer (Impossible)")
        print("6.  Pess q to quit")
        choice = input("Select an option: ").strip()
        
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
            
            if check_winner(board):
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
            if check_winner(board):
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
            if check_winner(board):
                playing = False
                winner = current_turn
            else: 
                turn +=1
        elif mode == "minimax" and current_turn ==2:
            time.sleep(0.2)
            board[best_move(board)] = check_turn(turn)
            
            if check_winner(board):
                playing = False
                winner = current_turn
            else: 
                turn +=1
        else:
            print(f"Player {current_turn}'s turn: (Pick a spot or enter q to exit)")
            choice = input('>').strip()
            if choice == 'q':
                playing = False
                break
            elif str.isdigit(choice) and int(choice) in board:
                if board[int(choice)] not in {"X","O"}:
                    board[int(choice)] = check_turn(turn)
                
                    if check_winner(board): 
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
