from tkinter import *
root = Tk()
root.geometry("645x433")

x = StringVar()
y = StringVar()
z= StringVar()

def add1 ():
    ans = int(x.get()) + int( y.get())
    z.set(ans)
def Mul ():
    ans = int(x.get()) * int( y.get())
    z.set(ans)
def div ():
    ans = int(x.get()) // int( y.get())
    z.set(ans)
def mod ():
    ans = int(x.get()) % int( y.get())
    z.set(ans)
def sub ():
    ans = int(x.get()) - int( y.get())
    z.set(ans)

X = Label(root, text = "Enter first number ").grid(row=0,column=0,pady=10)
xentry = Entry(root, textvariable=x).grid(row=0,column=1)

Y = Label(root, text = "Enter Second number ").grid(row=1,column=0,pady=10)
yentry = Entry(root, textvariable=y).grid(row=1,column=1)
Z = Label(root, text = " Answer : ").grid(row=2,column=0)
zentry = Entry(root, textvariable=z).grid(row=2,column=1)
A = Label(root, text = "Calculate : ").grid(row=3,column=1)
b1=Button(text="Add",command=add1)
b1.grid(row=3,column=2,pady=20,padx =10)
b2=Button(text="Sub",command=sub)
b2.grid(row=3,column=3,padx=10)
b3=Button(text="Multilply",command=Mul)
b3.grid(row=3,column=4,padx=10)
b4=Button(text="Divide",command=div)
b4.grid(row=3,column=5,padx=10)
b5=Button(text="Modulus",command=mod)
b5.grid(row=3,column=6)

root.mainloop()

