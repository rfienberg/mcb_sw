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

# Variables for computing Flows
FlowSample    = 0
FlowVolumeOld = 0

FlowHourly  = 0
FlowDaily = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


###############################################################################
###############################################################################
def takeFlowSample():
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
    return FlowSample


###############################################################################
# Updates and returns the current hour's total flow (in mL)
###############################################################################
def updateHourlyFlow(timestamp):
    global FlowHourly
    FlowHourly = compute_flow_over_range(timestamp-3600, timestamp)
    return FlowHourly


###############################################################################
# Updates the previous day's hourly flows
###############################################################################
def updateDailyFlows(timestamp):
    global FlowDaily

    # Compute the second of the last hour point
    time_flds = time.gmtime(timestamp)
    secs_from_hour = time_flds.tm_sec + (60 * time_flds.tm_min)
    last_ts = timestamp - secs_from_hour

    # For each of the last 24 hours...
    for hour in range(len(FlowDaily)):
        # Compute this hour's start/end timestamp range
        end_ts   = last_ts - (hour * 3600)
        start_ts = end_ts - 3600

        # Compute the total flow within this range
        FlowDaily[hour] = compute_flow_over_range(start_ts, end_ts)

    print(FlowDaily)


###############################################################################
###############################################################################
def getCurrentHourlyFlow():
    global FlowHourly
    return FlowHourly


###############################################################################
# Define the FLOWRATE HISTORY screen
###############################################################################
def create_history_screen(frame):
    global this_screen

    global back_btn_icon
    this_btn_img = Image.open("Icons/brn_back_btn.png").resize((150,50), Image.ANTIALIAS)
    back_btn_icon = ImageTk.PhotoImage(this_btn_img)

    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    top = create_top_line(this_screen)
    top.grid(row=0, column=0, sticky='nw')

    bot = create_bottom_line(this_screen)
    bot.grid(row=10, column=0)

    return this_screen


###############################################################################
# Show the FLOWRATE HISTORY screen
###############################################################################
def show_history_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
# Update the FLOWRATE HISTORY screen
###############################################################################



###############################################################################
###############################################################################
def on_back_press():
    screens.play_key_tone()
    screens.show_analyze_main_screen()


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
    global FlowVolumeOld

    FlowVolumeOld = 0

    # Take an initial sample to "prime the pump"
    takeFlowSample()


###############################################################################
###############################################################################
def compute_flow_over_range(start_sec, end_sec):
    total_flow = count = 0

    # Open the Analyze Log File to see the flow data
    with open(ANALYZE_FILE, 'rt') as myfile:

        # Sum all of the flows within the past hour (3600 secs)...
        for myline in myfile:
            # Split the line of comma seperated text into fields
            fields = myline.split(',')

            # As long as this line has a timestamp field...
            if (fields[0].isdigit()):
                timestamp = int(fields[0])

                # And as long as this line's timestamp field is within range...
                if ((timestamp > start_sec) and (timestamp <= end_sec)):

                    # Add it's flow delta field's value to the sum
                    total_flow = total_flow + int(fields[1])
                    count = count + 1

        return total_flow




