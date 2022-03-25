from tkinter import *

ws = Tk()
ws.title('Digikids Calculator')
ws.geometry("250x400+500+100")
ws.resizable(0,0)
num = ''
def display(number):
    global num
    num = num + str(number)
    scr_lbl['text'] = num

def clear_scr():
    global num
    num = ''
    scr_lbl['text'] = num

def equal_btn():
    global num
    add=str(eval(num))
    scr_lbl['text'] = add
    num=''
def equal_btn():
    global num
    sub=str(eval(num))
    scr_lbl['text'] = sub
    num=''
def equal_btn():
    global num
    mul=str(eval(num))
    scr_lbl['text'] = mul
    num=''
def equal_btn():
    global num
    div=str(eval(num))
    scr_lbl['text'] = div
    num=''

var = StringVar()

frame_1 = Frame(ws)
frame_1.pack(expand=True, fill=BOTH)

frame_2 = Frame(ws)
frame_2.pack(expand=True, fill=BOTH)

frame_3 = Frame(ws)
frame_3.pack(expand=True, fill=BOTH)

frame_4 = Frame(ws)
frame_4.pack(expand=True, fill=BOTH)

scr_lbl = Label(
    frame_1,
    textvariable='',
    font=('Arial',20),
    anchor = SE,
    bg = '#595954',
    fg = 'white'
    )

scr_lbl.pack(expand=True, fill=BOTH)

key_1 = Button(
    frame_1,
    text='1',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(1)
    )

key_1.pack(expand=True, fill=BOTH, side=LEFT)

key_2 = Button(
    frame_1,
    text='2',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(2)
    )

key_2.pack(expand=True, fill=BOTH, side=LEFT)

key_3 = Button(
    frame_1,
    text='3',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(3)
    )

key_3.pack(expand=True, fill=BOTH, side=LEFT)

key_add = Button(
    frame_1,
    text='+',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display('+')
    )

key_add.pack(expand=True, fill=BOTH, side=LEFT)

key_4 = Button(
    frame_2,
    text='4',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(4)
    )

key_4.pack(expand=True, fill=BOTH, side=LEFT)

key_5 = Button(
    frame_2,
    text='5',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(5)
    )

key_5.pack(expand=True, fill=BOTH, side=LEFT)

key_6 = Button(
    frame_2,
    text='6',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(6)
    )

key_6.pack(expand=True, fill=BOTH, side=LEFT)

key_sub = Button(
    frame_2,
    text='-',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display('-')
    )

key_sub.pack(expand=True, fill=BOTH, side=LEFT)

key_7 = Button(
    frame_1,
    text='7',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(7)
    )

key_7.pack(expand=True, fill=BOTH, side=LEFT)

key_8 = Button(
    frame_1,
    text='8',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(8)
    )

key_8.pack(expand=True, fill=BOTH, side=LEFT)

key_9 = Button(
    frame_1,
    text='9',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(9)
    )

key_9.pack(expand=True, fill=BOTH, side=LEFT)

key_mul = Button(
    frame_1,
    text='*',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display('*')
    )

key_mul.pack(expand=True, fill=BOTH, side=LEFT)

key_clr = Button(
    frame_1,
    text='C',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display('C')
    )

key_clr.pack(expand=True, fill=BOTH, side=LEFT)

key_0 = Button(
    frame_1,
    text='0',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(0)
    )

key_0.pack(expand=True, fill=BOTH, side=LEFT)

key_res = Button(
    frame_4,
    text='=',
    font=('Ariel', 22),
    border = 0,
    relief = GROOVE,
    bg = '#2E2E2B',
    fg = 'white',
    command = Lambda: display(=)
    )

key_1.pack(expand=True, fill=BOTH, side=LEFT)
