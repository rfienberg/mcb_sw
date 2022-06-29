from globals import *
import tkinter as tk
import screens

MY_FONT = ('Calibri', 14)


###############################################################################
###############################################################################
def create_main_screen(frame):
    global this_screen

    # Create and place this Screen
    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create and place the main frames
    top_frm = create_top_line(this_screen)
    bot_frm = tk.Frame(this_screen)
    top_frm.grid(row=0, column=0, sticky='w')
    bot_frm.grid(row=1, column=0, padx=40)

    # Create the screen Widgets
    pat_btn = create_patient_button(bot_frm)
    aud_btn = create_audio_button(bot_frm)
    alt_btn = create_alerts_button(bot_frm)
    cal_btn = create_calibrate_button(bot_frm)
    clk_btn = create_clock_button(bot_frm)
    lit_btn = create_lights_button(bot_frm)
    #tim_btn = create_timeouts_button(bot_frm)
    #log_btn = create_logging_button(bot_frm)

    # Place the Widgets into the frame
    pat_btn.grid(row=0, column=0, padx=20, pady=5)
    aud_btn.grid(row=0, column=1, padx=20, pady=5)
    alt_btn.grid(row=0, column=2, padx=20, pady=5)
    cal_btn.grid(row=0, column=3, padx=20, pady=5)
    clk_btn.grid(row=1, column=0, padx=20, pady=5)
    lit_btn.grid(row=1, column=1, padx=20, pady=5)
    #tim_btn.grid(row=1, column=2, padx=20, pady=5)
    #log_btn.grid(row=1, column=3, padx=20, pady=5)

    return this_screen


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
def on_set_patient_press():
    screens.play_key_tone()
    screens.show_set_patient_screen()


###############################################################################
###############################################################################
def on_set_audio_press():
    screens.play_key_tone()
    screens.show_set_audio_screen()


###############################################################################
###############################################################################
def on_set_alerts_press():
    screens.play_key_tone()
    screens.show_set_alerts_screen()


###############################################################################
###############################################################################
def on_set_calibrate_press():
    screens.play_key_tone()
    screens.show_calibrate_setup_screen()


###############################################################################
###############################################################################
def on_set_clock_press():
    screens.play_key_tone()
    screens.show_set_clock_screen()


###############################################################################
###############################################################################
def on_set_timeouts_press():
    screens.play_key_tone()
    screens.show_set_timeouts_screen()


###############################################################################
###############################################################################
def on_set_logging_press():
    screens.play_key_tone()
    screens.show_set_logging_screen()


###############################################################################
###############################################################################
def on_set_lights_press():
    screens.play_key_tone()
    screens.show_set_lights_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the widgets
    l1 = tk.Label(this_frame, text="Setup Options")
    b1 = tk.Button(this_frame)
    l1.configure(font=LG_FONT, fg=SETUP_COLOR)
    b1.configure(image=screens.blu_gohome_btn_icon, borderwidth=0)
    b1.configure(command=on_home_press)

    b1.grid(row=0, column=0, padx=5, pady=10)
    l1.grid(row=0, column=1, padx=80)

    return this_frame


###############################################################################
###############################################################################
def create_patient_button(frame):
    this_frame = tk.Frame(frame)

    patient_btn_button = tk.Button(this_frame, image=screens.patient_btn_icon, borderwidth=0)
    patient_btn_button.configure(command=on_set_patient_press)
    patient_btn_button.grid(row=0, column=0)

    patient_btn_label = tk.Label(this_frame, text="New Patient")
    patient_btn_label.configure(font=MY_FONT, fg=SETUP_COLOR)
    patient_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_audio_button(frame):
    this_frame = tk.Frame(frame)

    audio_btn_button = tk.Button(this_frame, image=screens.audio_btn_icon, borderwidth=0)
    audio_btn_button.configure(command=on_set_audio_press)
    audio_btn_button.grid(row=0, column=0)

    audio_btn_label = tk.Label(this_frame, text="Audio")
    audio_btn_label.configure(font=MY_FONT, fg=SETUP_COLOR)
    audio_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_alerts_button(frame):
    this_frame = tk.Frame(frame)

    alerts_btn_button = tk.Button(this_frame, image=screens.alerts_btn_icon, borderwidth=0)
    alerts_btn_button.configure(command=on_set_alerts_press)
    alerts_btn_button.grid(row=0, column=0)

    alerts_btn_label = tk.Label(this_frame, text="Alerts")
    alerts_btn_label.configure(font=MY_FONT, fg=SETUP_COLOR)
    alerts_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_calibrate_button(frame):
    this_frame = tk.Frame(frame)

    calibrate_btn_button = tk.Button(this_frame, image=screens.calibrate_btn_icon, borderwidth=0)
    calibrate_btn_button.configure(command=on_set_calibrate_press)
    calibrate_btn_button.grid(row=0, column=0)

    calibrate_btn_label = tk.Label(this_frame, text="Calibrate")
    calibrate_btn_label.configure(font=MY_FONT, fg=SETUP_COLOR)
    calibrate_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_clock_button(frame):
    this_frame = tk.Frame(frame)

    datetime_btn_button = tk.Button(this_frame, image=screens.datetime_btn_icon, borderwidth=0)
    datetime_btn_button.configure(command=on_set_clock_press)
    datetime_btn_button.grid(row=0, column=0)

    datetime_btn_label = tk.Label(this_frame, text="Clock")
    datetime_btn_label.configure(font=MY_FONT, fg=SETUP_COLOR)
    datetime_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_timeouts_button(frame):
    this_frame = tk.Frame(frame)

    timeouts_btn_button = tk.Button(this_frame, image=screens.timeouts_btn_icon, borderwidth=0)
    timeouts_btn_button.configure(command=on_set_timeouts_press)
    timeouts_btn_button.grid(row=0, column=0)

    timeouts_btn_label = tk.Label(this_frame, text="Timeouts")
    timeouts_btn_label.configure(font=MY_FONT, fg=SETUP_COLOR)
    timeouts_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_logging_button(frame):
    this_frame = tk.Frame(frame)

    logging_btn_button = tk.Button(this_frame, image=screens.logging_btn_icon, borderwidth=0)
    logging_btn_button.configure(command=on_set_logging_press)
    logging_btn_button.grid(row=0, column=0)

    logging_btn_label = tk.Label(this_frame, text="Logging")
    logging_btn_label.configure(font=MY_FONT, fg=SETUP_COLOR)
    logging_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_lights_button(frame):
    this_frame = tk.Frame(frame)

    lights_btn_button = tk.Button(this_frame, image=screens.blu_lights_btn_icon, borderwidth=0)
    lights_btn_button.configure(command=on_set_lights_press)
    lights_btn_button.grid(row=0, column=0)

    lights_btn_label = tk.Label(this_frame, text="Lights")
    lights_btn_label.configure(font=MY_FONT, fg=SETUP_COLOR)
    lights_btn_label.grid(row=1, column=0)

    return this_frame


