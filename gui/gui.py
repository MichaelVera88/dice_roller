### Creates the main window and GUI for program

### Importing custom tkinter to get graphical user interface tools
import customtkinter


### Window
# -------------------------------------------------

# Set light/dark theme based on system
theme = customtkinter.set_appearance_mode("System")

# Create window
window = customtkinter.CTk()

# Set window title
window.title("Dice Roller")

# Set minimum window size
window.minsize(600, 500)

# -------------------------------------------------


### Settings
# -------------------------------------------------

def settings_icon_click():
	"""
	Settings Icon Click Function:

	Opens and closes menu for settings when settings icon is clicked
	"""
	if settings_menu.winfo_manager():
		settings_menu.grid_forget()
	else:
		settings_menu.grid(row=0, column=1, padx=15, pady=15, sticky="nw")

# Create an icon for settings
settings_icon = customtkinter.CTkButton(window, text="Settings", width=50, height=25, command=settings_icon_click)
settings_icon.grid(row=0, column=0, padx=15, pady=15, sticky="nw")

# Create settings menu frame
settings_menu = customtkinter.CTkFrame(window, width=150, height=250, fg_color=theme)

# -------------------------------------------------

# Run Window
window.mainloop()


if __name__ == "__main__":
	print("Window file")