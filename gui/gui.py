### Creates the main window and GUI for program

### Importing custom tkinter to get graphical user interface tools
import customtkinter
### Importing Image from Pillow to properly get icons
from PIL import Image



### Window
# -------------------------------------------------

# Set Custom Theme
#customtkinter.set_default_color_theme("gui/theme/custom_theme.json")

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
		settings_menu.place_forget()
	else:
		settings_menu.place(relx=0, rely=0, x=95, y=15, anchor="nw")


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
dark_settings_icon = customtkinter.CTkImage(light_image=Image.open("gui/images/arnold.png"), dark_image=Image.open("gui/images/arnold.png"), size=(50, 50))
settings_button = customtkinter.CTkButton(master=window, text=None, width=50, height=50, image=dark_settings_icon, command=settings_icon_click)
settings_button.place(relx=0, rely=0, x=15, y=15, anchor="nw")

# Settings Menu Frame
settings_menu = customtkinter.CTkFrame(master=window)

# Light/Dark Theme Settings Option 
option_theme_label = customtkinter.CTkLabel(master=settings_menu, text="Theme Color:")
option_theme_label.grid(row=0, column=0, padx=15, pady=15, sticky='n')

option_theme_button = customtkinter.CTkSegmentedButton(master=settings_menu, values=["System", "Light", "Dark"], command=settings_theme_click)
option_theme_button.grid(row=0, column=1, padx=15, pady=15, sticky="n")
option_theme_button.set("System")

# -------------------------------------------------



### Dice
# -------------------------------------------------

d20_amount = 0

def increase(n):
	"""
	Increase Function:

	Increases amount of dice rolled
	"""
	n += 1


def decrease(n):
	"""
	Decrease Function:

	Decreases amount of dice rolled
	"""
	n -= 1

#D20
d20_amount_label = customtkinter.CTkLabel(master=window, text=d20_amount, width=25, height=50)
d20_amount_label.place(relx=1, rely=0, x=-45, y=15, anchor="ne")

d20_increase_button = customtkinter.CTkButton(master=window, text="+", width=25, height=50, command=increase(d20_amount))
d20_increase_button.place(relx=1, rely=0, x=-15, y=15, anchor="ne")

d20_decrease_button = customtkinter.CTkButton(master=window, text="-", width=25, height=50, command=decrease(d20_amount))
d20_decrease_button.place(relx=1, rely=0, x=-85, y=15, anchor="ne")

# -------------------------------------------------



# Run Window
window.mainloop()


if __name__ == "__main__":
	print("Window file")