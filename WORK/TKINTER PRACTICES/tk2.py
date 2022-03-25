import tkinter as tk 
import random

window = tk.Tk()
window.geometry("400x300")
window.title("Lets play Rock Paper Scissors")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissors':2}
    return rps[choice]
def number_to_choice(number):
    rps = {0:'rock',1:'paper',2:'scissor'}
    return rps[number]

def random_computer_choice():
    return random.choice(['rock','paper','scissors'])

def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You win")
        USER_SCORE+=1
    else:
        print("Comp wins")
        COMP_SCORE+=1
def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You win")
        USER_SCORE+=1
    else:
        print("Comp wins")
        COMP_SCORE+=1
    
    text_area = tk.Text(master=window,height=12,width=30,bg="#FFFF99")
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \nYour Score: {u} \nComputer's Score : {c}"
    text_area.insert(tk.END,answer)


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)
def scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissors'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

button1 = tk.Button(text="     Rock      ",bg="skyblue",command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="     Paper      ",bg="pink",command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="     Scissors      ",bg="lightgreen",command=rock)
button3.grid(column=0,row=3)

window.mainloop()