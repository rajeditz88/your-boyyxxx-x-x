import tkinter as tk
from tkinter import messagebox
import random

# Define the game class
class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe Game")
        self.master.geometry("400x450")
        self.master.config(bg="lightblue")

        self.player = "X"
        self.board = [None] * 9
        self.buttons = []
        self.create_start_menu()

    def create_start_menu(self):
        self.start_menu_frame = tk.Frame(self.master, bg="lightblue")
        self.start_menu_frame.pack(expand=True)

        self.title_label = tk.Label(self.start_menu_frame, text="Welcome to Tic Tac Toe", font=("Arial", 20), bg="lightblue")
        self.title_label.pack(pady=20)

        self.start_button = tk.Button(self.start_menu_frame, text="Start Game", font=("Arial", 16), command=self.start_game)
        self.start_button.pack(pady=10)

        self.exit_button = tk.Button(self.start_menu_frame, text="Exit Game", font=("Arial", 16), command=self.master.quit)
        self.exit_button.pack(pady=10)

    def start_game(self):
        self.start_menu_frame.pack_forget()  # Remove the start menu
        self.create_game_board()

    def create_game_board(self):
        self.game_frame = tk.Frame(self.master, bg="lightblue")
        self.game_frame.pack()

        self.turn_label = tk.Label(self.game_frame, text=f"Player {self.player}'s Turn", font=("Arial", 14), bg="lightblue")
        self.turn_label.grid(row=0, column=0, columnspan=3)

        for i in range(9):
            button = tk.Button(self.game_frame, text="", font=("Arial", 24), height=2, width=5, bg="white", 
                               command=lambda i=i: self.make_move(i))
            button.grid(row=(i // 3) + 1, column=i % 3)
            self.buttons.append(button)

    def make_move(self, i):
        if self.board[i] is None:  # Ensure the spot is empty
            self.board[i] = self.player
            self.buttons[i].config(text=self.player, state="disabled", bg="lightgreen" if self.player == "X" else "lightcoral")
            if self.check_winner():
                self.game_over(f"Player {self.player} Wins!")
            elif None not in self.board:
                self.game_over("It's a Draw!")
            else:
                self.switch_player()

    def switch_player(self):
        self.player = "O" if self.player == "X" else "X"
        self.turn_label.config(text=f"Player {self.player}'s Turn")

    def check_winner(self):
        # Check for rows, columns, and diagonals
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] is not None:
                return True
        return False

    def game_over(self, message):
        messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        for button in self.buttons:
            button.config(text="", state="normal", bg="white")
        self.board = [None] * 9
        self.player = "X"
        self.turn_label.config(text=f"Player {self.player}'s Turn")

# Set up the Tkinter window
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
