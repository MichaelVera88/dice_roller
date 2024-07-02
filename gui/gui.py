### Creates the main window and GUI for program

import customtkinter as ctk
from PIL import Image

# Main Window
class Window(ctk.CTk):
	def __init__(self):
		super().__init__()
		self.title("Dice Roller")
		self.resizable(False, False)
		self.geometry("500x500")

if __name__ == "__main__":
	print("Window file")