###############################################################################
# This module supports the TANK LIGHTS - both their manual control aspacts 
# and their automatic control aspects.
#
# The TANK LIGHTS can be commanded to go either: 
#     OFF, ON, or AUTO 
# The AUTO option can be configured, by the USER to either: 
#     OFF, ON, or ALS (controlled by ambient light sensor)
###############################################################################
from globals import *
import tkinter as tk
import screens
import dcb
import mcb_config


LIGHT_AUTO_OFF  = 'Off'
LIGHT_AUTO_ON   = 'On'
LIGHT_AUTO_ALS  = 'ALS'

# RAM copy of the Tank Lights AUTO configuration setting
ConfigLightsAuto = LIGHT_AUTO_OFF


###############################################################################
###############################################################################
def commandLightsOn():
    dcb.sendTankLightCommand('On')


###############################################################################
###############################################################################
def commandLightsAuto():
    dcb.sendTankLightCommand('Auto')


###############################################################################
###############################################################################
def pull_light_settings():
    # Read the saved CONFIG values from file
    global ConfigLightsAuto
    ConfigLightsAuto = mcb_config.getLightsAutoConfig()


###############################################################################
###############################################################################
def push_light_settings():
    # Write the new CONFIG values to file
    global ConfigLightsAuto
    mcb_config.setLightsAutoConfig(ConfigLightsAuto)
    mcb_config.writeConfigSettings()


###############################################################################
# Shows the screen for tank light SETUP/CONFIG
###############################################################################
def show_setup_screen():
    # Pull the CONFIG file values into local settings
    pull_light_settings()

    # Update the radio buttons based on the local settings
    update_radio_buttons()

    global setup_screen
    setup_screen.tkraise()


###############################################################################
# Handles a press of the CANCEL button
###############################################################################
def upon_cancel_press():
    # Chirp
    screens.play_key_tone()

    # Pull the CONFIG file values into local settings
    pull_light_settings()

    screens.show_setup_main_screen()


###############################################################################
# Handles a press of the OK button
###############################################################################
def upon_ok_press():
    # Chirp
    screens.play_key_tone()

    # Push local settings to CONFIG file
    push_light_settings()

    # Command the DCB with the new AUTO setting
    commandLightsAuto()

    # Go back to display the MAIN screen 
    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def upon_opt1_select():
    # Chirp
    screens.play_key_tone()

    global ConfigLightsAuto
    ConfigLightsAuto = LIGHT_AUTO_OFF

    update_radio_buttons()


###############################################################################
###############################################################################
def upon_opt2_select():
    # Chirp
    screens.play_key_tone()

    global ConfigLightsAuto
    ConfigLightsAuto = LIGHT_AUTO_ON

    update_radio_buttons()


###############################################################################
###############################################################################
def upon_opt3_select():
    # Chirp
    screens.play_key_tone()

    global ConfigLightsAuto
    ConfigLightsAuto = LIGHT_AUTO_ALS

    update_radio_buttons()


###############################################################################
###############################################################################
def update_radio_buttons():
    global ConfigLightsAuto

    # Operate the checkboxes as radio buttons (i.e. only 1 selected at a time)
    if (ConfigLightsAuto == LIGHT_AUTO_OFF):
        opt1_btn.configure(image=screens.checkbox_yes_icon)
        opt2_btn.configure(image=screens.checkbox_no_icon)
        opt3_btn.configure(image=screens.checkbox_no_icon)
    elif (ConfigLightsAuto == LIGHT_AUTO_ON):
        opt1_btn.configure(image=screens.checkbox_no_icon)
        opt2_btn.configure(image=screens.checkbox_yes_icon)
        opt3_btn.configure(image=screens.checkbox_no_icon)
    else:
        ConfigLightsAuto = LIGHT_AUTO_ALS
        opt1_btn.configure(image=screens.checkbox_no_icon)
        opt2_btn.configure(image=screens.checkbox_no_icon)
        opt3_btn.configure(image=screens.checkbox_yes_icon)


###############################################################################
# Creates the screen for tank light SETUP/CONFIG
###############################################################################
def create_setup_screen(frame):
    global setup_screen

    # Create and place the Screen
    setup_screen = tk.Frame(frame)
    setup_screen.grid(row=0, column=0, sticky='nsew')

    # Create the screen Widgets
    top_frm = create_setup_top_line(setup_screen)
    mid_frm = create_radio_buttons(setup_screen)
    bot_frm = create_bottom_line(setup_screen)

    # Place the Widgets onto the screen
    top_frm.grid(row=0, column=0, sticky='nw')
    mid_frm.grid(row=1, column=0, padx=40, pady=30, sticky='w')
    bot_frm.grid(row=2, column=0, padx=40, pady=30, sticky='w')

    # Update the radio buttons based on the local settings
    update_radio_buttons()

    return setup_screen


###############################################################################
# Creates the tank light SETUP screen top line
###############################################################################
def create_setup_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame)
    title_label.configure(font=LG_FONT, fg=SETUP_COLOR)
    title_label.configure(text="Tank Light Settings:")
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
# Creates the tank light SETUP screen radio buttons
###############################################################################
def create_radio_buttons(frame):
    global opt1_btn, opt2_btn, opt3_btn

    this_frame = tk.Frame(frame)

    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f3 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, sticky='w')
    f2.grid(row=1, column=0, sticky='w')
    f3.grid(row=2, column=0, sticky='w')

    opt1_btn = tk.Button(f1)
    opt1_btn.configure(relief="flat", command=upon_opt1_select)
    opt1_lbl = tk.Label(f1)
    opt1_lbl.configure(font=MD_FONT, fg=SETUP_COLOR)
    opt1_lbl.configure(text="Tank lights normally off")
    opt1_btn.grid(row=0, column=0)
    opt1_lbl.grid(row=0, column=1, padx=10)

    opt2_btn = tk.Button(f2)
    opt2_btn.configure(relief="flat", command=upon_opt2_select)
    opt2_lbl = tk.Label(f2)
    opt2_lbl.configure(font=MD_FONT, fg=SETUP_COLOR)
    opt2_lbl.configure(text="Tank lights normally on")
    opt2_btn.grid(row=0, column=0)
    opt2_lbl.grid(row=0, column=1, padx=10)

    opt3_btn = tk.Button(f3)
    opt3_btn.configure(relief="flat", command=upon_opt3_select)
    opt3_lbl = tk.Label(f3)
    opt3_lbl.configure(font=MD_FONT, fg=SETUP_COLOR)
    opt3_lbl.configure(text="Tank lights on when room is dark")
    opt3_btn.grid(row=0, column=0)
    opt3_lbl.grid(row=0, column=1, padx=10)

    return this_frame


###############################################################################
# Creates the tank light SETUP screen bottom line
###############################################################################
def create_bottom_line(frame):
    this_frame = tk.Frame(frame)

    b1 = tk.Button(this_frame)
    b1.configure(image=screens.blu_ok_btn_icon, borderwidth=0)
    b1.configure(command=upon_ok_press)

    l1 = tk.Label(this_frame)

    b2 = tk.Button(this_frame)
    b2.configure(image=screens.blu_cancel_btn_icon, borderwidth=0)
    b2.configure(command=upon_cancel_press)

    b1.grid(row=0, column=0, pady=10)
    l1.grid(row=0, column=1, padx=80)
    b2.grid(row=0, column=2, pady=10)

    return this_frame



