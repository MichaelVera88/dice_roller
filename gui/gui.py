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
		self.btn_settings.grid(row=0, column=0, padx=15, pady=15, sticky="nw")

		# Settings Menu
		self.frame_settings = FrameSettings(master=self)

		# Dice Options
		self.frame_dice = FrameDice(master=self)
		self.frame_dice.grid(row=0, column=2, padx=15, pady=15, sticky="ne")

	def open_settings(self):
		"""
		Open Settings Function:

		Opens and closes the menu for settings with the settings button.
		"""
		if self.frame_settings.winfo_manager():
			self.frame_settings.grid_forget()
		else:	
			self.frame_settings.grid(row=0, column=1, pady=15)


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

		self.temp_label = ctk.CTkLabel(master=self, text="0", width=15, height=15)
		self.temp_label.grid(row=0, column=1, padx=15, pady=15)

		self.temp_add_btn = ctk.CTkButton(master=self, text="+", width=15, height=15)
		self.temp_add_btn.grid(row=0, column=2, padx=(0, 15), pady=15)

		self.temp_sub_btn = ctk.CTkButton(master=self, text="-", width=15, height=15)
		self.temp_sub_btn.grid(row=0, column=0, padx=(15, 0), pady=15)

if __name__ == "__main__":
	print("Window file")