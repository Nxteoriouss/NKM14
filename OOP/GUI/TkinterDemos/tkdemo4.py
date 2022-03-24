import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digikids Application")
        self.label_text = tk.StringVar()
        self.label_text.set("Please Choose One")

        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)

        greetings_button =tk.Button(self, text="Good Afternoon",\
            command=self.goodAfternoon)
        greetings_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0,20))

        bye_button =tk.Button(self, text="Goodbye, see you tomorrow",\
            command=self.goodbye)
        bye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def goodAfternoon(self):
        msgbox.showinfo("Good Afternoon", "Have a nice day")

    def goodbye(self):
        if msgbox.askyesno("Close Window?",\
            "Would you like to close this window now?"):
            self.label_text.set("Window will close in the next 5 seconds")
            self.after(5000, self.destroy)
        else:
            msgbox.showinfo("Window not closing",\
                "Awesome, This window will remain open")

if __name__ == "__main__":
    window= Window()
    window.mainloop()