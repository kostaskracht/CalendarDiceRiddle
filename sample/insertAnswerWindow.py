# imports
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from calculations import calculations


class insertAnswerWindow():

	def __init__(self):
		pass

	def insertAnswer(self):
		window = Toplevel()
		window.title("Insert your answer")
		window.geometry('350x500')
		window.configure(bg="white")
		window.iconbitmap('../media/puzzle1.ico')

		lbl1 = Label(window, text="First dice", font=("Arial Bold", 10), bg="white")
		lbl1.grid(column=1, row=0)

		firstIndices = []
		for idx in range(10):
			val = BooleanVar()
			checkbox = Checkbutton(window, text=str(idx), var=val, bg="white")
			firstIndices.append(val)
			checkbox.grid(column=1, row=(idx + 1))

		lbl2 = Label(window, text="Second dice", font=("Arial Bold", 10), bg="white")
		lbl2.grid(column=2, row=0)

		secondIndices = []
		for idx in range(10):
			val = BooleanVar()
			checkbox = Checkbutton(window, text=str(idx), var=val, bg="white")
			checkbox.grid(column=2, row=(idx + 1))
			secondIndices.append(val)

		btn = Button(window, text="Check results", command=lambda: calculations().calculate(
			firstIndices, secondIndices), bg="white")
		btn.grid(column=1, row=11, ipadx=10, padx=50, pady=100)

		btn2 = Button(window, text="Show correct \n answer", command=self.showCorrect, bg="white")
		btn2.grid(column=2, row=11)

		btn.bind('<Return>', lambda event=None: btn.invoke())
		btn.focus()
		window.mainloop()

	@staticmethod
	def showCorrect():
		text = "First dice numbers:  0, 1, 2, 3, 4, 5 \n" \
				 "Second dice numbers: 0, 1, 2, 6, 7, 8"
		messagebox.showinfo("Correct answer", text)
