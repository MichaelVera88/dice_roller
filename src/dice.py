### Structure of dice

from random import randint

# Dice Class
class Dice():
	def __init__(self, name: str, faces: int, amount: int):
		self.name = name
		self.faces = faces
		self.amount = amount

	def roll(self, long_roll: bool) -> tuple:
		"""
		Roll Function:

		Rolls the number of dice currently in amount.
		Long Roll determines if addition is shown.
		"""
		total = 0
		addition = ""

		for roll in range(self.amount):

			rolled = randint(1, self.faces)
			total += rolled

			if long_roll:
				if roll == self.amount-1:
					addition += f"{rolled}"
				else:
					addition += f"{rolled} + "

		return addition, total

# Declare Dice
coin = Dice("coin", 2, 0)
d4 = Dice("d4", 4, 0)
d6 = Dice("d6", 6, 0)
d8 = Dice("d8", 8, 0)
d10 = Dice("d10", 10, 0)
d12 = Dice("d12", 12, 0)
d20 = Dice("d20", 20, 0)
d100 = Dice("d100", 100, 0)

# Dice List
dice_list = [coin, d4, d6, d8, d10, d12, d20, d100]

if __name__ == "__main__":
	print("Dice file")