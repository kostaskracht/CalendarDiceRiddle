# imports
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


class calculations():

	def __init__(self):
		pass

	def calculate(self, firstIndices, secondIndices):
		# import ipdb; ipdb.set_trace()
		x_bool = []
		y_bool = []
		for i in range(10):
			x_bool.append(int(firstIndices[i].get()))
			y_bool.append(int(secondIndices[i].get()))

		x = np.where(x_bool)[0]
		y = np.where(y_bool)[0]

		if len(x) != 6 or len(y) != 6:
			messagebox.showerror("Value Error", "Wrong number of values selected. Six values for each "
															"dice must be selected")
			return
		# perform the little trick
		x, y = self.littleTrick(x, y)

		# calculate the combinations
		flagWrongAnswer, wrongNums = self.calculateCombinations(x, y)

		# announce the results
		self.announceResults(flagWrongAnswer, wrongNums)

	@staticmethod
	def littleTrick(arr1, arr2):
		fnl_array = []
		for array in [arr1, arr2]:
			if 9 in array and 6 not in array:
				array = np.append(array, 6)
			elif 6 in array and 9 not in array:
				array = np.append(array, 9)
			fnl_array.append(array)
		return fnl_array

	@staticmethod
	def calculateCombinations(arr1, arr2):
		isAnswerWrong = False
		wrongNums = []
		for i in range(1, 32):
			flag = False
			for f in arr1:
				for s in arr2:
					if f * 10 + s == i or \
							  s * 10 + f == i:
						flag = True
						break
				if flag:
					break
			if flag:
				continue
			wrongNums.append(str(i).zfill(2))
			isAnswerWrong = True

		return isAnswerWrong, wrongNums

	@staticmethod
	def announceResults(isAnswerWrong, wrongNums):
		if isAnswerWrong:
			# print "Wrong answer. Please try again."
			nums = ""
			for num in wrongNums:
				nums += num + ", "
			messagebox.showinfo("Results", "Wrong answer. \nThe following numbers can't be "
													 "displayed with your current selection: " + nums[:-2] +
									  ". \nPlease try again.")

		else:
			# print "Your answer was correct!"
			messagebox.showinfo("Results", "Correct answer!")

