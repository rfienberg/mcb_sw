from globals import *
import tkinter as tk

import screens

MY_BG = 'red'
MY_FG = 'white'
MY_FONT = ('Calibri', 14)


###############################################################################
###############################################################################
def show():
    global this_screen
    this_screen.tkraise()

###############################################################################
###############################################################################
def on_ok_press():
    this_screen.lower()


###############################################################################
###############################################################################
def set_tank_message(message):
    pass


###############################################################################
###############################################################################
def create(frame):
    global this_screen, message

    this_screen = tk.LabelFrame(frame, text="Alarm Screen")
    this_screen.configure(bg=MY_BG)
    this_screen.grid(row=0, column=0, sticky='nsew')

    message = tk.Label(this_screen)
    message.configure(font=MY_FONT, fg=MY_FG, bg=MY_BG)
    message.configure(text="Left Tank Full")
    message.grid(row=0, column=0, columnspan=10)

    b1 = tk.Button(this_screen)
    b1.configure(text="OK")
    b1.configure(command=on_ok_press)
    b1.grid(row=1, column=0)

    return this_screen
