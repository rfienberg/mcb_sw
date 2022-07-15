from globals import *
import tkinter as tk

import titlebar
import screens
import statusbar

import alarms


###############################################################################
# Starts the GUI thread
###############################################################################
def startup():
    global window

    # Create the Main GUI Window
    window = tk.Tk()

    # Describe the Main Window's geometry
    window.geometry('800x480')
    window.overrideredirect(1)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=98)
    window.rowconfigure(2, weight=1)

    # Create the three Main Frames
    tb = titlebar.create_bar(window)
    sa = screens.create_screens(window)
    sb = statusbar.create_bar(window)

    # Start periodic screen updates
    start_screen_updates(window)


###############################################################################
###############################################################################
def start_screen_updates(window):
    alarms.start_periodic_popup_checks(window)


###############################################################################
# Runs the GUI main loop
###############################################################################
def mainloop():
    window.mainloop()

