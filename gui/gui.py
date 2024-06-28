### Creates the main window and GUI for program

### Importing custom tkinter to get graphical user interface tools
import customtkinter
### Importing Image from Pillow to properly get icons
from PIL import Image



### Window
# -------------------------------------------------

# Set Custom Theme
customtkinter.set_default_color_theme("gui/theme/custom_theme.json")

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
settings_icon = customtkinter.CTkImage(light_image=Image.open("gui/images/arnold.png"), dark_image=Image.open("gui/images/arnold.png"), size=(50, 50))
settings_button = customtkinter.CTkButton(master=window, text=None, width=50, height=50, image=settings_icon, command=settings_icon_click)
settings_button.grid(row=0, column=0, padx=15, pady=15, sticky="nw")

# Settings Menu Frame
settings_menu = customtkinter.CTkFrame(master=window)

# Light/Dark Theme Settings Option 
option_theme_label = customtkinter.CTkLabel(master=settings_menu, text="Theme Color:")
option_theme_label.grid(row=0, column=0, padx=15, pady=15, sticky='n')

option_theme_button = customtkinter.CTkSegmentedButton(master=settings_menu, values=["System", "Light", "Dark"], command=settings_theme_click)
option_theme_button.grid(row=0, column=1, padx=15, pady=15, sticky="n")
option_theme_button.set("System")




# Run Window
window.mainloop()


if __name__ == "__main__":
	print("Window file")