#!/usr/bin/python

from globals import *
import time
import threading
import telemetry
import flowrate
import color
import turbidity
import patientlog

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
            flowrate.take_flow_sample()
            flowrate.update_flow_rate()
            my_flow = flowrate.get_flow_accumulation()
            print("Flow = %s" % my_flow)

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

            printStatus("Analysis cycle complete!")

            dts = getDateTimeStamp()
            analyze_line = dts + f'Flow:{my_flow} Color:{my_color} Turbidity: \n'
            patientlog.write_line(analyze_line)


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


