from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens


BIG_FONT = ("Georgia", 30)
BIG_FG = '#0070C0'
MY_FONT = ('Calibri', 18)
MY_FG = '#0070C0'

###############################################################################
###############################################################################
def create_screen(frame):
    global this_screen

    this_screen = tk.LabelFrame(frame, text="Set Logging Screen")
    this_screen.grid(row=0, column=0, sticky='nsew')

    top = create_top_line(this_screen)
    top.grid(row=0, column=0, sticky='nw')

    bot = create_bottom_line(this_screen)
    bot.grid(row=10, column=0)

    return this_screen


###############################################################################
###############################################################################
def show_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
###############################################################################
def on_ok_press():
    screens.play_key_tone()
    screens.show_setup_screen()


###############################################################################
###############################################################################
def on_cancel_press():
    screens.play_key_tone()
    screens.show_setup_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame, text="Set Logging:", font=BIG_FONT, fg=MY_FG)
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_bottom_line(frame):
    this_frame = tk.Frame(frame)

    global ok_btn_icon
    ok_btn_img = Image.open("Icons/ok_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    ok_btn_icon = ImageTk.PhotoImage(ok_btn_img)
    ok_button = tk.Button(this_frame)
    ok_button.configure(image=ok_btn_icon, borderwidth=0)
    ok_button.configure(command=on_ok_press)
    ok_button.grid(row=0, column=0, padx=40, sticky='w')

    tk.Label(this_frame).grid(row=0, column=1, padx=100)

    global cancel_btn_icon
    cancel_btn_img = Image.open("Icons/cancel_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    cancel_btn_icon = ImageTk.PhotoImage(cancel_btn_img)
    cancel_button = tk.Button(this_frame)
    cancel_button.configure(image=cancel_btn_icon, borderwidth=0)
    cancel_button.configure(command=on_cancel_press)
    cancel_button.grid(row=0, column=2, padx=40)

    return this_frame


