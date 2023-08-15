import tkinter.messagebox as tmsg
from tkinter import *
root= Tk()
myslider2 = Scale(root, from_=0,to=100,orient = HORIZONTAL,tickinterval=10)
myslider2.pack()
root.mainloop()