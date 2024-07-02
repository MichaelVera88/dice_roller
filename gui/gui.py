### Creates the main window and GUI for program

import customtkinter as ctk
from PIL import Image

# Main Window
class Window(ctk.CTk):
	def __init__(self):

		super().__init__()

		self.title("Dice Roller")
		self.geometry("400x300")
		self.resizable(False, False)

		# Settings Button
		self.btn_settings = ctk.CTkButton(master=self, text="Settings", width=25, height=25, command=self.open_settings)
		self.btn_settings.grid(row=0, column=0, padx=15, pady=15, sticky="nw")

		# Settings Menu
		self.frame_settings = FrameSettings(master=self, width=200, height=100)

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


if __name__ == "__main__":
	print("Window file")