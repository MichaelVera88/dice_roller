# Main program file

# Importing custom tkinter to get graphical user interface tools
import customtkinter

# Import graphical user interface files
from gui.window import Window


# Create Window
root = customtkinter.CTk()
Window(root)
root.mainloop()