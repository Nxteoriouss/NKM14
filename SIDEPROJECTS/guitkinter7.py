import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("How are things at home?")
def button_clicked():
    print("Good to know")

button = ttk.Button(root, text='Better',\
    command=button_clicked)
button.pack()

def button_clicked():
    print("Do you need help?")

button = ttk.Button(root, text='Not great',\
    command=button_clicked)
button.pack()

root.geometry('600x400+50+50')
root.mainloop()