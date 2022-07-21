from globals import *
import tkinter as tk
from time import strftime
from PIL import ImageTk, Image
import telemetry
import shutdown

MY_BG = 'white'
MY_FG = 'black'
MY_FONT = ('Calibri', 14)

GOOD_COLOR = '#17F12C'
BAD_COLOR = 'red'
UNKNOWN_COLOR = 'yellow'


###############################################################################
# Create the entire Status Bar frame
###############################################################################
def create_bar(window):
    global this_frame, door_led, ltank_led, rtank_led, cart_led
    global plug_no, plug_yes

    # Open up the image files and size them correctly
    global plugged_in_icon
    plugged_in_img = Image.open("Graphics/plugged_in_yes.png").resize((30,30), Image.ANTIALIAS)
    plugged_in_icon = ImageTk.PhotoImage(plugged_in_img)
    global unplugged_icon
    unplugged_img = Image.open("Graphics/plugged_in_no.png").resize((30,30), Image.ANTIALIAS)
    unplugged_icon = ImageTk.PhotoImage(unplugged_img)

    # Create the Frame for this screen
    this_frame = tk.LabelFrame(window)
    this_frame.configure(bg=MY_BG)
    this_frame.grid(row=2, column=0, sticky='sew')

    # Create the Widgets for this screen
    status_btn = tk.Button(this_frame)
    status_btn.configure(text="Status:", font=MY_FONT, bg=MY_BG)
    status_btn.configure(relief='flat', command=quit)

    ltank_led = create_led(this_frame, UNKNOWN_COLOR)
    ltank_lab = tk.Label(this_frame)
    ltank_lab.configure(text="Left Tank", font=MY_FONT, bg=MY_BG, fg=MY_FG, width=10, anchor='w')

    rtank_led = create_led(this_frame, UNKNOWN_COLOR)
    rtank_lab = tk.Label(this_frame)
    rtank_lab.configure(text="Right Tank", font=MY_FONT, bg=MY_BG, fg=MY_FG, width=10, anchor='w')

    cart_led = create_led(this_frame, UNKNOWN_COLOR)
    cart_lab = tk.Label(this_frame)
    cart_lab.configure(text="Cartridge", font=MY_FONT, bg=MY_BG, fg=MY_FG, width=10, anchor='w')

    door_led = create_led(this_frame, UNKNOWN_COLOR)
    door_lab = tk.Label(this_frame)
    door_lab.configure(text="Door", font=MY_FONT, bg=MY_BG, fg=MY_FG, width=10, anchor='w')

    plug_no = tk.Label(this_frame, bg=MY_BG)
    plug_no.configure(image=unplugged_icon)
    plug_yes = tk.Label(this_frame, bg=MY_BG)
    plug_yes.configure(image=plugged_in_icon)

    # Place the Widgets into the Frame
    status_btn.grid(row=0, column=0, padx=10)
    ltank_led[0].grid(row=0, column=1)
    ltank_lab.grid(row=0, column=2)
    rtank_led[0].grid(row=0, column=3)
    rtank_lab.grid(row=0, column=4)
    cart_led[0].grid(row=0, column=5)
    cart_lab.grid(row=0, column=6)
    door_led[0].grid(row=0, column=7)
    door_lab.grid(row=0, column=8)
    plug_no.grid(row=0, column=10, padx=20)
    plug_yes.grid(row=0, column=10, padx=20)

    # Start the periodic update
    update_bar()

    return this_frame


###############################################################################
###############################################################################
def update_bar():
    door = telemetry.getTankDoorStatus()
    ltank = telemetry.getInstalledStatus('Left')
    rtank = telemetry.getInstalledStatus('Right')
    cartridge = telemetry.getInstalledStatus('Cart')
    charger = telemetry.getBatteryPlugStatus()

    # Update the Tank Door status LED based on the latest data
    if (door == "Closed"):
        set_led_color(door_led, GOOD_COLOR)
    elif (door == "Opened"):
        set_led_color(door_led, BAD_COLOR)
    else:
        set_led_color(door_led, UNKNOWN_COLOR)

    # Update the Left Tank Installed status LED based on the latest data
    if (ltank == "Installed"):
        set_led_color(ltank_led, GOOD_COLOR)
    elif (ltank == "Removed"):
        set_led_color(ltank_led, BAD_COLOR)
    else:
        set_led_color(ltank_led, UNKNOWN_COLOR)

    # Update the Right Tank Installed status LED based on the latest data
    if (rtank == "Installed"):
        set_led_color(rtank_led, GOOD_COLOR)
    elif (rtank == "Removed"):
        set_led_color(rtank_led, BAD_COLOR)
    else:
        set_led_color(rtank_led, UNKNOWN_COLOR)

    # Update the Cartridge Installed status LED based on the latest data
    if (cartridge == "Installed"):
        set_led_color(cart_led, GOOD_COLOR)
    elif (cartridge == "Removed"):
        set_led_color(cart_led, BAD_COLOR)
    else:
        set_led_color(cart_led, UNKNOWN_COLOR)

    # Update the Plugged-In status LED based on the latest data
    if (charger == "Plugged-In"):
        plug_yes.tkraise()
    else:
        plug_no.tkraise()

    # As long as we are not shutting down...
    if (shutdown.isShutDownRequested() == False):

        # After 1 second, perform another update
        this_frame.after(1000, update_bar)


###############################################################################
# Set the specified LED to the specified color
###############################################################################
def set_led_color(led, color):
    led[0].itemconfig(led[1], fill=color)


###############################################################################
# Create an LED widget
###############################################################################
def create_led(frame, color=UNKNOWN_COLOR):
    canvas = tk.Canvas(frame)
    canvas.configure(bg=MY_BG, height=20, width=20, highlightthickness=0)
    oval = canvas.create_oval(4, 4, 18, 18)
    my_led = (canvas, oval)
    set_led_color(my_led, color)
    return my_led

