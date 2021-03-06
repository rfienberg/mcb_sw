#!/usr/bin/python

from globals import *
from os.path import exists
import time
import threading
import telemetry
import flow
import color
import turbidity
import alerts
import patientinfo

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
    time.sleep(20)

    # Take an initial FLOW sample to "prime the pump"
    flow.getFlowSample()

    # Endless loop running ANALYZE operations...
    while True:

        # Spin and wait here for a new MINUTE to occur
        while (new_minute == old_minute):
            time.sleep(1)
            new_minute = time.strftime("%M", time.localtime(time.time()))

        old_minute = new_minute

        # Snap a new FLOW sample for analyzing FLOW
        #printStatus("Computing FLOW...")
        my_flow = flow.getFlowSample()
        #print("Delta Flow = %d" % my_flow)

        # Snap a new COLOR sample for analyzing COLOR
        #printStatus("Computing COLOR...")
        color.start_analysis()
        if (RUN_ON_CM4):
            color.take_snapshot(camera)
        color.analyze_snapshot()
        color.stop_analysis()
        my_color = color.getColorRating()

        # Snap a new TURBIDITY sample for analyzing TURBIDITY
        #printStatus("Computing TURBIDITY...")
        turbidity.start_analysis()
        if (RUN_ON_CM4):
            turbidity.take_snapshot(camera)
        turbidity.analyze_snapshot()
        turbidity.stop_analysis()
        my_turbidity = turbidity.getTurbidRating()

        # Get the current hour's total FLOW
        my_sec = int(time.time())
        flow.updateHourlyFlow(my_sec)
        hr_flow = flow.getCurrentHourlyFlow()

        # Test for flow ALERT conditions
        alerts.testForFlowTooLow(my_sec)
        alerts.testForFlowTooHigh(my_sec)

        # Record a new line into the ANALYZE log file
        #printStatus("Analysis cycle #%d complete!" % my_sec)
        analyze_line = f"{my_sec}, {my_flow}, {hr_flow}, {my_color}, {my_turbidity}"
        write_log_line(analyze_line)

        # Record a new line into the PATIENT log file
        (color_text,_,_) = color.getColorRatingParams(my_color)
        turbid_text = turbidity.getTurbidityRatingText(my_turbidity)
        log_line = getDateTimeStamp() + "FLOW=" + str(my_flow)
        log_line = log_line + " COLOR=" + color_text
        log_line = log_line + " TURBIDITY=" + turbid_text
        print(log_line)
        patientinfo.write_log_line(log_line)

        # Update today's FLOW information
        flow.updateDailyFlows(my_sec)


###############################################################################
# Returns True if FLOW is allowed into at least one tank
###############################################################################
def IsFlowAllowed():
    if (RUN_ON_CM4 == False):
        return True

    lvalve = telemetry.getTankValveStatus("Left")
    rvalve = telemetry.getTankValveStatus("Right")

    # If any valve is OPEN then FLOW is "allowed"...
    if ((lvalve == "Opened") or (rvalve == "Opened")):
        return True
    else:
        return False


###############################################################################
# Creates a new ANALYZE Log File for the specified patient name
###############################################################################
def create_log_file(name):
    log_line = "Started ANALYZE Log for: " + name
    print(log_line)
    file = open(ANALYZE_FILE, "w")
    file.write(log_line + "\n")
    file.close()


###############################################################################
# Writes the specified line of text into the ANALYZE log file
###############################################################################
def write_log_line(line):
    if (not exists(ANALYZE_FILE)):
        create_log_file("UNKNOWN PATIENT")

    file = open(ANALYZE_FILE, 'a')
    file.write(line + "\n")
    file.close()


