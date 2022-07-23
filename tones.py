from globals import *
if (RUN_ON_CM4):
    import RPi.GPIO as GPIO

AUDIO_PWM_PIN = 12

ToneGenerator = None


###############################################################################
###############################################################################
def initialize():
    global ToneGenerator

    if (RUN_ON_CM4):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(AUDIO_PWM_PIN, GPIO.OUT)
        ToneGenerator = GPIO.PWM(AUDIO_PWM_PIN, 2500)
    else:
        pass


###############################################################################
###############################################################################
def generate_tone(freq, duty=50):
    global ToneGenerator

    if (RUN_ON_CM4):
        # Start/Stop the PWM at the specified duty cycle
        if (freq == 0):
            ToneGenerator.stop()
        else:
            ToneGenerator.ChangeFrequency(freq)
            ToneGenerator.start(duty)
    else:
        pass


