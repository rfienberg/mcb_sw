from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens
import telemetry
import time


BIG_FONT = ("Georgia", 30)
BIG_FG = 'brown'
MY_FONT = ('Calibri', 18)
MY_FG = 'brown'

# Define a cycle time as 2 hours
FLOW_RATE_CYCLE_SECS = 7200


FlowSample    = 0
FlowVolumeOld = 0

# Variables for computing Flow Rates
FlowVolumeAcc   = 0
FlowCycleStart  = 0



###############################################################################
# Define the FLOWRATE HISTORY screen
###############################################################################
def create_screen(frame):
    global this_screen

    global back_btn_icon
    this_btn_img = Image.open("Icons/brn_back_btn.png").resize((150,50), Image.ANTIALIAS)
    back_btn_icon = ImageTk.PhotoImage(this_btn_img)

    this_screen = tk.LabelFrame(frame, text="Analyze Flow Rates")
    this_screen.grid(row=0, column=0, sticky='nsew')

    top = create_top_line(this_screen)
    top.grid(row=0, column=0, sticky='nw')

    bot = create_bottom_line(this_screen)
    bot.grid(row=10, column=0)

    return this_screen


###############################################################################
# Show the FLOWRATE HISTORY screen
###############################################################################
def show_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
# Update the FLOWRATE HISTORY screen
###############################################################################



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

    back_button = tk.Button(this_frame)
    back_button.configure(image=back_btn_icon, borderwidth=0)
    back_button.configure(command=on_back_press)
    back_button.grid(row=0, column=0, padx=40, sticky='w')

    tk.Label(this_frame).grid(row=0, column=1, padx=100)

    return this_frame


###############################################################################
# Starts a new Flow Rate accumulation cycle
###############################################################################
def start_new_cycle():
    global FlowCycleStart, FlowVolumeAcc, FlowVolumeOld

    FlowVolumeAcc = 0
    FlowVolumeOld = 0

    # Take an initial sample to "prime the pump"
    take_flow_sample()

    FlowCycleStart = time.time()


###############################################################################
###############################################################################
def take_flow_sample():
    global FlowSample, FlowVolumeOld

    # Accumulate more flow into the accumulator
    # Compute the total volume in the two tanks
    lvolume = telemetry.getRealTankVolume("Left")
    rvolume = telemetry.getRealTankVolume("Right")
    new_volume = lvolume + rvolume

    # Compute the delta volume since last update
    if (new_volume > FlowVolumeOld):
        delta_volume = new_volume - FlowVolumeOld
    else:
        delta_volume = 0
    FlowVolumeOld = new_volume

    # Record the new delta volume as the flow sample
    FlowSample = delta_volume


###############################################################################
###############################################################################
def update_flow_rate():
    global FlowCycleStart, FlowVolumeAcc, FlowSample

    # Add the new sample to the accumulator
    FlowVolumeAcc = FlowVolumeAcc + FlowSample

    # Compute the accumulation time (in seconds)
    acc_time = (time.time() - FlowCycleStart)

    # If the Flow Rate Cycle has ended...
    if (acc_time >= FLOW_RATE_CYCLE_SECS):

        # Compute the flow rate (in mL per hour)
        flow_rate = ((FlowVolumeAcc * 3600) / acc_time)
        flow_rate = round(flow_rate, 1)
        print("Flow Rate = %d" % flow_rate)

        # Start a new Flow Rate cycle
        start_new_cycle()


###############################################################################
###############################################################################
def get_flow_string():
    global FlowSample
    return (str(FlowSample).zfill(2))


###############################################################################
###############################################################################
def get_flow_accumulation():
    global FlowVolumeAcc
    accumulation = round(FlowVolumeAcc)
    return (str(accumulation).rjust(4, '0'))


