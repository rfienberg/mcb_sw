from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens


BIG_FONT = ("Georgia", 30)
BIG_FG = 'brown'
MY_FONT = ('Calibri', 18)
MY_FG = 'brown'


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
def on_flowrates_press():
    screens.play_key_tone()
    screens.show_analyze_flowrates_screen()


###############################################################################
###############################################################################
def on_color_press():
    screens.play_key_tone()
    screens.show_analyze_color_screen()


###############################################################################
###############################################################################
def on_turbidity_press():
    screens.play_key_tone()
    screens.show_analyze_turbidity_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the Go Home button
    global gohome_btn_icon
    gohome_btn_img = Image.open("Icons/brown_home_icon.png").resize((50,50), Image.ANTIALIAS)
    gohome_btn_icon = ImageTk.PhotoImage(gohome_btn_img)
    gohome_btn_button = tk.Button(this_frame, image=gohome_btn_icon, borderwidth=0)
    gohome_btn_button.configure(command=on_home_press)
    gohome_btn_button.grid(row=0, column=0, padx=5, pady=20, sticky='nw')

    # Create the Title label
    title_label = tk.Label(this_frame, text="Analyze:")
    title_label.configure(font=BIG_FONT, fg=MY_FG)
    title_label.grid(row=0, column=1, padx=5, pady=10)

    return this_frame


###############################################################################
###############################################################################
def create_flowrates_button(frame):
    this_frame = tk.Frame(frame)

    global flowrates_btn_icon
    this_btn_img = Image.open("Icons/flowrates_btn_icon.png").resize((100,100), Image.ANTIALIAS)
    flowrates_btn_icon = ImageTk.PhotoImage(this_btn_img)
    this_btn_button = tk.Button(this_frame, image=flowrates_btn_icon, borderwidth=0)
    this_btn_button.configure(command=on_flowrates_press)
    this_btn_button.grid(row=0, column=0)
    this_btn_label = tk.Label(this_frame, text="Flow Rates")
    this_btn_label.configure(font=MY_FONT, fg=MY_FG)
    this_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_color_button(frame):
    this_frame = tk.Frame(frame)

    global color_btn_icon
    this_btn_img = Image.open("Icons/color_btn_icon.png").resize((100,100), Image.ANTIALIAS)
    color_btn_icon = ImageTk.PhotoImage(this_btn_img)
    this_btn_button = tk.Button(this_frame, image=color_btn_icon, borderwidth=0)
    this_btn_button.configure(command=on_color_press)
    this_btn_button.grid(row=0, column=0)
    this_btn_label = tk.Label(this_frame, text="Color")
    this_btn_label.configure(font=MY_FONT, fg=MY_FG)
    this_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_turbidity_button(frame):
    this_frame = tk.Frame(frame)

    global turbidity_btn_icon
    this_btn_img = Image.open("Icons/turbidity_btn_icon.png").resize((100,100), Image.ANTIALIAS)
    turbidity_btn_icon = ImageTk.PhotoImage(this_btn_img)
    this_btn_button = tk.Button(this_frame, image=turbidity_btn_icon, borderwidth=0)
    this_btn_button.configure(command=on_turbidity_press)
    this_btn_button.grid(row=0, column=0)
    this_btn_label = tk.Label(this_frame, text="Turbidity")
    this_btn_label.configure(font=MY_FONT, fg=MY_FG)
    this_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create(frame):
    global this_screen

    # Create and place the Screen
    this_screen = tk.LabelFrame(frame, text="Analyze Screen")
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top = create_top_line(this_screen)
    fr_btn = create_flowrates_button(this_screen)
    ca_btn = create_color_button(this_screen)
    ta_btn = create_turbidity_button(this_screen)

    # Place the Widgets
    top.grid(row=0, column=0, columnspan=10, sticky='w')
    fr_btn.grid(row=1, column=0, padx=20, pady=5)
    ca_btn.grid(row=1, column=1, padx=20, pady=5)
    ta_btn.grid(row=1, column=2, padx=20, pady=5)

    return this_screen
