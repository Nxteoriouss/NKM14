import tkinter as tk
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digikids Application")

        label=tk.Label(self, text="Welcome to Digikids")
        label.pack(fill=tk.BOTH, expand=1, padx=200, pady=100)

if __name__ == "__main__":
    window = Window()
    window.mainloop()