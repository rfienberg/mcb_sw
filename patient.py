from globals import *
from os.path import exists
import tkinter as tk
from PIL import ImageTk, Image
import screens
import analyze

KEY_FONT = ('Calibri', 14)


###############################################################################
# Creates the PATIENT setup screen
###############################################################################
def create_setup_screen(frame):
    global this_screen, kb_lower, kb_upper

    # Open up the image files and size them correctly
    global ok_btn_icon
    ok_btn_img = Image.open("Icons/blue_ok_btn.png").resize((150,50), Image.ANTIALIAS)
    ok_btn_icon = ImageTk.PhotoImage(ok_btn_img)
    global cancel_btn_icon
    cancel_btn_img = Image.open("Icons/blue_cancel_btn.png").resize((150,50), Image.ANTIALIAS)
    cancel_btn_icon = ImageTk.PhotoImage(cancel_btn_img)

    # Create the Frame for this screen
    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets for this screen
    top_line = create_top_line(this_screen)
    pat_name = create_patient_name(this_screen)
    kb_upper = create_keyboard(this_screen, True)
    kb_lower = create_keyboard(this_screen, False)
    bot_line = create_bottom_line(this_screen)

    # Place the Widgets into the Frame
    top_line.grid(row=0, column=0, sticky='nw')
    pat_name.grid(row=1, column=0, pady=10, sticky='w')
    kb_upper.grid(row=2, column=0, pady=10)
    kb_lower.grid(row=2, column=0, pady=10)
    bot_line.grid(row=3, column=0, pady=10)

    return this_screen


###############################################################################
# Shows the PATIENT setup screen
###############################################################################
def show_setup_screen():
    global this_screen
    this_screen.tkraise()
    show_keyboard('upper')


###############################################################################
# Shows the specified type (upper/lower) of keyboard
###############################################################################
def show_keyboard(type):
    global use_caps

    patient_name_entry.index(tk.INSERT)
    patient_name_entry.focus()

    if (type == 'upper'):
        use_caps = True
        kb_upper.tkraise()
    else:
        use_caps = False
        kb_lower.tkraise()


###############################################################################
# Handles the OK button press event
###############################################################################
def on_ok_press():
    # Chirp
    screens.play_key_tone()

    # Pull the new patient's name from the entry box
    patient_name = patient_name_entry.get()
    patient_name_entry.delete(0, tk.END)

    # If it has at least one character filled in...
    if (len(patient_name) > 0):

        # Create a new Patient Log File with this name in it
        create_log_file(patient_name)

        # Create a new ANALYZE Log File
        analyze.create_log_file(patient_name)

        # Go back to the main SETUP screen
        screens.show_setup_main_screen()


###############################################################################
# Handles the CANCEL button press event
###############################################################################
def on_cancel_press():
    screens.play_key_tone()
    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def on_key_press(key):
    global use_caps

    screens.play_key_tone()
    keytext = key.lower()

    if (keytext == 'back'):
        my_text = patient_name_entry.get()
        patient_name_entry.delete(len(my_text)-1, tk.END)

    elif (keytext == 'space'):
        patient_name_entry.insert(tk.END, ' ')
        show_keyboard('upper')

    elif (keytext == 'shift'):
        if (use_caps == True):
            show_keyboard('lower')
        else:
            show_keyboard('upper')

    else:
        patient_name_entry.insert(tk.END, key)
        show_keyboard('lower')


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame)
    title_label.configure(font=LG_FONT, fg=SETUP_COLOR)
    title_label.configure(text="New Patient")

    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_patient_name(frame):
    global patient_name_entry

    this_frame = tk.Frame(frame)

    patient_name_label = tk.Label(this_frame)
    patient_name_label.configure(font=SM_FONT, fg=SETUP_COLOR)
    patient_name_label.configure(text="Patient Name: ")

    patient_name_entry = tk.Entry(this_frame)
    patient_name_entry.configure(font=SM_FONT, fg=SETUP_COLOR)
    patient_name_entry.configure(width=30, takefocus=1)

    patient_name_label.grid(row=0, column=0, padx=10)
    patient_name_entry.grid(row=0, column=1)

    return this_frame


###############################################################################
###############################################################################
def create_keyboard(frame, uppercase=False):
    # Define the keyboard keys
    keys = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 
    'z', 'x', 'c', 'v', 'b', 'n', 'm', '-', '.', 
    'back', 'space', 'shift'
    ]

    this_frame = tk.Frame(frame, padx=40)

    my_row = 0
    my_col = 0

    for key in keys:
        if (uppercase == True):
            key = key.upper()

        command = lambda x=key: on_key_press(x)

        my_relief = tk.RAISED
        my_bg = '#DAE3F3'

        if (my_row == 0):
            my_row = 1
            my_col = 0
            my_span = 2
            my_width = 3
        elif ((my_row == 1) and (my_col >= 20)):
            my_row = 2
            my_col = 1
            my_span = 2
            my_width = 3
        elif ((my_row == 2) and (my_col >= 18)):
            my_row = 3
            my_col = 1
            my_span = 2
            my_width = 3
        elif (key.lower() == 'back'):
            my_row = 4
            my_col = 1
            my_span = 4
            my_width = 9
        elif (key.lower() == 'space'):
            my_row = 4
            my_col = 5
            my_span = 10
            my_width = 27
        elif (key.lower() == 'shift'):
            my_row = 4
            my_col = 15
            my_span = 4
            my_width = 9
            if (uppercase == True):
                my_bg = '#8EA9DA'

        tk.Button(this_frame, 
                  text=key, 
                  font=KEY_FONT, 
                  width=my_width, 
                  bg=my_bg, 
                  fg='#294A52', 
                  relief=my_relief, 
                  overrelief=tk.SUNKEN, 
                  takefocus=0, 
                  bd=4, 
                  command=command).grid(row=my_row, column=my_col, columnspan=my_span)

        my_col += my_span

    return this_frame


###############################################################################
###############################################################################
def create_bottom_line(frame):
    this_frame = tk.Frame(frame)

    ok_button = tk.Button(this_frame)
    ok_button.configure(image=ok_btn_icon, borderwidth=0)
    ok_button.configure(command=on_ok_press)

    spacer_label = tk.Label(this_frame)

    cancel_button = tk.Button(this_frame)
    cancel_button.configure(image=cancel_btn_icon, borderwidth=0)
    cancel_button.configure(command=on_cancel_press)

    ok_button.grid(    row=0, column=0, pady=10)
    spacer_label.grid( row=0, column=1, padx=80)
    cancel_button.grid(row=0, column=2, pady=10)

    return this_frame


###############################################################################
###############################################################################
def get_patient_name():
    name = "UNKNOWN PATIENT"

    # Open (or create) the Patient Log File
    file = open_log_file("r")

    # Read the top line (i.e. Patient's Name)
    file.seek(0)
    line = file.readline()
    file.close()

    # If the Patient's Name is successfully found...
    if ('Patient:' in line):
        name = (line.split(':')[1]).rstrip()

    # If the Patient's Name is not found...
    else:
        create_log_file(name)

    return name


###############################################################################
# Creates a new Patient Log File for the specified name
###############################################################################
def create_log_file(name):
    print("Created new patient log file: " + PATIENT_FILE + " for " + name)
    file = open(PATIENT_FILE, "w")
    file.write("Patient: " + name + "\n")
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
    file = open(PATIENT_FILE, "a")
    file.write(line)
    file.close()


