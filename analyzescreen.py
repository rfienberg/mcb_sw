from globals import *
import tkinter as tk
import screens
import flow
import color
import turbidity
import time


FLOW_COLOR = '#00B050'
FLOW_FONT  = ("Arial Narrow", 80)
TINY_FONT  = ("Arial Narrow", 12)
TITLE_FONT = ('Calibri', 30)


###############################################################################
# Creates the ANALYZE Main Screen - which shows a summary of the current analysis
###############################################################################
def create_main_screen(frame):
    global this_screen

    # Create and place the Screen
    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top = create_top_line(this_screen)
    afw = create_flowrate_widget(this_screen)
    acw = create_color_widget(this_screen)
    atw = create_turbidity_widget(this_screen)

    # Place the Widgets
    top.grid(row=0, column=0, columnspan=3, padx=2, sticky='w')
    afw.grid(row=1, column=0, padx=2)
    acw.grid(row=1, column=1, padx=2)
    atw.grid(row=1, column=2, padx=2)

    return this_screen


###############################################################################
# Shows the ANALYZE Main Screen
###############################################################################
def show_main_screen():
    global this_screen
    this_screen.tkraise()

    periodic_screen_update()


###############################################################################
# Periodically update the ANALYZE main screen
###############################################################################
def periodic_screen_update():
    global this_screen, flowrate_items, color_items, turbid_items

    # Update with the last hour's total FLOW
    flow_text = str(flow.getCurrentHourlyFlow()).rjust(4, '0')
    flowrate_items[0].itemconfig(flowrate_items[1], text=flow_text)

    # Update with last minute's COLOR
    color_rating = color.getColorRating()
    color.populateRatingBox(color_items, color_rating)

    # Update with last minute's TURBIDITY
    turbid_rating = turbidity.getTurbidRating()
    turbidity.populateRatingBox(turbid_items, turbid_rating)

    # Schedule the next screen update
    this_screen.after(2000, periodic_screen_update)


###############################################################################
###############################################################################
def on_home_press():
    global this_screen

    # Chirp
    screens.play_key_tone()

    # Cancel the periodic screen updates
    this_screen.after_cancel(periodic_screen_update)

    screens.show_home_screen()


###############################################################################
###############################################################################
def on_flow_history_press():
    # Chirp
    screens.play_key_tone()

    screens.show_flowrate_history_screen()


###############################################################################
###############################################################################
def on_color_details_press():
    # Chirp
    screens.play_key_tone()

    screens.show_color_details_screen()


###############################################################################
###############################################################################
def on_turbidity_details_press():
    # Chirp
    screens.play_key_tone()

    screens.show_turbidity_details_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the widgets
    l1 = tk.Label(this_frame, text="Analyze:")
    b1 = tk.Button(this_frame)
    l1.configure(font=LG_FONT, fg=ANALYZE_COLOR)
    b1.configure(image=screens.brn_gohome_btn_icon, borderwidth=0)
    b1.configure(command=on_home_press)

    b1.grid(row=0, column=0, padx=5, pady=10)
    l1.grid(row=0, column=1, padx=5)

    return this_frame


###############################################################################
# Creates the ANALYZE FLOW widget
###############################################################################
def create_flowrate_widget(frame):
    global flowrate_items

    # Define a frame to encompass all of the widgets
    this_frame = tk.LabelFrame(frame)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f3 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    f2.grid(row=1, column=0, pady=15)
    f3.grid(row=2, column=0, pady=15)

    # Define the top frame widget
    l1 = tk.Label(f1)
    l1.configure(text="Flow")
    l1.configure(font=TITLE_FONT, fg=ANALYZE_COLOR)
    l2 = tk.Label(f1)
    l2.configure(text="(This Hour)")
    l2.configure(font=TINY_FONT, fg=ANALYZE_COLOR, anchor='s')
    l1.grid(row=0, column=0)
    l2.grid(row=0, column=1, sticky='s')

    # Define the middle frame widget
    c1 = tk.Canvas(f2, width=240, height=120)
    c1.grid(row=0, column=0, padx=10)
    flow = c1.create_text(100, 60)
    unit = c1.create_text(220, 100)
    c1.itemconfig(flow, font=FLOW_FONT, fill=CONTROL_COLOR)
    c1.itemconfig(unit, font=("Arial Narrow", 16), fill=CONTROL_COLOR)
    c1.itemconfig(flow, text="----")
    c1.itemconfig(unit, text="mL")
    flowrate_items = (c1, flow, unit)

    # Define the bottom frame widget
    my_spacer = tk.Label(f3)
    history_btn = tk.Button(f3)
    history_btn.configure(image=screens.history_btn_icon, borderwidth=0)
    history_btn.configure(command=on_flow_history_press)
    history_btn.grid(row=1, column=0)

    # Return the encompassing frame so it can be placed anywhere
    return this_frame


###############################################################################
# Creates the ANALYZE COLOR widget
###############################################################################
def create_color_widget(frame):
    global color_items

    # Define a frame to encompass all of the widgets
    this_frame = tk.LabelFrame(frame)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f3 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    f2.grid(row=1, column=0, pady=15)
    f3.grid(row=2, column=0, pady=15)

    # Define the top frame widget
    l1 = tk.Label(f1)
    l1.configure(text="Color")
    l1.configure(font=TITLE_FONT, fg=ANALYZE_COLOR)
    l2 = tk.Label(f1)
    l2.configure(text="(Last Minute)")
    l2.configure(font=TINY_FONT, fg=ANALYZE_COLOR, anchor='s')
    l1.grid(row=0, column=0)
    l2.grid(row=0, column=1, sticky='s')

    # Define the middle frame widget
    c1 = tk.Canvas(f2, width=220, height=120)
    c1.grid(row=0, column=0)
    rect_item = c1.create_rectangle(20, 35, 200, 85, width=3, outline=ANALYZE_COLOR)
    text_item = c1.create_text(110, 60, font=("Arial", 22))
    color_items = (c1, rect_item, text_item)

    # Define the bottom frame widget
    b1 = tk.Button(f3)
    b1.configure(image=screens.details_btn_icon, borderwidth=0)
    b1.configure(command=on_color_details_press)
    b1.grid(row=0, column=0)

    # Populate the updatable items with default values
    color_index = color.getColorRating()
    color.populateRatingBox(color_items, color_index)

    # Return the encompassing frame so it can be placed anywhere
    return this_frame


###############################################################################
# Creates the ANALYZE TURBIDITY widget
###############################################################################
def create_turbidity_widget(frame):
    global turbid_items

    # Define a frame to encompass all of the widgets
    this_frame = tk.LabelFrame(frame)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f3 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    f2.grid(row=1, column=0, pady=15)
    f3.grid(row=2, column=0, pady=15)

    # Define the top frame widget
    l1 = tk.Label(f1)
    l1.configure(text="Turbidity")
    l1.configure(font=TITLE_FONT, fg=ANALYZE_COLOR)
    l2 = tk.Label(f1)
    l2.configure(text="(Last Minute)")
    l2.configure(font=TINY_FONT, fg=ANALYZE_COLOR, anchor='s')
    l1.grid(row=0, column=0)
    l2.grid(row=0, column=1, sticky='s')

    # Define the middle frame widget
    c1 = tk.Canvas(f2, width=220, height=120)
    c1.grid(row=0, column=0)
    rect_item = c1.create_rectangle(20, 35, 200, 85, width=3, outline=ANALYZE_COLOR)
    text_item = c1.create_text(110, 60, font=("Arial", 22))
    image_item = c1.create_image(110, 65)
    turbid_items = (c1, rect_item, text_item, image_item)

    # Define the bottom frame widget
    b1 = tk.Button(f3)
    b1.configure(image=screens.details_btn_icon, borderwidth=0)
    b1.configure(command=on_turbidity_details_press)
    b1.grid(row=0, column=0)

    # Populate the updatable items with default values
    turbid_rating = turbidity.getTurbidRating()
    turbidity.populateRatingBox(turbid_items, turbid_rating)

    # Return the encompassing frame so it can be placed anywhere
    return this_frame


