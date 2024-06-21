# File includes structure of dice

# Importing random integer from random module
from random import randint


class Dice():
	def __init__(self, faces):
		"""
		Initialization:

		Declares faces of dice
		"""
		self.faces = faces

	def roll(self, n):
		"""
		Roll Function:

		Rolls n amount of dice
		"""
		total = 0

		for _ in range(n):
			total += randint(range(self.faces))
		
		return total
