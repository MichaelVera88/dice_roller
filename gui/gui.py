### Creates the main window and GUI for program

import customtkinter as ctk
from PIL import Image

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

	def open_settings(self):
		"""
		Open Settings Function:

		Opens and closes the menu for settings with the settings button.
		"""
		if self.frame_settings.winfo_manager():
			self.frame_settings.pack_forget()
		else:	
			self.frame_settings.pack(side="left", anchor="n", pady=15)


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

		# Dice Amounts
		self.coin_amount = 0

		# Frame Title
		self.dice_label = ctk.CTkLabel(master=self, text="DICE")
		self.dice_label.grid(row=0, column=1, padx=15, pady=(5, 0))

		# Coin Labels
		self.coin_label = ctk.CTkLabel(master=self, text="COIN (1-2)")
		self.coin_label.grid(row=1, column=1, pady=(20, 0))

		self.coin_amount_label = ctk.CTkLabel(master=self, text=str(self.coin_amount))
		self.coin_amount_label.grid(row=1, column=1, pady=(0, 20))

		# Coin Buttons
		self.coin_add_btn = ctk.CTkButton(master=self, text="+", width=15, height=40, command=self.add_coin)
		self.coin_add_btn.grid(row=1, column=2, padx=15, pady=15)

		self.coin_sub_btn = ctk.CTkButton(master=self, text="-", width=15, height=40, command=self.sub_coin)
		self.coin_sub_btn.grid(row=1, column=0, padx=15, pady=15)

	def add_coin(self):
		"""
		Add Coin Function:

		Increments coin amount by +1
		"""
		if self.coin_amount < 10:
			self.coin_amount += 1
		self.coin_amount_label.configure(text=str(self.coin_amount))
	
	def sub_coin(self):
		"""
		Sub Coin Function:

		Increments coin amount by -1
		"""
		if self.coin_amount > 0:
			self.coin_amount -= 1
		self.coin_amount_label.configure(text=str(self.coin_amount))

if __name__ == "__main__":
	print("Window file")