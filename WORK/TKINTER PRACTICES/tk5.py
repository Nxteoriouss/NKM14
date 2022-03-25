from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Digikids Application for pop Up window")
window.geometry('500x300')
def clicked():
    messagebox.showinfo('Pop Up Window', 'Message content')
btn = Button(window, text='Click Here', command=clicked)
btn.grid(column=0, row=0)
window.mainloop()
