import tkinter as tk
from tkinter import messagebox

# Calculator functions
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error"
def power(x, y): return x ** y
def floor_divide(x, y):
    try:
        return x // y
    except ZeroDivisionError:
        return "Error"

# Map operation symbols to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power,
    '//': floor_divide
}

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()
        if op not in operations:
            raise ValueError("Invalid Operation")
        result = operations[op](num1, num2)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers and operation.")

# GUI setup
root = tk.Tk()
root.title("Perfect Calculator GUI")

tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Operation (+, -, *, /, **, //):").grid(row=2, column=0)
operation = tk.Entry(root)
operation.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
