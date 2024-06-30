### Main program file

### Import graphical user interface file
import gui.gui
### Import dice usage
from src.dice import Dice



d20 = Dice(20)

for _ in range(3):
	roll = d20.roll(2, False)
	print(f"{roll[0]}{roll[1]}")

	   