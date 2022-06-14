#!/usr/bin/python

from globals import *
import threading
import time
import scram
import telemetry
import shutdown


###############################################################################
# Starts the STATUS thread
###############################################################################
def start_thread():
    printStatus("Start-up STATUS thread")
    global y
    y = threading.Thread(target=runStatusTask, daemon=True)
    y.start()


###############################################################################
# Stops the STATUS thread
###############################################################################
def stop_thread():
    printStatus("Shut-down STATUS thread")
    global y
    y.terminate()


###############################################################################
# Run the STATUS thread
###############################################################################
def runStatusTask():
    # Endless loop running STATUS operations...
    while True:
        time.sleep(1.0)
        sendStatusUpdate()


###############################################################################
# Build and send a STATUS UPDATE message to the DCB
###############################################################################
def sendStatusUpdate():
    # Default to: Shut-Down Status=Not Requested, Tanks=Not Full
    status_string = ">SU: 0000\n"
    my_status = list(status_string)

    # If a shut-down has been requested...
    if (shutdown.isShutDownRequested()):
        my_status[5] = '1'

    # If the Left Tank is fillable...
    if (isTankFull("Left")):
        my_status[6] = '1'

    # If the Right Tank is fillable...
    if (isTankFull("Right")):
        my_status[7] = '1'

    # Send our latest STATUS to the DCB
    status_string = "".join(my_status)
    #printStatus(status_string)
    rsp = scram.SendCommand(status_string)


###############################################################################
# Returns True if the specified TANK is full, False otherwise
###############################################################################
def isTankFull(side="Left"):
    # Get the latest volume reading for this tank
    volume = telemetry.getRealTankVolume(side)

    # Is this tank's volume indicate that it is full?
    if (volume >= TANK_FULL_VOLUME):
        return True
    else:
        return False


