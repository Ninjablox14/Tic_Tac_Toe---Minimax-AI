import tkinter as tk
from helpers import check_winner, best_move, rand_move, check_turn, roll

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c3e50")
        
        self.board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        self.turn = 0
        self.mode = None
        self.board_buttons = {}
        self.ai_thinking = False  # Track AI delay state globally
        
        self.show_menu()
    
    def show_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Tic Tac Toe", font=("Arial", 32, "bold"), 
                 bg="#2c3e50", fg="white").pack(pady=20)
        tk.Label(self.root, text="Choose opponent:", font=("Arial", 14), 
                 bg="#2c3e50", fg="white").pack(pady=10)
        
        modes = [
            ("PvP", "pvp"),
            ("Easy AI", "very easy"),
            ("Normal AI", "normal"),
            ("Hard AI", "hard"),
            ("Impossible AI", "minimax")
        ]
        
        for label, mode in modes:
            tk.Button(self.root, text=label, font=("Arial", 12), width=20, height=2,
                     bg="#3498db", fg="white", 
                     command=lambda m=mode: self.start_game(m)).pack(pady=5)
    
    def start_game(self, mode):
        self.mode = mode
        self.board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        self.turn = 0
        self.ai_thinking = False  # Reset flag at the start of a game
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        board_frame = tk.Frame(self.root, bg="#2c3e50")
        board_frame.pack(pady=20)
        
        self.board_buttons = {}
        for i in range(1, 10):
            btn = tk.Button(board_frame, text="", font=("Arial", 24, "bold"), 
                           width=4, height=2, bg="#34495e", fg="white",
                           command=lambda pos=i: self.on_click(pos))
            btn.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)
            self.board_buttons[i] = btn
        
        self.status = tk.Label(self.root, text="Your turn (X)", font=("Arial", 12),
                              bg="#2c3e50", fg="white")
        self.status.pack(pady=10)
        
        tk.Button(self.root, text="Back to Menu", font=("Arial", 10), bg="#95a5a6",
                 fg="white", command=self.show_menu).pack()
    
    def on_click(self, pos):
        # Prevent input if square is taken or if AI is currently waiting out its delay
        if self.board[pos] in {"X", "O"} or self.ai_thinking:
            return
        
        self.board[pos] = check_turn(self.turn)
        self.turn += 1
        self.update_display()
        
        if check_winner(self.board):
            self.status.config(text=f"{check_winner(self.board)} wins!")
            self.disable_all()
            return
        
        if self.turn >= 9:
            self.status.config(text="It's a tie!")
            self.disable_all()
            return
        
        if self.mode != "pvp":
            self.ai_thinking = True  # Block further clicks
            self.status.config(text="AI is thinking...")
            self.root.after(500, self.ai_move)
    
    def ai_move(self):
        if self.mode == "very easy":
            pos = rand_move(self.board)
        elif self.mode == "normal":
            pos = rand_move(self.board) if roll() <= 50 else best_move(self.board)
        elif self.mode == "hard":
            pos = rand_move(self.board) if roll() <= 40 else best_move(self.board)
        else:
            pos = best_move(self.board)
        
        self.board[pos] = check_turn(self.turn)
        self.turn += 1
        self.update_display()
        
        if check_winner(self.board):
            result = "AI wins!" if check_winner(self.board) == "O" else "You win!"
            self.status.config(text=result)
            self.disable_all()
            return
        
        if self.turn >= 9:
            self.status.config(text="It's a tie!")
            self.disable_all()
            return
        
        self.ai_thinking = False  # Safely allow player input again
        self.status.config(text="Your turn (X)")
    
    def update_display(self):
        for pos, btn in self.board_buttons.items():
            if self.board[pos] in {"X", "O"}:
                if self.board[pos] == "X":
                    btn.config(text=self.board[pos], state="disabled", fg="white", bg="#e74c3c")
                else:
                    btn.config(text=self.board[pos], state="disabled", fg="white", bg="#2ecc71")
    
    def disable_all(self):
        for btn in self.board_buttons.values():
            btn.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()