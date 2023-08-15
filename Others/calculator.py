from tkinter import *
expression = ""

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	global expression
	total = str(eval(expression))
	equation.set(total)
	expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":
	root = Tk()
	root.configure(background="grey")
	root.title("Simple Calculator")
	root.geometry("330x230")
	equation = StringVar()

	expression_field = Entry(root, textvariable=equation)
	expression_field.grid(columnspan=4, ipadx=70)

	button1 = Button(root, text=' 1 ', fg='black', bg='white',command=lambda: press(1), height=2, width=8)
	button1.grid(row=2, column=0)

	button2 = Button(root, text=' 2 ', fg='black', bg='white',command=lambda: press(2), height=2, width=8)
	button2.grid(row=2, column=1)

	button3 = Button(root, text=' 3 ', fg='black', bg='white',command=lambda: press(3), height=2, width=8)
	button3.grid(row=2, column=2)

	button4 = Button(root, text=' 4 ', fg='black', bg='white',command=lambda: press(4), height=2, width=8)
	button4.grid(row=3, column=0)

	button5 = Button(root, text=' 5 ', fg='black', bg='white',command=lambda: press(5), height=2, width=8)
	button5.grid(row=3, column=1)

	button6 = Button(root, text=' 6 ', fg='black', bg='white',command=lambda: press(6), height=2, width=8)
	button6.grid(row=3, column=2)

	button7 = Button(root, text=' 7 ', fg='black', bg='white',command=lambda: press(7), height=2, width=8)
	button7.grid(row=4, column=0)

	button8 = Button(root, text=' 8 ', fg='black', bg='white',command=lambda: press(8), height=2, width=8)
	button8.grid(row=4, column=1)

	button9 = Button(root, text=' 9 ', fg='black', bg='white',command=lambda: press(9), height=2, width=8)
	button9.grid(row=4, column=2)

	button0 = Button(root, text=' 0 ', fg='black', bg='white',command=lambda: press(0), height=2, width=8)
	button0.grid(row=5, column=0)

	plus = Button(root, text=' + ', fg='black', bg='white',command=lambda: press("+"), height=2, width=8)
	plus.grid(row=2, column=3)

	minus = Button(root, text=' - ', fg='black', bg='white',command=lambda: press("-"), height=2, width=8)
	minus.grid(row=3, column=3)

	multiply = Button(root, text=' * ', fg='black', bg='white',command=lambda: press("*"), height=2, width=8)
	multiply.grid(row=4, column=3)

	divide = Button(root, text=' / ', fg='black', bg='white',command=lambda: press("/"), height=2, width=8)
	divide.grid(row=5, column=3)

	equal = Button(root, text=' = ', fg='black', bg='white',command=equalpress, height=2, width=8)
	equal.grid(row=5, column=2)

	clear = Button(root, text='Clear', fg='black', bg='white',command=clear, height=2, width=8)
	clear.grid(row=5, column='1')

	Decimal= Button(root, text='.', fg='black', bg='white',command=lambda: press('.'), height=2, width=8)
	Decimal.grid(row=6, column=0)
	root.mainloop()