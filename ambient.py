from globals import *
import tkinter as tk
import screens
import telemetry

URINE_COLOR = '#DCC5ED'
TANK_HEIGHT = 180
TANK_WIDTH = 100


###############################################################################
###############################################################################
def create_main_screen(frame):
    global this_screen

    # Create the Frame for this screen
    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets for this screen
    tline = create_top_line(this_screen)
    ltank = create_ltank_widget(this_screen)
    rtank = create_rtank_widget(this_screen)
    lights = create_lighting_widget(this_screen)

    # Place the Widgets into the Frame
    tline.grid( row=0, column=0, padx=5, sticky='nw', columnspan=10)
    ltank.grid( row=1, column=0, padx=5, sticky='n')
    rtank.grid( row=1, column=1, padx=5, sticky='n')
    lights.grid(row=1, column=2, padx=5, sticky='n')

    return this_screen


###############################################################################
# Display the Status Screen in the screen area
###############################################################################
def show_main_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
# Update the Status Screen widgets based on the latest data
###############################################################################
def update_screen():
    lvalve = telemetry.getTankValveStatus("Left")
    lvolume = telemetry.getRealTankVolume("Left")
    rvalve = telemetry.getTankValveStatus("Right")
    rvolume = telemetry.getRealTankVolume("Right")

    # Update the Left Tank flow status based on its valve status
    if (lvalve == "Opened"):
        ltank_droplet.configure(image=screens.yes_flow_icon)
    else:
        ltank_droplet.configure(image=screens.no_flow_icon)

    # Update the Left Tank fill status based on the specified volume (in mL)
    percent = lvolume / 10
    pct_text = str(percent) + '%'
    ltank_cv.itemconfig(ltank_percent, text=pct_text)

    fill_line = TANK_HEIGHT - ((percent/100) * TANK_HEIGHT)
    ltank_cv.coords(ltank_fill, 4, fill_line, TANK_WIDTH, TANK_HEIGHT)

    vol_text = str(percent*10) + ' mL'
    ltank_volume.configure(text=vol_text)

    # Update the Right Tank flow status based on its valve status
    if (rvalve == "Opened"):
        rtank_droplet.configure(image=screens.yes_flow_icon)
    else:
        rtank_droplet.configure(image=screens.no_flow_icon)

    # Update the Right Tank fill status based on the specified volume (in mL)
    percent = rvolume / 10
    pct_text = str(percent) + '%'
    rtank_cv.itemconfig(rtank_percent, text=pct_text)

    fill_line = TANK_HEIGHT - ((percent/100) * TANK_HEIGHT)
    rtank_cv.coords(rtank_fill, 4, fill_line, TANK_WIDTH, TANK_HEIGHT)

    vol_text = str(percent*10) + ' mL'
    rtank_volume.configure(text=vol_text)


###############################################################################
###############################################################################
def on_home_press():
    screens.play_key_tone()
    screens.show_home_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the widgets
    b1 = tk.Button(this_frame)
    l1 = tk.Label(this_frame, text="Status:")
    l1.configure(font=LG_FONT, fg=STATUS_COLOR)
    b1.configure(image=screens.pur_gohome_btn_icon, borderwidth=0)
    b1.configure(command=on_home_press)

    b1.grid(row=0, column=0, padx=5, pady=10)
    l1.grid(row=0, column=1, padx=5)

    return this_frame


###############################################################################
###############################################################################
def create_ltank_widget(frame):
    global ltank_cv, ltank_fill, ltank_percent, ltank_volume, ltank_droplet

    this_frame = tk.LabelFrame(frame, text="Left Tank")

    ltank_droplet = tk.Label(this_frame)
    ltank_droplet.configure(image=screens.no_flow_icon)
    ltank_droplet.grid(row=0, column=0)

    ltank_cv = tk.Canvas(this_frame)
    ltank_cv.configure(width=TANK_WIDTH, height=TANK_HEIGHT)
    ltank_cv.grid(row=1, column=0, padx=40)

    ltank_fill = ltank_cv.create_rectangle(4, TANK_HEIGHT, TANK_WIDTH, TANK_HEIGHT, fill=URINE_COLOR)
    ltank_glass = ltank_cv.create_rectangle(4, 0, TANK_WIDTH, TANK_HEIGHT, width=5, outline='purple')
    ltank_percent = ltank_cv.create_text(TANK_WIDTH/2, TANK_HEIGHT/2, text="0%", font=SM_FONT, fill=STATUS_COLOR)

    ltank_volume = tk.Label(this_frame, font=SM_FONT, fg=STATUS_COLOR)
    ltank_volume.configure(text="0 mL")
    ltank_volume.grid(row=2, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_rtank_widget(frame):
    global rtank_cv, rtank_fill, rtank_percent, rtank_volume, rtank_droplet

    this_frame = tk.LabelFrame(frame, text="Right Tank")

    rtank_droplet = tk.Label(this_frame)
    rtank_droplet.configure(image=screens.no_flow_icon)
    rtank_droplet.grid(row=0, column=0)

    rtank_cv = tk.Canvas(this_frame)
    rtank_cv.configure(width=TANK_WIDTH, height=TANK_HEIGHT)
    rtank_cv.grid(row=1, column=0, padx=40)

    rtank_fill = rtank_cv.create_rectangle(4, TANK_HEIGHT, TANK_WIDTH, TANK_HEIGHT, fill=URINE_COLOR)
    rtank_glass = rtank_cv.create_rectangle(4, 0, TANK_WIDTH, TANK_HEIGHT, width=5, outline='purple')
    rtank_percent = rtank_cv.create_text(TANK_WIDTH/2, TANK_HEIGHT/2, text="0%", font=SM_FONT, fill=STATUS_COLOR)

    rtank_volume = tk.Label(this_frame, font=SM_FONT, fg=STATUS_COLOR)
    rtank_volume.configure(text="0 mL")
    rtank_volume.grid(row=2, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_lighting_widget(frame):
    this_frame = tk.LabelFrame(frame, text="Lighting")

    """
    lighting_bulb = tk.Label(this_frame)
    lighting_bulb.configure(image=screens.light_bulb_icon)
    lighting_bulb.grid(row=0, column=0, columnspan=2, pady=10)
    """

    tank_lights_label = tk.Label(this_frame, font=SM_FONT, fg=STATUS_COLOR)
    tank_lights_label.configure(text="Tanks:")
    tank_lights_label.grid(row=1, column=0, pady=10)
    tank_lights_status = tk.Label(this_frame, font=SM_FONT, fg=STATUS_COLOR)
    tank_lights_status.configure(text="Lights On")
    tank_lights_status.grid(row=1, column=1, padx=5, sticky='w')

    room_lights_label = tk.Label(this_frame, font=SM_FONT, fg=STATUS_COLOR)
    room_lights_label.configure(text="Room:")
    room_lights_label.grid(row=2, column=0, pady=10)
    room_lights_status = tk.Label(this_frame, font=SM_FONT, fg=STATUS_COLOR)
    room_lights_status.configure(text="Bright")
    room_lights_status.grid(row=2, column=1, padx=5, sticky='w')

    return this_frame


