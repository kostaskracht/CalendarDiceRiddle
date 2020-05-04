# imports
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


class explanationWindow():

	def __init__(self):
		pass

	@staticmethod
	def solution():
		window = Toplevel()
		window.title("Solution explanation")
		window.geometry('390x500')
		window.configure(bg="white")
		window.iconbitmap('../media/puzzle1.ico')

		# Create window canvas
		wFrame = Frame(window)
		wFrame.pack()
		canvas = Canvas(wFrame)
		wiFrame = Frame(canvas)
		scrollbar = Scrollbar(wFrame, orient="vertical", command=canvas.yview)
		canvas.configure(yscrollcommand=scrollbar.set)

		# Scroll bar function
		def scrollFunc(event):
			canvas_height = event.height
			canvas.configure(scrollregion=canvas.bbox("all"), height=canvas_height)

		scrollbar.pack(side="right", fill="y")
		canvas.pack(side="left")
		canvas.create_window((0, 0), window=wiFrame, anchor='nw')
		wiFrame.bind("<Configure>", scrollFunc)

		# Create correct answer frame
		correctFrame = LabelFrame(wiFrame, borderwidth=10, pady=10, bg="white")
		correctFrame.grid(row=0, column=0)

		corAnsLabel1 = Label(correctFrame, text="Correct Answer:", font="bold", bg="white")
		corAnsLabel1.grid(row=0, column=0)

		corAns = "One of the solutions is to write 0, 1, 2, 3, 4 and 5 on the sides of the first " \
					"die, and 0, 1, 2, 6, 7 and 8 on the faces of the second die. We note that 9 is " \
					"not present in any of the dice."
		corAnsLabel2 = Label(correctFrame, text=corAns, wraplength=350, bg="white")
		corAnsLabel2.grid(row=1, column=0)

		corrPhoto = ImageTk.PhotoImage(Image.open("../media/CorrectAnswer.png"))
		corrPhotoLabel = Label(correctFrame, image=corrPhoto, bg="white")
		corrPhotoLabel.image = corrPhoto
		corrPhotoLabel.grid(row=2, column=0)

		# Create explanation frame
		explFrame = LabelFrame(wiFrame, borderwidth=0, pady=10, bg="white")
		explFrame.grid(row=1, column=0)

		explLabel1 = Label(explFrame, text="Explanation:", font="bold", bg="white")
		explLabel1.grid(row=0, column=0)

		expl = "The first thing to realize is that we need 1 and 2 in both the dice in order to be " \
				 "able to display 11 and 22. Moreover, 0 is needed in both dices, so that the numbers " \
				 "from 01 to 09 are displayed."

		explLabel2 = Label(explFrame, text=expl, wraplength=350, bg="white")
		explLabel2.grid(row=1, column=0)

		explPhoto1 = ImageTk.PhotoImage(Image.open("../media/AllCombinations.png"))
		explPhotoLabel1 = Label(explFrame, image=explPhoto1, bg="white")
		explPhotoLabel1.image = explPhoto1
		explPhotoLabel1.grid(row=2, column=0)

		expl2 = "At that point, the are 6 dice sides left empty and 7 numbers to enter" \
				  "(3, 4, 5, 6, 7, 8, 9). All days containing a 9 can’t be displayed."

		explLabel3 = Label(explFrame, text=expl2, wraplength=350, bg="white")
		explLabel3.grid(row=3, column=0)

		expl3 = "But, remember that the numbers will be displayed on dice. This means that 6 and 9 can" \
				  "be displayed in one side, simply by rotating the die 180 degrees."

		explLabel4 = Label(explFrame, text=expl3, wraplength=350, bg="white")
		explLabel4.grid(row=4, column=0)

		explPhoto2 = ImageTk.PhotoImage(Image.open("../media/SixToNine.png"))
		explPhotoLabel2 = Label(explFrame, image=explPhoto2, bg="white")
		explPhotoLabel2.image = explPhoto2
		explPhotoLabel2.grid(row=5, column=0)

		expl4 = "Now all calendar days can be displayed!"

		explLabel4 = Label(explFrame, text=expl4, wraplength=350, bg="white")
		explLabel4.grid(row=6, column=0)

