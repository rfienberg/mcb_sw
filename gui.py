from globals import *
import tkinter as tk

import telemetry
import shutdown

import screens
import titlebar
import statusbar
import analyzescreen
import statusscreen


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
    periodic_update()


###############################################################################
# Updates the GUI screens once every second
###############################################################################
def periodic_update():
    # Get the latest Telemetry
    telem = telemetry.getLatestTelemetry()
    #print("telem = %s" % telem)

    # Update the Title Bar widgets
    titlebar.update_bar()

    # As long as we have new Telemetry...
    if (len(telem) > 0):

        # Update the Status Bar widgets
        statusbar.update_bar()

        # Update the Screen widgets
        screens.update_screens()

    # As long as we are not shutting down...
    if (shutdown.isShutDownRequested() == False):
        # After 1 second, perform another update
        window.after(1000, periodic_update)


###############################################################################
# Runs the GUI main loop
###############################################################################
def mainloop():
    window.mainloop()

