import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry_length.get())
        
        if length < 4:
            messagebox.showerror("Error", "Length must be at least 4")
            return

        
        lowercase = random.choice(string.ascii_lowercase)
        uppercase = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        symbol = random.choice(string.punctuation)

      
        remaining_length = length - 4
        all_chars = string.ascii_letters + string.digits + string.punctuation
        remaining_chars = [random.choice(all_chars) for _ in range(remaining_length)]

       
        password_list = [lowercase, uppercase, digit, symbol] + remaining_chars
        
       
        random.shuffle(password_list)

        password = ''.join(password_list)
        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("450x300")
root.resizable(False, False)

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password Length:").pack()
entry_length = tk.Entry(root, justify="center", width=20)
entry_length.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Arial", 12), justify="center", width=40)
result_entry.pack(pady=10)

tk.Button(root, text="Copy Password", command=copy_password).pack(pady=5)

root.mainloop()