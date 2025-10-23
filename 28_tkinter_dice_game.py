import tkinter as tk
import random

def roll():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    result_var.set(f"{d1} + {d2} = {d1 + d2}")

root = tk.Tk()
root.title("Dice Game")
result_var = tk.StringVar(value="Нажми Roll")
tk.Label(root, textvariable=result_var, font=("Arial", 24)).pack(padx=20, pady=10)
tk.Button(root, text="Roll", command=roll, font=("Arial", 16)).pack(pady=10)
root.mainloop()
