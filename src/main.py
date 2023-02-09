import os
import customtkinter
import tkinter
from game_settings import *
from PIL import Image, ImageTk
from sys import argv

# Set the current directory as the directory of the executable.
os.chdir(os.path.split(argv[1])[0])

# Paths

homedir = os.path.expanduser('~')
apexpath = fr'{homedir}\Saved Games\Respawn\Apex\local\videoconfig.txt'

valpath = fr'{homedir}\AppData\Local\VALORANT\Saved\Config\\'
valkey = fr'{homedir}\AppData\Local\VALORANT\Saved\Config\Windows\RiotLocalMachine.ini'

fortpath = fr'{homedir}\AppData\Local\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini'

ow2path_onedrive = fr'{homedir}\OneDrive\Documents\Overwatch\Settings\Settings_v0.ini'
ow2path_local = fr'{homedir}\Documents\Overwatch\Settings\Settings_v0.ini'

# Checking if the Paths Exist

installed = []

if os.path.exists(apexpath):
    installed.append('Apex')

if os.path.exists(valkey):
    installed.append('Valorant')

if os.path.exists(fortpath):
    installed.append('Fortnite')

if os.path.exists(ow2path_onedrive):
    ow2path = ow2path_onedrive
    installed.append('Overwatch 2')
elif os.path.exists(ow2path_local):
    ow2path = ow2path_local
    installed.append('Overwatch 2')

# GUI


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title('Butter: Automatic Game Optimiser')
root.geometry('450x350')

ico = Image.open('assets/logo.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# Frames

frame = customtkinter.CTkFrame(
    master=root, width=300, height=50, corner_radius=10)
frame.pack(pady=10, padx=20, fill="x")

frame2 = customtkinter.CTkFrame(
    master=root, width=300, height=400, corner_radius=10)
frame2.pack(pady=10, padx=20, fill="both", expand=True)

# Window


def optimise():
    if chosen[(len(chosen))-1] == 'Apex':
        apex(apexpath)
    elif chosen[(len(chosen))-1] == 'Valorant':
        val(valpath, valkey)
    elif chosen[(len(chosen))-1] == 'Fortnite':
        fortnite(fortpath)
    elif chosen[(len(chosen))-1] == 'Overwatch 2':
        overwatch(ow2path)

# Define


chosen = []


def optionmenu_callback(choice):
    chosen.append(choice)


# Image

my_image = customtkinter.CTkImage(Image.open(r"assets\butter.png"),
                                  size=(250, 60))

button1 = customtkinter.CTkButton(frame, text='', image=my_image, fg_color='#F8D038',
                                  hover_color='#F8D038', border_color='#e5e5e5', anchor=tkinter.CENTER)
button1.pack(padx=20, pady=60, anchor=tkinter.CENTER)

# Dropdown

selected = customtkinter.StringVar(value='No Games')
if installed != []:
    selected = customtkinter.StringVar(value='Select Game')

combobox = customtkinter.CTkComboBox(
    master=frame2, values=installed, command=optionmenu_callback, variable=selected)
combobox.pack(padx=20, pady=10)

# Button

button = customtkinter.CTkButton(
    master=frame2, text="Optimise", fg_color='#3F3F3F', hover_color='#2B2B2B', command=optimise)
button.pack(padx=20, pady=10)

# Run

root.mainloop()
