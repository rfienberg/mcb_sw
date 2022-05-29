from globals import *
import tkinter as tk
import telemetry

MY_FONT = ('Calibri', 28)
MY_FG = 'black'


ShutDownRequested = False


###############################################################################
###############################################################################
def create_screen(frame):
    global this_screen

    # Create and place the Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    sd = create_shutdown_widget(this_screen)

    # Place the Widgets
    sd.grid(row=0, column=0, sticky='nsew')

    return this_screen


###############################################################################
###############################################################################
def show_screen():
    global this_screen
    this_screen.tkraise()
    global ShutDownRequested
    ShutDownRequested = True


###############################################################################
###############################################################################
def isShutDownRequested():
    global ShutDownRequested

    # If the latest telemetry indicates a shut-down request...
    if (telemetry.getShutdownStatus() == "Shutting-down"):
        ShutDownRequested = True

    return ShutDownRequested


###############################################################################
###############################################################################
def create_shutdown_widget(frame):
    this_frame = tk.Frame(frame)

    my_label = tk.Label(this_frame)
    my_label.configure(font=MY_FONT, fg=MY_FG)
    my_label.configure(text="Shutting down! Please wait...")
    my_label.grid(row=0, column=0, padx=20, pady=40)

    return this_frame


