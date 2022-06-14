from datetime import datetime

# Define some global information
RUN_ON_CM4 = True
#RUN_ON_CM4 = False

# Define the dimensions of the touch screen display
SCREEN_WIDTH = 780
SCREEN_HEIGHT = 480

# Define parameters needed for serial port communication with DCB
if (RUN_ON_CM4):
    COMPORT = "/dev/ttyS0"
else:
    COMPORT = "COM5"
BAUD_RATE = 115200

# Define some fonts
SM_FONT = ('Tahoma', 18)
MD_FONT = ('Tahoma', 22)
LG_FONT = ("Georgia", 30)

# Define the CONFIG file name
CONFIG_FILE = "mcb_config.ini"

# Define some log file names
TELEM_FILE = "Logs/telemetry.log"
PATIENT_FILE = "Logs/patient.log"

# Define some snap shot file names
SNAP_COLOR_RAW =  'SnapShots/color_raw.jpg'
SNAP_COLOR_IMG =  'SnapShots/color_new.jpg'
SNAP_TURBID_RAW = 'SnapShots/turbid_raw.jpg'
SNAP_TURBID_IMG = 'SnapShots/turbid_new.jpg'

# Each Tank has some weight to it (determined empirically)
TANK_WEIGHT      = 130

TANK_FULL_VOLUME = 900
TANK_MAX_VOLUME  = 1000

DEFAULT_CAL_OFFSET = 100
MAXIMUM_CAL_OFFEST = 200


###############################################################################
###############################################################################
def getDateTimeStamp():
    dts = datetime.now().strftime("%Y-%m-%d %H:%M:%S: ")
    return dts

###############################################################################
###############################################################################
def printStatus(status_string):
    dts = getDateTimeStamp()
    print(dts + status_string)


