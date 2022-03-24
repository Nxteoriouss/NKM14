import tkinter as tk

root = tk.Tk()
root.title("Digikids example 3")
root.geometry("600x400+50+50")
#resizable() has two parameters that specify the height and width of the window, you specify if it is
# resizable or not
root.resizable(False, False)
root.attributes('-topmost', 1)
root.mainloop()