from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens
import patientlog

BIG_FONT = ("Georgia", 30)
BIG_FG = 'purple'
MY_FONT = ('Calibri', 18)
MY_FG = '#0070C0'
KEY_FONT = ('Calibri', 14)


###############################################################################
###############################################################################
def create_screen(frame):
    global this_screen, kb_lower, kb_upper

    this_screen = tk.LabelFrame(frame, text="New Patient Screen")
    this_screen.grid(row=0, column=0, sticky='nsew')

    top = create_top_line(this_screen)
    top.grid(row=0, column=0, sticky='nw')

    pat = create_patient_name(this_screen)
    pat.grid(row=1, column=0, sticky='w', pady=10)

    kb_lower = create_keyboard(this_screen, False)
    kb_lower.grid(row=2, column=0)
    kb_upper = create_keyboard(this_screen, True)
    kb_upper.grid(row=2, column=0)

    bot = create_bottom_line(this_screen)
    bot.grid(row=10, column=0)

    return this_screen


###############################################################################
###############################################################################
def show_screen():
    global this_screen
    show_keyboard('upper')
    this_screen.tkraise()


###############################################################################
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
###############################################################################
def on_ok_press():
    screens.play_key_tone()
    save_and_return()


###############################################################################
###############################################################################
def on_cancel_press():
    screens.play_key_tone()
    screens.show_setup_screen()


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
def save_and_return():
    patient_name = patient_name_entry.get()
    print(patient_name)
    patient_name_entry.delete(0, tk.END)
    patientlog.create(patient_name)
    screens.show_setup_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame, text="New Patient", font=BIG_FONT, fg=MY_FG)
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_patient_name(frame):
    global patient_name_entry

    this_frame = tk.Frame(frame)

    patient_name_label = tk.Label(this_frame, text="Patient Name: ", font=MY_FONT, fg=MY_FG)
    patient_name_label.grid(row=0, column=0, padx=10)

    patient_name_entry = tk.Entry(this_frame, 
                                  font=MY_FONT, 
                                  fg=MY_FG, 
                                  takefocus=1, 
                                  width=30)
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

    this_frame = tk.LabelFrame(frame, padx=40)
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
            my_width = 8
        elif (key.lower() == 'space'):
            my_row = 4
            my_col = 5
            my_span = 10
            my_width = 21
        elif (key.lower() == 'shift'):
            my_row = 4
            my_col = 15
            my_span = 4
            my_width = 8
            if (uppercase == True):
                my_bg = '#8EA9DA'

        tk.Button(this_frame, 
                  text=key, 
                  font=KEY_FONT, 
                  width=my_width, 
                  bg=my_bg, 
                  #activebackground="white", 
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

    global ok_btn_icon
    ok_btn_img = Image.open("Icons/ok_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    ok_btn_icon = ImageTk.PhotoImage(ok_btn_img)
    ok_button = tk.Button(this_frame)
    ok_button.configure(image=ok_btn_icon, borderwidth=0)
    ok_button.configure(command=on_ok_press)
    ok_button.grid(row=0, column=0, padx=40, sticky='w')

    tk.Label(this_frame).grid(row=0, column=1, padx=100)

    global cancel_btn_icon
    cancel_btn_img = Image.open("Icons/cancel_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    cancel_btn_icon = ImageTk.PhotoImage(cancel_btn_img)
    cancel_button = tk.Button(this_frame)
    cancel_button.configure(image=cancel_btn_icon, borderwidth=0)
    cancel_button.configure(command=on_cancel_press)
    cancel_button.grid(row=0, column=2, padx=40)

    return this_frame


