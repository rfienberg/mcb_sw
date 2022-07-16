###############################################################################
# Filename: dcb.py
# Purpose: Control the Data Collection Board (DCB) over its SCRAM interface
###############################################################################
#!/usr/bin/python

from globals import *
import scram


###############################################################################
###############################################################################
def sendBacklightCommand(pattern):
    if (pattern == 'white'):
        cmd = ">SC: F2FF\n"
    elif (pattern == 'red'):
        cmd = ">SC: F4FF\n"
    elif (pattern == 'green'):
        cmd = ">SC: F5FF\n"
    elif (pattern == 'blue'):
        cmd = ">SC: F6FF\n"
    elif (pattern == 'hatch'):
        cmd = ">SC: F3FF\n"
    else:
        cmd = ">SC: F1FF\n"

    rsp = scram.SendCommand(cmd)



###############################################################################
###############################################################################
def sendValveFlowCommand(control):
    if (control == 'Auto'):
        cmd = ">SC: FF1F\n"
    elif (control == 'Stop'):
        cmd = ">SC: FF2F\n"
    else:
        cmd = ">SC: FFFF\n"

    rsp = scram.SendCommand(cmd)



###############################################################################
###############################################################################
def sendTankLightCommand(control):
    if (control == 'Off'):
        cmd = ">SC: FFF1\n"
    elif (control == 'On'):
        cmd = ">SC: FFF2\n"
    elif (control == 'Auto'):
        cmd = ">SC: FFF3\n"
    else:
        cmd = ">SC: FFF3\n"

    rsp = scram.SendCommand(cmd)


