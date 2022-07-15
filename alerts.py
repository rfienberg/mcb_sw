from globals import *
import tkinter as tk
import screens
import flow
import mcb_config


DISABLED_COLOR = '#64A0DC'
ENABLED_COLOR  = SETUP_COLOR
ADJ_FONT = ('Calibri', 22)


# Define default Alert configuration settings
ConfigMinFlowAlertEnabled = False
ConfigMaxFlowAlertEnabled = False
ConfigMinFlowVolume = 100
ConfigMaxFlowVolume = 500
ConfigMinFlowHours = 1
ConfigMaxFlowHours = 1

# Flags for TOO LOW and TOO HIGH
FlowIsTooLow  = False
FlowIsTooHigh = False


###############################################################################
###############################################################################
def testForFlowTooLow(time_in_secs):
    global FlowIsTooLow

    # As long as this ALERT mechanism is enabled...
    if (mcb_config.getMinFlowAlertEnabled()):
        # Compute the timestamp range we will sum over
        end_ts = time_in_secs
        start_ts = end_ts - (3600 * ConfigMinFlowHours)

        # Sum up the flow deltas over this range
        (flow_total, count) = flow.compute_flow_over_period(start_ts, end_ts)

        # Don't test the sum until we have enough data
        if (count < (60 * ConfigMinFlowHours)):
            FlowIsTooLow = False
        # Test if this sum falls below the threshold
        elif (flow_total < ConfigMinFlowVolume):
            FlowIsTooLow = True
        else:
            FlowIsTooLow = False
    else:
        FlowIsTooLow = False


###############################################################################
###############################################################################
def testForFlowTooHigh(time_in_secs):
    global FlowIsTooHigh

    # As long as this ALERT mechanism is enabled...
    if (mcb_config.getMaxFlowAlertEnabled()):
        # Compute the timestamp range we will search over
        end_ts = time_in_secs
        start_ts = end_ts - (3600 * ConfigMaxFlowHours)

        # Sum up the flow deltas over this range
        (flow_total, count) = flow.compute_flow_over_period(start_ts, end_ts)

        # Test if this sum rises above the threshold
        if (flow_total > ConfigMaxFlowVolume):
            FlowIsTooHigh = True
        else:
            FlowIsTooHigh = False
    else:
        FlowIsTooHigh = False


###############################################################################
###############################################################################
def isFlowTooLow():
    global FlowIsTooLow

    # If this ALERT is disabled...
    if (mcb_config.getMinFlowAlertEnabled() == False):
        return False

    # Otherwise, return our flag's value
    return FlowIsTooLow


###############################################################################
###############################################################################
def isFlowTooHigh():
    global FlowIsTooHigh

    # If this ALERT is disabled...
    if (mcb_config.getMaxFlowAlertEnabled() == False):
        return False

    # Otherwise, return our flag's value
    return FlowIsTooHigh


###############################################################################
###############################################################################
def show_setup_screen():
    global this_screen

    # Pull the CONFIG file values into local settings
    pull_alert_settings()

    this_screen.tkraise()


###############################################################################
###############################################################################
def pull_alert_settings():
    global ConfigMinFlowAlertEnabled, ConfigMaxFlowAlertEnabled
    global ConfigMinFlowVolume, ConfigMaxFlowVolume
    global ConfigMinFlowHours, ConfigMaxFlowHours

    # Pull the CONFIG settings from the INI file 
    # and store them into local variables
    ConfigMinFlowAlertEnabled = mcb_config.getMinFlowAlertEnabled()
    ConfigMaxFlowAlertEnabled = mcb_config.getMaxFlowAlertEnabled()

    ConfigMinFlowVolume = mcb_config.getMinFlowVolume()
    ConfigMaxFlowVolume = mcb_config.getMaxFlowVolume()

    ConfigMinFlowHours = mcb_config.getMinFlowHours()
    ConfigMaxFlowHours = mcb_config.getMaxFlowHours()

    # Populate the controls with these local variable values
    min_flow_threshold.set(str(ConfigMinFlowVolume))
    max_flow_threshold.set(str(ConfigMaxFlowVolume))
    min_hours_threshold.set(str(ConfigMinFlowHours))
    max_hours_threshold.set(str(ConfigMaxFlowHours))

    if (ConfigMinFlowAlertEnabled):
        min_enb.tkraise()
    else:
        min_dis.tkraise()

    if (ConfigMaxFlowAlertEnabled):
        max_enb.tkraise()
    else:
        max_dis.tkraise()


###############################################################################
###############################################################################
def push_alert_settings():
    global ConfigMinFlowAlertEnabled, ConfigMaxFlowAlertEnabled
    global ConfigMinFlowVolume, ConfigMaxFlowVolume
    global ConfigMinFlowHours, ConfigMaxFlowHours

    # Pull local variable values from the widgets
    ConfigMinFlowVolume = int(min_flow_threshold.get())
    ConfigMaxFlowVolume = int(max_flow_threshold.get())
    ConfigMinFlowHours = int(min_hours_threshold.get())
    ConfigMaxFlowHours = int(max_hours_threshold.get())

    # Push local variable values into the INI file
    mcb_config.setMinFlowAlertEnabled(ConfigMinFlowAlertEnabled)
    mcb_config.setMaxFlowAlertEnabled(ConfigMaxFlowAlertEnabled)

    mcb_config.setMinFlowVolume(ConfigMinFlowVolume)
    mcb_config.setMaxFlowVolume(ConfigMaxFlowVolume)

    mcb_config.setMinFlowHours(ConfigMinFlowHours)
    mcb_config.setMaxFlowHours(ConfigMaxFlowHours)

    # Write the new CONFIG values to the INI file
    mcb_config.writeConfigSettings()


###############################################################################
###############################################################################
def on_min_alert_checked():
    global ConfigMinFlowAlertEnabled
    ConfigMinFlowAlertEnabled = True
    min_enb.tkraise()


###############################################################################
###############################################################################
def on_min_alert_unchecked():
    global ConfigMinFlowAlertEnabled
    ConfigMinFlowAlertEnabled = False
    min_dis.tkraise()


###############################################################################
###############################################################################
def on_max_alert_checked():
    global ConfigMaxFlowAlertEnabled
    ConfigMaxFlowAlertEnabled = True
    max_enb.tkraise()


###############################################################################
###############################################################################
def on_max_alert_unchecked():
    global ConfigMaxFlowAlertEnabled
    ConfigMaxFlowAlertEnabled = False
    max_dis.tkraise()


###############################################################################
###############################################################################
def inc_min_flow():
    flow = int(min_flow_threshold.get())
    if (flow < 300):
        flow = flow + 50
        screens.play_key_tone()
    min_flow_threshold.set(str(flow))


###############################################################################
###############################################################################
def dec_min_flow():
    flow = int(min_flow_threshold.get())
    if (flow > 50):
        flow = flow - 50
        screens.play_key_tone()
    min_flow_threshold.set(str(flow))


###############################################################################
###############################################################################
def inc_max_flow():
    flow = int(max_flow_threshold.get())
    if (flow < 1000):
        flow = flow + 50
        screens.play_key_tone()
    max_flow_threshold.set(str(flow))


###############################################################################
###############################################################################
def dec_max_flow():
    flow = int(max_flow_threshold.get())
    if (flow > 500):
        flow = flow - 50
        screens.play_key_tone()
    max_flow_threshold.set(str(flow))


###############################################################################
###############################################################################
def inc_min_hours():
    hours = int(min_hours_threshold.get())
    if (hours < 24):
        hours = hours + 1
        screens.play_key_tone()
    min_hours_threshold.set(str(hours))


###############################################################################
###############################################################################
def dec_min_hours():
    hours = int(min_hours_threshold.get())
    if (hours > 1):
        hours = hours - 1
        screens.play_key_tone()
    min_hours_threshold.set(str(hours))


###############################################################################
###############################################################################
def inc_max_hours():
    hours = int(max_hours_threshold.get())
    if (hours < 24):
        hours = hours + 1
        screens.play_key_tone()
    max_hours_threshold.set(str(hours))


###############################################################################
###############################################################################
def dec_max_hours():
    hours = int(max_hours_threshold.get())
    if (hours > 1):
        hours = hours - 1
        screens.play_key_tone()
    max_hours_threshold.set(str(hours))


###############################################################################
###############################################################################
def on_ok_press():
    # Chirp
    screens.play_key_tone()

    # Push local settings to INI file
    push_alert_settings()

    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def on_cancel_press():
    # Chirp
    screens.play_key_tone()

    # Pull the CONFIG file values into local settings
    pull_alert_settings()

    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def create_setup_screen(frame):
    global this_screen, min_dis, min_enb, max_dis, max_enb

    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    top_line = create_top_line(this_screen)
    min_dis  = create_min_alert_disabled_widget(this_screen)
    min_enb  = create_min_alert_enabled_widget(this_screen)
    max_dis  = create_max_alert_disabled_widget(this_screen)
    max_enb  = create_max_alert_enabled_widget(this_screen)
    bot_line = create_bottom_line(this_screen)

    top_line.grid(row=0, column=0, columnspan=10, sticky='nw')
    min_dis.grid( row=1, column=0, padx=30, pady=10, sticky='ew')
    min_enb.grid( row=1, column=0, padx=30, pady=10, sticky='ew')
    max_dis.grid( row=2, column=0, padx=30, pady=10, sticky='ew')
    max_enb.grid( row=2, column=0, padx=30, pady=10, sticky='ew')
    bot_line.grid(row=3, column=0, columnspan=10, pady=20)

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=LG_FONT, fg=SETUP_COLOR)
    l1.configure(text="Flow Alert Setup:")
    l1.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_min_alert_disabled_widget(frame):
    this_frame = tk.Frame(frame)

    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, sticky='w')
    f2.grid(row=1, column=0, padx=30, sticky='w')

    b1 = tk.Button(f1)
    b1.configure(relief="flat", command=on_min_alert_checked)
    b1.configure(image=screens.checkbox_no_icon)
    l1 = tk.Label(f1)
    l1.configure(font=MD_FONT, fg=DISABLED_COLOR)
    l1.configure(text="Enable low flow alert")
    b1.grid(row=0, column=0)
    l1.grid(row=0, column=1, padx=10)

    l2 = tk.Label(f2)
    l2.configure(font=MD_FONT, fg=DISABLED_COLOR)
    l2.configure(text="Sound an alert when flow drops too low")
    l2.grid(row=0, column=0, padx=20, pady=5, stick='n')

    return this_frame


###############################################################################
###############################################################################
def create_max_alert_disabled_widget(frame):
    this_frame = tk.Frame(frame)

    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, sticky='w')
    f2.grid(row=1, column=0, padx=30, sticky='w')

    b1 = tk.Button(f1)
    b1.configure(relief="flat", command=on_max_alert_checked)
    b1.configure(image=screens.checkbox_no_icon)
    l1 = tk.Label(f1)
    l1.configure(font=MD_FONT, fg=DISABLED_COLOR)
    l1.configure(text="Enable high flow alert")
    b1.grid(row=0, column=0)
    l1.grid(row=0, column=1, padx=10)

    l2 = tk.Label(f2)
    l2.configure(font=MD_FONT, fg=DISABLED_COLOR)
    l2.configure(text="Sound an alert when flow rises too high")
    l2.grid(row=0, column=0, padx=20, pady=5, stick='n')

    return this_frame


###############################################################################
###############################################################################
def create_min_alert_enabled_widget(frame):
    this_frame = tk.Frame(frame)

    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, sticky='w')
    f2.grid(row=1, column=0, padx=40, sticky='w')

    b1 = tk.Button(f1)
    b1.configure(relief="flat", command=on_min_alert_unchecked)
    b1.configure(image=screens.checkbox_yes_icon)
    l1 = tk.Label(f1)
    l1.configure(font=MD_FONT, fg=ENABLED_COLOR)
    l1.configure(text="Sound alert when flow stays below:")
    b1.grid(row=0, column=0)
    l1.grid(row=0, column=1, padx=10)

    mf = create_min_flow_adjuster(f2)
    l2 = tk.Label(f2)
    l2.configure(font=MD_FONT, fg=ENABLED_COLOR)
    l2.configure(text="mL over a ")
    mh = create_min_hours_adjuster(f2)
    l3 = tk.Label(f2)
    l3.configure(font=MD_FONT, fg=ENABLED_COLOR)
    l3.configure(text="hour period")

    mf.grid(row=0, column=0)
    l2.grid(row=0, column=1)
    mh.grid(row=0, column=2, padx=5)
    l3.grid(row=0, column=3)

    return this_frame


###############################################################################
###############################################################################
def create_max_alert_enabled_widget(frame):
    this_frame = tk.Frame(frame)

    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, sticky='w')
    f2.grid(row=1, column=0, padx=40, sticky='w')

    b1 = tk.Button(f1)
    b1.configure(relief="flat", command=on_max_alert_unchecked)
    b1.configure(image=screens.checkbox_yes_icon)
    l1 = tk.Label(f1)
    l1.configure(font=MD_FONT, fg=ENABLED_COLOR)
    l1.configure(text="Sound alert when flow stays above:")
    b1.grid(row=0, column=0)
    l1.grid(row=0, column=1, padx=10)

    mf = create_max_flow_adjuster(f2)
    l2 = tk.Label(f2)
    l2.configure(font=MD_FONT, fg=ENABLED_COLOR)
    l2.configure(text="mL over a ")
    mh = create_max_hours_adjuster(f2)
    l3 = tk.Label(f2)
    l3.configure(font=MD_FONT, fg=ENABLED_COLOR)
    l3.configure(text="hour period")

    mf.grid(row=0, column=0)
    l2.grid(row=0, column=1)
    mh.grid(row=0, column=2, padx=5)
    l3.grid(row=0, column=3)

    return this_frame


###############################################################################
###############################################################################
def create_min_flow_adjuster(frame):
    global min_flow_threshold

    min_flow_threshold = tk.StringVar()

    this_frame = tk.Frame(frame)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=0, column=1)

    e1 = tk.Entry(f1)
    e1.configure(width=4, justify='center', bd=4, relief='groove')
    e1.configure(font=ADJ_FONT, fg=SETUP_COLOR, bg='white')
    e1.configure(textvariable=min_flow_threshold)
    e1.grid(row=0, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.inc_btn_icon, borderwidth=0)
    b1.configure(repeatdelay=500, repeatinterval=100)
    b1.configure(command=inc_min_flow)
    b2 = tk.Button(f2)
    b2.configure(image=screens.dec_btn_icon, borderwidth=0)
    b2.configure(repeatdelay=500, repeatinterval=100)
    b2.configure(command=dec_min_flow)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_max_flow_adjuster(frame):
    global max_flow_threshold

    max_flow_threshold = tk.StringVar()

    this_frame = tk.Frame(frame)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=0, column=1)

    e1 = tk.Entry(f1)
    e1.configure(width=4, justify='center', bd=4, relief='groove')
    e1.configure(font=ADJ_FONT, fg=SETUP_COLOR, bg='white')
    e1.configure(textvariable=max_flow_threshold)
    e1.grid(row=0, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.inc_btn_icon, borderwidth=0)
    b1.configure(repeatdelay=500, repeatinterval=100)
    b1.configure(command=inc_max_flow)
    b2 = tk.Button(f2)
    b2.configure(image=screens.dec_btn_icon, borderwidth=0)
    b2.configure(repeatdelay=500, repeatinterval=100)
    b2.configure(command=dec_max_flow)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_min_hours_adjuster(frame):
    global min_hours_threshold

    min_hours_threshold = tk.StringVar()

    this_frame = tk.Frame(frame)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=0, column=1)

    e1 = tk.Entry(f1)
    e1.configure(width=3, justify='center', bd=4, relief='groove')
    e1.configure(font=ADJ_FONT, fg=SETUP_COLOR, bg='white')
    e1.configure(textvariable=min_hours_threshold)
    e1.grid(row=0, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.inc_btn_icon, borderwidth=0)
    b1.configure(repeatdelay=500, repeatinterval=100)
    b1.configure(command=inc_min_hours)
    b2 = tk.Button(f2)
    b2.configure(image=screens.dec_btn_icon, borderwidth=0)
    b2.configure(repeatdelay=500, repeatinterval=100)
    b2.configure(command=dec_min_hours)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_max_hours_adjuster(frame):
    global max_hours_threshold

    max_hours_threshold = tk.StringVar()

    this_frame = tk.Frame(frame)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=0, column=1)

    e1 = tk.Entry(f1)
    e1.configure(width=3, justify='center', bd=4, relief='groove')
    e1.configure(font=ADJ_FONT, fg=SETUP_COLOR, bg='white')
    e1.configure(textvariable=max_hours_threshold)
    e1.grid(row=0, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.inc_btn_icon, borderwidth=0)
    b1.configure(repeatdelay=500, repeatinterval=100)
    b1.configure(command=inc_max_hours)
    b2 = tk.Button(f2)
    b2.configure(image=screens.dec_btn_icon, borderwidth=0)
    b2.configure(repeatdelay=500, repeatinterval=100)
    b2.configure(command=dec_max_hours)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_bottom_line(frame):
    this_frame = tk.Frame(frame)

    b1 = tk.Button(this_frame)
    b1.configure(image=screens.blu_ok_btn_icon, borderwidth=0)
    b1.configure(command=on_ok_press)

    sl = tk.Label(this_frame)

    b2 = tk.Button(this_frame)
    b2.configure(image=screens.blu_cancel_btn_icon, borderwidth=0)
    b2.configure(command=on_cancel_press)

    b1.grid(row=0, column=0, pady=10)
    sl.grid(row=0, column=1, padx=80)
    b2.grid(row=0, column=2, pady=10)

    return this_frame


