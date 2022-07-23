from globals import *
import mcb_config
import tkinter as tk
import screens
import telemetry
import dcb


CalStep = 0

# Local CAL Offsets (integers)
LeftCalOffset  = 91
RightCalOffset = 109


###############################################################################
###############################################################################
def getCalibrationOffset(side="Left"):
    if (side == "Left"):
        return LeftCalOffset
    else:
        return RightCalOffset


###############################################################################
###############################################################################
def pull_calibation_settings():
    global LeftCalOffset, RightCalOffset

    offset = mcb_config.getLTankCalOffset()
    if (offset > 0):
        LeftCalOffset = offset
    else:
        LeftCalOffset = DEFAULT_CAL_OFFSET

    offset = mcb_config.getRTankCalOffset()
    if (offset > 0):
        RightCalOffset = offset
    else:
        RightCalOffset = DEFAULT_CAL_OFFSET


###############################################################################
###############################################################################
def push_calibration_settings():
    global LeftCalOffset, RightCalOffset

    mcb_config.setLTankCalOffset(LeftCalOffset)
    mcb_config.setRTankCalOffset(RightCalOffset)

    # Write the new CONFIG values to file
    mcb_config.writeConfigSettings()


###############################################################################
# Shows the CALIBRATION instructions
###############################################################################
def show_setup_screen():
    # Pull the CONFIG file values into local settings
    pull_calibation_settings()

    # Display the CAL instructions to the operator
    instruct.tkraise()
    cal_screen.tkraise()
    start_button.configure(state='disabled')

    # Wait for the user to follow the instructions
    # before enabling the Start button
    wait_for_tanks_removed()


###############################################################################
# Polls for the tanks to be removed before enabling the Start button
###############################################################################
def wait_for_tanks_removed():
    global cal_screen

    if (RUN_ON_CM4):
        if ((telemetry.getTankDoorStatus()     == "Closed") and 
        (telemetry.getInstalledStatus("Left")  == "Removed") and 
        (telemetry.getInstalledStatus("Right") == "Removed")):
            start_button.configure(state='normal')
        else:
            cal_screen.after(200, wait_for_tanks_removed)
    else:
        start_button.configure(state='normal')


###############################################################################
# Handles the START button press - starts the calibration
###############################################################################
def upon_start_press():
    # Chirp
    screens.play_key_tone()

    # Display "Calibration In Progress message
    progress.tkraise()

    # Initialize for calibration
    global CalStep
    CalStep = 0

    # Perform the tank scale calibration
    print("Performing tank scale calibration...")
    perform_calibration()


###############################################################################
# Handles the BACK button press - returns to the SETUP screen
###############################################################################
def upon_back_press():
    screens.play_key_tone()
    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def perform_calibration():
    global cal_screen, CalStep
    global cal_inprogress_icon

    # If not waited long enough for the scales to settle...
    if (CalStep < 10):
        # Count another calibration step
        CalStep = CalStep + 1

        # RLF: It would be nice to rotate the in-progress icon

        # Toggle the tank lights on/off
        if (CalStep % 2):
            dcb.sendTankLightCommand('On')
        else:
            dcb.sendTankLightCommand('Off')

        cal_screen.after(1000, perform_calibration)

    # If waited long enough for the scales to settle...
    else:
        dcb.sendTankLightCommand('Off')

        record_calibration()


###############################################################################
# Records the new CAL Offsets for LEFT/RIGHT Tank scales
###############################################################################
def record_calibration():
    global cal_screen, LeftCalOffset, RightCalOffset

    # Chirp
    screens.play_key_tone()

    # Read in, and record, the calibration offsets
    LeftCalOffset  = telemetry.getRawTankVolume("Left")
    RightCalOffset = telemetry.getRawTankVolume("Right")
    print("Left Cal Offset  = %d" % LeftCalOffset)
    print("Right Cal Offset = %d" % RightCalOffset)

    # Push local settings to CONFIG file
    push_calibration_settings()

    # Display a message that calibration is finished
    finished.tkraise()


###############################################################################
# Creates the CALIBRATION screen
###############################################################################
def create_setup_screen(frame):
    global cal_screen, instruct, progress, finished, start_btns

    # Create and place this Screen
    cal_screen = tk.Frame(frame)
    cal_screen.grid(row=0, column=0, sticky='nsew')

    # Create the screen Widgets
    top_line = create_top_line(cal_screen)
    instruct = create_cal_instructions(cal_screen)
    progress = create_cal_in_progress(cal_screen)
    finished = create_cal_finished(cal_screen)

    # Place the Widgets onto the screen
    top_line.grid(row=0, column=0, sticky='nw')
    instruct.grid(row=1, column=0, sticky='nsew')
    progress.grid(row=1, column=0, sticky='nsew')
    finished.grid(row=1, column=0, sticky='nsew')

    return cal_screen


###############################################################################
# Creates the screen title label
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    b1 = tk.Button(this_frame)
    b1.configure(image=screens.blu_gohome_btn_icon, borderwidth=0)
    b1.configure(command=upon_back_press)

    l1 = tk.Label(this_frame)
    l1.configure(font=LG_FONT, fg=SETUP_COLOR)
    l1.configure(text="Tank Calibration:")

    b1.grid(row=0, column=0, padx=5, pady=10)
    l1.grid(row=0, column=1, padx=20)

    return this_frame


###############################################################################
# Creates the CALIBRATION intructions widgets
###############################################################################
def create_cal_instructions(frame):
    global start_button

    this_frame = tk.Frame(frame)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, padx=10, pady=10)
    f2.grid(row=1, column=0, padx=10, pady=20)

    instr_msg = "In order to properly calibrate the device, \n first ensure that both tanks are removed...\n\n Press Start when ready"

    m1 = tk.Label(f1)
    m1.configure(font=MD_FONT, fg=SETUP_COLOR)
    m1.configure(text=instr_msg)
    m1.grid(row=0, column=0)

    start_button = tk.Button(f2)
    start_button.configure(image=screens.start_btn_icon, borderwidth=0)
    start_button.configure(command=upon_start_press)
    start_button.grid(row=0, column=0)

    return this_frame


###############################################################################
# Creates the CALIBRATION in progress widgets
###############################################################################
def create_cal_in_progress(frame):
    this_frame = tk.Frame(frame)

    message = "Tank calibration is in progress..."

    text_label = tk.Label(this_frame)
    text_label.configure(text=message, font=MD_FONT, fg=SETUP_COLOR)

    icon_label = tk.Label(this_frame)
    icon_label.configure(image=screens.cal_inprogress_icon)

    text_label.grid(row=0, column=0, padx=40, pady=20)
    icon_label.grid(row=1, column=0)

    return this_frame


###############################################################################
# Creates the CALIBRATION finished widgets
###############################################################################
def create_cal_finished(frame):
    this_frame = tk.Frame(frame)

    message = "Tank calibration is complete!"

    m1 = tk.Label(this_frame)
    m1.configure(text=message, font=MD_FONT, fg=SETUP_COLOR)

    i1 = tk.Label(this_frame)
    i1.configure(image=screens.cal_complete_icon)

    b1 = tk.Button(this_frame)
    b1.configure(image=screens.blu_ok_btn_icon, borderwidth=0)
    b1.configure(command=upon_back_press)

    m1.grid(row=0, column=0, padx=40, pady=20)
    i1.grid(row=1, column=0)
    b1.grid(row=2, column=0, pady=20)

    return this_frame


