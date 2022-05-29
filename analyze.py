#!/usr/bin/python

from globals import *
import threading
import dcb
import time
import color
import turbidity

if (RUN_ON_CM4):
    from picamera import PiCamera

# List of base colors
colors = [
    ([153, 151, 168]), 
    ([249, 249, 227]), 
    ([255, 255, 128]), 
    ([155, 177, 31]), 
    ([255, 230, 153]), 
    ([255, 217, 102]), 
    ([191, 144, 0]), 
    ([197, 90, 17]), 
    ([210, 40, 5]), 
    ([0, 0, 0])
]


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

    # Endless loop running ANALYZE operations...
    while True:
        time.sleep(10)

        printStatus("Computing FLOWRATE...")
        time.sleep(1)

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


###############################################################################
###############################################################################
def take_color_snapshot():
    if (RUN_ON_CM4):
        camera.capture(SNAP_COLOR_RAW)


###############################################################################
###############################################################################
def take_turbidity_snapshot():
    if (RUN_ON_CM4):
        camera.capture(SNAP_TURBID_RAW)



