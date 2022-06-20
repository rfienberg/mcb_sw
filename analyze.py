#!/usr/bin/python

from globals import *
from os.path import exists
import time
import threading
import telemetry
import flowrate
import color
import turbidity
import patient

if (RUN_ON_CM4):
    from picamera import PiCamera


###############################################################################
# Starts the ANALYZE thread
###############################################################################
def start_thread():
    printStatus("Start-up ANALYZE thread")
    global y
    y = threading.Thread(target=runAnalyzeTask, daemon=True)
    y.start()


###############################################################################
# Stops the ANALYZE thread
###############################################################################
def stop_thread():
    printStatus("Shut-down ANALYZE thread")
    global y
    y.terminate()


###############################################################################
# Runs the ANALYZE thread
###############################################################################
def runAnalyzeTask():
    # Create an Analysis Camera object
    if (RUN_ON_CM4):
        camera = PiCamera()

    # Initialize this thread
    new_minute = 0
    old_minute = 0

    # Delay some time to allow some telemetry to come in...
    time.sleep(30)
    flowrate.start_new_cycle()

    # Endless loop running ANALYZE operations...
    while True:
        # Wait for a new MINUTE to occur
        while (new_minute == old_minute):
            time.sleep(1)
            new_minute = time.strftime("%M", time.gmtime(time.time()))
        old_minute = new_minute

        # As long as flow is allowed...
        if (IsFlowAllowed()):

            # Snap a FLOW sample for analyzing FLOW and FLOWRATE
            printStatus("Computing FLOW...")
            my_flow = flowrate.takeFlowSample()
            print("Delta Flow = %d" % my_flow)

            printStatus("Computing COLOR...")
            color.start_analysis()
            if (RUN_ON_CM4):
                color.take_snapshot(camera)
            color.analyze()
            color.stop_analysis()
            my_color = color.getColorRating()

            printStatus("Computing TURBIDITY...")
            turbidity.start_analysis()
            if (RUN_ON_CM4):
                turbidity.take_snapshot(camera)
            turbidity.analyze()
            turbidity.stop_analysis()
            my_turbidity = turbidity.getTurbidRating()

            # Update last hour's total flow
            my_sec = int(time.time())
            hr_flow = flowrate.updateHourlyFlow(my_sec)

            # Record a new line into the ANALYZE log file
            printStatus("Analysis cycle #%d complete!" % my_sec)
            analyze_line = f"{my_sec}, {my_flow}, {hr_flow}, {my_color}, {my_turbidity}\n"
            write_log_line(analyze_line)

            # Update today's hourly flows
            flowrate.updateDailyFlows(my_sec)


###############################################################################
###############################################################################
def IsFlowAllowed():
    if (RUN_ON_CM4 == False):
        return True

    lvalve = telemetry.getTankValveStatus("Left")
    rvalve = telemetry.getTankValveStatus("Right")

    # If any valve is open...
    if ((lvalve == "Opened") or (rvalve == "Opened")):
        return True
    else:
        return False


###############################################################################
# Creates a new Analyze Log File for the specified name
###############################################################################
def create_log_file():
    print("Created new log file: " + ANALYZE_FILE)
    file = open(ANALYZE_FILE, "w")
    file.write("Started Analyze Log\n")
    file.close()


###############################################################################
###############################################################################
def write_log_line(line):
    file = open_log_file("a")
    file.write(line)
    file.close()


###############################################################################
###############################################################################
def open_log_file(mode="a"):
    if (not exists(ANALYZE_FILE)):
        create_log_file()

    file = open(ANALYZE_FILE, mode)
    return file


