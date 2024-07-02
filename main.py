### Main program file

from gui.gui import *
from src.dice import Dice

# Main Window
class Window(ctk.CTk):
	def __init__(self):

		super().__init__()

		self.title("Dice Roller")
		self.geometry("600x400")
		self.resizable(False, False)

		# Settings Button
		self.btn_settings = ctk.CTkButton(master=self, text="Settings", width=25, height=25, command=self.open_settings)
		self.btn_settings.pack(side="left", anchor="n", padx=15, pady=15)

		# Settings Menu
		self.frame_settings = FrameSettings(master=self)

		# Dice Options
		self.frame_dice = FrameDice(master=self)
		self.frame_dice.pack(side="right", anchor="n", padx=15, pady=15)

		# Roll Button
		self.roll_button = ctk.CTkButton(master=self, text="ROLL", command=self.rolled)
		self.roll_button.pack(side="bottom", anchor="s", padx=15, pady=15)

	def open_settings(self):
		"""
		Open Settings Function:

		Opens and closes the menu for settings with the settings button.
		"""
		if self.frame_settings.winfo_manager():
			self.frame_settings.pack_forget()
		else:	
			self.frame_settings.pack(side="left", anchor="n", pady=15)

	def rolled(self):
		"""
		"""
		coins = Dice(2)
		total = coins.roll(self.frame_dice.return_coins(), True)
		print(f"{total[0]}{total[1]}")

if __name__ == "__main__":
	dice_roller = Window()
	dice_roller.mainloop()