from globals import *
import configparser


parser = None


###############################################################################
# Starts the CONFIG File parser
###############################################################################
def startup():
    global parser
    parser = configparser.ConfigParser()


###############################################################################
###############################################################################
def writeConfigSettings():
    global parser

    # Open our CONFIG file
    fp = open(CONFIG_FILE, 'w')

    # Write it with the latest SETTINGS
    parser.write(fp)

    # Close our CONFIG file
    fp.close()


###############################################################################
###############################################################################
def getFlowAnalysisEnabled():
    global parser

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Alarms', 'flowanalysisenabled')):
        return parser.get('Alarms', 'flowanalysisenabled')

    return '0'



###############################################################################
###############################################################################
def setFlowAnalysisEnabled(value):
    global parser

    if (parser.has_option('Alarms', 'flowanalysisenabled')):
        parser.set('Alarms', 'flowanalysisenabled', value)


###############################################################################
###############################################################################
def getFlowAnalysisPeriod():
    global parser

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Alarms', 'flowanalysisperiod')):
        return parser.get('Alarms', 'flowanalysisperiod')

    return '0'



###############################################################################
###############################################################################
def setFlowAnalysisPeriod(value):
    global parser

    if (parser.has_option('Alarms', 'flowanalysisperiod')):
        parser.set('Alarms', 'flowanalysisperiod', value)


###############################################################################
###############################################################################
def getFlowLowThreshold():
    global parser

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Alarms', 'flowlowthreshold')):
        return parser.get('Alarms', 'flowlowthreshold')

    return '0'



###############################################################################
###############################################################################
def setFlowLowThreshold(value):
    global parser

    if (parser.has_option('Alarms', 'flowlowthreshold')):
        parser.set('Alarms', 'flowlowthreshold', value)


###############################################################################
###############################################################################
def getFlowHighThreshold():
    global parser

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Alarms', 'flowhighthreshold')):
        return parser.get('Alarms', 'flowhighthreshold')

    return '0'



###############################################################################
###############################################################################
def setFlowHighThreshold(value):
    global parser

    if (parser.has_option('Alarms', 'flowhighthreshold')):
        parser.set('Alarms', 'flowhighthreshold', value)


###############################################################################
###############################################################################
def getLTankCalOffset():
    global parser

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Calibration', 'ltankcaloffset')):
        return parser.get('Calibration', 'ltankcaloffset')

    return '0'



###############################################################################
###############################################################################
def setLTankCalOffset(value):
    global parser

    if (parser.has_option('Calibration', 'ltankcaloffset')):
        parser.set('Calibration', 'ltankcaloffset', value)


###############################################################################
###############################################################################
def getRTankCalOffset():
    global parser

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Calibration', 'rtankcaloffset')):
        return parser.get('Calibration', 'rtankcaloffset')

    return '0'



###############################################################################
###############################################################################
def setRTankCalOffset(value):
    global parser

    if (parser.has_option('Calibration', 'rtankcaloffset')):
        parser.set('Calibration', 'rtankcaloffset', value)


###############################################################################
###############################################################################
def getPlayKeyPressTone():
    global parser

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Audio', 'playkeypresstone')):
        return parser.get('Audio', 'playkeypresstone')

    return '0'



###############################################################################
###############################################################################
def setPlayKeyPressTone(value):
    global parser

    if (parser.has_option('Audio', 'playkeypresstone')):
        parser.set('Audio', 'playkeypresstone', value)


###############################################################################
###############################################################################
def getPlayWarningTone():
    global parser

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Audio', 'playwarningtone')):
        return parser.get('Audio', 'playwarningtone')

    return '0'



###############################################################################
###############################################################################
def setPlayWarningTone(value):
    global parser

    if (parser.has_option('Audio', 'playwarningtone')):
        parser.set('Audio', 'playwarningtone', value)


###############################################################################
###############################################################################
def getPlayAlarmTone():
    global parser

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Audio', 'playalarmtone')):
        return parser.get('Audio', 'playalarmtone')

    return '0'



###############################################################################
###############################################################################
def setPlayAlarmTone(value):
    global parser

    if (parser.has_option('Audio', 'playalarmtone')):
        parser.set('Audio', 'playalarmtone', value)



