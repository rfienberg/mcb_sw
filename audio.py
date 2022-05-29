from globals import *
import mcb_config
import tkinter as tk
from PIL import ImageTk, Image
import screens
import time
if (RUN_ON_CM4):
    import RPi.GPIO as GPIO

BIG_FONT = ("Georgia", 30)
BIG_FG   = 'purple'
MY_FONT  = ('Calibri', 24)
MY_FG    = '#0070C0'

# Temporary Audio Settings
KeyPressToneEnabled = True
WarningToneEnabled = True
AlarmToneEnabled = True


###############################################################################
###############################################################################
def create_screen(frame):
    global this_screen

    # Open the images for this screen
    global ok_btn_icon
    ok_btn_img = Image.open("Icons/ok_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    ok_btn_icon = ImageTk.PhotoImage(ok_btn_img)
    global cancel_btn_icon
    cancel_btn_img = Image.open("Icons/cancel_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    cancel_btn_icon = ImageTk.PhotoImage(cancel_btn_img)
    global checkbox_yes_icon
    checkbox_yes_img = Image.open("Icons/checkbox_yes.png").resize((25,25), Image.ANTIALIAS)
    checkbox_yes_icon = ImageTk.PhotoImage(checkbox_yes_img)
    global checkbox_no_icon
    checkbox_no_img = Image.open("Icons/checkbox_no.png").resize((25,25), Image.ANTIALIAS)
    checkbox_no_icon = ImageTk.PhotoImage(checkbox_no_img)

    # Create and place this Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the screen Widgets
    top = create_top_line(this_screen)
    chk = create_checkboxes(this_screen)
    bot = create_bottom_line(this_screen)

    # Place the Widgets onto the screen
    top.grid(row=0, column=0, sticky='nw')
    chk.grid(row=1, column=0, padx=20, pady=30, sticky='w')
    bot.grid(row=10, column=0, pady=30, sticky='sw')

    # Update the check boxes based on the local settings
    update_checkboxes()

    return this_screen


###############################################################################
###############################################################################
def show_screen():
    global this_screen
    global KeyPressToneEnabled, WarningToneEnabled, AlarmToneEnabled

    # Pull the CONFIG file values into local settings
    pullSettings()

    # Update the check boxes based on the local settings
    update_checkboxes()

    this_screen.tkraise()


###############################################################################
###############################################################################
def play_key_tone():
    global this_screen

    if (KeyPressToneEnabled):
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
def key_tone_toggle():
    global KeyPressToneEnabled

    if (KeyPressToneEnabled):
        KeyPressToneEnabled = False
    else:
        KeyPressToneEnabled = True

    update_checkboxes()
    play_key_tone()


###############################################################################
###############################################################################
def warn_tone_toggle():
    global WarningToneEnabled

    if (WarningToneEnabled):
        WarningToneEnabled = False
    else:
        WarningToneEnabled = True

    update_checkboxes()
    play_key_tone()


###############################################################################
###############################################################################
def alarm_tone_toggle():
    global AlarmToneEnabled

    if (AlarmToneEnabled):
        AlarmToneEnabled = False
    else:
        AlarmToneEnabled = True

    update_checkboxes()
    play_key_tone()


###############################################################################
###############################################################################
def on_cancel_press():
    # Pull the CONFIG file values into local settings
    pullSettings()

    play_key_tone()
    screens.show_setup_screen()


###############################################################################
###############################################################################
def on_ok_press():
    # Push local settings to CONFIG file
    pushSettings()

    play_key_tone()
    screens.show_setup_screen()


###############################################################################
###############################################################################
def pullSettings():
    global KeyPressToneEnabled, WarningToneEnabled, AlarmToneEnabled

    if (mcb_config.getPlayKeyPressTone() == '1'):
        KeyPressToneEnabled = True
    else:
        KeyPressToneEnabled = False

    if (mcb_config.getPlayWarningTone() == '1'):
        WarningToneEnabled = True
    else:
        WarningToneEnabled = False

    if (mcb_config.getPlayAlarmTone() == '1'):
        AlarmToneEnabled = True
    else:
        AlarmToneEnabled = False


###############################################################################
###############################################################################
def pushSettings():
    global KeyPressToneEnabled, WarningToneEnabled, AlarmToneEnabled

    if (KeyPressToneEnabled):
        mcb_config.setPlayKeyPressTone('1')
    else:
        mcb_config.setPlayKeyPressTone('0')

    if (WarningToneEnabled):
        mcb_config.setPlayWarningTone('1')
    else:
        mcb_config.setPlayWarningTone('0')

    if (AlarmToneEnabled):
        mcb_config.setPlayAlarmTone('1')
    else:
        mcb_config.setPlayAlarmTone('0')

    # Write the new CONFIG values to file
    mcb_config.writeConfigSettings()


###############################################################################
###############################################################################
def update_checkboxes():
    global KeyPressToneEnabled, WarningToneEnabled, AlarmToneEnabled

    if (KeyPressToneEnabled):
        key_cb.configure(image=checkbox_yes_icon)
    else:
        key_cb.configure(image=checkbox_no_icon)

    if (WarningToneEnabled):
        warn_cb.configure(image=checkbox_yes_icon)
    else:
        warn_cb.configure(image=checkbox_no_icon)

    if (AlarmToneEnabled):
        alarm_cb.configure(image=checkbox_yes_icon)
    else:
        alarm_cb.configure(image=checkbox_no_icon)


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame)
    title_label.configure(text="Audio Settings:", font=BIG_FONT, fg=MY_FG)
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_checkboxes(frame):
    global key_cb, warn_cb, alarm_cb

    this_frame = tk.Frame(frame)

    key_cb = tk.Button(this_frame)
    key_cb.configure(relief="flat", command=key_tone_toggle)
    key_cb.grid(row=0, column=0)
    key_lbl = tk.Label(this_frame)
    key_lbl.configure(font=MY_FONT, fg=MY_FG)
    key_lbl.configure(text="Sound a tone upon any key press")
    key_lbl.grid(row=0, column=1, padx=10, sticky='w')

    warn_cb = tk.Button(this_frame)
    warn_cb.configure(relief="flat", command=warn_tone_toggle)
    warn_cb.grid(row=1, column=0)
    warn_lbl = tk.Label(this_frame)
    warn_lbl.configure(font=MY_FONT, fg=MY_FG)
    warn_lbl.configure(text="Play a sound upon any warning")
    warn_lbl.grid(row=1, column=1, padx=10, sticky='w')

    alarm_cb = tk.Button(this_frame)
    alarm_cb.configure(relief="flat", command=alarm_tone_toggle)
    alarm_cb.grid(row=2, column=0)
    alarm_lbl = tk.Label(this_frame)
    alarm_lbl.configure(font=MY_FONT, fg=MY_FG)
    alarm_lbl.configure(text="Play a sound upon any alarm condition")
    alarm_lbl.grid(row=2, column=1, padx=10, sticky='w')

    return this_frame


###############################################################################
###############################################################################
def create_bottom_line(frame):
    this_frame = tk.Frame(frame)

    ok_button = tk.Button(this_frame)
    ok_button.configure(image=ok_btn_icon, borderwidth=0)
    ok_button.configure(command=on_ok_press)
    ok_button.grid(row=0, column=0, padx=40, sticky='w')

    tk.Label(this_frame).grid(row=0, column=1, padx=100)

    cancel_button = tk.Button(this_frame)
    cancel_button.configure(image=cancel_btn_icon, borderwidth=0)
    cancel_button.configure(command=on_cancel_press)
    cancel_button.grid(row=0, column=2, padx=40)

    return this_frame


