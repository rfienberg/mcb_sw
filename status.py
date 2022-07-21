#!/usr/bin/python

from globals import *
import threading
import time
import scram
import telemetry
import shutdown

import mcb_config
import patient
import lights


BATTERY_PERCENT_BAD = 10
BATTERY_PERCENT_LOW = 50

TANK_LIGHTS_CONFIG_OFF = '0'
TANK_LIGHTS_CONFIG_ON  = '1'
TANK_LIGHTS_CONFIG_ALS = '2'

STATUS_SLEEP_TIME = 0.400
Status1SecServiceTime = 0

# Variables to keep the latest status of the break-the-beam sensors
StatusTankDoor  = "Unknown"
StatusCartridge = "Unknown"
StatusTankLeft  = "Unknown"
StatusTankRight = "Unknown"


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

        # Check for changes in STATUS that should be logged
        log_status_changes()


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

    # Populate the Tank Light AUTO config STATUS character...
    my_status[8] = getTankLightsConfigCharacter()

    # Send our latest STATUS to the DCB
    status_string = "".join(my_status)
    #printStatus(status_string)
    rsp = scram.SendCommand(status_string)


###############################################################################
###############################################################################
def log_status_changes():
    global StatusTankDoor, StatusCartridge, StatusTankLeft, StatusTankRight

    # Check for a STATUS change of the Tank Door
    new_status = telemetry.getTankDoorStatus()
    if (new_status != StatusTankDoor):
        StatusTankDoor = new_status
        log_line = getDateTimeStamp() + "Tank Door is now " + new_status
        print(log_line)
        patient.write_log_line(log_line)

    # Check for a STATUS change of the Analysis Cartridge
    new_status = telemetry.getInstalledStatus('Cart')
    if (new_status != StatusCartridge):
        StatusCartridge = new_status
        log_line = getDateTimeStamp() + "Analysis Cartridge is now " + new_status
        print(log_line)
        patient.write_log_line(log_line)

    # Check for a STATUS change of the Left Tank
    new_status = telemetry.getInstalledStatus('Left')
    if (new_status != StatusTankLeft):
        StatusTankLeft = new_status
        log_line = getDateTimeStamp() + "Left Tank is now " + new_status
        print(log_line)
        patient.write_log_line(log_line)

    # Check for a STATUS change of the Right Tank
    new_status = telemetry.getInstalledStatus('Right')
    if (new_status != StatusTankRight):
        StatusTankRight = new_status
        log_line = getDateTimeStamp() + "Right Tank is now " + new_status
        print(log_line)
        patient.write_log_line(log_line)


###############################################################################
###############################################################################
def getTankLightsConfigCharacter():
    auto = mcb_config.getLightsAutoConfig()

    # Convert the text string  into a single character
    if (auto == lights.LIGHT_AUTO_OFF):
        return TANK_LIGHTS_CONFIG_OFF
    elif (auto == lights.LIGHT_AUTO_ON):
        return TANK_LIGHTS_CONFIG_ON
    elif (auto == lights.LIGHT_AUTO_ALS):
        return TANK_LIGHTS_CONFIG_ALS
    else:
        return 'F'


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



