import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def select(option):
    print(option)

ttk.Button(root, text="Rock", command=lambda: select("Rock")).pack()
ttk.Button(root, text="Paper", command=lambda: select("Paper")).pack()
ttk.Button(root, text="Scissors", command=lambda: select("Scissors")).pack()

root.geometry('600x400+50+50')
root.mainloop()