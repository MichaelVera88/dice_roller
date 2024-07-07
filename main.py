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
		self.btn_settings.place(x=15, y=15, anchor="nw")

		# Settings Menu
		self.frame_settings = FrameSettings(master=self)

		# Dice Options
		self.frame_dice = FrameDice(master=self)
		self.frame_dice.place(x=585, y=15, anchor="ne")

		# Roll Button
		self.roll_button = ctk.CTkButton(master=self, text="ROLL", command=self.rolled)
		self.roll_button.place(x=585, y=385, anchor="se")

	def open_settings(self):
		"""
		Open Settings Function:

		Opens and closes the menu for settings with the settings button.
		"""
		if self.frame_settings.winfo_manager():
			self.frame_settings.place_forget()
		else:	
			self.frame_settings.place(x=85, y=15, anchor="nw")

	def rolled(self):
		"""
		"""
		

if __name__ == "__main__":
	dice_roller = Window()
	dice_roller.mainloop()