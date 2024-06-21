# Main program file

# Importing tkinter to get graphical user interface tools
import tkinter

# Import graphical user interface files
from gui.window import Window


# Create Window
root = tkinter.Tk()
Window(root)
root.mainloop()