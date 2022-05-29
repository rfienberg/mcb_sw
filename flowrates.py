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
def create_screen(frame):
    global this_screen

    this_screen = tk.LabelFrame(frame, text="Analyze Flow Rates")
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
def on_back_press():
    screens.play_key_tone()
    screens.show_analyze_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame, text="Flow Rates:", font=BIG_FONT, fg=MY_FG)
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_bottom_line(frame):
    this_frame = tk.Frame(frame)

    global back_btn_icon
    back_btn_img = Image.open("Icons/back_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    back_btn_icon = ImageTk.PhotoImage(back_btn_img)
    back_button = tk.Button(this_frame)
    back_button.configure(image=back_btn_icon, borderwidth=0)
    back_button.configure(command=on_back_press)
    back_button.grid(row=0, column=0, padx=40, sticky='w')

    tk.Label(this_frame).grid(row=0, column=1, padx=100)

    return this_frame


