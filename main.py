### Main program file

### Import graphical user interface files
from gui.gui import window
### Import dice usage
from src.dice import Dice



d20 = Dice(20)

for _ in range(3):
	roll = d20.roll(2, False)
	print(f"{roll[0]}{roll[1]}")

	   