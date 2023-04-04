import random 
from tkinter import *
from tkinter import font

root = Tk() 
root.geometry("700x450") 

l1 = Label(root, font = ('times', 200))   # type: ignore

def roll():
    num = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(num)}{random.choice(num)}')
    l1.pack()

b1 = Button(root,text="lets roll!!",command = roll) 
b1.place(x=330,y=0) 


root.mainloop()