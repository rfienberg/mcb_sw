#!/usr/bin/python

from globals import *
import threading
import dcb
import time
import telemetry
import color
import turbidity

if (RUN_ON_CM4):
    from picamera import PiCamera

# Define the cycle time as 2 hours
FLOW_RATE_CYCLE_SECS = 7200

# Variables for computing Flow Rates
FlowVolumeAcc  = 0
FlowVolumeOld  = 0
FlowCycleStart = 0


###############################################################################
###############################################################################
def startup():
    y = threading.Thread(target=runAnalyzeTask, daemon = True)
    y.start()


###############################################################################
###############################################################################
def runAnalyzeTask():
    # Create a Camera object
    if (RUN_ON_CM4):
        camera = PiCamera()

    printStatus("Started ANALYZE task")
    startFlowRateCycle()

    # Endless loop running ANALYZE operations...
    while True:
        printStatus("Computing FLOWRATE...")
        serviceFlowRateCycle()

        # Set the Analysis Backlight for analyzing COLOR
        printStatus("Setting up for COLOR analysis")
        dcb.sendBacklightCommand('white')
        time.sleep(5)

        # Snap a picture for analyzing COLOR
        printStatus("Take a COLOR snapshot")
        if (RUN_ON_CM4):
            color.take_snapshot(camera)
        time.sleep(1)

        # Analyze the picture for its COLOR
        printStatus("Computing COLOR...")
        color.analyze()

        # Set the Analysis Backlight for analyzing TURBIDITY
        printStatus("Setting up for TURBIDITY analysis")
        dcb.sendBacklightCommand('hatch')
        time.sleep(5)

        # Snap a picture for analyzing TURBIDITY
        printStatus("Take a TURBIDITY snapshot")
        if (RUN_ON_CM4):
            turbidity.take_snapshot(camera)
        time.sleep(1)

        # Analyze the picture for its TURBIDITY
        printStatus("Computing TURBIDITY...")
        turbidity.analyze()

        # Set the Analysis Backlight to OFF
        printStatus("Analysis cycle complete!")
        dcb.sendBacklightCommand('off')
        time.sleep(10)


###############################################################################
###############################################################################
def startFlowRateCycle():
    global FlowVolumeAcc, FlowVolumeOld, FlowCycleStart
    FlowVolumeAcc = 0
    FlowVolumeOld = 0
    FlowCycleStart = time.time()


###############################################################################
###############################################################################
def serviceFlowRateCycle():
    # Accumulate more volume into the accumulator
    accumulateFlow()

    # If the Flow Rate Cycle has run for at least 2 hours...
    if ((time.time() - FlowCycleStart) > 3600):

        # Compute and record the Flow Rate for this Flow Rate cycle
        flow_rate = computeFlowRate()
        print("Flow Rate = %d" % flow_rate)

        # Start a new Flow Rate cycle
        startFlowRateCycle()


###############################################################################
###############################################################################
def accumulateFlow():
    global FlowVolumeAcc, FlowVolumeOld

    # Compute the total volume
    lvolume = telemetry.getRealTankVolume("Left")
    rvolume = telemetry.getRealTankVolume("Right")
    new_volume = lvolume + rvolume

    # Compute the delta volume
    if (new_volume > FlowVolumeOld):
        delta_volume = new_volume - FlowVolumeOld
    else:
        delta_volume = 0
    FlowVolumeOld = new_volume

    # Add the delta volume to the accumulator
    FlowVolumeAcc = FlowVolumeAcc + delta_volume


###############################################################################
###############################################################################
def computeFlowRate():
    global FlowVolumeAcc, FlowCycleStart

    # Get the accumulated volume (in mL)
    acc_volume = FlowVolumeAcc

    # Compute the accumulation time (in seconds)
    acc_time = (time.time() - FlowCycleStart)

    # Compute the flow rate (in mL per hour)
    flow_rate = ((acc_volume * 3600) / acc_time)

    return flow_rate


