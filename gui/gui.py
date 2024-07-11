### Creates the GUI elements for program

import customtkinter as ctk
from PIL import Image
from src.dice import *

# Settings Menu Class
class FrameSettings(ctk.CTkFrame):
	def __init__(self, master, **kwargs):

		super().__init__(master, **kwargs)

		# Change Theme Label & Button
		self.theme_options = ["System", "Light", "Dark"]

		self.settings_theme_label = ctk.CTkLabel(master=self, text="Theme:")
		self.settings_theme_label.grid(row=0, column=0, padx=(55, 0), pady=15)

		self.settings_theme_btn = ctk.CTkSegmentedButton(master=self, values=self.theme_options, command=self.change_theme)
		self.settings_theme_btn.grid(row=0, column=1, padx=15, pady=15)
		self.settings_theme_btn.set(self.theme_options[0])

		# Show Addition
		self.addition_option = ctk.BooleanVar(value=False)

		self.settings_addition_label = ctk.CTkLabel(master=self, text="Show Addition:")
		self.settings_addition_label.grid(row=1, column=0, padx=(15, 0), pady=15)

		self.settings_addition_switch = ctk.CTkSwitch(master=self, text="", command=self.show_addition, variable=self.addition_option, onvalue=True, offvalue=False)
		self.settings_addition_switch.grid(row=1, column=1, padx=(0, 15), pady=15)

	def change_theme(self, value):
		"""
		Change Theme Function:

		Changes theme of program with a segmented button to light or dark mode.
		"""
		if value == "Light":
			ctk.set_appearance_mode("Light")
		elif value == "Dark":
			ctk.set_appearance_mode("Dark")
		else:
			ctk.set_appearance_mode("System")

	def show_addition(self):
		"""
		Show Addition Function:

		Toggles showing all addition in each dice roll.
		"""
		return self.addition_option.get()

# Dice Options Class
class FrameDice(ctk.CTkFrame):
	def __init__(self, master, **kwargs):

		super().__init__(master, **kwargs)

		# Frame Title
		self.dice_label = ctk.CTkLabel(master=self, text="DICE")
		self.dice_label.grid(row=0, column=1, padx=15, pady=(5, 0))

		# Coin Labels
		self.coin_label = ctk.CTkLabel(master=self, text=coin.name)
		self.coin_label.grid(row=1, column=1, pady=(20, 0))

		self.coin_amount_label = ctk.CTkLabel(master=self, text=coin.amount)
		self.coin_amount_label.grid(row=1, column=1, pady=(0, 20))

		# Coin Buttons
		self.coin_add_btn = ctk.CTkButton(master=self, text="+", width=15, height=40, command=lambda : self.add(self.coin_amount_label, coin))
		self.coin_add_btn.grid(row=1, column=2, padx=15, pady=5)

		self.coin_sub_btn = ctk.CTkButton(master=self, text="-", width=15, height=40, command=lambda : self.sub(self.coin_amount_label, coin))
		self.coin_sub_btn.grid(row=1, column=0, padx=15, pady=5)

		# d4 Labels
		self.d4_label = ctk.CTkLabel(master=self, text=d4.name)
		self.d4_label.grid(row=2, column=1, pady=(20,0))

		self.d4_amount_label = ctk.CTkLabel(master=self, text=d4.amount)
		self.d4_amount_label.grid(row=2, column=1, pady=(0, 20))

		# d4 Buttons
		self.d4_add_btn = ctk.CTkButton(master=self, text="+", width=15, height=40, command=lambda : self.add(self.d4_amount_label, d4))
		self.d4_add_btn.grid(row=2, column=2, padx=15, pady=5)

		self.d4_sub_btn = ctk.CTkButton(master=self, text="-", width=15, height=40, command=lambda : self.sub(self.d4_amount_label, d4))
		self.d4_sub_btn.grid(row=2, column=0, padx=15, pady=5)

		# d6 Labels
		self.d6_label = ctk.CTkLabel(master=self, text=d6.name)
		self.d6_label.grid(row=3, column=1, pady=(20,0))

		self.d6_amount_label = ctk.CTkLabel(master=self, text=d6.amount)
		self.d6_amount_label.grid(row=3, column=1, pady=(0, 20))

		# d6 Buttons
		self.d6_add_btn = ctk.CTkButton(master=self, text="+", width=15, height=40, command=lambda : self.add(self.d6_amount_label, d6))
		self.d6_add_btn.grid(row=3, column=2, padx=15, pady=5)

		self.d6_sub_btn = ctk.CTkButton(master=self, text="-", width=15, height=40, command=lambda : self.sub(self.d6_amount_label, d6))
		self.d6_sub_btn.grid(row=3, column=0, padx=15, pady=5)

		# d8 Labels
		self.d8_label = ctk.CTkLabel(master=self, text=d8.name)
		self.d8_label.grid(row=4, column=1, pady=(20,0))

		self.d8_amount_label = ctk.CTkLabel(master=self, text=d8.amount)
		self.d8_amount_label.grid(row=4, column=1, pady=(0, 20))

		# d8 Buttons
		self.d8_add_btn = ctk.CTkButton(master=self, text="+", width=15, height=40, command=lambda : self.add(self.d8_amount_label, d8))
		self.d8_add_btn.grid(row=4, column=2, padx=15, pady=5)

		self.d8_sub_btn = ctk.CTkButton(master=self, text="-", width=15, height=40, command=lambda : self.sub(self.d8_amount_label, d8))
		self.d8_sub_btn.grid(row=4, column=0, padx=15, pady=5)

		# d10 Labels
		self.d10_label = ctk.CTkLabel(master=self, text=d10.name)
		self.d10_label.grid(row=5, column=1, pady=(20,0))

		self.d10_amount_label = ctk.CTkLabel(master=self, text=d10.amount)
		self.d10_amount_label.grid(row=5, column=1, pady=(0, 20))

		# d10 Buttons
		self.d10_add_btn = ctk.CTkButton(master=self, text="+", width=15, height=40, command=lambda : self.add(self.d10_amount_label, d10))
		self.d10_add_btn.grid(row=5, column=2, padx=15, pady=5)

		self.d10_sub_btn = ctk.CTkButton(master=self, text="-", width=15, height=40, command=lambda : self.sub(self.d10_amount_label, d10))
		self.d10_sub_btn.grid(row=5, column=0, padx=15, pady=5)

		# d12 Labels
		self.d12_label = ctk.CTkLabel(master=self, text=d12.name)
		self.d12_label.grid(row=6, column=1, pady=(20,0))

		self.d12_amount_label = ctk.CTkLabel(master=self, text=d12.amount)
		self.d12_amount_label.grid(row=6, column=1, pady=(0, 20))

		# d12 Buttons
		self.d12_add_btn = ctk.CTkButton(master=self, text="+", width=15, height=40, command=lambda : self.add(self.d12_amount_label, d12))
		self.d12_add_btn.grid(row=6, column=2, padx=15, pady=5)

		self.d12_sub_btn = ctk.CTkButton(master=self, text="-", width=15, height=40, command=lambda : self.sub(self.d12_amount_label, d12))
		self.d12_sub_btn.grid(row=6, column=0, padx=15, pady=5)

		# d20 Labels
		self.d20_label = ctk.CTkLabel(master=self, text=d20.name)
		self.d20_label.grid(row=7, column=1, pady=(20,0))

		self.d20_amount_label = ctk.CTkLabel(master=self, text=d20.amount)
		self.d20_amount_label.grid(row=7, column=1, pady=(0, 20))

		# d20 Buttons
		self.d20_add_btn = ctk.CTkButton(master=self, text="+", width=15, height=40, command=lambda : self.add(self.d20_amount_label, d20))
		self.d20_add_btn.grid(row=7, column=2, padx=15, pady=5)

		self.d20_sub_btn = ctk.CTkButton(master=self, text="-", width=15, height=40, command=lambda : self.sub(self.d20_amount_label, d20))
		self.d20_sub_btn.grid(row=7, column=0, padx=15, pady=5)

		# d100 Labels
		self.d100_label = ctk.CTkLabel(master=self, text=d100.name)
		self.d100_label.grid(row=8, column=1, pady=(20,0))

		self.d100_amount_label = ctk.CTkLabel(master=self, text=d100.amount)
		self.d100_amount_label.grid(row=8, column=1, pady=(0, 20))

		# d100 Buttons
		self.d100_add_btn = ctk.CTkButton(master=self, text="+", width=15, height=40, command=lambda : self.add(self.d100_amount_label, d100))
		self.d100_add_btn.grid(row=8, column=2, padx=15, pady=5)

		self.d100_sub_btn = ctk.CTkButton(master=self, text="-", width=15, height=40, command=lambda : self.sub(self.d100_amount_label, d100))
		self.d100_sub_btn.grid(row=8, column=0, padx=15, pady=5)

	def add(self, label, dice):
		"""
		Add Function:

		Increments amount by +1.
		"""
		if dice.amount < 10:
			dice.amount += 1
		label.configure(text=dice.amount)
	
	def sub(self, label, dice):
		"""
		Sub Function:

		Increments amount by -1.
		"""
		if dice.amount > 0:
			dice.amount -= 1
		label.configure(text=dice.amount)

# Roll Display
class FrameRoll(ctk.CTkFrame):
	def __init__(self, master, **kwargs):

		super().__init__(master, **kwargs)

		# Display Addition
		self.addition_label = ctk.CTkLabel(master=self, text="", font=("arial", 14))

		# Display Total
		self.total_label = ctk.CTkLabel(master=self, text="", width=50, height=25, font=("arial", 28))
		self.total_label.grid(row=1, column=0, padx=15, pady=15, sticky="s")
		self.total_label.grid_propagate(False)

# Roll History
class FrameHistory(ctk.CTkFrame):
	def __init__(self, master, **kwargs):

		super().__init__(master, **kwargs)

		

if __name__ == "__main__":
	print("Window file")