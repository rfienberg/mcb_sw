from globals import *
import tkinter as tk
import screens
import telemetry

TANK_HEIGHT = 170
TANK_WIDTH = 140

URINE_COLOR = '#DCC5ED'
TINY_FONT = ('Franklin Gothic', 12)

###############################################################################
# Display the TANKS screen in the screen area
###############################################################################
def show_status_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
###############################################################################
def on_home_press():
    # Chirp
    screens.play_key_tone()
    screens.show_home_screen()


###############################################################################
# Exits back to the STATUS main screen
###############################################################################
def on_control_exit():
    # Chirp
    screens.play_key_tone()
    screens.show_status_main_screen()


###############################################################################
# Update the TANKS screen widgets based on the latest data
###############################################################################
def update_screen():
    lvalve = telemetry.getTankValveStatus("Left")
    lvolume = telemetry.getRealTankVolume("Left")
    rvalve = telemetry.getTankValveStatus("Right")
    rvolume = telemetry.getRealTankVolume("Right")

    # Update the Left Tank flow status based on its valve status
    if (lvalve == "Opened"):
        ltank_params[0].configure(image=screens.yes_flow_icon)
    else:
        ltank_params[0].configure(image=screens.no_flow_icon)

    # Update the Right Tank flow status based on its valve status
    if (rvalve == "Opened"):
        rtank_params[0].configure(image=screens.yes_flow_icon)
    else:
        rtank_params[0].configure(image=screens.no_flow_icon)

    # Update the Left Tank fill status based on the specified volume (in mL)
    percent = lvolume / 10
    pct_text = str(percent) + '%'
    vol_text = '(' + str(percent*10) + ' mL)'
    fill_line = TANK_HEIGHT - ((percent/100) * TANK_HEIGHT)
    ltank_params[1].itemconfig(ltank_params[2], text=pct_text)
    ltank_params[1].itemconfig(ltank_params[3], text=vol_text)
    ltank_params[1].coords(ltank_params[4], 4, fill_line, TANK_WIDTH, TANK_HEIGHT)

    # Update the Right Tank fill status based on the specified volume (in mL)
    percent = rvolume / 10
    pct_text = str(percent) + '%'
    vol_text = '(' + str(percent*10) + ' mL)'
    fill_line = TANK_HEIGHT - ((percent/100) * TANK_HEIGHT)
    rtank_params[1].itemconfig(rtank_params[2], text=pct_text)
    rtank_params[1].itemconfig(rtank_params[3], text=vol_text)
    rtank_params[1].coords(rtank_params[4], 4, fill_line, TANK_WIDTH, TANK_HEIGHT)


###############################################################################
###############################################################################
def create_status_screen(frame):
    global this_screen

    # Create the Frame for this screen
    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets for this screen
    tline = create_top_line(this_screen)
    mline = create_mid_line(this_screen)
    bline = create_bot_line(this_screen)

    # Place the Widgets into the Frame
    tline.grid(row=0, column=0, padx=5, sticky='nw')
    mline.grid(row=1, column=0, padx=80, pady=10)
    bline.grid(row=2, column=0, padx=10)

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=LG_FONT, fg=STATUS_COLOR)
    l1.configure(text="Tank Status:")
    l1.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_mid_line(frame):
    this_frame = tk.Frame(frame)

    ltank = create_ltank_widget(this_frame)
    rtank = create_rtank_widget(this_frame)
    ltank.grid(row=0, column=0, padx=5)
    rtank.grid(row=0, column=1, padx=5)

    return this_frame


###############################################################################
###############################################################################
def create_bot_line(frame):
    this_frame = tk.Frame(frame)

    b1 = tk.Button(this_frame)
    b1.configure(image=screens.pur_ok_btn_icon, borderwidth=0)
    b1.configure(command=on_control_exit)
    b1.grid(row=0, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_ltank_widget(frame):
    global ltank_params

    this_frame = tk.LabelFrame(frame, text="Left Tank")
    this_frame.configure(font=TINY_FONT, fg=STATUS_COLOR)

    # Create the droplet
    d1 = tk.Label(this_frame)
    d1.configure(image=screens.no_flow_icon)

    # Create the tank with it (g)lass, (u)rine, and (t)ext
    c1 = tk.Canvas(this_frame)
    c1.configure(width=TANK_WIDTH, height=TANK_HEIGHT)
    g1 = c1.create_rectangle(4, 0, TANK_WIDTH, TANK_HEIGHT)
    u1 = c1.create_rectangle(4, TANK_HEIGHT, TANK_WIDTH, TANK_HEIGHT)
    t1 = c1.create_text(TANK_WIDTH/2, ((TANK_HEIGHT/2)-30))
    t2 = c1.create_text(TANK_WIDTH/2, TANK_HEIGHT/2)

    # Configure the canvas items
    c1.itemconfig(g1, width=10, outline=STATUS_COLOR)
    c1.itemconfig(u1, fill=URINE_COLOR)
    c1.itemconfig(t1, fill=STATUS_COLOR)
    c1.itemconfig(t1, font=MD_FONT)
    c1.itemconfig(t1, text="0%")
    c1.itemconfig(t2, fill=STATUS_COLOR)
    c1.itemconfig(t2, font=TINY_FONT)
    c1.itemconfig(t2, text="(0 mL)")

    d1.grid(row=0, column=0)
    c1.grid(row=1, column=0, padx=40, pady=5, sticky='s')

    ltank_params = (d1, c1, t1, t2, u1)

    return this_frame


###############################################################################
###############################################################################
def create_rtank_widget(frame):
    global rtank_params

    this_frame = tk.LabelFrame(frame, text="Right Tank")
    this_frame.configure(font=TINY_FONT, fg=STATUS_COLOR)

    # Create the droplet
    d1 = tk.Label(this_frame)
    d1.configure(image=screens.no_flow_icon)

    # Create the tank with it (g)lass, (u)rine, and (t)ext
    c1 = tk.Canvas(this_frame)
    c1.configure(width=TANK_WIDTH, height=TANK_HEIGHT)
    g1 = c1.create_rectangle(4, 0, TANK_WIDTH, TANK_HEIGHT)
    u1 = c1.create_rectangle(4, TANK_HEIGHT, TANK_WIDTH, TANK_HEIGHT)
    t1 = c1.create_text(TANK_WIDTH/2, ((TANK_HEIGHT/2)-30))
    t2 = c1.create_text(TANK_WIDTH/2, TANK_HEIGHT/2)

    # Configure the canvas items
    c1.itemconfig(g1, width=10, outline=STATUS_COLOR)
    c1.itemconfig(u1, fill=URINE_COLOR)
    c1.itemconfig(t1, fill=STATUS_COLOR)
    c1.itemconfig(t1, font=MD_FONT)
    c1.itemconfig(t1, text="0%")
    c1.itemconfig(t2, fill=STATUS_COLOR)
    c1.itemconfig(t2, font=TINY_FONT)
    c1.itemconfig(t2, text="(0 mL)")

    d1.grid(row=0, column=0)
    c1.grid(row=1, column=0, padx=40, pady=5, sticky='s')

    rtank_params = (d1, c1, t1, t2, u1)

    return this_frame


