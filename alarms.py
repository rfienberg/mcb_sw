from globals import *
import threading
import time
import tkinter as tk
import audio
import alerts
import status
import screens
import shutdown
import mcb_config


# Definitions for popup window theme colors
ALARM_COLOR = 'red'
ALERT_COLOR = 'yellow'
WARN_COLOR  = 'orange'

# Definitions for popup window dimension/position
POPUP_WIDTH  = 700
POPUP_HEIGHT = 200
POPUP_X = 40
POPUP_Y = 100

# Definitions for HOLDOFF periods
INITIAL_HOLDOFF_SECS = 60
WARNING_HOLDOFF_SECS = 60
ALERT_HOLDOFF_SECS   = 60
ALARM_HOLDOFF_SECS   = 60

# Enumeration of alarm detection states
ALARM_STATE_HOLDOFF  = 0
ALARM_STATE_DETECT   = 1
ALARM_STATE_WARNING  = 2
ALARM_STATE_ALERTING = 3
ALARM_STATE_ALARMING = 4

# Definitions for alarm tone timings
ALARMS_SLEEP_TIME   = 0.200
WARNING_TONE_TICKS  = 3
WARNING_GAP_TICKS   = 15
ALERTING_TONE_TICKS = 3
ALERTING_GAP_TICKS  = 15
ALARMING_TONE_TICKS = 3
ALARMING_GAP_TICKS  = 15

# Global variables
Alarm1SecServiceTime = 0
AlarmState = ALARM_STATE_HOLDOFF
AlarmHoldoffSecs = WARNING_HOLDOFF_SECS
AlarmTicks = 0

LeftTankFullCount    = 0
RightTankFullCount   = 0
BatteryIsLowCount    = 0
BatteryDepletedCount = 0

AlarmMessage   = ""
AlertMessage   = ""
WarningMessage = ""


###############################################################################
# Starts the ALARMS thread
###############################################################################
def start_thread():
    printStatus("Start-up ALARMS thread")
    global y
    y = threading.Thread(target=runAlarmsTask, daemon=True)
    y.start()


###############################################################################
# Stops the ALARMS thread
###############################################################################
def stop_thread():
    printStatus("Shut-down ALARMS thread")
    global y
    y.terminate()


###############################################################################
# Run the ALARMS thread
###############################################################################
def runAlarmsTask():
    # Initialize this thread
    start_holdoff_period(INITIAL_HOLDOFF_SECS)

    # Endless loop running ALARMS operations...
    while True:

        # If it is time for the once-per-second service...
        global Alarm1SecServiceTime
        if ((time.time() - Alarm1SecServiceTime) >= 1.00):
            Alarm1SecServiceTime = time.time()

            # Update the alarm sensor counters
            update_sensor_counters()

            # Service the HOLDOFF seconds here
            global AlarmHoldoffSecs
            if (AlarmHoldoffSecs):
                AlarmHoldoffSecs = AlarmHoldoffSecs - 1

        # Run the ALARMS servicing
        run_state_machine()

        # Sleep to allow other things to occur
        time.sleep(ALARMS_SLEEP_TIME)


###############################################################################
###############################################################################
def run_state_machine():
    global AlarmState, AlarmTicks, AlarmHoldoffSecs

    #----------------------------------------------------------------
    # Handle the HOLDOFF state here - 
    #----------------------------------------------------------------
    if (AlarmState == ALARM_STATE_HOLDOFF):
        # Once the HOLDOFF period has expired then start DETECTing again
        if (AlarmHoldoffSecs == 0):
            AlarmTicks = 0
            AlarmState = ALARM_STATE_DETECT

    #----------------------------------------------------------------
    # Handle the DETECT state here - 
    #----------------------------------------------------------------
    elif (AlarmState == ALARM_STATE_DETECT):
        # Test for ALARM conditions
        if (check_for_alarm_condition()):
            AlarmState = ALARM_STATE_ALARMING

        # Test for ALERT conditions
        elif (check_for_alert_condition()):
            AlarmState = ALARM_STATE_ALERTING

        # Test for WARNING conditions
        elif (check_for_warn_condition()):
            AlarmState = ALARM_STATE_WARNING

    #----------------------------------------------------------------
    # Handle the ALARMING state here - 
    #----------------------------------------------------------------
    elif (AlarmState == ALARM_STATE_ALARMING):
        # Run the ALARM tone
        AlarmTicks = AlarmTicks + 1
        if (mcb_config.getPlayAlarmTone()):
            if (AlarmTicks == 1):
                audio.play_audio_tone(2500, 50)
            elif (AlarmTicks == (1 + (1 * ALARMING_TONE_TICKS))):
                audio.play_audio_tone(2000, 50)
            elif (AlarmTicks == (1 + (2 * ALARMING_TONE_TICKS))):
                audio.play_audio_tone(0)
            elif (AlarmTicks >= (1 + (2 * ALARMING_TONE_TICKS) + (ALARMING_GAP_TICKS))):
                AlarmTicks = 0

    #----------------------------------------------------------------
    # Handle the ALERTING state here - 
    #----------------------------------------------------------------
    elif (AlarmState == ALARM_STATE_ALERTING):
        # Run the ALERT tone
        AlarmTicks = AlarmTicks + 1
        if (AlarmTicks == 1):
            audio.play_audio_tone(2500, 50)
        elif (AlarmTicks == (1 + (1 * ALERTING_TONE_TICKS))):
            audio.play_audio_tone(2000, 50)
        elif (AlarmTicks == (1 + (2 * ALERTING_TONE_TICKS))):
            audio.play_audio_tone(0)
        elif (AlarmTicks >= (1 + (2 * ALERTING_TONE_TICKS) + (ALERTING_GAP_TICKS))):
            AlarmTicks = 0

    #----------------------------------------------------------------
    # Handle the WARNING state here - 
    #----------------------------------------------------------------
    elif (AlarmState == ALARM_STATE_WARNING):
        # Run the WARNING tone
        AlarmTicks = AlarmTicks + 1
        if (mcb_config.getPlayWarningTone()):
            if (AlarmTicks == 1):
                audio.play_audio_tone(2500, 50)
            elif (AlarmTicks == (1 + (1 * WARNING_TONE_TICKS))):
                audio.play_audio_tone(2000, 50)
            elif (AlarmTicks == (1 + (2 * WARNING_TONE_TICKS))):
                audio.play_audio_tone(0)
            elif (AlarmTicks >= (1 + (2 * WARNING_TONE_TICKS) + (WARNING_GAP_TICKS))):
                AlarmTicks = 0

    #----------------------------------------------------------------
    # DEFAULT - should not get here
    #----------------------------------------------------------------
    else:
        start_holdoff_period(INITIAL_HOLDOFF_SECS)


###############################################################################
###############################################################################
def start_holdoff_period(secs):
    global AlarmState, AlarmHoldoffSecs

    # Start a new HOLDOFF period
    AlarmHoldoffSecs = secs
    AlarmState = ALARM_STATE_HOLDOFF

    # Stop any alarm tones
    audio.play_audio_tone(0)


###############################################################################
###############################################################################
def update_sensor_counters():
    global LeftTankFullCount, RightTankFullCount
    global BatteryIsLowCount, BatteryDepletedCount

    # Update the LEFT Tank Full counter
    if (status.isTankFull("Left")):
        if (LeftTankFullCount < 1000):
            LeftTankFullCount = LeftTankFullCount + 1
    else:
        if (LeftTankFullCount > 0):
            LeftTankFullCount = LeftTankFullCount - 1

    # Update the RIGHT Tank Full counter
    if (status.isTankFull("Right")):
        if (RightTankFullCount < 1000):
            RightTankFullCount = RightTankFullCount + 1
    else:
        if (RightTankFullCount > 0):
            RightTankFullCount = RightTankFullCount - 1

    # Update the BATTERY is LOW counter
    if (status.isBatteryLow()):
        if (BatteryIsLowCount < 1000):
            BatteryIsLowCount = BatteryIsLowCount + 1
    else:
        if (BatteryIsLowCount > 0):
            BatteryIsLowCount = BatteryIsLowCount - 1

    # Update the BATTERY is DEPLETED counter
    if (status.isBatteryDepleted()):
        if (BatteryDepletedCount < 1000):
            BatteryDepletedCount = BatteryDepletedCount + 1
    else:
        if (BatteryDepletedCount > 0):
            BatteryDepletedCount = BatteryDepletedCount - 1


###############################################################################
###############################################################################
def check_for_alarm_condition():
    # If both Tanks needs emptying...
    if ((isLeftTankFull()) and (isRightTankFull())):
        msg = "Both tanks are FULL!"
        post_alarm_message(msg)
        return True

    # If the Battery is DEPLETED...
    if (isBatteryDepleted()):
        msg = "Battery charge is depleted!"
        post_alarm_message(msg)
        return True

    return False


###############################################################################
###############################################################################
def check_for_alert_condition():
    # If the FLOW is too LOW...
    if (isFlowTooLow()):
        msg = "Flow has dropped too LOW!"
        post_alert_message(msg)
        return True

    # If the FLOW is too HIGH...
    if (isFlowTooHigh()):
        msg = "Flow has risen too HIGH!"
        post_alert_message(msg)
        return True

    return False


###############################################################################
###############################################################################
def check_for_warn_condition():
    # If the Left Tank needs emptying...
    if ((isLeftTankFull()) and (not isRightTankFull())):
        msg = "Left Tank needs to be emptied!"
        post_warning_message(msg)
        return True

    # If the Right Tank needs emptying...
    if ((isRightTankFull()) and (not isLeftTankFull())):
        msg = "Right Tank needs to be emptied!"
        print(msg)
        post_warning_message(msg)
        return True

    # If the Battery is LOW...
    if ((isBatteryLow()) and ( not isBatteryDepleted())):
        msg = "Battery needs to be charged!"
        post_warning_message(msg)
        return True

    return False


###############################################################################
###############################################################################
def isLeftTankFull():
    global LeftTankFullCount

    # If the TANK has been FULL for at least 30 seconds...
    if (LeftTankFullCount > 30):
        return True
    else:
        return False


###############################################################################
###############################################################################
def isRightTankFull():
    global RightTankFullCount

    # If the TANK has been FULL for at least 30 seconds...
    if (RightTankFullCount > 30):
        return True
    else:
        return False


###############################################################################
###############################################################################
def isFlowTooLow():
    if (alerts.isFlowTooLow()):
        return True
    else:
        return False


###############################################################################
###############################################################################
def isFlowTooHigh():
    if (alerts.isFlowTooHigh()):
        return True
    else:
        return False


###############################################################################
###############################################################################
def isBatteryLow():
    global BatteryIsLowCount

    # If the BATTERY has been LOW for at least 30 seconds...
    if (BatteryIsLowCount > 30):
        return True
    else:
        return False


###############################################################################
###############################################################################
def isBatteryDepleted():
    global BatteryDepletedCount

    # If the BATTERY has been DEPLETED for at least 30 seconds...
    if (BatteryDepletedCount > 30):
        return True
    else:
        return False


###############################################################################
###############################################################################
def post_alarm_message(msg):
    global AlarmMessage
    AlarmMessage = msg
    #print(msg)


###############################################################################
###############################################################################
def post_alert_message(msg):
    global AlertMessage
    AlertMessage = msg
    #print(msg)


###############################################################################
###############################################################################
def post_warning_message(msg):
    global WarningMessage
    WarningMessage = msg
    #print(msg)


###############################################################################
###############################################################################
def start_periodic_popup_checks(window):
    global root

    # Make the parent window the root
    root = window

    # Perform the 1st periodic popup check
    periodic_popup_check()


###############################################################################
###############################################################################
def periodic_popup_check():
    global AlarmMessage, AlertMessage, WarningMessage
    global root

    # If a new ALARM message has been posted...
    if (len(AlarmMessage) > 0):
        popup_alarm_screen(AlarmMessage)
        AlarmMessage = ""

    # If a new ALERT message has been posted...
    elif (len(AlertMessage) > 0):
        popup_alert_screen(AlertMessage)
        AlertMessage = ""

    # If a new WARNING message has been posted...
    elif (len(WarningMessage) > 0):
        popup_warning_screen(WarningMessage)
        WarningMessage = ""

    # As long as we are not shutting down...
    if (shutdown.isShutDownRequested() == False):

        # After 1 second, perform another update
        root.after(1000, periodic_popup_check)


###############################################################################
###############################################################################
def popup_alarm_screen(msg):
    global alarm_screen

    alarm_screen = tk.Toplevel()
    alarm_screen.geometry("%dx%d+%d+%d" % (POPUP_WIDTH, POPUP_HEIGHT, POPUP_X, POPUP_Y))
    alarm_screen.attributes('-topmost',True)
    alarm_screen.overrideredirect(1)

    outer = tk.Frame(alarm_screen)
    outer.configure(width=POPUP_WIDTH, height=POPUP_HEIGHT)
    outer.configure(background=ALARM_COLOR)
    outer.configure(highlightbackground='black', highlightthickness=2)
    inner = tk.Frame(outer)
    inner.configure(highlightbackground='black', highlightthickness=2)
    outer.pack(fill='both')
    inner.pack(fill='both', padx=20, pady=20)

    left  = tk.Frame(inner)
    right = tk.Frame(inner)
    left.grid( row=0, column=0, padx=5, pady=5)
    right.grid(row=0, column=1, pady=5)

    icon = tk.Label(left)
    icon.configure(image=screens.urgent_icon)
    icon.grid(row=0, column=0, padx=5)

    l1 = tk.Label(right)
    l1.configure(font=SM_FONT, fg='black')
    l1.configure(text=msg)
    b1 = tk.Button(right)
    b1.configure(image=screens.blk_dismiss_btn_icon, borderwidth=0)
    b1.configure(command=popdown_alarm_screen)
    l1.grid(row=0, column=0, pady=10)
    b1.grid(row=1, column=0, pady=8)

    alarm_screen.mainloop()


###############################################################################
###############################################################################
def popdown_alarm_screen():
    # Chirp
    screens.play_key_tone()

    # Destroy the pop-up
    alarm_screen.destroy()
    alarm_screen.quit()

    # Start a new HOLDOFF period
    start_holdoff_period(ALARM_HOLDOFF_SECS)


###############################################################################
###############################################################################
def popup_alert_screen(msg):
    global alert_screen

    alert_screen = tk.Toplevel()
    alert_screen.geometry("%dx%d+%d+%d" % (POPUP_WIDTH, POPUP_HEIGHT, POPUP_X, POPUP_Y))
    alert_screen.attributes('-topmost',True)
    alert_screen.overrideredirect(1)

    outer = tk.Frame(alert_screen)
    outer.configure(width=POPUP_WIDTH, height=POPUP_HEIGHT)
    outer.configure(background=ALERT_COLOR)
    outer.configure(highlightbackground='black', highlightthickness=2)
    inner = tk.Frame(outer)
    inner.configure(highlightbackground='black', highlightthickness=2)
    outer.pack(fill='both')
    inner.pack(fill='both', padx=20, pady=20)

    left  = tk.Frame(inner)
    right = tk.Frame(inner)
    left.grid( row=0, column=0, padx=5, pady=5)
    right.grid(row=0, column=1, pady=5)

    icon = tk.Label(left)
    icon.configure(image=screens.alert_icon)
    icon.grid(row=0, column=0, padx=5)

    l1 = tk.Label(right)
    l1.configure(font=SM_FONT, fg='black')
    l1.configure(text=msg)
    b1 = tk.Button(right)
    b1.configure(image=screens.blk_dismiss_btn_icon, borderwidth=0)
    b1.configure(command=popdown_alert_screen)
    l1.grid(row=0, column=0, pady=10)
    b1.grid(row=1, column=0, pady=8)

    alert_screen.mainloop()


###############################################################################
###############################################################################
def popdown_alert_screen():
    # Chirp
    screens.play_key_tone()

    # Destroy the pop-up
    alert_screen.destroy()
    alert_screen.quit()

    # Start a new HOLDOFF period
    start_holdoff_period(ALERT_HOLDOFF_SECS)


###############################################################################
###############################################################################
def popup_warning_screen(msg):
    global warning_screen

    warning_screen = tk.Toplevel()
    warning_screen.geometry("%dx%d+%d+%d" % (POPUP_WIDTH, POPUP_HEIGHT, POPUP_X, POPUP_Y))
    warning_screen.attributes('-topmost',True)
    warning_screen.overrideredirect(1)

    outer = tk.Frame(warning_screen)
    outer.configure(width=POPUP_WIDTH, height=POPUP_HEIGHT)
    outer.configure(background=WARN_COLOR)
    outer.configure(highlightbackground='black', highlightthickness=2)
    inner = tk.Frame(outer)
    inner.configure(highlightbackground='black', highlightthickness=2)
    outer.pack(fill='both')
    inner.pack(fill='both', padx=20, pady=20)

    left  = tk.Frame(inner)
    right = tk.Frame(inner)
    left.grid( row=0, column=0, padx=5, pady=5)
    right.grid(row=0, column=1, pady=5)

    icon = tk.Label(left)
    icon.configure(image=screens.warning_icon)
    icon.grid(row=0, column=0, padx=5)

    l1 = tk.Label(right)
    l1.configure(font=SM_FONT, fg='black')
    l1.configure(text=msg)
    b1 = tk.Button(right)
    b1.configure(image=screens.blk_dismiss_btn_icon, borderwidth=0)
    b1.configure(command=popdown_warning_screen)
    l1.grid(row=0, column=0, pady=10)
    b1.grid(row=1, column=0, pady=8)

    warning_screen.mainloop()


###############################################################################
###############################################################################
def popdown_warning_screen():
    # Chirp
    screens.play_key_tone()

    # Destroy the pop-up
    warning_screen.destroy()
    warning_screen.quit()

    # Start a new HOLDOFF period
    start_holdoff_period(WARNING_HOLDOFF_SECS)




