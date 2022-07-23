###############################################################################
# This module supports the TANK LIGHTS manual control
# The TANK LIGHTS can be commanded to go either: 
#     OFF, ON, or AUTO 
###############################################################################
from globals import *
import tkinter as tk

import screens
import lights


###############################################################################
# Shows the screen for tank light CONTROL
###############################################################################
def show_control_screen():
    # Bring up the lights CONTROL screen
    global control_screen
    control_screen.tkraise()

    # Command the DCB to turn the Tank Lights to ON
    lights.commandLightsOn()


###############################################################################
# Exits back to the CONTROL main screen
###############################################################################
def upon_ok_press():
    # Chirp
    screens.play_key_tone()

    # Command the DCB to turn the Tank Lights back to AUTO setting
    lights.commandLightsAuto()

    # Go back to display the MAIN screen 
    screens.show_control_main_screen()


##############################################################################
# Creates the screen for tank light CONTROL
###############################################################################
def create_control_screen(frame):
    global control_screen

    # Create and place the Screen
    control_screen = tk.Frame(frame)
    control_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top_line = create_top_line(control_screen)
    message1 = create_bot_line(control_screen)

    # Place the Widgets
    top_line.grid(row=0, column=0, sticky='nw')
    message1.grid(row=1, column=0, padx=40, pady=20, sticky='nsew')

    return control_screen


###############################################################################
# Creates the tank light CONTROL screen top line
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=LG_FONT, fg=CONTROL_COLOR)
    l1.configure(text="Control Lights:")
    l1.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
# Creates the tank light CONTROL screen lights on widget
###############################################################################
def create_bot_line(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=MD_FONT, fg=CONTROL_COLOR)
    l1.configure(text="Tank Lights are now ON")

    l2 = tk.Label(this_frame)
    l2.configure(font=MD_FONT, fg=CONTROL_COLOR)
    l2.configure(text="Press OK when done...")

    b1 = tk.Button(this_frame)
    b1.configure(image=screens.grn_ok_btn_icon, borderwidth=0)
    b1.configure(command=upon_ok_press)

    l1.grid(row=0, column=0, padx=20, pady=20, sticky='ew')
    l2.grid(row=1, column=0, padx=20, sticky='ew')
    b1.grid(row=2, column=0, pady=30)

    return this_frame


