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
def on_lights_press():
    screens.play_key_tone()
    screens.show_control_lights_screen()


###############################################################################
###############################################################################
def on_cartridge_press():
    screens.play_key_tone()
    screens.show_control_cartridge_screen()


###############################################################################
###############################################################################
def on_shutdown_press():
    screens.play_key_tone()
    screens.show_verify_shutdown_screen()


###############################################################################
###############################################################################
def create_main_screen(frame):
    global this_screen

    # Create and place the Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top_line = create_top_line(this_screen)
    buttons  = create_control_buttons(this_screen)

    # Place the Widgets
    top_line.grid(row=0, column=0, sticky='w')
    buttons.grid( row=1, column=0, padx=40, pady=20, sticky='w')

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the widgets
    l1 = tk.Label(this_frame, text="Control Options")
    b1 = tk.Button(this_frame)
    l1.configure(font=LG_FONT, fg=CONTROL_COLOR)
    b1.configure(image=screens.grn_gohome_btn_icon, borderwidth=0)
    b1.configure(command=on_home_press)

    b1.grid(row=0, column=0, padx=5, pady=10)
    l1.grid(row=0, column=1, padx=80)

    return this_frame


###############################################################################
###############################################################################
def create_control_buttons(frame):
    this_frame = tk.Frame(frame)

    lits_btn = create_lights_button(this_frame)
    cart_btn = create_cartridge_button(this_frame)
    shut_btn = create_shutdown_button(this_frame)
    lits_btn.grid(row=1, column=0, padx=20, pady=5, sticky='n')
    cart_btn.grid(row=1, column=1, padx=20, pady=5, sticky='n')
    shut_btn.grid(row=1, column=2, padx=20, pady=5, sticky='n')

    return this_frame


###############################################################################
###############################################################################
def create_lights_button(frame):
    this_frame = tk.Frame(frame)

    this_btn_button = tk.Button(this_frame, image=screens.grn_bulb_icon, borderwidth=0)
    this_btn_button.configure(command=on_lights_press)
    this_btn_button.grid(row=0, column=0)
    this_btn_label = tk.Label(this_frame, text="Turn On\nLights")
    this_btn_label.configure(font=SM_FONT, fg=CONTROL_COLOR)
    this_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_cartridge_button(frame):
    this_frame = tk.Frame(frame)

    this_btn_button = tk.Button(this_frame, image=screens.grn_cartridge_icon, borderwidth=0)
    this_btn_button.configure(command=on_cartridge_press)
    this_btn_button.grid(row=0, column=0)
    this_btn_label = tk.Label(this_frame, text="Remove\nCartridge")
    this_btn_label.configure(font=SM_FONT, fg=CONTROL_COLOR)
    this_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_shutdown_button(frame):
    this_frame = tk.Frame(frame)

    this_btn_button = tk.Button(this_frame, image=screens.grn_power_btn_icon, borderwidth=0)
    this_btn_button.configure(command=on_shutdown_press)
    this_btn_button.grid(row=0, column=0)
    this_btn_label = tk.Label(this_frame, text="Shutdown\nUnit")
    this_btn_label.configure(font=SM_FONT, fg=CONTROL_COLOR)
    this_btn_label.grid(row=1, column=0)

    return this_frame


