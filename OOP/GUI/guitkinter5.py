import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#1. Using keyword arguments
# ttk.Label(root, text="Tomorrow is Thursday").pack()

#2. using a dictionary index after idget creation
label = ttk.Label(root)
label['text'] = "Tomorrow is Thursday"
label.pack()
#3. Using the config( methhod with keyword attributes)
root.geometry('600x400+50+50')
root.mainloop()