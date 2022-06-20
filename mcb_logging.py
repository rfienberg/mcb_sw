from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens



###############################################################################
###############################################################################
def create_setup_screen(frame):
    global this_screen

    global ok_btn_icon
    ok_btn_img = Image.open("Icons/blue_ok_btn.png").resize((150,50), Image.ANTIALIAS)
    ok_btn_icon = ImageTk.PhotoImage(ok_btn_img)
    global cancel_btn_icon
    cancel_btn_img = Image.open("Icons/blue_cancel_btn.png").resize((150,50), Image.ANTIALIAS)
    cancel_btn_icon = ImageTk.PhotoImage(cancel_btn_img)

    this_screen = tk.LabelFrame(frame, text="Set Logging Screen")
    this_screen.grid(row=0, column=0, sticky='nsew')

    top = create_top_line(this_screen)
    top.grid(row=0, column=0, sticky='nw')

    bot = create_bottom_line(this_screen)
    bot.grid(row=10, column=0)

    return this_screen


###############################################################################
###############################################################################
def show_setup_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
###############################################################################
def on_ok_press():
    screens.play_key_tone()
    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def on_cancel_press():
    screens.play_key_tone()
    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame, text="Set Logging:", font=LG_FONT, fg=SETUP_COLOR)
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
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


