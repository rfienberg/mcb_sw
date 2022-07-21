from globals import *
import mcb_config
import dcb
import gui
import scram
import status
import alarms
import analyze
import telemetry
import calibrate
import audio
import lights
import patient

MCB_VERSION = "0.1.00"


###############################################################################
# This is the main process of our MCB application
###############################################################################
if __name__ == "__main__":
    # Log the startup event
    log_line = getDateTimeStamp() + "MCB started up!"
    print(log_line.rstrip())
    patient.write_log_line("\n------------------------------------------")
    patient.write_log_line(log_line)

    # Start the CONFIG File parser
    mcb_config.startup()

    # Start up the AUDIO interface
    audio.startup()

    # Start up the Graphical User Interface
    gui.startup()

    # Attempt to open the SCRAM serial port for DCB communications
    if (scram.startup()):
        scram_status = "Successfully opened serial port"
    else:
        scram_status = "Error opening serial port"

    # Log the SCRAM startup results
    log_line = getDateTimeStamp() + scram_status
    print(log_line)
    patient.write_log_line(log_line)

    # Log the SW version
    log_line = getDateTimeStamp() + "MCB Version=" + MCB_VERSION
    print(log_line)
    patient.write_log_line(log_line)

    # Log the FW version
    log_line = getDateTimeStamp() + "DCB Version=" + dcb.getDcbFwVersionString()
    print(log_line)
    patient.write_log_line(log_line)

    # Start the TELEMETRY logger thread
    telemetry.start_thread()

    # Start the STATUS thread
    status.start_thread()

    # Start the ALARMS thread
    alarms.start_thread()

    # Start the ANALYZE thread
    analyze.start_thread()

    # Pull the latest CONFIG settings
    calibrate.pull_calibation_settings()
    audio.pull_audio_settings()
    lights.pull_light_settings()

    # Log the Cal Offsets
    offset = calibrate.getCalibrationOffset('Left')
    log_line = getDateTimeStamp() + "Left  Cal Offset = " + str(offset)
    print(log_line)
    patient.write_log_line(log_line)

    offset = calibrate.getCalibrationOffset('Right')
    log_line = getDateTimeStamp() + "Right Cal Offset = " + str(offset)
    print(log_line)
    patient.write_log_line(log_line)

    # Start running the Graphical User Interface
    gui.mainloop()
