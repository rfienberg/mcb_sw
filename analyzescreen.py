from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import screens
import flow
import color
import turbidity
import time



###############################################################################
# Creates the ANALYZE Main Screen - which shows a summary of the current analysis
###############################################################################
def create_main_screen(frame):
    global this_screen

    # Open up the images for this screen and keep them global
    global gohome_btn_icon
    this_btn_img = Image.open("Icons/brn_home.png").resize((50,50), Image.ANTIALIAS)
    gohome_btn_icon = ImageTk.PhotoImage(this_btn_img)
    global history_btn_icon
    this_btn_img = Image.open("Icons/brn_history_btn.png").resize((150,50), Image.ANTIALIAS)
    history_btn_icon = ImageTk.PhotoImage(this_btn_img)
    global details_btn_icon
    this_btn_img = Image.open("Icons/brn_details_btn.png").resize((150,50), Image.ANTIALIAS)
    details_btn_icon = ImageTk.PhotoImage(this_btn_img)
    global flowrates_icon
    this_btn_img = Image.open("Icons/brn_droplet.png").resize((30,30), Image.ANTIALIAS)
    flowrates_icon = ImageTk.PhotoImage(this_btn_img)
    global color_icon
    this_btn_img = Image.open("Icons/brn_crayons.png").resize((30,30), Image.ANTIALIAS)
    color_icon = ImageTk.PhotoImage(this_btn_img)
    global turbidity_icon
    this_btn_img = Image.open("Icons/brn_clouds.png").resize((30,30), Image.ANTIALIAS)
    turbidity_icon = ImageTk.PhotoImage(this_btn_img)

    # Create and place the Screen
    this_screen = tk.LabelFrame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top = create_top_line(this_screen)
    afw = create_flowrate_widget(this_screen)
    acw = create_color_widget(this_screen)
    atw = create_turbidity_widget(this_screen)

    # Place the Widgets
    top.grid(row=0, column=0, padx=2, sticky='w')
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
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the Go Home button
    gohome_btn_button = tk.Button(this_frame)
    gohome_btn_button.configure(image=gohome_btn_icon, borderwidth=0)
    gohome_btn_button.configure(command=on_home_press)

    # Create the Title label
    title_label = tk.Label(this_frame, text="Analyze:")
    title_label.configure(font=LG_FONT, fg=ANALYZE_COLOR)

    gohome_btn_button.grid(row=0, column=0, padx=5, pady=10, sticky='nw')
    title_label.grid(row=0, column=1, padx=5, pady=5)

    return this_frame


###############################################################################
# Creates the ANALYZE FLOW RATE widget
###############################################################################
def create_flowrate_widget(frame):
    global flowrate_items

    # Define a frame to encompass all of the widgets
    this_frame = tk.LabelFrame(frame)

    # Define the top frame widget
    top_frame = tk.Frame(this_frame)
    top_icon = tk.Label(top_frame)
    top_icon.configure(image=flowrates_icon)
    top_label = tk.Label(top_frame)
    top_label.configure(text="Flow:")
    top_label.configure(font=MD_FONT, fg=ANALYZE_COLOR, anchor='w')
    top_icon.grid(row=0,  column=0, padx=10)
    top_label.grid(row=0, column=1)

    # Define the middle frame widget
    mid_frame = tk.Frame(this_frame)
    flowrate_cv = tk.Canvas(mid_frame, width=240, height=120)
    flowrate_cv.grid(row=0, column=0, padx=10)
    rate_item = flowrate_cv.create_text(100, 60)
    unit_item = flowrate_cv.create_text(220, 100)
    flowrate_cv.itemconfig(rate_item, font=("Arial Narrow", 80), fill=CONTROL_COLOR)
    flowrate_cv.itemconfig(unit_item, font=("Arial Narrow", 16), fill=CONTROL_COLOR)
    flowrate_items = (flowrate_cv, rate_item, unit_item)

    # Define the bottom frame widget
    bot_frame = tk.Frame(this_frame)
    my_spacer = tk.Label(bot_frame)
    history_btn = tk.Button(bot_frame)
    history_btn.configure(image=history_btn_icon, borderwidth=0)
    history_btn.configure(command=on_flow_history_press)
    history_btn.grid(row=1, column=0)

    # Grid the three frame widgets
    top_frame.grid(row=0, column=0, pady=5, sticky='w')
    mid_frame.grid(row=1, column=0, pady=15)
    bot_frame.grid(row=2, column=0, pady=15)

    # Populate the updatable items with default values
    flowrate_cv.itemconfig(rate_item, text="----")
    flowrate_cv.itemconfig(unit_item, text="mL")

    # Return the encompassing frame so it can be placed anywhere
    return this_frame


###############################################################################
###############################################################################
def on_flow_history_press():
    # Chirp
    screens.play_key_tone()

    screens.show_flowrate_history_screen()


###############################################################################
# Creates the ANALYZE COLOR widget
###############################################################################
def create_color_widget(frame):
    # Define a frame to encompass all of the widgets
    this_frame = tk.LabelFrame(frame)

    # Define the top frame widget
    top_frame = tk.Frame(this_frame)
    top_icon = tk.Label(top_frame)
    top_icon.configure(image=color_icon)
    top_label = tk.Label(top_frame)
    top_label.configure(text="Color:")
    top_label.configure(font=MD_FONT, fg=ANALYZE_COLOR, anchor='w')
    top_icon.grid(row=0, column=0, padx=10)
    top_label.grid(row=0, column=1)

    # Define the middle frame widget
    mid_frame = tk.Frame(this_frame)
    color_cv = tk.Canvas(mid_frame, width=220, height=120)
    rect_item = color_cv.create_rectangle(20, 35, 200, 85, width=5, outline=ANALYZE_COLOR)
    text_item = color_cv.create_text(110, 60, font=("Arial", 22))
    color_cv.grid(row=0, column=0, padx=10)

    # Define the bottom frame widget
    bot_frame = tk.Frame(this_frame)
    color_btn = tk.Button(bot_frame)
    color_btn.configure(image=details_btn_icon, borderwidth=0)
    color_btn.configure(command=on_color_details_press)
    color_btn.grid(row=0, column=0)

    # Grid the three frame widgets
    top_frame.grid(row=0, column=0, pady=5, sticky='w')
    mid_frame.grid(row=1, column=0, pady=15)
    bot_frame.grid(row=2, column=0, pady=15)

    # Populate the updatable items with default values
    global color_items
    color_items = (color_cv, rect_item, text_item)
    color_index = color.getColorRating()
    color.populateRatingBox(color_items, color_index)

    # Return the encompassing frame so it can be placed anywhere
    return this_frame


###############################################################################
###############################################################################
def on_color_details_press():
    # Chirp
    screens.play_key_tone()

    screens.show_color_details_screen()


###############################################################################
# Creates the ANALYZE TURBIDITY widget
###############################################################################
def create_turbidity_widget(frame):
    # Define a frame to encompass all of the widgets
    this_frame = tk.LabelFrame(frame)

    # Define the top frame widget
    top_frame = tk.Frame(this_frame)
    top_icon = tk.Label(top_frame)
    top_icon.configure(image=turbidity_icon)
    top_label = tk.Label(top_frame)
    top_label.configure(text="Turbidity:")
    top_label.configure(font=MD_FONT, fg=ANALYZE_COLOR, anchor='w')
    top_icon.grid(row=0, column=0, padx=10)
    top_label.grid(row=0, column=1)

    # Define the middle frame widget
    mid_frame = tk.Frame(this_frame)
    turbid_cv = tk.Canvas(mid_frame, width=220, height=120)

    rect_item = turbid_cv.create_rectangle(20, 35, 200, 85, width=5, outline=ANALYZE_COLOR)
    text_item = turbid_cv.create_text(110, 60, font=("Arial", 22))
    image_item = turbid_cv.create_image(110, 65)
    turbid_cv.grid(row=0, column=0, padx=10)

    # Define the bottom frame widget
    bot_frame = tk.Frame(this_frame)
    turbidity_btn = tk.Button(bot_frame)
    turbidity_btn.configure(image=details_btn_icon, borderwidth=0)
    turbidity_btn.configure(command=on_turbidity_details_press)
    turbidity_btn.grid(row=0, column=0)

    # Grid the three frame widgets
    top_frame.grid(row=0, column=0, pady=5, sticky='w')
    mid_frame.grid(row=1, column=0, pady=15)
    bot_frame.grid(row=2, column=0, pady=15)

    # Populate the updatable items with default values
    global turbid_items
    turbid_items = (turbid_cv, rect_item, text_item, image_item)
    turbid_rating = turbidity.getTurbidRating()
    turbidity.populateRatingBox(turbid_items, turbid_rating)

    # Return the encompassing frame so it can be placed anywhere
    return this_frame


###############################################################################
###############################################################################
def on_turbidity_details_press():
    # Chirp
    screens.play_key_tone()

    screens.show_turbidity_details_screen()


