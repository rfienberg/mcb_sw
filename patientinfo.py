from globals import *
from os.path import exists
import tkinter as tk
import screens
import analyze

KEY_FONT = ('Calibri', 14)


###############################################################################
# Shows the PATIENT INFO screen
###############################################################################
def show_setup_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
# Handles the OK button press event
###############################################################################
def upon_ok_press():
    # Chirp
    screens.play_key_tone()


###############################################################################
# Handles the CANCEL button press event
###############################################################################
def upon_cancel_press():
    # Chirp
    screens.play_key_tone()


###############################################################################
# Creates the PATIENT INFO screen
###############################################################################
def create_info_screen(frame):
    global this_screen

    # Create the Frame for this screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets for this screen
    top_line = create_top_line(this_screen)

    # Place the Widgets into the Frame
    top_line.grid(row=0, column=0, sticky='nw')

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=LG_FONT, fg=SETUP_COLOR)
    l1.configure(text="Patient Info")

    l1.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def get_patient_name():
    name = "UNKNOWN PATIENT"

    # Open (or create) the Patient Log File
    file = open_log_file("r")

    # Read the 1st line (i.e. Patient's Name)
    file.seek(0)
    line = file.readline()
    file.close()

    # If the 1st line is successfully found...
    if ('Created' in line):
        # Extract the patient's name string from the 1st line
        name = (line.split(':')[4]).rstrip()

    # If the Patient's Name is not found...
    else:
        create_log_file(name)

    return name


###############################################################################
# Creates a new Patient Log File for the specified name
###############################################################################
def create_log_file(name):
    # Create the new patient log file
    file = open(PATIENT_FILE, "w")

    # Build the 1st log line
    log_line = getDateTimeStamp()
    log_line = log_line + "Created patient log file for: "
    log_line = log_line + name
    print(log_line)

    # Write the 1st line and exit
    file.write(log_line + "\n")
    file.close()


###############################################################################
###############################################################################
def open_log_file(mode="a"):
    if (not exists(PATIENT_FILE)):
        create_log_file("UNKNOWN PATIENT")

    file = open(PATIENT_FILE, mode)
    return file


###############################################################################
###############################################################################
def write_log_line(line):
    file = open_log_file("a")
    file.write(line + "\n")
    file.close()


