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
def getMinFlowAlertEnabled():
    global parser

    value = False

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Alerts', 'minflowalertenabled')):
        if (parser.get('Alerts', 'minflowalertenabled') == '1'):
            value = True

    return value



###############################################################################
###############################################################################
def setMinFlowAlertEnabled(value):
    global parser

    if (parser.has_option('Alerts', 'minflowalertenabled')):
        if (value == True):
            parser.set('Alerts', 'minflowalertenabled', '1')
        else:
            parser.set('Alerts', 'minflowalertenabled', '0')


###############################################################################
###############################################################################
def getMaxFlowAlertEnabled():
    global parser

    value = False

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Alerts', 'maxflowalertenabled')):
        if (parser.get('Alerts', 'maxflowalertenabled') == '1'):
            value = True

    return value



###############################################################################
###############################################################################
def setMaxFlowAlertEnabled(value):
    global parser

    if (parser.has_option('Alerts', 'maxflowalertenabled')):
        if (value == True):
            parser.set('Alerts', 'maxflowalertenabled', '1')
        else:
            parser.set('Alerts', 'maxflowalertenabled', '0')




###############################################################################
###############################################################################
def getMinFlowVolume():
    global parser

    value = 0

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Alerts', 'minflowthreshold')):
        value = int(parser.get('Alerts', 'minflowthreshold'), 10)

    return value



###############################################################################
###############################################################################
def setMinFlowVolume(value):
    global parser

    if (parser.has_option('Alerts', 'minflowthreshold')):
        parser.set('Alerts', 'minflowthreshold', str(value))


###############################################################################
###############################################################################
def getMaxFlowVolume():
    global parser

    value = 0

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Alerts', 'maxflowthreshold')):
        value = int(parser.get('Alerts', 'maxflowthreshold'), 10)

    return value


###############################################################################
###############################################################################
def setMaxFlowVolume(value):
    global parser

    if (parser.has_option('Alerts', 'maxflowthreshold')):
        parser.set('Alerts', 'maxflowthreshold', str(value))


###############################################################################
###############################################################################
def getMinFlowHours():
    global parser

    value = 0

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Alerts', 'minflowhours')):
        value = int(parser.get('Alerts', 'minflowhours'))

    return value



###############################################################################
###############################################################################
def setMinFlowHours(value):
    global parser

    if (parser.has_option('Alerts', 'minflowhours')):
        parser.set('Alerts', 'minflowhours', str(value))


###############################################################################
###############################################################################
def getMaxFlowHours():
    global parser

    value = 0

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Alerts', 'maxflowhours')):
        value = parser.get('Alerts', 'maxflowhours')

    return value


###############################################################################
###############################################################################
def setMaxFlowHours(value):
    global parser

    if (parser.has_option('Alerts', 'maxflowhours')):
        parser.set('Alerts', 'maxflowhours', str(value))


###############################################################################
###############################################################################
def getLTankCalOffset():
    global parser

    value = 0

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Calibration', 'ltankcaloffset')):
        value = int(parser.get('Calibration', 'ltankcaloffset'), 10)

    return value


###############################################################################
###############################################################################
def setLTankCalOffset(value):
    global parser

    if (parser.has_option('Calibration', 'ltankcaloffset')):
        parser.set('Calibration', 'ltankcaloffset', str(value))


###############################################################################
###############################################################################
def getRTankCalOffset():
    global parser

    value = 0

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Calibration', 'rtankcaloffset')):
        value = int(parser.get('Calibration', 'rtankcaloffset'), 10)

    return value



###############################################################################
###############################################################################
def setRTankCalOffset(value):
    global parser

    if (parser.has_option('Calibration', 'rtankcaloffset')):
        parser.set('Calibration', 'rtankcaloffset', str(value))


###############################################################################
###############################################################################
def getPlayKeyPressTone():
    global parser

    value = False

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Audio', 'playkeypresstone')):
        if (parser.get('Audio', 'playkeypresstone') == '1'):
            value = True

    return value



###############################################################################
###############################################################################
def setPlayKeyPressTone(value):
    global parser

    if (parser.has_option('Audio', 'playkeypresstone')):
        if (value == True):
            parser.set('Audio', 'playkeypresstone', '1')
        else:
            parser.set('Audio', 'playkeypresstone', '0')


###############################################################################
###############################################################################
def getPlayWarningTone():
    global parser

    value = False

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Audio', 'playwarningtone')):
        if (parser.get('Audio', 'playwarningtone') == '1'):
            value = True

    return value



###############################################################################
###############################################################################
def setPlayWarningTone(value):
    global parser

    if (parser.has_option('Audio', 'playwarningtone')):
        if (value == True):
            parser.set('Audio', 'playwarningtone', '1')
        else:
            parser.set('Audio', 'playwarningtone', '0')


###############################################################################
###############################################################################
def getPlayAlarmTone():
    global parser

    value = False

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Audio', 'playalarmtone')):
        if (parser.get('Audio', 'playalarmtone') == '1'):
            value = True

    return value



###############################################################################
###############################################################################
def setPlayAlarmTone(value):
    global parser

    if (parser.has_option('Audio', 'playalarmtone')):
        if (value == True):
            parser.set('Audio', 'playalarmtone', '1')
        else:
            parser.set('Audio', 'playalarmtone', '0')


###############################################################################
###############################################################################
def getLightsAutoConfig():
    global parser

    value = 'Off'

    # Read the entire CONFIG file
    parser.read(CONFIG_FILE)

    # Extract our SETTING and return it if available
    if (parser.has_option('Lights', 'tanklightconfig')):
        value = parser.get('Lights', 'tanklightconfig')

    return value



###############################################################################
###############################################################################
def setLightsAutoConfig(value):
    global parser

    if (parser.has_option('Lights', 'tanklightconfig')):
        parser.set('Lights', 'tanklightconfig', value)



