from tkinter import *
root = Tk()
# root.geometry('600x400')
root.minsize(100,100)
root.maxsize(900,500)
root.title("TRY FORM")
# redbutton = Button(root,text="Red",fg="red")  # .pack(side=LEFT)
# name = Label(root,text="Name").grid(row=0,column=0)
# e1=Entry(root).grid(row=0,column=1)
# Paasword = Label(root,text="Password").grid(row=1,column=0)
# e2=Entry(root).grid(row=1,column=1)
# Submit = Button(root,text="Submit",fg="Black").grid(row=3,column=0)
#we can use place to place on any particular pixel point
name = Label(root, text ="Name").place(x=50,y=70)
email = Label(root, text ="Email").place(x=80,y=90)

# redbutton.pack(side=LEFT)
root.mainloop()#shows windows until we exit
# print("sdfs sdfd") --wil run after main loop

