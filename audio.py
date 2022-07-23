from globals import *
import tkinter as tk

import screens
import time
import mcb_config

# Temporary Audio Settings
ConfigKeyPressToneEnabled = True
ConfigWarningToneEnabled = True
ConfigAlarmToneEnabled = True


###############################################################################
###############################################################################
def pull_audio_settings():
    global ConfigKeyPressToneEnabled, ConfigWarningToneEnabled, ConfigAlarmToneEnabled

    ConfigKeyPressToneEnabled = mcb_config.getPlayKeyPressTone()
    ConfigWarningToneEnabled  = mcb_config.getPlayWarningTone()
    ConfigAlarmToneEnabled    = mcb_config.getPlayAlarmTone()


###############################################################################
###############################################################################
def push_audio_settings():
    global ConfigKeyPressToneEnabled, ConfigWarningToneEnabled, ConfigAlarmToneEnabled

    mcb_config.setPlayKeyPressTone(ConfigKeyPressToneEnabled)
    mcb_config.setPlayWarningTone(ConfigWarningToneEnabled)
    mcb_config.setPlayAlarmTone(ConfigAlarmToneEnabled)

    # Write the new CONFIG values to file
    mcb_config.writeConfigSettings()


###############################################################################
###############################################################################
def show_setup_screen():
    global this_screen

    # Pull the CONFIG file values into local settings
    pull_audio_settings()

    # Update the check boxes based on the local settings
    update_checkboxes()

    this_screen.tkraise()


###############################################################################
###############################################################################
def upon_back_press():
    # Chirp
    screens.play_key_tone()

    # Pull the CONFIG file values into local settings
    pull_audio_settings()

    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def upon_ok_press():
    # Chirp
    screens.play_key_tone()

    # Push local settings to CONFIG file
    push_audio_settings()

    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def opt1_select():
    global ConfigKeyPressToneEnabled

    # Chirp
    screens.play_key_tone()

    if (ConfigKeyPressToneEnabled):
        ConfigKeyPressToneEnabled = False
    else:
        ConfigKeyPressToneEnabled = True

    update_checkboxes()


###############################################################################
###############################################################################
def opt2_select():
    global ConfigWarningToneEnabled

    # Chirp
    screens.play_key_tone()

    if (ConfigWarningToneEnabled):
        ConfigWarningToneEnabled = False
    else:
        ConfigWarningToneEnabled = True

    update_checkboxes()


###############################################################################
###############################################################################
def opt3_select():
    global ConfigAlarmToneEnabled

    # Chirp
    screens.play_key_tone()

    if (ConfigAlarmToneEnabled):
        ConfigAlarmToneEnabled = False
    else:
        ConfigAlarmToneEnabled = True

    update_checkboxes()


###############################################################################
###############################################################################
def update_checkboxes():
    global ConfigKeyPressToneEnabled, ConfigWarningToneEnabled, ConfigAlarmToneEnabled

    if (ConfigKeyPressToneEnabled):
        opt1_cb.configure(image=screens.checkbox_yes_icon)
    else:
        opt1_cb.configure(image=screens.checkbox_no_icon)

    if (ConfigWarningToneEnabled):
        opt2_cb.configure(image=screens.checkbox_yes_icon)
    else:
        opt2_cb.configure(image=screens.checkbox_no_icon)

    if (ConfigAlarmToneEnabled):
        opt3_cb.configure(image=screens.checkbox_yes_icon)
    else:
        opt3_cb.configure(image=screens.checkbox_no_icon)


###############################################################################
###############################################################################
def create_setup_screen(frame):
    global this_screen

    # Create and place this Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the screen Widgets
    top_line = create_top_line(this_screen)
    mid_line = create_checkboxes(this_screen)
    bot_line = create_bottom_line(this_screen)

    # Place the Widgets onto the screen
    top_line.grid(row=0, column=0, sticky='nw')
    mid_line.grid(row=1, column=0, padx=40, pady=20, sticky='w')
    bot_line.grid(row=3, column=0, padx=40, sticky='w')

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    b1 = tk.Button(this_frame)
    b1.configure(image=screens.blu_gohome_btn_icon, borderwidth=0)
    b1.configure(command=upon_back_press)

    l1 = tk.Label(this_frame)
    l1.configure(font=LG_FONT, fg=SETUP_COLOR)
    l1.configure(text="Audio Settings")

    b1.grid(row=0, column=0, padx=5, pady=10)
    l1.grid(row=0, column=1, padx=20)

    return this_frame


###############################################################################
###############################################################################
def create_checkboxes(frame):
    global opt1_cb, opt2_cb, opt3_cb

    this_frame = tk.Frame(frame)

    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f3 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, sticky='w')
    f2.grid(row=1, column=0, sticky='w')
    f3.grid(row=2, column=0, sticky='w')

    opt1_cb = tk.Button(f1)
    opt1_cb.configure(relief="flat", command=opt1_select)
    opt1_lbl = tk.Label(f1)
    opt1_lbl.configure(font=MD_FONT, fg=SETUP_COLOR)
    opt1_lbl.configure(text="Sound a tone upon any key press")
    opt1_cb.grid( row=0, column=0)
    opt1_lbl.grid(row=0, column=1, padx=10)

    opt2_cb = tk.Button(f2)
    opt2_cb.configure(relief="flat", command=opt2_select)
    opt2_lbl = tk.Label(f2)
    opt2_lbl.configure(font=MD_FONT, fg=SETUP_COLOR)
    opt2_lbl.configure(text="Play a sound upon any warning")
    opt2_cb.grid(row=1, column=0)
    opt2_lbl.grid(row=1, column=1, padx=10)

    opt3_cb = tk.Button(f3)
    opt3_cb.configure(relief="flat", command=opt3_select)
    opt3_lbl = tk.Label(f3)
    opt3_lbl.configure(font=MD_FONT, fg=SETUP_COLOR)
    opt3_lbl.configure(text="Play a sound upon any alarm condition")
    opt3_cb.grid(row=2, column=0)
    opt3_lbl.grid(row=2, column=1, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_bottom_line(frame):
    this_frame = tk.Frame(frame)

    b1 = tk.Button(this_frame)
    b1.configure(image=screens.blu_ok_btn_icon, borderwidth=0)
    b1.configure(command=upon_ok_press)
    b1.grid(row=0, column=0)

    return this_frame


