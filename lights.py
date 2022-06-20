from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens
import dcb
import mcb_config


ConfigTankLights = 'Off'


###############################################################################
# Creates the screen for tank light SETUP
###############################################################################
def create_setup_screen(frame):
    global setup_screen

    # Open up the image files and size them correctly
    global checkbox_yes_icon
    checkbox_yes_img = Image.open("Icons/checkbox_yes.png").resize((25,25), Image.ANTIALIAS)
    checkbox_yes_icon = ImageTk.PhotoImage(checkbox_yes_img)
    global checkbox_no_icon
    checkbox_no_img = Image.open("Icons/checkbox_no.png").resize((25,25), Image.ANTIALIAS)
    checkbox_no_icon = ImageTk.PhotoImage(checkbox_no_img)

    global ok_btn_icon
    ok_btn_img = Image.open("Icons/blue_ok_btn.png").resize((150,50), Image.ANTIALIAS)
    ok_btn_icon = ImageTk.PhotoImage(ok_btn_img)
    global cancel_btn_icon
    cancel_btn_img = Image.open("Icons/blue_cancel_btn.png").resize((150,50), Image.ANTIALIAS)
    cancel_btn_icon = ImageTk.PhotoImage(cancel_btn_img)

    # Create and place the Screen
    setup_screen = tk.LabelFrame(frame)
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
# Shows the screen for tank light SETUP
###############################################################################
def show_setup_screen():
    global setup_screen

    # Pull the CONFIG file values into local settings
    pull_light_settings()

    # Update the radio buttons based on the local settings
    update_radio_buttons()

    setup_screen.tkraise()


###############################################################################
###############################################################################
def opt1_select():
    global ConfigTankLights
    ConfigTankLights = 'Off'

    update_radio_buttons()

    screens.play_key_tone()


###############################################################################
###############################################################################
def opt2_select():
    global ConfigTankLights
    ConfigTankLights = 'On'

    update_radio_buttons()

    screens.play_key_tone()


###############################################################################
###############################################################################
def opt3_select():
    global ConfigTankLights
    ConfigTankLights = 'Dark'

    update_radio_buttons()

    screens.play_key_tone()


###############################################################################
###############################################################################
def update_radio_buttons():
    global ConfigTankLights

    if (ConfigTankLights == 'Off'):
        opt1_btn.configure(image=checkbox_yes_icon)
        opt2_btn.configure(image=checkbox_no_icon)
        opt3_btn.configure(image=checkbox_no_icon)
    elif (ConfigTankLights == 'On'):
        opt1_btn.configure(image=checkbox_no_icon)
        opt2_btn.configure(image=checkbox_yes_icon)
        opt3_btn.configure(image=checkbox_no_icon)
    else:
        ConfigTankLights = 'Dark'
        opt1_btn.configure(image=checkbox_no_icon)
        opt2_btn.configure(image=checkbox_no_icon)
        opt3_btn.configure(image=checkbox_yes_icon)


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
    opt1_btn.configure(relief="flat", command=opt1_select)
    opt1_lbl = tk.Label(f1)
    opt1_lbl.configure(font=MD_FONT, fg=SETUP_COLOR)
    opt1_lbl.configure(text="Tank lights normally off")
    opt1_btn.grid(row=0, column=0)
    opt1_lbl.grid(row=0, column=1, padx=10)

    opt2_btn = tk.Button(f2)
    opt2_btn.configure(relief="flat", command=opt2_select)
    opt2_lbl = tk.Label(f2)
    opt2_lbl.configure(font=MD_FONT, fg=SETUP_COLOR)
    opt2_lbl.configure(text="Tank lights normally on")
    opt2_btn.grid(row=0, column=0)
    opt2_lbl.grid(row=0, column=1, padx=10)

    opt3_btn = tk.Button(f3)
    opt3_btn.configure(relief="flat", command=opt3_select)
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
# Handles a press of the CANCEL button
###############################################################################
def on_cancel_press():
    # Pull the CONFIG file values into local settings
    pull_light_settings()

    screens.play_key_tone()

    screens.show_setup_main_screen()


###############################################################################
# Handles a press of the OK button
###############################################################################
def on_ok_press():
    # Push local settings to CONFIG file
    push_light_settings()

    screens.play_key_tone()

    screens.show_setup_main_screen()




###############################################################################
# Creates the screen for tank light CONTROL
###############################################################################
def create_control_screen(frame):
    global control_screen

    # Open up the image files and size them correctly
    global control_ok_btn_icon
    control_ok_btn_img = Image.open("Icons/green_ok_btn.png").resize((150,50), Image.ANTIALIAS)
    control_ok_btn_icon = ImageTk.PhotoImage(control_ok_btn_img)

    # Create and place the Screen
    control_screen = tk.LabelFrame(frame)
    control_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top_frm = create_control_top_line(control_screen)
    bot_frm = create_control_bot_line(control_screen)

    # Place the Widgets
    top_frm.grid(row=0, column=0, sticky='nw')
    bot_frm.grid(row=1, column=0, sticky='nsew')

    return control_screen


###############################################################################
# Shows the screen for tank light CONTROL
###############################################################################
def show_control_screen():
    global control_screen
    control_screen.tkraise()

    dcb.sendTankLightCommand('On')


###############################################################################
# Exits back to the CONTROL main screen
###############################################################################
def on_control_exit():
    screens.play_key_tone()

    screens.show_control_main_screen()

    dcb.sendTankLightCommand('Off')


###############################################################################
# Creates the tank light CONTROL screen top line
###############################################################################
def create_control_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame)
    title_label.configure(font=LG_FONT, fg=CONTROL_COLOR)
    title_label.configure(text="Control Lights:")
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
# Creates the tank light CONTROL screen lights on widget
###############################################################################
def create_control_bot_line(frame):
    this_frame = tk.Frame(frame)

    label_1 = tk.Label(this_frame)
    label_1.configure(font=MD_FONT, fg=CONTROL_COLOR)
    label_1.configure(text="Tank Lights are now ON")

    label_2 = tk.Label(this_frame)
    label_2.configure(font=MD_FONT, fg=CONTROL_COLOR)
    label_2.configure(text="Press OK when done...")

    ok_button = tk.Button(this_frame)
    ok_button.configure(image=control_ok_btn_icon, borderwidth=0)
    ok_button.configure(command=on_control_exit)

    label_1.grid(  row=0, column=0, padx=20, pady=20, sticky='ew')
    label_2.grid(  row=1, column=0, padx=20, sticky='ew')
    ok_button.grid(row=2, column=0, pady=30)

    return this_frame


###############################################################################
###############################################################################
def pull_light_settings():
    global ConfigTankLights

    ConfigTankLights = mcb_config.getTankLightsConfig()


###############################################################################
###############################################################################
def push_light_settings():
    global ConfigTankLights

    mcb_config.setTankLightsConfig(ConfigTankLights)

    # Write the new CONFIG values to file
    mcb_config.writeConfigSettings()

