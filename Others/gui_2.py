from tkinter import *
from PIL import Image , ImageTk
root = Tk()
root.geometry("1255x944")
# for PNG FILES
# photo = PhotoImage(file ="others/texture@2x.png")
# FOR JGP FILES
image = Image.open("others/Tech.jpg")
photo = ImageTk.PhotoImage(image)
label1 = Label(image=photo)
label1.pack()
root.mainloop()