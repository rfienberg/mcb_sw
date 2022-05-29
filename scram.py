#!/usr/bin/python

from globals import *
import serial, threading

###############################################################################
###############################################################################
def startup():
    global scram
    global lock

    lock = threading.Lock()

    # Create the serial port object
    scram = serial.Serial()
    scram.port     = COMPORT
    scram.baudrate = BAUD_RATE
    scram.timeout  = 1

    # Try to open the serial port
    try:
        scram.open()
    except:
        print("error opening serial port")

    # Get the DCB version string
    rsp = SendCommand(">GV?\n")
    print(rsp)


###############################################################################
# Sends a specified CMD string out the serial port and 
# returns its corresponding RSP string
###############################################################################
def SendCommand(cmd_string):
    lock.acquire()

    rsp = ""

    if (scram.is_open):
        # Start with empty buffers
        scram.flushInput()
        scram.flushOutput()

        # Send the Get Telemetry command...
        scram.write(bytes(cmd_string, 'utf-8'))

        # Receive the response
        rsp = scram.readline().decode()

    lock.release()

    return rsp


