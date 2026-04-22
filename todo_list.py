import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return
    task_listbox.insert(tk.END, "☐ " + task)
    task_entry.delete(0, tk.END)

def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to delete.")
        return
    task_listbox.delete(selected)

def mark_done():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to mark complete.")
        return
    index = selected[0]
    task = task_listbox.get(index)
    if task.startswith("✔ "):
        messagebox.showinfo("Info", "Task is already completed.")
        return
    updated_task = "✔ " + task[2:]
    task_listbox.delete(index)
    task_listbox.insert(index, updated_task)

def update_task():
    selected = task_listbox.curselection()
    new_task = task_entry.get().strip()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to update.")
        return
    if new_task == "":
        messagebox.showwarning("Warning", "Please enter updated task text.")
        return
    index = selected[0]
    current_task = task_listbox.get(index)
    prefix = "✔ " if current_task.startswith("✔ ") else "☐ "
    task_listbox.delete(index)
    task_listbox.insert(index, prefix + new_task)
    task_entry.delete(0, tk.END)

def load_task_to_entry(event):
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected[0])[2:]
        task_entry.delete(0, tk.END)
        task_entry.insert(0, task)

def clear_all():
    if task_listbox.size() == 0:
        messagebox.showinfo("Info", "No tasks to clear.")
        return
    confirm = messagebox.askyesno("Confirm", "Do you want to clear all tasks?")
    if confirm:
        task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("520x620")
root.config(bg="#0f172a")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="To-Do List",
    font=("Segoe UI", 24, "bold"),
    bg="#0f172a",
    fg="white"
)
title_label.pack(pady=(20, 10))

subtitle_label = tk.Label(
    root,
    text="Manage your daily tasks in a smart and simple way",
    font=("Segoe UI", 10),
    bg="#0f172a",
    fg="#94a3b8"
)
subtitle_label.pack()

main_frame = tk.Frame(root, bg="#1e293b", bd=0)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

entry_frame = tk.Frame(main_frame, bg="#1e293b")
entry_frame.pack(pady=20)

task_entry = tk.Entry(
    entry_frame,
    font=("Segoe UI", 14),
    width=28,
    bd=0,
    relief="flat",
    bg="#e2e8f0",
    fg="#0f172a"
)
task_entry.grid(row=0, column=0, padx=10, ipady=10)

add_button = tk.Button(
    entry_frame,
    text="Add Task",
    font=("Segoe UI", 12, "bold"),
    bg="#22c55e",
    fg="white",
    activebackground="#16a34a",
    activeforeground="white",
    bd=0,
    padx=15,
    pady=10,
    command=add_task
)
add_button.grid(row=0, column=1, padx=5)

list_frame = tk.Frame(main_frame, bg="#1e293b")
list_frame.pack(padx=20, pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(
    list_frame,
    font=("Segoe UI", 13),
    bg="#0f172a",
    fg="white",
    selectbackground="#38bdf8",
    selectforeground="black",
    bd=0,
    height=15,
    yscrollcommand=scrollbar.set
)
task_listbox.pack(fill="both", expand=True)
scrollbar.config(command=task_listbox.yview)

task_listbox.bind("<<ListboxSelect>>", load_task_to_entry)

button_frame = tk.Frame(main_frame, bg="#1e293b")
button_frame.pack(pady=20)

update_button = tk.Button(
    button_frame,
    text="Update",
    font=("Segoe UI", 12, "bold"),
    bg="#f59e0b",
    fg="white",
    activebackground="#d97706",
    activeforeground="white",
    bd=0,
    width=10,
    pady=10,
    command=update_task
)
update_button.grid(row=0, column=0, padx=8, pady=8)

done_button = tk.Button(
    button_frame,
    text="Complete",
    font=("Segoe UI", 12, "bold"),
    bg="#3b82f6",
    fg="white",
    activebackground="#2563eb",
    activeforeground="white",
    bd=0,
    width=10,
    pady=10,
    command=mark_done
)
done_button.grid(row=0, column=1, padx=8, pady=8)

delete_button = tk.Button(
    button_frame,
    text="Delete",
    font=("Segoe UI", 12, "bold"),
    bg="#ef4444",
    fg="white",
    activebackground="#dc2626",
    activeforeground="white",
    bd=0,
    width=10,
    pady=10,
    command=delete_task
)
delete_button.grid(row=0, column=2, padx=8, pady=8)

clear_button = tk.Button(
    button_frame,
    text="Clear All",
    font=("Segoe UI", 12, "bold"),
    bg="#8b5cf6",
    fg="white",
    activebackground="#7c3aed",
    activeforeground="white",
    bd=0,
    width=10,
    pady=10,
    command=clear_all
)
clear_button.grid(row=0, column=3, padx=8, pady=8)

root.mainloop()