#!/usr/bin/python
###############################################################################
# This script deals with Telemetry acquired from the Data Collection Board
###############################################################################

from globals import *
import threading
from calibrate import getCalibrationOffset
from datetime import datetime
import scram
import status
import shutdown
import time

GET_TELEMETRY_CMD = ">GT?\n"
GET_TELEMETRY_RSP_0_5 = '<GT: '

STATUS_UPDATE_CMD = ">SU: "

SOD_IDX = 0
TSB_IDX = (SOD_IDX+1)

TDS_IDX = (SOD_IDX+6)
CSS_IDX = (SOD_IDX+7)
LSS_IDX = (SOD_IDX+8)
RSS_IDX = (SOD_IDX+9)

LOS_IDX = (SOD_IDX+11)
ROS_IDX = (SOD_IDX+12)
LVS_IDX = (SOD_IDX+13)
RVS_IDX = (SOD_IDX+14)

OPM_IDX = (SOD_IDX+16)
BLS_IDX = (SOD_IDX+17)
ERR_IDX = (SOD_IDX+18)
FUT_IDX = (SOD_IDX+19)

LTV_IDX = (SOD_IDX+21)

RTV_IDX = (SOD_IDX+26)

BLV_IDX = (SOD_IDX+31)
FLG_IDX = (SOD_IDX+33)

TelemetryLatest = ""
TelemetryLock = threading.Lock()


###############################################################################
# Starts the TELEMETRY thread
###############################################################################
def start_thread():
    # Create a lock so multiple threads can access Telemetry
    #global TelemetryLock
    #TelemetryLock = threading.Lock()

    # Try to open the log file and write the header
    with open(TELEM_FILE, 'w') as file:
        file.write("Starting file\n")

    # Start a thread that periodically pulls in new Telemetry
    printStatus("Start-up TELEMETRY thread")
    global y
    y = threading.Thread(target=runTelemetryTask, daemon=True)
    y.start()


###############################################################################
# Stops the TELEMETRY thread
###############################################################################
def stop_thread():
    printStatus("Shut-down TELEMETRY thread")
    global y
    y.terminate()


###############################################################################
# Runs a thread that periodically pulls in new Telemetry
###############################################################################
def runTelemetryTask():
    global TelemetryLatest, TelemetryLock

    # Endless loop running TELEMETRY operations...
    while True:
        # Wait for the cycle to start...
        time.sleep(0.5)

        # Send the GET TELEMETRY command and wait for its response...
        telem = scram.SendCommand(GET_TELEMETRY_CMD)

        # Verify the response and decode its fields
        if (isTelemetryValid(telem)):

            # Extract and record the latest valid telemetry values
            fields = telem.split(':')
            TelemetryLock.acquire()
            TelemetryLatest = fields[1]
            TelemetryLock.release()
            #print(TelemetryLatest)

            # Tack on a Date/Time stamp
            dts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            telem_string = f"{dts}: {telem}"

            # Write the telemetry string to a log file
            with open(TELEM_FILE, 'a') as telemfile:
                telemfile.write(telem_string)

            # If the latest telemetry indicates a shut-down request...
            if (getShutdownStatus() == "Shutting-down"):
                shutdown.requestShutdown()

        else:
            TelemetryLock.acquire()
            TelemetryLatest = " 0000 0000 0000 0000 0000 0000 1B00 0000\n"
            TelemetryLock.release()


###############################################################################
# Returns True if telem is a valid Telemetry Response, False otherwise
###############################################################################
def isTelemetryValid(telem):
    # Verify that the telemetry response exists
    size = len(telem)-5
    if (size < 0):
        return False

    # Verify the response first 5 characters
    if (telem[0:5] != GET_TELEMETRY_RSP_0_5):
        return False

    # Extract the received checksum
    cks_received = int(telem[size:size+4], 16)

    # Compute the checksum of the received bytes
    cks_computed = 0
    for i in range (size):
        cks_computed += ord(telem[i])

    # Verify checksum match...
    if (cks_received != cks_computed):
        return False

    return True
 

###############################################################################
# Returns the latest Telemetry string of values from the DCB
###############################################################################
def getLatestTelemetry():
    global TelemetryLatest, TelemetryLock

    # Get the latest Telemetry
    TelemetryLock.acquire()
    telem = TelemetryLatest
    TelemetryLock.release()

    # If that Telemetry is invalid...
    if (len(telem) < 10):
        telem = ""

    return telem


###############################################################################
# Returns the latest Time Since Boot (in seconds)
###############################################################################
def getTimeSinceBoot():
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        tsb = 0
    else:
        tsb = int(telem[TSB_IDX:TSB_IDX+4], 16)
    return tsb


###############################################################################
# Returns the latest Shut-Down Status string
###############################################################################
def getShutdownStatus():
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        flags = 0
    else:
        flags = int(telem[FLG_IDX:FLG_IDX+2], 16)

    if (flags & 0x01):
        return "Shutting-down"
    else:
        return "Running"


###############################################################################
# Returns the latest Seated Status string for the specified side
###############################################################################
def getSeatedStatus(side):
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        sss = 'F'
    elif (side == 'Left'):
        sss = telem[LSS_IDX]
    elif (side == 'Right'):
        sss = telem[RSS_IDX]
    elif (side == 'Door'):
        sss = telem[TDS_IDX]
    else:
        sss = telem[CSS_IDX]

    if (sss == '0'):
        return "Unseated"
    elif (sss == '1'):
        return "Seated"
    else:
        return "Unknown"


###############################################################################
# Returns the latest Backlight Status string
###############################################################################
def getBacklightStatus():
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        bls = 'F'
    else:
        bls = telem[BLS_IDX]

    if (bls == '0'):
        return "Off"
    elif (bls == '1'):
        return "Color"
    elif (bls == '2'):
        return "Turbidity"
    elif (bls == '3'):
        return "Testing"
    else:
        return "Unknown"


###############################################################################
# Returns the latest Battery Voltage (in centi-volts)
###############################################################################
def getBatteryCentiVolts():
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        blv = 0
    else:
        blv = int(telem[BLV_IDX:BLV_IDX+2], 16)
    return blv


###############################################################################
# Returns the latest Battery Charge Status (in percentage of full)
###############################################################################
def getBatteryChargePercent():
    blv = getBatteryCentiVolts()

    # Assuming MIN = 21.0 cV and MAX = 30.0 cV
    if (blv >= 30):
        bcp = 100.0
    elif (blv <= 21):
        bcp = 0.0
    else:
        bcp = round(((blv - 21.0) / 0.08))

    return bcp


###############################################################################
# Returns the latest Battery Charging Status string
###############################################################################
def getBatteryChargeStatus():
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        flags = 0
    else:
        flags = int(telem[FLG_IDX:FLG_IDX+2], 16)

    if (flags & 0x04):
        return "Charging"
    else:
        return "Not Charging"


###############################################################################
# Returns the latest Battery Plug-In Status string
###############################################################################
def getBatteryPlugStatus():
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        flags = 0
    else:
        flags = int(telem[FLG_IDX:FLG_IDX+2], 16)

    if (flags & 0x02):
        return "Plugged-In"
    else:
        return "Unplugged"


###############################################################################
# Returns the latest Error Code integer
###############################################################################
def getErrorCode():
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        err = 0
    else:
        err = int(telem[ERR_IDX], 16)
    return err


###############################################################################
# Returns the latest Tasnk Light Status string for the specified side
###############################################################################
def getTankLightStatus(side):
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        flags = 0
    else:
        flags = int(telem[FLG_IDX:FLG_IDX+2], 16)

    if (side == 'Left'):
        bitmask = 0x08
    else:
        bitmask = 0x10

    if (flags & bitmask):
        return "Illuminated"
    else:
        return "Extinguished"


###############################################################################
# Returns the latest Tank Space Status string for the specified side
###############################################################################
def getTankSpaceStatus(side):
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        ofs = 'F'
    elif (side == 'Left'):
        ofs = telem[LOS_IDX]
    else:
        ofs = telem[ROS_IDX]

    if (ofs == '0'):
        return "Fillable"
    elif (ofs == '1'):
        return "Overfilled"
    else:
        return "Unknown"


###############################################################################
# Returns the latest Tank Valve Status string for the specified side
###############################################################################
def getTankValveStatus(side):
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        vps = 'F'
    elif (side == 'Left'):
        vps = telem[LVS_IDX]
    else:
        vps = telem[RVS_IDX]

    if (vps == '0'):
        return "Opening"
    elif (vps == '1'):
        return "Closing"
    elif (vps == '2'):
        return "Opened"
    elif (vps == '3'):
        return "Closed"
    else:
        return "Unknown"


###############################################################################
# Returns the latest Raw Tank Volume (in mL) for the specified side
###############################################################################
def getRawTankVolume(side):
    telem = getLatestTelemetry()

    if (len(telem) == 0):
        tvs = 0
    elif (side == 'Left'):
        tvs = int(telem[LTV_IDX:LTV_IDX+4], 16)
    else:
        tvs = int(telem[RTV_IDX:RTV_IDX+4], 16)
    return tvs


###############################################################################
# Returns the latest Real Tank Volume (in mL) for the specified side
###############################################################################
def getRealTankVolume(side="Left"):
    if (side == "Left"):
        volume = getRawTankVolume("Left")
        cal_offset = getCalibrationOffset("Left") 
    else:
        volume = getRawTankVolume("Right")
        cal_offset = getCalibrationOffset("Right") 

    # Adjust volume for calibration offset
    if (volume > cal_offset):
        volume = volume - cal_offset
    else:
        volume = 0

    # Adjust for TANK_WEIGHT
    if (volume > TANK_WEIGHT):
        volume = volume - TANK_WEIGHT
    else:
        volume = 0

    # Clamp VOLUME to no more than expected MAXIMUM
    if (volume > TANK_MAX_VOLUME):
        volume = TANK_MAX_VOLUME

    return volume


