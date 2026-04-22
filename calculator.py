import tkinter as tk

# ---------- Functions ----------
def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(expression))
            screen_var.set(result)
            expression = result
        except:
            screen_var.set("Error")
            expression = ""

    elif text == "C":
        expression = ""
        screen_var.set("")

    else:
        expression += text
        screen_var.set(expression)


# ---------- Main Window ----------
root = tk.Tk()
root.title("✨ Stylish Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

expression = ""

# ---------- Display ----------
screen_var = tk.StringVar()

screen = tk.Entry(root, textvar=screen_var, font=("Arial", 20),
                  bd=10, relief=tk.FLAT, justify="right",
                  bg="#2d2d44", fg="white")
screen.pack(fill="both", ipadx=8, pady=10, padx=10)


# ---------- Button Frame ----------
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(expand=True, fill="both")

# ---------- Button Design ----------
btn_font = ("Arial", 14, "bold")

def create_button(text, row, col, bg="#3b3b5c"):
    btn = tk.Button(frame, text=text, font=btn_font, bg=bg, fg="white",
                    activebackground="#50507a", activeforeground="white",
                    bd=0, padx=20, pady=15)
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    btn.bind("<Button-1>", click)


# ---------- Buttons ----------
create_button("C", 0, 0, "#ff4d4d")

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

row_num = 1
for row in buttons:
    col_num = 0
    for btn in row:
        create_button(btn, row_num, col_num)
        col_num += 1
    row_num += 1


# ---------- Grid Config ----------
for i in range(5):
    frame.grid_rowconfigure(i, weight=1)

for j in range(4):
    frame.grid_columnconfigure(j, weight=1)


root.mainloop()