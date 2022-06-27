from globals import *
from os.path import exists
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import screens
import telemetry
import time


# Variables for computing Flows
FlowVolumePrev = 0
FlowHourly  = 0
FlowLabels  = ['10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm', '12am', '1am', '2am', '3am', '4am', '5am', '6am', '7am', '8am', '9am']
FlowVolumes  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


###############################################################################
# Returns the delta FLOW volume between now and the previous time called
###############################################################################
def getFlowSample():
    global FlowVolumePrev

    # Accumulate more flow into the accumulator
    # Compute the total volume in the two tanks
    lvolume = telemetry.getRealTankVolume("Left")
    rvolume = telemetry.getRealTankVolume("Right")
    new_volume = lvolume + rvolume

    # Compute the delta volume since last update
    if (new_volume > FlowVolumePrev):
        delta_volume = new_volume - FlowVolumePrev
    else:
        delta_volume = 0
    FlowVolumePrev = new_volume

    # Return the new delta volume as the flow sample
    return delta_volume


###############################################################################
# Returns the FLOW that has accumulated within the current hour
###############################################################################
def getCurrentHourlyFlow():
    global FlowHourly
    return FlowHourly


###############################################################################
# Updates the total flow (in mL) that occurred within a 1 hour period
###############################################################################
def updateHourlyFlow(time_in_secs):
    global FlowHourly

    # Compute all of the FLOW that occurred between the specified 
    # time and 1 hour (3600 seconds) before that specified time
    FlowHourly = compute_flow_over_period(time_in_secs-3600, time_in_secs)


###############################################################################
# Updates the current day's hourly FLOW volumes
###############################################################################
def updateDailyFlows(timestamp):
    global FlowLabels, FlowVolumes

    # Compute the second of the last hour point
    time_flds = time.localtime(timestamp)
    secs_from_hour = time_flds.tm_sec + (60 * time_flds.tm_min)
    last_ts = timestamp - secs_from_hour

    # For each hour in the past 24 hours...
    for hour in (range(24)):
        # Compute this hour's start/end timestamp range
        end_ts   = last_ts - (hour * 3600)
        start_ts = end_ts - 3600

        # Form this hour's label
        ts = time.localtime(end_ts)
        hr = time.strftime("%I", ts)
        pm = time.strftime("%p", ts).lower()

        # In order to fit all labels on the screen, we needed to make
        # some special rules:
        #   o Single-digit hours have their leading '0' removed
        #   o 12am is displayed as 'Mid'
        #   o Dual-digit hours are displayed without the 'a'/'p'
        if (hr[0] == '0'):
            hr = hr[1:]
        if ((hr == '12') and (pm == 'am')):
            label = 'Mid'
        elif ((hr == '10') or (hr == '11') or (hr == '12')):
            label = f"{hr}"
        else:
            pm = pm[0]
            label = f"{hr}{pm}"

        # Compute the total flow within this 1 hour range
        volume = compute_flow_over_period(start_ts, end_ts)
        #volume = 10 + (10 * hour)

        FlowLabels[hour]  = label
        FlowVolumes[hour] = volume


###############################################################################
# Define the FLOW HISTORY screen
###############################################################################
def create_history_screen(frame):
    global this_screen

    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    history = create_flow_history(this_screen)
    history.grid(row=0, column=0, sticky='w')

    return this_screen


###############################################################################
# Show the FLOW HISTORY screen
###############################################################################
def show_history_screen():
    # Update the data to be plotted
    updateDailyFlows(time.time())

    # Raise the FLOW HISTORY screen
    global this_screen
    this_screen.tkraise()

    # Start periodic screen updates
    periodic_screen_update()


###############################################################################
# Periodically update the FLOW HISTORY screen
###############################################################################
def periodic_screen_update():
    # Plot the latest FLOW history data
    plot_flow_history()

    # Schedule the next screen update
    global this_screen
    this_screen.after(30000, periodic_screen_update)


###############################################################################
# Handles a press event of the BACK button
###############################################################################
def on_back_press():
    global this_screen

    # Chirp
    screens.play_key_tone()

    # Cancel the periodic screen updates
    this_screen.after_cancel(periodic_screen_update)

    # Bring up the main ANALYZE screen
    screens.show_analyze_main_screen()


###############################################################################
# Creates the FLOW history screen
###############################################################################
def create_flow_history(frame):
    global flowplot, plot_canvas

    plt.rc('font', size=16)
    plt.rc('axes', titlesize=18)

    this_frame = tk.Frame(frame)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, sticky='w')
    f2.grid(row=1, column=0, sticky='w')

    # Create FigureCanvasTkAgg object
    figure = Figure(figsize=(8, 3), dpi=100)
    figure.set_facecolor("#F0F0F0")
    plot_canvas = FigureCanvasTkAgg(figure, f1)
    my_canvas = plot_canvas.get_tk_widget()
    my_canvas.grid(row=0, column=0, pady=10, sticky='n')

    flowplot = figure.add_subplot(1,1,1)
    flowplot.set_facecolor('white')
    flowplot.xaxis.label.set_color(ANALYZE_COLOR)
    flowplot.yaxis.label.set_color(ANALYZE_COLOR)
    flowplot.tick_params(axis='x', colors=ANALYZE_COLOR)
    flowplot.tick_params(axis='y', colors=ANALYZE_COLOR)
    flowplot.spines['top'].set_color(ANALYZE_COLOR)
    flowplot.spines['bottom'].set_color(ANALYZE_COLOR)
    flowplot.spines['left'].set_color(ANALYZE_COLOR)
    flowplot.spines['right'].set_color(ANALYZE_COLOR)

    b1 = tk.Button(f2)
    b1.configure(image=screens.back_btn_icon, borderwidth=0)
    b1.configure(command=on_back_press)
    l1 = tk.Label(f2)
    l1.configure(font=SM_FONT, fg=ANALYZE_COLOR)
    l1.configure(image=screens.past_arrow_icon)

    b1.grid(row=0, column=0, padx=40)
    l1.grid(row=0, column=1, padx=340, sticky='ne')

    return this_frame


###############################################################################
# Plots the latest FLOW history data
###############################################################################
def plot_flow_history():
    global FlowLabels, FlowVolumes
    global flowplot, plot_canvas

    x = []
    y = []

    # We will plot every hour with the newest hour on the right
    for hour in reversed(range(24)):
        x.append(FlowLabels[hour])
        y.append(FlowVolumes[hour])

    flowplot.clear()
    flowplot.bar(x, y, color='#C86430')
    flowplot.title.set_color(ANALYZE_COLOR)
    flowplot.set_title('Flow Over Past 24-Hours')
    flowplot.set_ylabel('Flow (mL)')
    flowplot.tick_params(labelsize=11)
    flowplot.grid(axis = 'y')

    plot_canvas.draw()


###############################################################################
# Returns the sum of all FLOW found over the specified time period
###############################################################################
def compute_flow_over_period(start_sec, end_sec):
    total_flow = count = 0

    if (exists(ANALYZE_FILE)):
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




