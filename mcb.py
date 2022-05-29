from globals import *
import mcb_config
import gui
import scram
import status
import analyze
import telemetry
import calibrate
import audio

###############################################################################
# This is the main thread of our MCB application
###############################################################################
if __name__ == "__main__":
    # Start the CONFIG File parser
    mcb_config.startup()

    # Start up the Graphical User Interface
    gui.startup()

    # Open the SCRAM serial port for DCB communications
    scram.startup()

    # Start the TELEMETRY logger thread
    telemetry.startup()

    # Start the STATUS thread
    status.startup()

    # Start the ANALYZE thread
    analyze.startup()

    # Pull the latest CONFIG settings
    calibrate.pullSettings()
    audio.pullSettings()

    # Start running the Graphical User Interface
    gui.mainloop()
