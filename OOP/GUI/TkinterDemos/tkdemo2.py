from tkinter import *

class Window(Frame):
    def __init__(Self, master=None):
        Frame.__init__(Self, master)
        Self.master = master

        Self.pack(fill=BOTH, expand=1)

        #create button and link it toclickexitbutton
        exitButton = Button(Self, text="Exit", command=Self.clickExitButton)

        #Location of the button (x, y)
        exitButton.place(x=175, y=75)

    def clickExitButton(Self):
        exit()

root = Tk()
app = Window(root)
root.wm_title("Button example")
root.geometry("400x200")
root.mainloop()