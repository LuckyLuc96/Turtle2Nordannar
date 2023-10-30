## Made by Judgefae and a sprinkle of ChatGPT <3
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()


# You'll want to make changes to this to fit your addon. Find the line
# or lines that will need to be changed and subtract by -1. The program
# counts the first line starting at 0. For the aux-addon I need to change 
# line 3 for example.

# Put your addon's lua file name here to help guide the user to the file path they need to select
Addonlua = "aux-addon.lua"
lines_to_modify = [2] 

print("Go to your Turtle WoW folder and follow this path: WTF > Account > Account name > SavedVariables and click on ", Addonlua)
file_path = filedialog.askopenfilename(title="Select" + Addonlua + " in the WTF saved variables folder.")

if not file_path:
    print("No file selected. Exiting.")
    exit(1)


with open(file_path, 'r') as file:
    lines = file.readlines()


for line_number in lines_to_modify:
    try:
        lines[line_number] = lines[line_number].replace("Turtle WoW", "Nordannar")
    except IndexError:
        print("Line {line_number} does not exist in the file.")


with open(file_path, 'w') as file:
        file.writelines(lines)
        print("Turtle's squished and replaced with Nordannar!")
