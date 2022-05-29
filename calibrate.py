from globals import *
import mcb_config
import tkinter as tk
from PIL import ImageTk, Image
import screens
import telemetry


BIG_FONT = ("Georgia", 30)
BIG_FG = '#0070C0'
MY_FONT = ('Calibri', 26)
MY_FG = '#0070C0'

# Local CAL Offsets (integers)
LeftCalOffset  = 91
RightCalOffset = 109


###############################################################################
###############################################################################
def create_screen(frame):
    global this_screen, instructions, progress, start_btns, finished

    # Open the images for this screen
    global ok_btn_icon
    ok_btn_img = Image.open("Icons/ok_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    ok_btn_icon = ImageTk.PhotoImage(ok_btn_img)
    global cancel_btn_icon
    cancel_btn_img = Image.open("Icons/cancel_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    cancel_btn_icon = ImageTk.PhotoImage(cancel_btn_img)

    # Create and place this Screen
    this_screen = tk.LabelFrame(frame, text="Tank Calibration Screen")
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the screen Widgets
    top = create_top_line(this_screen)
    instructions = create_cal_instructions(this_screen)
    progress = create_cal_in_progress(this_screen)
    finished = create_cal_finished(this_screen)
    start_btns = create_start_buttons(this_screen)

    # Place the Widgets onto the screen
    top.grid(row=0, column=0, sticky='nw')
    instructions.grid(row=1, column=0, pady=40, sticky='nsew')
    progress.grid(row=1, column=0, pady=40, sticky='nsew')
    finished.grid(row=1, column=0, pady=40, sticky='nsew')
    start_btns.grid(row=10, column=0)

    return this_screen


###############################################################################
###############################################################################
def show_screen():
    # Pull the CONFIG file values into local settings
    pullSettings()

    # Display the CAL instructions to the operator
    instructions.tkraise()
    this_screen.tkraise()
    ok_button.configure(state='disabled')
    cancel_button.configure(state='normal')

    wait_for_tanks_removed()


###############################################################################
###############################################################################
def pullSettings():
    global LeftCalOffset, RightCalOffset

    offset = int(mcb_config.getLTankCalOffset(), 10)
    if (offset < MAXIMUM_CAL_OFFEST):
        LeftCalOffset = offset
    else:
        LeftCalOffset = DEFAULT_CAL_OFFSET

    offset = int(mcb_config.getRTankCalOffset(), 10)
    if (offset < MAXIMUM_CAL_OFFEST):
        RightCalOffset = offset
    else:
        RightCalOffset = DEFAULT_CAL_OFFSET


###############################################################################
###############################################################################
def pushSettings():
    global LeftCalOffset, RightCalOffset

    offset_str = str(LeftCalOffset)
    mcb_config.setLTankCalOffset(offset_str)

    offset_str = str(RightCalOffset)
    mcb_config.setRTankCalOffset(offset_str)

    # Write the new CONFIG values to file
    mcb_config.writeConfigSettings()


###############################################################################
###############################################################################
def getCalibrationOffset(side="Left"):
    if (side == "Left"):
        return LeftCalOffset
    else:
        return RightCalOffset


###############################################################################
###############################################################################
def wait_for_tanks_removed():
    global this_screen

    ok_button.configure(state='normal')
    """
    if ((telemetry.getSeatedStatus("Left") == "Unseated") and 
    (telemetry.getSeatedStatus("Right") == "Unseated") and 
    (telemetry.getSeatedStatus("Door")  == "Seated")):
        ok_button.configure(state='normal')
    else:
        this_screen.after(500, wait_for_tanks_removed)
    """


###############################################################################
###############################################################################
def on_start_press():
    global this_screen

    screens.play_key_tone()
    progress.tkraise()
    ok_button.configure(state='disabled')
    cancel_button.configure(state='disabled')

    # Give enough time for the scales to settle before calibrating
    this_screen.after(10000, perform_calibration)


###############################################################################
###############################################################################
def perform_calibration():
    global this_screen, LeftCalOffset, RightCalOffset

    # Read in, and record, the calibration offsets
    print("Performing tank scale calibration...")
    LeftCalOffset  = telemetry.getRawTankVolume("Left")
    RightCalOffset = telemetry.getRawTankVolume("Right")
    print("Left Cal Offset  = %d" % LeftCalOffset)
    print("Right Cal Offset = %d" % RightCalOffset)

    # Push local settings to CONFIG file
    pushSettings()

    # Display a temporary message that calibration is finished
    finished.tkraise()
    ok_button.configure(state='disabled')
    cancel_button.configure(state='disabled')

    this_screen.after(4000, on_cancel_press)


###############################################################################
###############################################################################
def on_cancel_press():
    screens.play_key_tone()
    screens.show_setup_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame, text="Tank Calibration:", font=BIG_FONT, fg=MY_FG)
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_cal_instructions(frame):
    this_frame = tk.Frame(frame)

    message = "In order to properly calibrate the device, \n first insure that both tanks are removed...\n\n Press Start when ready"

    my_label = tk.Label(this_frame)
    my_label.configure(text=message, font=MY_FONT, fg=MY_FG)
    my_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_cal_in_progress(frame):
    this_frame = tk.Frame(frame)

    message = "Tank calibration is in progress..."

    my_label = tk.Label(this_frame)
    my_label.configure(text=message, font=MY_FONT, fg=MY_FG)
    my_label.grid(row=0, column=0, padx=40, pady=40)

    return this_frame


###############################################################################
###############################################################################
def create_cal_finished(frame):
    this_frame = tk.Frame(frame)

    message = "Tank calibration is complete!"

    my_label = tk.Label(this_frame)
    my_label.configure(text=message, font=MY_FONT, fg=MY_FG)
    my_label.grid(row=0, column=0, padx=40, pady=40)

    return this_frame


###############################################################################
###############################################################################
def create_start_buttons(frame):
    global ok_button, cancel_button

    this_frame = tk.Frame(frame)

    ok_button = tk.Button(this_frame)
    ok_button.configure(image=ok_btn_icon, borderwidth=0)
    ok_button.configure(command=on_start_press)
    ok_button.grid(row=0, column=0, padx=40, sticky='w')

    tk.Label(this_frame).grid(row=0, column=1, padx=100)

    cancel_button = tk.Button(this_frame)
    cancel_button.configure(image=cancel_btn_icon, borderwidth=0)
    cancel_button.configure(command=on_cancel_press)
    cancel_button.grid(row=0, column=2, padx=40)

    return this_frame


