# Creates the main window for program

# Importing custom tkinter to get graphical user interface tools
import customtkinter


# Create window
window = customtkinter.CTk()

# Window title
window.title("Dice Roller")

# Minimum window size
window.minsize(600, 500)


# Settings
settings_menu = customtkinter.CTkFrame(window, width=100, height=100, fg_color="white")

def settings_click():
	if settings_menu.winfo_manager():
		settings_menu.place_forget()
	else:
		settings_menu.place(relx=0.1, rely=0.1, anchor="nw")

settings_button = customtkinter.CTkButton(window, text="Settings", height=20, width=40, command=settings_click)
settings_button.place(relx=0.05, rely=0.05, anchor="nw")


# Run Window
window.mainloop()


if __name__ == "__main__":
	print("Window file")