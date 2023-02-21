
from textwrap import indent
from tkinter import *
from tkinter import ttk
import tkinter as tk
def solve_quadratic():
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())
    d = b**2 - 4*a*c
    if d < 0:
        result_label.config(text="Уравнение не имеет действительных корней")
    else:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        result_label.config(text=f"Корни уравнения:\n x1 = {x1}\n x2 = {x2}")

root = tk.Tk()
root.title("Квадратные уравнения")
root.geometry("320x180")

title_label = tk.Label(root, text="Решение квадратных уравнений", bg="lightblue", fg="green", font=("Arial", 16))


entry_a = tk.Entry(root, width=3, bg="lightblue")

x2_label = tk.Label(root, text="x**2 +", font=("Arial", 16))

entry_b = tk.Entry(root, width=3, bg="lightblue")

x_label = tk.Label(root, text="x +", font=("Arial", 16))

entry_c = tk.Entry(root, width=3, bg="lightblue")

eq_label = tk.Label(root, text="= 0", font=("Arial", 16))

solve_button = tk.Button(root, text="Решить", bg="green", fg="white", font=("Arial", 16), command=solve_quadratic)

result_label = tk.Label(root, text="Решение", bg="yellow", width=25, height=4, font=("Arial", 16))

title_label.grid(row=0, column=0,columnspan=10)
x2_label.grid(row=1, column=1)
entry_a.grid(row=1, column=0)
x_label.grid(row=1, column=3)
entry_b.grid(row=1, column=2)
eq_label.grid(row=1, column=5)
entry_c.grid(row=1, column=4)
solve_button.grid(row=1, column=6)
result_label.grid(row=4, column=0,columnspan=10)

root.mainloop()
