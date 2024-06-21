# Creates the main window and GUI for program

# Importing custom tkinter to get graphical user interface tools
import customtkinter


# Window
# -------------------------------------------------

# Create window
window = customtkinter.CTk()

# Set window title
window.title("Dice Roller")

# Set minimum window size
window.minsize(600, 500)

# Set light/dark theme based on system
customtkinter.set_appearance_mode("Dark")

# -------------------------------------------------


# Settings
# -------------------------------------------------

# Declare an icon for settings
settings_icon = customtkinter.CTkButton(window, text="Settings", width=50, height=25)
settings_icon.grid(row=0, column=0, pady=15, padx=15)


# -------------------------------------------------

# Run Window
window.mainloop()


if __name__ == "__main__":
	print("Window file")