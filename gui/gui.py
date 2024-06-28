### Creates the main window and GUI for program

### Importing custom tkinter to get graphical user interface tools
import customtkinter



### Window
# -------------------------------------------------

# Set light/dark theme based on system
system_theme = customtkinter.set_appearance_mode("System")
light_theme = customtkinter.set_appearance_mode("Light")
dark_theme = customtkinter.set_appearance_mode("Dark")

# Create Window
window = customtkinter.CTk()

# Window Title
window.title("Dice Roller")

# Minimum Window Size
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


def settings_theme_click(value):
	"""
	Settings Theme Click Function:

	Sets the theme of the program to either light or dark; defaults to system on startup
	"""
	if value == "System":
		customtkinter.set_appearance_mode("System")
	elif value == "Light":
		customtkinter.set_appearance_mode("Light")
	elif value == "Dark":
		customtkinter.set_appearance_mode("Dark")
		
		

# Settings Icon
settings_icon = customtkinter.CTkButton(window, text="Settings", width=50, height=25, command=settings_icon_click)
settings_icon.grid(row=0, column=0, padx=15, pady=15, sticky="nw")

# Settings Menu Frame
settings_menu = customtkinter.CTkFrame(window, fg_color=system_theme)

# Light/Dark Theme Settings Option 
option_theme_label = customtkinter.CTkLabel(settings_menu, text="Theme Color:")
option_theme_label.grid(row=0, column=0, padx=15, pady=15, sticky='n')

option_theme_button = customtkinter.CTkSegmentedButton(settings_menu, values=["System", "Light", "Dark"], command=settings_theme_click)
option_theme_button.grid(row=0, column=1, padx=15, pady=15, sticky="n")
option_theme_button.set("System")




# Run Window
window.mainloop()


if __name__ == "__main__":
	print("Window file")