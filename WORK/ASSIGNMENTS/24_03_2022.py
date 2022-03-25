import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digikids Application")
        self.label_text = tk.StringVar()
        self.label_text.set("My Name is: ")

        self.name_text = tk.StringVar()

        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=10)

        self.name_entry = tk.Entry(self, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)

        hello_button = tk.Button(self,text="Hello", command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))

        goodbye_button = tk.Button(self,text="Goodbye", command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def say_hello(self):
        message = "Good Morning " + self.name_entry.get()
        msgbox.showinfo("Hello", message)

    def say_goodbye(self):
        if msgbox.askyesno("Close the Window","Would You Like to Close This Window?"):
            message = "Thank you. Closing the window in 5 seconds " + self.name_entry.get()
            self.label_text.set(message)
            self.after(5000, self.destroy)
        else:
            msgbox.showinfo("Not Closing", "Great! This window will stay open.")

if __name__ == "__main__":
    window = Window()
    window.mainloop()