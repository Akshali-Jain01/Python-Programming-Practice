from tkinter import *
from time import strftime
root = Tk()
root.title("digital clock")
l1= Label(root , bg="black",fg="white",font="Arial 18 bold")
l1.pack(anchor="center")

def my_time():
    string = strftime("%H : %M : %S %p")
    l1.config(text= string)
    l1.after(1000,my_time)
    
my_time()
root.mainloop()