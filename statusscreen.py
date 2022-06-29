from globals import *
import tkinter as tk
import screens


###############################################################################
###############################################################################
def show_main_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
###############################################################################
def on_home_press():
    screens.play_key_tone()
    screens.show_home_screen()


###############################################################################
###############################################################################
def on_tanks_press():
    screens.play_key_tone()
    screens.show_tank_status_screen()


###############################################################################
###############################################################################
def on_lights_press():
    screens.play_key_tone()


###############################################################################
###############################################################################
def create_main_screen(frame):
    global this_screen

    # Create and place the Screen
    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top_line = create_top_line(this_screen)
    buttons  = create_status_buttons(this_screen)

    # Place the Widgets
    top_line.grid(row=0, column=0, sticky='w')
    buttons.grid( row=1, column=0, padx=40, pady=20, sticky='w')

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the widgets
    l1 = tk.Label(this_frame, text="Status Options")
    b1 = tk.Button(this_frame)
    l1.configure(font=LG_FONT, fg=STATUS_COLOR)
    b1.configure(image=screens.pur_gohome_btn_icon, borderwidth=0)
    b1.configure(command=on_home_press)

    b1.grid(row=0, column=0, padx=5, pady=10)
    l1.grid(row=0, column=1, padx=80)

    return this_frame


###############################################################################
###############################################################################
def create_status_buttons(frame):
    this_frame = tk.Frame(frame)

    b1 = create_tanks_button(this_frame)
    b2 = create_lights_button(this_frame)

    b1.grid(row=1, column=0, padx=20, pady=5, sticky='n')
    b2.grid(row=1, column=1, padx=20, pady=5, sticky='n')

    return this_frame


###############################################################################
###############################################################################
def create_tanks_button(frame):
    this_frame = tk.Frame(frame)

    b1 = tk.Button(this_frame, image=screens.tank_levels_icon, borderwidth=0)
    b1.configure(command=on_tanks_press)
    b1.grid(row=0, column=0)
    l1 = tk.Label(this_frame, text="Tank \nLevels")
    l1.configure(font=SM_FONT, fg=STATUS_COLOR)
    l1.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_lights_button(frame):
    this_frame = tk.Frame(frame)

    b1 = tk.Button(this_frame, image=screens.room_lights_icon, borderwidth=0)
    b1.configure(command=on_lights_press)
    b1.grid(row=0, column=0)
    l1 = tk.Label(this_frame, text="Room \nLights")
    l1.configure(font=SM_FONT, fg=STATUS_COLOR)
    l1.grid(row=1, column=0)

    return this_frame


