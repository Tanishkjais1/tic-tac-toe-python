import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Variables to track the game state
current_player = "X"
game_board = [""] * 9  # List to hold the state of each cell
buttons = []

# Function to check if there is a winner
def check_winner():
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pattern in win_patterns:
        a, b, c = pattern
        if game_board[a] == game_board[b] == game_board[c] != "":
            return game_board[a]
    return None

# Function to check if the game is a draw
def check_draw():
    return all(cell != "" for cell in game_board)

# Function that handles button clicks
def on_button_click(i):
    global current_player

    if game_board[i] == "" and not check_winner():
        game_board[i] = current_player
        buttons[i].config(text=current_player)

        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global current_player, game_board
    current_player = "X"
    game_board = [""] * 9
    for button in buttons:
        button.config(text="")
    
# Create the buttons (cells of the Tic-Tac-Toe grid)
for i in range(9):
    button = tk.Button(root, text="", font=('Arial', 24), width=5, height=2,
                       command=lambda i=i: on_button_click(i))
    row = i // 3
    col = i % 3
    button.grid(row=row, column=col)
    buttons.append(button)

# Reset button to start a new game
reset_button = tk.Button(root, text="Reset Game", font=('Arial', 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=20)

# Run the game
root.mainloop()
