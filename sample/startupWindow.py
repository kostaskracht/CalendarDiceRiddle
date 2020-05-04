# imports
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from explanationWindow import explanationWindow
from insertAnswerWindow import insertAnswerWindow


class startupWindow():

	def __init__(self):
		pass

	def startup(self):
		window = Tk()
		window.title("Welcome to Calendar Dice Riddle")
		window.geometry('400x550')
		window.configure(bg="white")
		window.iconbitmap('../media/puzzle1.ico')

		menubar = Menu(window)
		# create more pulldown menus
		editmenu = Menu(menubar, tearoff=0)
		editmenu.add_command(label="About", command=self.aboutToolbar)
		menubar.add_cascade(label="Options", menu=editmenu)
		window.config(menu=menubar)

		# Create the frame for the problem statement
		descFrame = LabelFrame(window, padx=10, bg="white")
		descFrame.grid(padx=10, pady=10, columnspan=3)

		description = "How can you represent the days of all months using two 6 sided dice? "\
							"You can write one number on each face of the dice from 0 to 9 and you have " \
							" to represent days from 1 to 31, for example for 1, one dice should show 0 " \
							"and another should show 1, similarly for 29 one dice should show 2 and " \
							"another should show 9."

		descLabel = Label(descFrame, text=description, font=("Arial Bold", 10), wraplength=350,
								bg="white")
		descLabel.grid(column=0, row=0)
		photo = ImageTk.PhotoImage(Image.open("../media/calendarDices.jpg"))
		photoLabel = Label(descFrame, image=photo, bg="white")
		photoLabel.grid(column=0, row=1)

		# Create a buttons' frame
		btnFrame = LabelFrame(window, borderwidth=0, bg="white")
		btnFrame.grid(row=1, column=0, pady=10, columnspan=3)

		insertBtn = Button(btnFrame, text="Give an answer", width=20,
								 command=insertAnswerWindow().insertAnswer, bg="white")
		insertBtn.grid(row=0, column=0)

		emptyLabel = Label(btnFrame, text=str(26 * " "), bg="white")
		emptyLabel.grid(row=0, column=1)

		solutionBtn = Button(btnFrame, text="Show solution", width=20,
									command=explanationWindow().solution, bg="white")
		solutionBtn.grid(row=0, column=2)

		window.mainloop()

	def aboutToolbar():
		messagebox.showinfo("About", "The code was created and developed by Kostas Krachtopoulos.")
