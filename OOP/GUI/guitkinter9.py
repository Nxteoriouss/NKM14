import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Simple Tkinter button example")
root.geometry("600x400+50+50")
root.resizable(False, False)

#Create Cancel/quit button
exit_button = ttk.Button(
    root,
    text="Cancel",
    command=lambda: root.quit()
)
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand = True
)
root.mainloop()