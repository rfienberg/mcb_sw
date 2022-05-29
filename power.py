from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens


BIG_FONT = ("Georgia", 30)
BIG_FG = '#00B050'
MY_FONT = ('Calibri', 28)
MY_FG = '#00B050'


###############################################################################
###############################################################################
def create_screen(frame):
    global this_screen, ver_msg, off_msg

    # Open up the image files and size them correctly
    global yes_btn_icon
    yes_btn_img = Image.open("Icons/yes_btn_green.png").resize((150,50), Image.ANTIALIAS)
    yes_btn_icon = ImageTk.PhotoImage(yes_btn_img)
    global no_btn_icon
    no_btn_img = Image.open("Icons/no_btn_green.png").resize((150,50), Image.ANTIALIAS)
    no_btn_icon = ImageTk.PhotoImage(no_btn_img)

    # Create and place the Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top_line = create_top_line(this_screen)
    ver_msg = create_verify_widget(this_screen)

    # Place the Widgets
    top_line.grid(row=0, column=0, sticky='nw')
    ver_msg.grid(row=1, column=0, sticky='nsew')

    return this_screen


###############################################################################
###############################################################################
def show_screen():
    global this_screen, ver_msg
    this_screen.tkraise()


###############################################################################
###############################################################################
def on_yes_press():
    # Chirp
    screens.play_key_tone()

    # Bring-up the "Shutting down!" screen
    screens.show_shut_down_screen()


###############################################################################
###############################################################################
def on_no_press():
    screens.play_key_tone()

    # Go back to display the parent screen
    screens.show_control_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame)
    title_label.configure(font=BIG_FONT, fg=MY_FG)
    title_label.configure(text="Shut-Down:")
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_verify_widget(frame):
    this_frame = tk.Frame(frame)

    my_label = tk.Label(this_frame)
    my_label.configure(font=MY_FONT, fg=MY_FG)
    my_label.configure(text="Are you sure that you want to shut-down?")
    my_label.grid(row=0, column=0, columnspan=10, padx=20, pady=40)

    yes_button = tk.Button(this_frame, image=yes_btn_icon, borderwidth=0)
    yes_button.configure(command=on_yes_press)
    yes_button.grid(row=1, column=0, padx=60, pady=10, sticky='w')

    no_button = tk.Button(this_frame, image=no_btn_icon, borderwidth=0)
    no_button.configure(command=on_no_press)
    no_button.grid(row=1, column=2, padx=60, pady=10, sticky='e')

    return this_frame


