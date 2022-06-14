#!/usr/bin/python

from globals import *
import serial, threading

###############################################################################
###############################################################################
def startup():
    global scram_port, lock

    lock = threading.Lock()

    # Create the serial port object
    scram_port = serial.Serial()
    scram_port.port     = COMPORT
    scram_port.baudrate = BAUD_RATE
    scram_port.timeout  = 1

    # Try to open the serial port
    try:
        scram_port.open()
    except:
        print("Error opening serial port")

    # Get the DCB version string
    rsp = SendCommand(">GV?\n")
    print(rsp)


###############################################################################
# Sends a specified CMD string out the serial port and 
# returns its corresponding RSP string
###############################################################################
def SendCommand(cmd_string):
    global lock
    lock.acquire()

    rsp = ""

    if (scram_port.is_open):
        # Start with empty buffers
        scram_port.flushInput()
        scram_port.flushOutput()

        # Send the Get Telemetry command...
        scram_port.write(bytes(cmd_string, 'utf-8'))
        #print(cmd_string)

        # Receive the response
        rsp = scram_port.readline().decode()
        #print(rsp)

    lock.release()

    return rsp


