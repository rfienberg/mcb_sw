from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens

BIG_FONT = ("Georgia", 30)
BIG_FG = 'purple'


###############################################################################
###############################################################################
def create_menu_screen(frame):
    global this_screen

    # Open up the image files and size them correctly
    global setup_btn_icon
    setup_btn_img = Image.open("Icons/setup_btn_img.png").resize((140,250), Image.ANTIALIAS)
    setup_btn_icon = ImageTk.PhotoImage(setup_btn_img)
    global analyze_btn_icon
    analyze_btn_img = Image.open("Icons/analyze_btn_img.png").resize((140,250), Image.ANTIALIAS)
    analyze_btn_icon = ImageTk.PhotoImage(analyze_btn_img)
    global control_btn_icon
    control_btn_img = Image.open("Icons/control_btn_img.png").resize((140,250), Image.ANTIALIAS)
    control_btn_icon = ImageTk.PhotoImage(control_btn_img)
    global status_btn_icon
    status_btn_img = Image.open("Icons/status_btn_img.png").resize((140,250), Image.ANTIALIAS)
    status_btn_icon = ImageTk.PhotoImage(status_btn_img)

    # Create the Frame for this screen
    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets for this screen
    title_label = tk.Label(this_screen)
    title_label.configure(text="Welcome to Tessefi Medical", font=BIG_FONT, fg=BIG_FG)
    setup_btn_button = tk.Button(this_screen, image=setup_btn_icon, borderwidth=0)
    analyze_btn_button = tk.Button(this_screen, image=analyze_btn_icon, borderwidth=0)
    control_btn_button = tk.Button(this_screen, image=control_btn_icon, borderwidth=0)
    status_btn_button = tk.Button(this_screen, image=status_btn_icon, borderwidth=0)

    # Bind button press events to functions
    setup_btn_button.configure(command=on_setup_press)
    analyze_btn_button.configure(command=on_analyze_press)
    control_btn_button.configure(command=on_control_press)
    status_btn_button.configure(command=on_status_press)

    # Place the Widgets into the Frame
    title_label.grid(row=0, column=0, pady=20, columnspan=4)
    setup_btn_button.grid(row=1,   column=0, padx=20, pady=20)
    analyze_btn_button.grid(row=1, column=1, padx=20, pady=20)
    control_btn_button.grid(row=1, column=2, padx=20, pady=20)
    status_btn_button.grid(row=1,  column=3, padx=20, pady=20)

    return this_screen


###############################################################################
###############################################################################
def show_menu_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
###############################################################################
def on_setup_press():
    screens.play_key_tone()
    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def on_analyze_press():
    screens.play_key_tone()
    screens.show_analyze_main_screen()


###############################################################################
###############################################################################
def on_status_press():
    screens.play_key_tone()
    screens.show_status_main_screen()
    #screens.popup_tank_warning()


###############################################################################
###############################################################################
def on_control_press():
    screens.play_key_tone()
    screens.show_control_main_screen()


