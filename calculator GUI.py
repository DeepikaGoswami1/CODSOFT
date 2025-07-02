import tkinter as tk
from tkinter import messagebox

def get_numbers():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        return a, b
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        return None, None

def add():
    a, b = get_numbers()
    if a is not None:
        result_label.config(text=f"Result: {a + b}")

def subtract():
    a, b = get_numbers()
    if a is not None:
        result_label.config(text=f"Result: {a - b}")

def multiply():
    a, b = get_numbers()
    if a is not None:
        result_label.config(text=f"Result: {a * b}")

def divide():
    a, b = get_numbers()
    if a is not None:
        if b != 0:
            result_label.config(text=f"Result: {a / b}")
        else:
            messagebox.showerror("Math Error", "Cannot divide by zero.")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result:")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x350")


tk.Label(root, text="Enter First Number").pack()
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number").pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)


tk.Button(root, text="Add (+)", command=add, width=20).pack(pady=4)
tk.Button(root, text="Subtract (-)", command=subtract, width=20).pack(pady=4)
tk.Button(root, text="Multiply (*)", command=multiply, width=20).pack(pady=4)
tk.Button(root, text="Divide (/)", command=divide, width=20).pack(pady=4)
tk.Button(root, text="Clear", command=clear, width=20, bg="lightgrey").pack(pady=10)


result_label = tk.Label(root, text="Result:", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
