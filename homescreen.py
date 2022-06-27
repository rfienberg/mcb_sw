from globals import *
import tkinter as tk
import screens



###############################################################################
###############################################################################
def create_menu_screen(frame):
    global this_screen

    # Create the Frame for this screen
    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')
    buttons = tk.Frame(this_screen)

    # Create the Widgets for this screen
    title_label = tk.Label(this_screen)
    title_label.configure(text="Welcome to Tessefi Medical", font=LG_FONT, fg=STATUS_COLOR)
    setup_btn_button = tk.Button(  buttons, image=screens.setup_btn_icon, borderwidth=0)
    analyze_btn_button = tk.Button(buttons, image=screens.analyze_btn_icon, borderwidth=0)
    control_btn_button = tk.Button(buttons, image=screens.control_btn_icon, borderwidth=0)
    status_btn_button = tk.Button( buttons, image=screens.status_btn_icon, borderwidth=0)
    analyze_btn_button.grid(row=0, column=0, padx=20)
    control_btn_button.grid(row=0, column=1, padx=20)
    setup_btn_button.grid(  row=0, column=2, padx=20)
    status_btn_button.grid( row=0, column=3, padx=20)

    # Bind button press events to functions
    setup_btn_button.configure(command=on_setup_press)
    analyze_btn_button.configure(command=on_analyze_press)
    control_btn_button.configure(command=on_control_press)
    status_btn_button.configure(command=on_status_press)

    # Place the Widgets into the Frame
    title_label.grid(row=0, column=0, pady=20)
    buttons.grid(row=1, column=0, padx=10, pady=10)

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


