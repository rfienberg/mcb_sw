from globals import *
import tkinter as tk
import screens
import telemetry

TANK_WIDTH    = 180
TANK_HEIGHT   = 220
TANK_CENTER_X = ((TANK_WIDTH/2)  + 6)
TANK_CENTER_Y = ((TANK_HEIGHT/2) - 6)
GLASS_WIDTH   = 10
LIQUID_WIDTH  = (TANK_WIDTH - GLASS_WIDTH)
LIQUID_HEIGHT = (TANK_HEIGHT - 6)

URINE_COLOR = '#DCC5ED'

TINY_FONT = ('Franklin Gothic', 12)


###############################################################################
# Display the TANKS screen in the screen area
###############################################################################
def show_status_screen():
    global this_screen
    this_screen.tkraise()
    periodic_screen_update()


###############################################################################
# Update the TANKS screen widgets based on the latest data
###############################################################################
def periodic_screen_update():
    global this_screen, updates

    # Update the LEFT Tank information
    valve = telemetry.getTankValveStatus("Left")
    volume = telemetry.getRealTankVolume("Left")
    droplet  = ltank_params[0]
    tank     = ltank_params[1]
    text_vol = ltank_params[2]
    text_pct = ltank_params[3]
    liquid   = ltank_params[4]

    # Update the Tank flow status based on its valve status
    if (valve == "Opened"):
        droplet.configure(image=screens.yes_flow_icon)
    else:
        droplet.configure(image=screens.no_flow_icon)

    # Update the Tank fill status based on the specified volume (in mL)
    vol_text = str(volume) + ' mL'
    percent = ((volume/900) * 100)
    #fill_line = TANK_HEIGHT - ((percent/100) * TANK_HEIGHT)
    tank.itemconfig(text_vol, text=vol_text)
    percent = round(percent, 1)
    pct_text = '(' + str(percent) + '%)'
    tank.itemconfig(text_pct, text=pct_text)

    x1 = TANK_CENTER_X - (LIQUID_WIDTH/2)
    x2 = TANK_CENTER_X + (LIQUID_WIDTH/2)
    y2 = TANK_CENTER_Y + (LIQUID_HEIGHT/2)
    y1 = y2 - ((percent/100) * LIQUID_HEIGHT)


    #y1 = TANK_CENTER_Y - (LIQUID_HEIGHT/2)

    tank.coords(liquid, x1,y1, x2,y2)


    #tank.coords(liquid, 8,fill_line, TANK_WIDTH-6,TANK_HEIGHT-6)

    # Update the RIGHT Tank information
    valve = telemetry.getTankValveStatus("Right")
    volume = telemetry.getRealTankVolume("Right")
    droplet  = rtank_params[0]
    tank     = rtank_params[1]
    text_vol = rtank_params[2]
    text_pct = rtank_params[3]
    liquid   = rtank_params[4]

    # Update the Tank flow status based on its valve status
    if (valve == "Opened"):
        droplet.configure(image=screens.yes_flow_icon)
    else:
        droplet.configure(image=screens.no_flow_icon)

    # Update the Tank fill status based on the specified volume (in mL)
    vol_text = str(volume) + ' mL'
    percent = ((volume/900) * 100)
    #fill_line = TANK_HEIGHT - ((percent/100) * TANK_HEIGHT)
    tank.itemconfig(text_vol, text=vol_text)
    percent = round(percent, 1)
    pct_text = '(' + str(percent) + '%)'
    tank.itemconfig(text_pct, text=pct_text)

    x1 = TANK_CENTER_X - (LIQUID_WIDTH/2)
    x2 = TANK_CENTER_X + (LIQUID_WIDTH/2)
    y2 = TANK_CENTER_Y + (LIQUID_HEIGHT/2)
    y1 = y2 - ((percent/100) * LIQUID_HEIGHT)


    #y1 = TANK_CENTER_Y - (LIQUID_HEIGHT/2)

    tank.coords(liquid, x1,y1, x2,y2)


    #tank.coords(liquid, 8,fill_line, TANK_WIDTH-6,TANK_HEIGHT-6)

    # Schedule the next screen update
    updates = this_screen.after(500, periodic_screen_update)


###############################################################################
# Exits back to the INFO main screen
###############################################################################
def on_back_press():
    global this_screen, updates

    this_screen.after_cancel(updates)

    # Chirp
    screens.play_key_tone()

    screens.show_info_main_screen()


###############################################################################
###############################################################################
def create_info_screen(frame):
    global this_screen

    # Create the Frame for this screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets for this screen
    tline = create_top_line(this_screen)
    bline = create_bot_line(this_screen)

    # Place the Widgets into the Frame
    tline.grid(row=0, column=0, padx=5, sticky='nw')
    bline.grid(row=1, column=0, padx=80)

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the widgets
    l1 = tk.Label(this_frame, text="Tank Info")
    b1 = tk.Button(this_frame)
    l1.configure(font=LG_FONT, fg=STATUS_COLOR)
    b1.configure(image=screens.pur_gohome_btn_icon, borderwidth=0)
    b1.configure(command=on_back_press)

    b1.grid(row=0, column=0, padx=5, pady=10)
    l1.grid(row=0, column=1, padx=80)

    return this_frame


###############################################################################
###############################################################################
def create_bot_line(frame):
    this_frame = tk.Frame(frame)

    ltank = create_ltank_widget(this_frame)
    rtank = create_rtank_widget(this_frame)
    ltank.grid(row=0, column=0, padx=5)
    rtank.grid(row=0, column=1, padx=5)

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
    c1.configure(width=TANK_WIDTH+10, height=TANK_HEIGHT)
    x1 = TANK_CENTER_X - (TANK_WIDTH/2)
    x2 = TANK_CENTER_X + (TANK_WIDTH/2)
    y1 = TANK_CENTER_Y - (TANK_HEIGHT/2)
    y2 = TANK_CENTER_Y + (TANK_HEIGHT/2)
    g1 = c1.create_rectangle(x1,y1, x2,y2)
    u1 = c1.create_rectangle(0,0, 0,0)
    t1 = c1.create_text(TANK_CENTER_X,(TANK_CENTER_Y-30))
    t2 = c1.create_text(TANK_CENTER_X,TANK_CENTER_Y)

    # Configure the canvas items
    c1.itemconfig(g1, width=GLASS_WIDTH, outline=STATUS_COLOR)
    c1.itemconfig(u1, fill=URINE_COLOR)
    c1.itemconfig(t1, fill=STATUS_COLOR)
    c1.itemconfig(t1, font=MD_FONT)
    c1.itemconfig(t1, text="0 mL")
    c1.itemconfig(t2, fill=STATUS_COLOR)
    c1.itemconfig(t2, font=TINY_FONT)
    c1.itemconfig(t2, text="(0%)")

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
    c1.configure(width=TANK_WIDTH+10, height=TANK_HEIGHT)
    x1 = TANK_CENTER_X - (TANK_WIDTH/2)
    x2 = TANK_CENTER_X + (TANK_WIDTH/2)
    y1 = TANK_CENTER_Y - (TANK_HEIGHT/2)
    y2 = TANK_CENTER_Y + (TANK_HEIGHT/2)
    g1 = c1.create_rectangle(x1,y1, x2,y2)
    u1 = c1.create_rectangle(0,0, 0,0)
    t1 = c1.create_text(TANK_CENTER_X,(TANK_CENTER_Y-30))
    t2 = c1.create_text(TANK_CENTER_X,TANK_CENTER_Y)

    # Configure the canvas items
    c1.itemconfig(g1, width=GLASS_WIDTH, outline=STATUS_COLOR)
    c1.itemconfig(u1, fill=URINE_COLOR)
    c1.itemconfig(t1, fill=STATUS_COLOR)
    c1.itemconfig(t1, font=MD_FONT)
    c1.itemconfig(t1, text="0 mL")
    c1.itemconfig(t2, fill=STATUS_COLOR)
    c1.itemconfig(t2, font=TINY_FONT)
    c1.itemconfig(t2, text="(0%)")

    d1.grid(row=0, column=0)
    c1.grid(row=1, column=0, padx=40, pady=5, sticky='s')

    rtank_params = (d1, c1, t1, t2, u1)

    return this_frame


