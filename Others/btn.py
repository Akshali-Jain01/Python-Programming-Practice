from tkinter import *
root = Tk()
root.geometry("655x333")

def hello():
    print("Hello tkinter buttons")
def name():
    print("Nmae is vijay")

frame = Frame(root, borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1 = Button(frame, fg= "red",text ="print now",command=hello)
b1.pack(side=LEFT,padx=23)
b2=Button(frame , fg="red", text ="Tell me now", command= name)
b2.pack(side=LEFT,padx=23)
root.mainloop()