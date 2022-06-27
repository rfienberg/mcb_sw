#!/usr/bin/python

from globals import *
import threading
import time
import scram
import telemetry
import shutdown


StatusUpdateServiceTime = 0

LeftTankFullServiceTime = 0

RightTankFullServiceTime = 0

BothTanksFullServiceTime = 0

BatteryLowServiceTime = 0

BatteryDepletedServiceTime = 0



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
        # Sleep to allow other things to occur
        time.sleep(0.200)

        # Send a periodic STATUS report to the DCB
        status_update_send_service()

        run_left_tank_full_service()

        run_right_tank_full_service()

        run_both_tanks_full_service()

        run_battery_low_service()

        run_battery_depleted_service()


###############################################################################
# Periodically build and send a STATUS UPDATE message to the DCB
###############################################################################
def status_update_send_service():
    # If it is time for service...
    global StatusUpdateServiceTime
    if ((time.time() - StatusUpdateServiceTime) >= 1.00):
        StatusUpdateServiceTime = time.time()

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
###############################################################################
def run_left_tank_full_service():
    # If it is time for service...
    global LeftTankFullServiceTime
    if ((time.time() - LeftTankFullServiceTime) >= 0.200):
        LeftTankFullServiceTime = time.time()

    #printStatus("Left Tank Full Service")


###############################################################################
###############################################################################
def run_right_tank_full_service():
    # If it is time for service...
    global RightTankFullServiceTime
    if ((time.time() - RightTankFullServiceTime) >= 0.200):
        RightTankFullServiceTime = time.time()

    #printStatus("Right Tank Full Service")


###############################################################################
###############################################################################
def run_both_tanks_full_service():
    # If it is time for service...
    global BothTanksFullServiceTime
    if ((time.time() - BothTanksFullServiceTime) >= 0.200):
        BothTanksFullServiceTime = time.time()

    #printStatus("Both Tanks Full Service")


###############################################################################
###############################################################################
def run_battery_low_service():
    # If it is time for service...
    global BatteryLowServiceTime
    if ((time.time() - BatteryLowServiceTime) >= 0.200):
        BatteryLowServiceTime = time.time()

    #printStatus("Battery Low Service")


###############################################################################
###############################################################################
def run_battery_depleted_service():
    # If it is time for service...
    global BatteryDepletedServiceTime
    if ((time.time() - BatteryDepletedServiceTime) >= 0.200):
        BatteryDepletedServiceTime = time.time()

    #printStatus("Battery Depleted Service")




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


