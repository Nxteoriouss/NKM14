from tkinter import *

class Window(Frame):
    def __init__(Self, master=None):
        Frame.__init__(Self, master)
        Self.master = master

#Code to initialize the tkinter
root = Tk()
app = Window(root)

#Add the Window title
root.wm_title("Digikids Application")

#To show the window and retain it on the screen
root.mainloop()