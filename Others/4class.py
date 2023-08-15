from tkinter import *
from PIL import Image ,ImageTk
root = Tk()
root.geometry("644x434")
root.minsize(300,100)
root.maxsize(1200,988)
# L1 = Label(root,test="knjahdjas",bg='Red',fg='white')
f1 = Frame(root, bg='grey', borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
f2 = Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f2.pack(side = TOP, fill="x")
l = Label(f1,text="Project Tkinter")
l.pack(pady=142)
logo=Image.open(f"Others/texture@2x.png")
logo=logo.resize((50,50),Image.ANTIALIAS)
logo=ImageTk.PhotoImage(logo)
l = Label(f2,text="Welcome to text", font="Arial",fg ="red",pady=22, image=logo,compound=LEFT)
l.pack()
root.mainloop()