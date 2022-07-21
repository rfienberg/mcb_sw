#!/usr/bin/python

from globals import *
import serial
import threading


###############################################################################
###############################################################################
def startup():
    global scram_port, ScramLock

    # Create a lock for multi-threading
    ScramLock = threading.Lock()

    # Create the serial port object
    scram_port = serial.Serial()
    scram_port.port     = COMPORT
    scram_port.baudrate = BAUD_RATE
    scram_port.timeout  = 1

    # Attempt to open the serial port
    if (open_scram_port()):
        return True
    else:
        return False


###############################################################################
# Sends a specified CMD string out the serial port and 
# returns its corresponding RSP string
###############################################################################
def SendCommand(cmd_string):
    global ScramLock

    rsp = ""

    # Make sure the serial port is connected...
    if (not isScramConnected()):
        if (open_scram_port()):
            printStatus("Restored serial port connection")

    # As long as it is connected...
    if (isScramConnected()):
        ScramLock.acquire()

        # Start with empty buffers
        scram_port.flushInput()
        scram_port.flushOutput()

        # Send the specified command string...
        scram_port.write(bytes(cmd_string, 'utf-8'))

        # Receive the DCB response
        rsp = scram_port.readline().decode()

        # If we timed-out waiting for the response...
        if (len(rsp) == 0):
            # Close the connection
            scram_port.close()
            printStatus("Lost serial port connection")

        ScramLock.release()

    return rsp


###############################################################################
###############################################################################
def open_scram_port():
    # Attempt to open the SCRAM serial port
    try:
        scram_port.open()
        return True
    except:
        return False


###############################################################################
###############################################################################
def isScramConnected():
    if (scram_port.is_open):
        return True
    else:
        return False


