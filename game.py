import random
import tkinter as tk

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
round_count = 0

def get_winner(user, computer):
    if user == computer:
        return "It's a Tie!"
    if (user == "Rock" and computer == "Scissors") or \
       (user == "Paper" and computer == "Rock") or \
       (user == "Scissors" and computer == "Paper"):
        return "You Win!"
    return "Computer Wins!"

def play(user_choice):
    global user_score, computer_score, round_count
    computer_choice = random.choice(choices)
    result = get_winner(user_choice, computer_choice)
    round_count += 1

    if result == "You Win!":
        user_score += 1
        result_label.config(fg="#22c55e")
    elif result == "Computer Wins!":
        computer_score += 1
        result_label.config(fg="#ef4444")
    else:
        result_label.config(fg="#facc15")

    user_choice_label.config(text=f"You Chose: {user_choice}")
    computer_choice_label.config(text=f"Computer Chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score  You: {user_score}   Computer: {computer_score}")
    round_label.config(text=f"Round: {round_count}")

def reset_game():
    global user_score, computer_score, round_count
    user_score = 0
    computer_score = 0
    round_count = 0
    user_choice_label.config(text="You Chose: -")
    computer_choice_label.config(text="Computer Chose: -")
    result_label.config(text="Make your move!", fg="#38bdf8")
    score_label.config(text="Score  You: 0   Computer: 0")
    round_label.config(text="Round: 0")

root = tk.Tk()
root.title("Rock Paper Scissors Pro")
root.geometry("520x590")
root.configure(bg="#0f172a")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Segoe UI", 24, "bold"),
    bg="#0f172a",
    fg="#f8fafc"
)
title_label.pack(pady=(20, 8))

subtitle_label = tk.Label(
    root,
    text="Choose your move and challenge the computer",
    font=("Segoe UI", 11),
    bg="#0f172a",
    fg="#94a3b8"
)
subtitle_label.pack(pady=(0, 20))

card = tk.Frame(root, bg="#1e293b", bd=0, relief="flat")
card.pack(padx=25, pady=10, fill="both", expand=True)

instruction_label = tk.Label(
    card,
    text="Select one option below",
    font=("Segoe UI", 14, "bold"),
    bg="#1e293b",
    fg="#e2e8f0"
)
instruction_label.pack(pady=(25, 15))

button_frame = tk.Frame(card, bg="#1e293b")
button_frame.pack(pady=10)

rock_btn = tk.Button(
    button_frame,
    text="🪨 Rock",
    font=("Segoe UI", 13, "bold"),
    bg="#334155",
    fg="white",
    activebackground="#475569",
    activeforeground="white",
    bd=0,
    width=12,
    pady=12,
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=8, pady=8)

paper_btn = tk.Button(
    button_frame,
    text="📄 Paper",
    font=("Segoe UI", 13, "bold"),
    bg="#334155",
    fg="white",
    activebackground="#475569",
    activeforeground="white",
    bd=0,
    width=12,
    pady=12,
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=8, pady=8)

scissors_btn = tk.Button(
    button_frame,
    text="✂️ Scissors",
    font=("Segoe UI", 13, "bold"),
    bg="#334155",
    fg="white",
    activebackground="#475569",
    activeforeground="white",
    bd=0,
    width=12,
    pady=12,
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=8, pady=8)

result_box = tk.Frame(card, bg="#0f172a")
result_box.pack(padx=20, pady=25, fill="both")

user_choice_label = tk.Label(
    result_box,
    text="You Chose: -",
    font=("Segoe UI", 13),
    bg="#0f172a",
    fg="#cbd5e1"
)
user_choice_label.pack(pady=(20, 10))

computer_choice_label = tk.Label(
    result_box,
    text="Computer Chose: -",
    font=("Segoe UI", 13),
    bg="#0f172a",
    fg="#cbd5e1"
)
computer_choice_label.pack(pady=10)

result_label = tk.Label(
    result_box,
    text="Make your move!",
    font=("Segoe UI", 18, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
result_label.pack(pady=20)

score_label = tk.Label(
    card,
    text="Score  You: 0   Computer: 0",
    font=("Segoe UI", 14, "bold"),
    bg="#1e293b",
    fg="#f8fafc"
)
score_label.pack(pady=(5, 10))

round_label = tk.Label(
    card,
    text="Round: 0",
    font=("Segoe UI", 12),
    bg="#1e293b",
    fg="#94a3b8"
)
round_label.pack(pady=(0, 20))

reset_btn = tk.Button(
    card,
    text="Play Again",
    font=("Segoe UI", 13, "bold"),
    bg="#06b6d4",
    fg="white",
    activebackground="#0891b2",
    activeforeground="white",
    bd=0,
    width=18,
    pady=12,
    command=reset_game
)
reset_btn.pack(pady=(0, 25))

root.mainloop()