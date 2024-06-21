# Creates the main window for program

# Importing custom tkinter to get graphical user interface tools
import customtkinter


def window():
	"""
	Window Function creates main window
	"""

	# Create window
	window = customtkinter.CTk()

	# Window title
	window.title("Dice Roller")

	# Minimum window size
	window.minsize(600, 500)

	# Run Window
	window.mainloop()


if __name__ == "__main__":
	print("Window file")