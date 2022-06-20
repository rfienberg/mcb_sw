from globals import *
import mcb_config
import gui
import scram
import status
import analyze
import telemetry
import calibrate
import audio
import lights

###############################################################################
# This is the main process of our MCB application
###############################################################################
if __name__ == "__main__":
    # Start the CONFIG File parser
    mcb_config.startup()

    # Start up the Graphical User Interface
    gui.startup()

    # Open the SCRAM serial port for DCB communications
    scram.startup()

    # Start the TELEMETRY logger process
    telemetry.start_thread()

    # Start the STATUS process
    status.start_thread()

    # Start the ANALYZE process
    analyze.start_thread()

    # Pull the latest CONFIG settings
    calibrate.pull_calibation_settings()
    audio.pull_audio_settings()
    lights.pull_light_settings()

    # Start running the Graphical User Interface
    gui.mainloop()
