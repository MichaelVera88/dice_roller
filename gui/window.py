# Creates the main window for program

# Importing tkinter to get graphical user interface tools
import tkinter
from tkinter import ttk


class Window:

	def __init__(self, root):
		"""
		Initialization:

		Creates basic parts for a window.
		"""

		# Window title
		root.title("Dice Roller")

		# Declare frame to hold content inside window
		content = ttk.Frame(root).grid()


if __name__ == "__main__":
	print("Window file")