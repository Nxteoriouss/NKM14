import tkinter as tk
import tkinter.messagebox as msgbox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("How are Things at Home?")
        self.label_text = tk.StringVar()
        self.label_text.set("Please Choose One")

        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)

        greetings_button =tk.Button(self, text="Better",\
            command=self.goodAfternoon)
        greetings_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0,20))

        bye_button =tk.Button(self, text="Not Great",\
            command=self.goodbye)
        bye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))

    def goodAfternoon(self):
        msgbox.showinfo("Better", "Good to Know")

    def goodbye(self):
        if msgbox.askyesno("Do you need Help?",\
            "Are you sure?"):
            self.label_text.set("Contacting the Police")
            self.after(5000, self.destroy)
        else:
            msgbox.showinfo("Ok",\
                "Contacting a Therapist")

if __name__ == "__main__":
    window= Window()
    window.mainloop()
    