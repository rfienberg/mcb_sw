from globals import *
import tkinter as tk
import screens
import time
if (RUN_ON_CM4):
    import RPi.GPIO as GPIO
import mcb_config

BIG_FONT = ("Georgia", 30)

# Temporary Audio Settings
ConfigKeyPressToneEnabled = True
ConfigWarningToneEnabled = True
ConfigAlarmToneEnabled = True


###############################################################################
###############################################################################
def play_key_tone():
    global this_screen

    if (ConfigKeyPressToneEnabled):
        if (RUN_ON_CM4):
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(12, GPIO.OUT)
            pwm = GPIO.PWM(12, 2500)
            pwm.start(25)

        time.sleep(.100)

        if (RUN_ON_CM4):
            pwm.stop()
            #GPIO.cleanup()


###############################################################################
###############################################################################
def create_setup_screen(frame):
    global this_screen

    # Create and place this Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the screen Widgets
    top_frm = create_top_line(this_screen)
    mid_frm = create_checkboxes(this_screen)
    bot_frm = create_bottom_line(this_screen)

    # Place the Widgets onto the screen
    top_frm.grid(row=0, column=0, sticky='nw')
    mid_frm.grid(row=1, column=0, padx=40, pady=30, sticky='w')
    bot_frm.grid(row=2, column=0, padx=40, pady=30, sticky='w')

    return this_screen


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
def on_cancel_press():
    # Chirp
    screens.play_key_tone()

    # Pull the CONFIG file values into local settings
    pull_audio_settings()

    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def on_ok_press():
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
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame)
    title_label.configure(font=LG_FONT, fg=SETUP_COLOR)
    title_label.configure(text="Audio Settings:")
    title_label.grid(row=0, column=0, padx=10)

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

    ok_button = tk.Button(this_frame)
    ok_button.configure(image=screens.blu_ok_btn_icon, borderwidth=0)
    ok_button.configure(command=on_ok_press)

    spacer_label = tk.Label(this_frame)

    cancel_button = tk.Button(this_frame)
    cancel_button.configure(image=screens.blu_cancel_btn_icon, borderwidth=0)
    cancel_button.configure(command=on_cancel_press)

    ok_button.grid(    row=0, column=0, pady=10)
    spacer_label.grid( row=0, column=1, padx=80)
    cancel_button.grid(row=0, column=2, pady=10)

    return this_frame


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


