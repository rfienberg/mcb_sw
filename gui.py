from globals import *
import tkinter as tk

import telemetry
import shutdown

import screens
import titlebar
import statusscreen
import statusbar


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
    tb = titlebar.create(window)
    sa = screens.create(window)
    sb = statusbar.create(window)

    # Start periodic screen updates
    periodic_update()


###############################################################################
# Updates the GUI screens once every second
###############################################################################
def periodic_update():
    # Get the latest Telemetry
    telem = telemetry.getLatestTelemetry()

    # Update the Title Bar widgets
    titlebar.update()

    # As long as we have new Telemetry...
    if (len(telem) > 0):

        # Update the Status Screen widgets
        statusscreen.update()

        # Update the Status Bar widgets
        statusbar.update()

    # Check for a new shut-down request...
    if (shutdown.isShutDownRequested()):
        screens.show_shut_down_screen()

    # As long as we are not shutting down...
    else:
        # After 1 second, perform another update
        window.after(1000, periodic_update)


###############################################################################
# Runs the GUI main loop
###############################################################################
def mainloop():
    window.mainloop()

