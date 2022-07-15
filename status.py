#!/usr/bin/python

from globals import *
import threading
import time
import scram
import telemetry
import shutdown

STATUS_SLEEP_TIME = 0.400
Status1SecServiceTime = 0

BATTERY_PERCENT_BAD = 10
BATTERY_PERCENT_LOW = 50


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
        # Run the once per second service
        run_one_second_service()

        # Sleep to allow other things to occur
        time.sleep(STATUS_SLEEP_TIME)


###############################################################################
###############################################################################
def run_one_second_service():
    # If it is time for the once-per-second service...
    global Status1SecServiceTime
    if ((time.time() - Status1SecServiceTime) >= 1.00):
        Status1SecServiceTime = time.time()

        # Send a periodic STATUS report to the DCB
        status_update_send_service()


###############################################################################
# Periodically build and send a STATUS UPDATE message to the DCB
###############################################################################
def status_update_send_service():
    # Default to: Shut-Down Status=Not Requested, Tanks=Not Full
    status_string = ">SU: 0000\n"
    my_status = list(status_string)

    # If a shut-down has been requested...
    if (shutdown.isShutDownRequested()):
        my_status[5] = '1'

    # If the Left Tank is not fillable...
    if (isTankFull("Left")):
        my_status[6] = '1'

    # If the Right Tank is not fillable...
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
    space  = telemetry.getTankSpaceStatus(side)

    # Does this tank's space indicate that it is full?
    if (space == "Overfilled"):
        return True
    # Does this tank's volume indicate that it is full?
    elif (volume >= TANK_FULL_VOLUME):
        return True
    else:
        return False


###############################################################################
# Returns True if the BATTERY is in the "LOW" range, False otherwise
###############################################################################
def isBatteryLow():
    # If the BATTERY is charging then we won't call it "LOW"
    if (telemetry.getBatteryChargeStatus() == "Charging"):
        return False

    # Get the latest BATTERY percentage from the DCB
    percent = telemetry.getBatteryChargePercent()

    # Is the BATTERY percentage within the LOW threshold?
    if ((percent < BATTERY_PERCENT_LOW) and (percent > BATTERY_PERCENT_BAD)):
        return True
    else:
        return False


###############################################################################
# Returns True if the BATTERY is in the "DEPLETED" range, False otherwise
###############################################################################
def isBatteryDepleted():
    # If the BATTERY is charging then we won't call it "DEPLETED"
    if (telemetry.getBatteryChargeStatus() == "Charging"):
        return False

    # Get the latest BATTERY percentage from the DCB
    percent = telemetry.getBatteryChargePercent()

    # Is the BATTERY percentage below the DEPLETED threshold?
    if (percent < BATTERY_PERCENT_BAD):
        return True
    else:
        return False



