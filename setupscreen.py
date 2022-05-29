from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens

BIG_FONT = ("Georgia", 30)
BIG_FG = 'purple'
MY_FONT = ('Calibri', 14)
MY_FG = '#0070C0'


###############################################################################
###############################################################################
def show():
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
def on_set_datetime_press():
    screens.play_key_tone()
    screens.show_set_clock_screen()


###############################################################################
###############################################################################
def on_set_timeouts_press():
    screens.play_key_tone()
    screens.show_set_timeouts_screen()


###############################################################################
###############################################################################
def on_set_alarms_press():
    screens.play_key_tone()
    screens.show_set_alarms_screen()


###############################################################################
###############################################################################
def on_set_audio_press():
    screens.play_key_tone()
    screens.show_set_audio_screen()


###############################################################################
###############################################################################
def on_set_logging_press():
    screens.play_key_tone()
    screens.show_set_logging_screen()


###############################################################################
###############################################################################
def on_set_calibrate_press():
    screens.play_key_tone()
    screens.show_calibrate_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the Go Home button
    gohome_btn_button = tk.Button(this_frame, image=gohome_btn_icon, borderwidth=0)
    gohome_btn_button.configure(command=on_home_press)
    gohome_btn_button.grid(row=0, column=0, padx=5, pady=10, sticky='w')

    # Create the Title label
    title_label = tk.Label(this_frame, text="Setup:")
    title_label.configure(font=BIG_FONT, fg=MY_FG)
    title_label.grid(row=0, column=1, padx=5, pady=10)

    return this_frame


###############################################################################
###############################################################################
def create_patient_button(frame):
    this_frame = tk.Frame(frame)

    patient_btn_button = tk.Button(this_frame, image=patient_btn_icon, borderwidth=0)
    patient_btn_button.configure(command=on_set_patient_press)
    patient_btn_button.grid(row=0, column=0)

    patient_btn_label = tk.Label(this_frame, text="Patient")
    patient_btn_label.configure(font=MY_FONT, fg=MY_FG)
    patient_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_datetime_button(frame):
    this_frame = tk.Frame(frame)

    datetime_btn_button = tk.Button(this_frame, image=datetime_btn_icon, borderwidth=0)
    datetime_btn_button.configure(command=on_set_datetime_press)
    datetime_btn_button.grid(row=0, column=0)

    datetime_btn_label = tk.Label(this_frame, text="Date/Time")
    datetime_btn_label.configure(font=MY_FONT, fg=MY_FG)
    datetime_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_timeouts_button(frame):
    this_frame = tk.Frame(frame)

    timeouts_btn_button = tk.Button(this_frame, image=timeouts_btn_icon, borderwidth=0)
    timeouts_btn_button.configure(command=on_set_timeouts_press)
    timeouts_btn_button.grid(row=0, column=0)

    timeouts_btn_label = tk.Label(this_frame, text="Timeouts")
    timeouts_btn_label.configure(font=MY_FONT, fg=MY_FG)
    timeouts_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_alarms_button(frame):
    this_frame = tk.Frame(frame)

    alarms_btn_button = tk.Button(this_frame, image=alarms_btn_icon, borderwidth=0)
    alarms_btn_button.configure(command=on_set_alarms_press)
    alarms_btn_button.grid(row=0, column=0)

    alarms_btn_label = tk.Label(this_frame, text="Alarms")
    alarms_btn_label.configure(font=MY_FONT, fg=MY_FG)
    alarms_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_audio_button(frame):
    this_frame = tk.Frame(frame)

    audio_btn_button = tk.Button(this_frame, image=audio_btn_icon, borderwidth=0)
    audio_btn_button.configure(command=on_set_audio_press)
    audio_btn_button.grid(row=0, column=0)

    audio_btn_label = tk.Label(this_frame, text="Audio")
    audio_btn_label.configure(font=MY_FONT, fg=MY_FG)
    audio_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_logging_button(frame):
    this_frame = tk.Frame(frame)

    logging_btn_button = tk.Button(this_frame, image=logging_btn_icon, borderwidth=0)
    logging_btn_button.configure(command=on_set_logging_press)
    logging_btn_button.grid(row=0, column=0)

    logging_btn_label = tk.Label(this_frame, text="Logging")
    logging_btn_label.configure(font=MY_FONT, fg=MY_FG)
    logging_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_calibrate_button(frame):
    this_frame = tk.Frame(frame)

    calibrate_btn_button = tk.Button(this_frame, image=calibrate_btn_icon, borderwidth=0)
    calibrate_btn_button.configure(command=on_set_calibrate_press)
    calibrate_btn_button.grid(row=0, column=0)

    calibrate_btn_label = tk.Label(this_frame, text="Calibrate")
    calibrate_btn_label.configure(font=MY_FONT, fg=MY_FG)
    calibrate_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create(frame):
    global this_screen

    # Open the images for this screen
    global gohome_btn_icon
    image = Image.open("Icons/blue_home_icon.png").resize((50,50), Image.ANTIALIAS)
    gohome_btn_icon = ImageTk.PhotoImage(image)
    global patient_btn_icon
    image = Image.open("Icons/set_patient_btn_img.png").resize((100,100), Image.ANTIALIAS)
    patient_btn_icon = ImageTk.PhotoImage(image)
    global datetime_btn_icon
    image = Image.open("Icons/set_datetime_btn_img.png").resize((100,100), Image.ANTIALIAS)
    datetime_btn_icon = ImageTk.PhotoImage(image)
    global timeouts_btn_icon
    image = Image.open("Icons/set_timeouts_btn_img.png").resize((100,100), Image.ANTIALIAS)
    timeouts_btn_icon = ImageTk.PhotoImage(image)
    global alarms_btn_icon
    image = Image.open("Icons/set_alarms_btn_img.png").resize((100,100), Image.ANTIALIAS)
    alarms_btn_icon = ImageTk.PhotoImage(image)
    global audio_btn_icon
    image = Image.open("Icons/set_audio_btn_img.png").resize((100,100), Image.ANTIALIAS)
    audio_btn_icon = ImageTk.PhotoImage(image)
    global logging_btn_icon
    image = Image.open("Icons/logging_btn_img.png").resize((100,100), Image.ANTIALIAS)
    logging_btn_icon = ImageTk.PhotoImage(image)
    global calibrate_btn_icon
    image = Image.open("Icons/set_calibrate_btn_img.png").resize((100,100), Image.ANTIALIAS)
    calibrate_btn_icon = ImageTk.PhotoImage(image)

    # Create and place this Screen
    this_screen = tk.LabelFrame(frame, text="Setup Screen")
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the screen Widgets
    top = create_top_line(this_screen)
    pat_btn = create_patient_button(this_screen)
    dt_btn = create_datetime_button(this_screen)
    to_btn = create_timeouts_button(this_screen)
    alm_btn = create_alarms_button(this_screen)
    aud_btn = create_audio_button(this_screen)
    log_btn = create_logging_button(this_screen)
    cal_btn = create_calibrate_button(this_screen)

    # Place the Widgets onto the screen
    top.grid(row=0, column=0, columnspan=10, sticky='w')
    pat_btn.grid(row=1, column=0, padx=20, pady=5)
    dt_btn.grid(row=1, column=1, padx=20, pady=5)
    to_btn.grid(row=1, column=2, padx=20, pady=5)
    cal_btn.grid(row=1, column=3, padx=20, pady=5)
    alm_btn.grid(row=2, column=0, padx=20, pady=5)
    aud_btn.grid(row=2, column=1, padx=20, pady=5)
    log_btn.grid(row=2, column=2, padx=20, pady=5)

    return this_screen
