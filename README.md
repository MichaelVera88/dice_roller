# Dice Roller

#### Video Demo: https://youtu.be/VdWRcQ8VX4Q

## Description: 
A program that rolls certain amounts and certain types of dice through a graphical user interface using Python.

## What I Learned:
	- Custom Tkinter Library (Frames, Layout Managers, Other Widgets)
	- Python OOP

#### Backstory:
For this project, I really wanted to try and tackle something a bit larger than a standard Python program that I've been working with. What I mean is the small program that takes in something from a terminal or does something and prints it out, you know what I mean. I wanted something a bit more interactive and more user friendly than running it and using it within the terminal. So, my mind immediately went over to creating something with Pygame since it is potentially one of the most interactive things I can build with Python as a beginner. However, I didn't want to create a full game. I wanted to do something a bit smaller to get a grasp on how to create something that uses some type of user interface like most programs do. Therefore, I decided to base this project around that. At least having an idea on some type of user interface library would get me started with building something more "real" and universal to use.

#### Learning:
Firstly, I had to pick out a library to get a user interface started. As I was digging around, I immediately came across TKinter. I did get started in TKinter but I really liked how Custom TKinter (CTk) looked by default instead. So, I went ahead and used that. Otherwise, there isn't any other things that were completely foreign to me. I learned everything else in the course. However, here is a list of some aspects I really got to understand:

	- The CTk libaray & having widgets do/work with other aspects of the program
	- Classes and their structure
	- Organizing code (this helped tremendously rather than putting everything in project.py)
		- Using code from different files that I created (The "*" for a wildcard feels nice. Not too sure if there's better ways to do it rather than just importing a bunch of stuff manually)
		- Working with multiple directories in the root for better organization (I know it's not necessary for this type of program, but I like it.)

#### Obstacles:
Besides learning the basics of CTk and getting familiar with Python, I did come across some obstacles that took me some time to understand and get around:

	- Having CTk frames & widgets interact and change each other across files.
		- Before, I did not have anything in classes or frames. I simply put the widgets within the file directly. So, having a main file run the main window with everything along with a seperate GUI file that also had widgets didn't really work out well and when I tried it got very messy very quickly. 
	- Layout Managers.
		- Was confused at first when looking at the documentation and seeing other examples online of putting widgets within the window in different ways. Found out that there are different managers (grid, pack, and place) that can be used for different reasons. I used place since I wanted the widgets in specific parts of the window. 

#### Learning Next:
	- Get better at creating a more intuitive/cleaner/modern looking UI.
	- Taking on a bigger challenge.




