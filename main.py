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
		self.frame_roll_display.place(x=400, y=500, anchor="s")

		# Roll History
		self.btn_history = ctk.CTkButton(master=self, text=">", width=10, height=25, command=self.open_history)
		self.btn_history.place(x=15, y=275)

		self.frame_roll_history = FrameHistory(master=self, width=100, height=425)
		
		# Roll Button
		self.roll_button = ctk.CTkButton(master=self, text="ROLL", command=self.rolled)
		self.roll_button.place(x=785, y=500, anchor="se")

	def open_settings(self):
		"""
		Open Settings Function:

		Opens and closes the menu for settings with the settings button.
		"""
		if self.frame_settings.winfo_viewable():
			self.frame_settings.place_forget()
		else:	
			self.frame_settings.place(x=85, y=15, anchor="nw")

	def open_history(self):
		"""
		Open History Function:

		Opens and closes the frame for roll history with the history button.
		"""
		if self.frame_roll_history.winfo_viewable():
			self.btn_history.place(x=15, y=275)
			self.frame_roll_history.place_forget()
		else:
			self.btn_history.place(x=145, y=275)
			self.frame_roll_history.place(x=15, y=75)

	def rolled(self):
		"""
		Rolled Function:

		Rolls selected dice, displays total and addition if setting is checked, and records roll.
		"""
		addition = ""
		total = 0

		for dice in dice_list:
			if dice.amount > 0:
				if self.frame_settings.show_addition():
					current_dice = dice.roll(self.frame_settings.show_addition())

					addition += f"{dice.name}({current_dice[0]}) \n"
					total += current_dice[1]
				else:
					current_dice = dice.roll(False)

					total += current_dice[1]

		#addition = addition[:-2]

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

		self.frame_roll_history.record_history(addition, total)
		
if __name__ == "__main__":
	dice_roller = Window()
	dice_roller.mainloop()