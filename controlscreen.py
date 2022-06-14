from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens

BIG_FONT = ("Georgia", 30)
BIG_FG = '#02AB4F'
MY_FONT = ('Calibri', 18)
MY_FG = '#02AB4F'

###############################################################################
###############################################################################
def create_screen(frame):
    global this_screen

    # Open up the image files and size them correctly
    global gohome_btn_icon
    gohome_btn_img = Image.open("Icons/green_home_icon.png").resize((50,50), Image.ANTIALIAS)
    gohome_btn_icon = ImageTk.PhotoImage(gohome_btn_img)
    global cartridge_btn_icon
    this_btn_img = Image.open("Icons/cartridge_btn.png").resize((100,100), Image.ANTIALIAS)
    cartridge_btn_icon = ImageTk.PhotoImage(this_btn_img)
    global color_btn_icon
    this_btn_img = Image.open("Icons/control_lights_btn_icon.png").resize((100,100), Image.ANTIALIAS)
    color_btn_icon = ImageTk.PhotoImage(this_btn_img)
    global turbidity_btn_icon
    this_btn_img = Image.open("Icons/control_power_btn_icon.png").resize((100,100), Image.ANTIALIAS)
    turbidity_btn_icon = ImageTk.PhotoImage(this_btn_img)

    # Create and place the Screen
    this_screen = tk.LabelFrame(frame, text="Control Screen")
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top = create_top_line(this_screen)
    lits_btn = create_lights_button(this_screen)
    cart_btn = create_cartridge_button(this_screen)
    shut_btn = create_shutdown_button(this_screen)

    # Place the Widgets
    top.grid(row=0, column=0, columnspan=10, sticky='w')
    lits_btn.grid(row=1, column=0, padx=20, pady=5, sticky='n')
    cart_btn.grid(row=1, column=1, padx=20, pady=5, sticky='n')
    shut_btn.grid(row=1, column=2, padx=20, pady=5, sticky='n')

    return this_screen


###############################################################################
###############################################################################
def show_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
###############################################################################
def on_home_press():
    screens.play_key_tone()
    screens.show_home_screen()


###############################################################################
###############################################################################
def on_lights_press():
    screens.play_key_tone()
    screens.show_control_lights_screen()


###############################################################################
###############################################################################
def on_cartridge_press():
    screens.play_key_tone()
    screens.show_control_cartridge_screen()


###############################################################################
###############################################################################
def on_shutdown_press():
    screens.play_key_tone()
    screens.show_verify_shutdown_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    gohome_btn_button = tk.Button(this_frame, image=gohome_btn_icon, borderwidth=0)
    gohome_btn_button.configure(command=on_home_press)
    gohome_btn_button.grid(row=0, column=0, padx=5, pady=20, sticky='w')

    # Create the Title label
    title_label = tk.Label(this_frame, text="Control:")
    title_label.configure(font=BIG_FONT, fg=MY_FG)
    title_label.grid(row=0, column=1, padx=5, pady=10)

    return this_frame


###############################################################################
###############################################################################
def create_lights_button(frame):
    this_frame = tk.Frame(frame)

    this_btn_button = tk.Button(this_frame, image=color_btn_icon, borderwidth=0)
    this_btn_button.configure(command=on_lights_press)
    this_btn_button.grid(row=0, column=0)
    this_btn_label = tk.Label(this_frame, text="Turn On\nLights")
    this_btn_label.configure(font=MY_FONT, fg=MY_FG)
    this_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_cartridge_button(frame):
    this_frame = tk.Frame(frame)

    this_btn_button = tk.Button(this_frame, image=cartridge_btn_icon, borderwidth=0)
    this_btn_button.configure(command=on_cartridge_press)
    this_btn_button.grid(row=0, column=0)
    this_btn_label = tk.Label(this_frame, text="Remove\nCartridge")
    this_btn_label.configure(font=MY_FONT, fg=MY_FG)
    this_btn_label.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_shutdown_button(frame):
    this_frame = tk.Frame(frame)

    this_btn_button = tk.Button(this_frame, image=turbidity_btn_icon, borderwidth=0)
    this_btn_button.configure(command=on_shutdown_press)
    this_btn_button.grid(row=0, column=0)
    this_btn_label = tk.Label(this_frame, text="Shutdown\nUnit")
    this_btn_label.configure(font=MY_FONT, fg=MY_FG)
    this_btn_label.grid(row=1, column=0)

    return this_frame


