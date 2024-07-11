### Main program file

from gui.gui import *

# Main Window
class Window(ctk.CTk):
	def __init__(self):

		super().__init__()

		self.title("Dice Roller")
		self.geometry("800x600")
		self.resizable(False, False)

		# Settings
		self.btn_settings = ctk.CTkButton(master=self, text="Settings", width=25, height=25, command=self.open_settings)
		self.btn_settings.place(x=15, y=15, anchor="nw")

		self.frame_settings = FrameSettings(master=self)

		# Dice Options
		self.frame_dice = FrameDice(master=self)
		self.frame_dice.place(x=785, y=15, anchor="ne")

		# Roll Display
		self.frame_roll_display = FrameRoll(master=self)
		self.frame_roll_display.place(x=400, y=585, anchor="s")

		# Roll History
		self.btn_history = ctk.CTkButton(master=self, text=">", width=10, height=25)
		self.btn_history.place(x=130, y=325)

		self.frame_roll_history = FrameHistory(master=self, width=100, height=425)
		self.frame_roll_history.place(x=15, y=125)

		# Roll Button
		self.roll_button = ctk.CTkButton(master=self, text="ROLL", command=self.rolled)
		self.roll_button.place(x=785, y=585, anchor="se")

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
		Rolled Function:

		Rolls selected dice.
		"""
		addition = ""
		total = 0
		multiple_dice = 0

		for dice in dice_list:

			if dice.amount > 0:
				current_dice = dice.roll(self.frame_settings.show_addition())

				addition += f"{dice.name}({current_dice[0]}) \n"
				total += current_dice[1]
				multiple_dice += 1

		addition = addition[:-2]

		if total == 0:
			self.frame_roll_display.addition_label.grid(row=0, column=0, padx=15, pady=15, sticky="n")
			self.frame_roll_display.addition_label.configure(text="No Dice Selected")
			self.frame_roll_display.total_label.grid_forget()
		elif self.frame_settings.show_addition() == True:
			self.frame_roll_display.addition_label.grid(row=0, column=0, padx=15, pady=(15, 0), sticky="n")
			self.frame_roll_display.addition_label.configure(text=f"{addition}\n=")
			self.frame_roll_display.total_label.grid(row=1, column=0, padx=15, pady=(0, 15), sticky="s")
			self.frame_roll_display.total_label.configure(text=total)
		else:
			self.frame_roll_display.addition_label.grid_forget()
			self.frame_roll_display.total_label.grid(row=1, column=0, padx=15, pady=15, sticky="s")
			self.frame_roll_display.total_label.configure(text=total)
		
if __name__ == "__main__":
	dice_roller = Window()
	dice_roller.mainloop()