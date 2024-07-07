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
		self.settings_theme_label.grid(row=0, column=0, padx=(15, 0), pady=15)

		self.settings_theme_btn = ctk.CTkSegmentedButton(master=self, values=self.theme_options, command=self.change_theme)
		self.settings_theme_btn.grid(row=0, column=1, padx=15, pady=15)
		self.settings_theme_btn.set(self.theme_options[0])

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

if __name__ == "__main__":
	print("Window file")