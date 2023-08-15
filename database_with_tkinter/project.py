import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image , ImageTk

root = Tk()
db = sqlite3.connect(database="school.db")
cr = db.cursor()
root.geometry("1350x700")
root.config(bg="white")

# def show_course():

logo = Image.open("student.png")
logo = logo.resize((50,50),Image.LANCZOS)
logo = ImageTk.PhotoImage(logo)
title = Label(root,text="Student Management and Result System", padx=20,font = ("goudy ols style",20,"bold"),bg="black", fg ="white", image =logo , compound =LEFT,height =50)
title.place(x=0,y=0,height=70,width=1350)

my_frame = LabelFrame(root,text="Menu Card", font = ("goudy ols style",15,"bold"),bg="white", fg ="SlateBlue",height =50)
my_frame.place(x=30, y=100 , height=120 , width=1320)


def menu_course():
    top=Toplevel()
    top.geometry("650x400+10+260")
    top.focus()
    title = Label(top,text="Course Mnanagement",padx=20,font=("goudy ols style",20,"bold"),bg="black",fg="white",image=logo,compound=LEFT,height=50)
    title.place(x=0,y=0,height=70,relwidth=1)
    var_name = StringVar()
    var_duration= StringVar()
    var_charges= StringVar()
    cname = Label(top,text="course name : ",font=("goudy ols style",15,"bold"),fg="black")
    cname.place(x=10,y=90,height=40)

    duration = Label(top,text="Duration : ",font=("goudy ols style",15,"bold"),fg="black")
    duration.place(x=10,y=140,height=40)

    charges = Label(top,text="charges : ",font=("goudy ols style",15,"bold"),fg="black")
    charges.place(x=10,y=190,height=40)

    dis = Label(top,text="Description : ",font=("goudy ols style",15,"bold"),fg="black")
    dis.place(x=10,y=240,height=40)

    txt_cname = Entry(top,textvariable=var_name,font=("goudy ols style",15,"bold"),fg="black")
    txt_cname.place(x=180,y=90,height=40,width=300)

    duration_ = Entry(top,textvariable=var_duration,font=("goudy ols style",15,"bold"),fg="black")
    duration_.place(x=180,y=140,height=40,width=300)

    charges_ = Entry(top,textvariable=var_charges,font=("goudy ols style",15,"bold"),fg="black")
    charges_.place(x=180,y=190,height=40,width=300)

    dis_ = Text(top,font=("goudy ols style",15,"bold"),fg="black")
    dis_.place(x=180,y=240,height=40,width=300)

    btn_add = Button(top,text="ADD",font =("goudy ols style",10,"bold"),bg="blue",fg="white",cursor="hand2",command=add_course)
    btn_add.place(x=10,y=340,height=40,widht=100)
    btn_update=Button(top,text="UPDATE",font=("goudy ols style",10,"bold"),bg="maroon",fg="white",cursor="hand2",command=update)
    btn_update.place(x=120,y=340,height=40,width=100)

    btn_delete=Button(top,text="DELETE",font=("goudy ols style",10,"bold"),bg="maroon",fg="white",cursor="hand2",command=delete)
    btn_delete.place(x=240,y=340,height=40,width=100)
    btn_clear = Button(top,text="Clear",font=("goudy ols style",10,"bold"),bg="maroon",fg="white",cursor="hand2",command=clear)
    btn_clear.place(x=360,y=340,height=40,width=100)

    

b1=Button(my_frame, text="Course", font=("goudy ols style",20,"bold"),bg="Tomato",fg="white",command=menu_course)
b1.place(x=12, y=5,height=70,width=204)

b2=Button(my_frame, text="Student", font=("goudy ols style",20,"bold"),bg="Tomato",fg="white")
b2.place(x=228, y=5,height=70,width=204)

b3=Button(my_frame, text="All Student", font=("goudy ols style",20,"bold"),bg="Tomato",fg="white")
b3.place(x=444, y=5,height=70,width=204)

b4=Button(my_frame, text="Result", font=("goudy ols style",20,"bold"),bg="Tomato",fg="white")
b4.place(x=660, y=5,height=70,width=204)

b5=Button(my_frame, text="Log Out", font=("goudy ols style",20,"bold"),bg="Tomato",fg="white")
b5.place(x=876, y=5,height=70,width=204)

b6=Button(my_frame, text="Exit", font=("goudy ols style",20,"bold"),bg="Tomato",fg="white")
b6.place(x=1092, y=5,height=70,width=204)

## student image
student = Image.open("result.png")
student = student.resize((920,350),Image.LANCZOS)
student = ImageTk.PhotoImage(student)
lbl_student = Label(root,image=student)
lbl_student.place(x=700 , y=250 , width=620 , height=300)

course = Label(root,text="Course [0]", font = ("goudy ols style",20,"bold"),bg="orange", fg ="white",bd=5 ,relief=GROOVE)
course.place(x=700, y=570 , height=70 , width=170)

student1 = Label(root,text="Course [0]", font = ("goudy ols style",20,"bold"),bg="red", fg ="white",bd=5 ,relief=SUNKEN)
student1.place(x=920, y=570 , height=70 , width=170)

result = Label(root,text="Course [0]", font = ("goudy ols style",20,"bold"),bg="maroon", fg ="white",bd=5 ,relief=RAISED)
result.place(x=1150, y=570 , height=70 , width=170)

footer = Label(root,text="SMRS - Student Management & Result System \n contact us 7742214354",padx=15, font = ("goudy ols style",10,"bold"),bg="black", fg ="white",image =logo,compound=LEFT,height=50)
result.place(x=1150, y=570 , height=70 , width=170)


title = Label
root.mainloop()