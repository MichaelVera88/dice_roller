### File includes structure of dice

### Importing random integer from random module
from random import randint



class Dice():
	def __init__(self, faces: int):
		"""
		Initialization:

		Declares faces of dice
		"""
		self.faces = faces


	def roll(self, n: int, long_roll: bool):
		"""
		Roll Function:

		Rolls n amount of dice; Long Roll determines if addition is shown
		"""
		total = 0
		addition = ""

		for roll in range(n):

			rolled = randint(1, self.faces)
			total += rolled

			if long_roll:
				if roll == n-1:
					addition += f"{rolled} = "
				else:
					addition += f"{rolled} + "

		return addition, total



if __name__ == "__main__":
	print("Dice file")