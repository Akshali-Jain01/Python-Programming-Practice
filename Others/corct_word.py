from textblob import TextBlob
from tkinter import *
from translate import Translator
# data = input("ënter : ")
# ans = TextBlob(data)
# print(ans.correct())

def getvals():
    # print(f"The value of username is: {uservalue.get()}")
    # print(f"The value of password is {passvalue.get()}")
#    ans = TextBlob(langvalue.get())
#    ans = ans.correct()
   translator = Translator(to_lang=langvalue.get())
   ans= translator.translate(uservalue.get())
   print(ans)
   z.set(ans)

root = Tk()
z= StringVar()
root.geometry("655x333")
user = Label(root, text = "User Text")
# password = Label(root , text="Password")
user.grid()
# password.grid()
# password.grid(row=1)
uservalue = StringVar()
langvalue = StringVar()
userentry = Entry(root, textvariable=uservalue)
langentry = Entry(root , textvariable=langvalue)
userentry.grid(row=0,column=1)
langentry.grid(row=1,column=1)
zentry = Entry(root,textvariable=z).grid(row=1,column=  2)
Button(text="Submit",command=getvals).grid()
root.mainloop()