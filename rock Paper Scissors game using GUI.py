import tkinter as tk
from tkinter import messagebox
import random
choices = ["rock", "paper", "scissors"]
you_score = 0
com_score = 0
rounds_left = 0

def start_game():
    global you_score, com_score, rounds_left
    try:
        rounds_left = int(entry_rounds.get())
        if rounds_left <= 0:
            raise ValueError
        you_score = 0
        com_score = 0
        update_score()
        label_result.config(text="Game started! Make your move.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of rounds.")

def player_choice(player):
    global you_score, com_score, rounds_left
    if rounds_left <= 0:
        label_result.config(text="Game over! Start a new game.")
        return

    comp = random.choice(choices)
    label_computer.config(text=f"Computer chose: {comp}")

    if player == comp:
        result = "It's a Tie!"
    elif (player == "rock" and comp == "scissors") or \
         (player == "paper" and comp == "rock") or \
         (player == "scissors" and comp == "paper"):
        result = "You win this round!"
        you_score += 1
    else:
        result = "Computer wins this round!"
        com_score += 1

    rounds_left -= 1
    label_result.config(text=result)
    update_score()

    if rounds_left == 0:
        show_final_result()

def update_score():
    label_score.config(text=f"You: {you_score} | Computer: {com_score} | Rounds Left: {rounds_left}")

def show_final_result():
    if you_score > com_score:
        final = f"You won the match!  ({you_score} - {com_score})"
    elif you_score < com_score:
        final = f"Computer won the match.  ({com_score} - {you_score})"
    else:
        final = "It's a tie match!"
    messagebox.showinfo("Game Over", final)

# ----------------- UI Setup -----------------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="#f0f0f0")

label_title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="#f0f0f0")
label_title.pack(pady=10)

entry_rounds = tk.Entry(root, width=10, font=("Arial", 12))
entry_rounds.pack()
entry_rounds.insert(0, "3")

btn_start = tk.Button(root, text="Start Game", command=start_game, bg="green", fg="white", width=15)
btn_start.pack(pady=5)

frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=10)

btn_rock = tk.Button(frame_buttons, text="Rock", command=lambda: player_choice("rock"), width=10)
btn_rock.grid(row=0, column=0, padx=5)

btn_paper = tk.Button(frame_buttons, text="Paper", command=lambda: player_choice("paper"), width=10)
btn_paper.grid(row=0, column=1, padx=5)

btn_scissors = tk.Button(frame_buttons, text="Scissors", command=lambda: player_choice("scissors"), width=10)
btn_scissors.grid(row=0, column=2, padx=5)

label_result = tk.Label(root, text="Press 'Start Game' to begin.", font=("Arial", 12), bg="#f0f0f0")
label_result.pack(pady=10)

label_computer = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
label_computer.pack()

label_score = tk.Label(root, text="You: 0 | Computer: 0 | Rounds Left: 0", font=("Arial", 12), bg="#f0f0f0")
label_score.pack(pady=10)

root.mainloop()
