from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens
import dcb


BIG_FONT = ("Georgia", 30)
BIG_FG = '#00B050'
MY_FONT = ('Calibri', 28)
MY_FG = '#00B050'


###############################################################################
###############################################################################
def create_screen(frame):
    global this_screen, unlock_msg, ready_msg

    # Open up the image files and size them correctly
    global ok_btn_icon
    ok_btn_img = Image.open("Icons/ok_btn_green.png").resize((150,50), Image.ANTIALIAS)
    ok_btn_icon = ImageTk.PhotoImage(ok_btn_img)

    # Create and place the Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top = create_top_line(this_screen)
    unlock_msg = create_unlocking_widget(this_screen)
    ready_msg = create_safe_widget(this_screen)

    # Place the Widgets
    top.grid(row=0, column=0, sticky='nw')
    unlock_msg.grid(row=1, column=0, sticky='nsew')
    ready_msg.grid(row=1, column=0, sticky='nsew')

    return this_screen


###############################################################################
###############################################################################
def show_screen():
    global this_screen, unlock_msg

    # Display the "Unlocking" message screen
    unlock_msg.tkraise()
    this_screen.tkraise()

    # Stop fluid flow (i.e. close all valves) to unlock cartridge
    dcb.sendValveFlowCommand("Stop")

    # Now display the "Ready" message screen
    this_screen.after(1000, on_remove_ready)


###############################################################################
###############################################################################
def on_remove_ready():
    global ready_msg

    # Display the "Ready" message screen
    ready_msg.tkraise()


###############################################################################
###############################################################################
def on_ok_press():
    screens.play_key_tone()
    screens.show_control_screen()

    # Allow fluid flow again
    dcb.sendValveFlowCommand("Auto")


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame, text="Remove Cartridge:", font=BIG_FONT, fg=MY_FG)
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_unlocking_widget(frame):
    this_frame = tk.Frame(frame)

    my_label = tk.Label(this_frame)
    my_label.configure(font=MY_FONT, fg=MY_FG)
    my_label.configure(text="Unlocking Cartridge! Please wait...")
    my_label.grid(row=0, column=0, columnspan=10, padx=20, pady=40)

    return this_frame


###############################################################################
###############################################################################
def create_safe_widget(frame):
    this_frame = tk.Frame(frame)

    label_1 = tk.Label(this_frame)
    label_1.configure(font=MY_FONT, fg=MY_FG)
    label_1.configure(text="It is now safe to remove the Cartridge")
    label_1.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    label_2 = tk.Label(this_frame)
    label_2.configure(font=MY_FONT, fg=MY_FG)
    label_2.configure(text="Press OK when done...")
    label_2.grid(row=1, column=0, padx=20, sticky='ew')

    ok_button = tk.Button(this_frame, image=ok_btn_icon, borderwidth=0)
    ok_button.configure(command=on_ok_press)
    ok_button.grid(row=2, column=0, pady=30)

    return this_frame

