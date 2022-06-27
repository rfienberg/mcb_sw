from globals import *
import time
import tkinter as tk
from PIL import ImageTk, Image
import cv2 as cv
import numpy as np
import screens
if (RUN_ON_CM4):
    from picamera import PiCamera
import dcb



# Initialize TURBIDITY rating to value for "Unknown"
TurbidRating = 15


###############################################################################
###############################################################################
def create_details_screen(frame):
    global this_screen

    # Create and place the Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top = create_top_line(this_screen)
    photo = create_turbidity_photo(this_screen)
    chart = create_turbidity_chart(this_screen)

    # Place the Widgets
    top.grid(row=0, column=0, sticky='nw')
    photo.grid(row=1, column=0, sticky='nw')
    chart.grid(row=1, column=1, sticky='ne')

    return this_screen


###############################################################################
###############################################################################
def show_details_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
###############################################################################
def getTurbidRating():
    global TurbidRating
    return TurbidRating


###############################################################################
###############################################################################
def start_analysis():
    global TurbidRating
    TurbidRating = 15

    dcb.sendBacklightCommand('hatch')
    time.sleep(5)


###############################################################################
###############################################################################
def take_snapshot(camera):
    if (RUN_ON_CM4):
        camera.capture(SNAP_TURBID_RAW)
    time.sleep(1)


###############################################################################
###############################################################################
def analyze():
    global TurbidRating
    #global analyze_turbid_img

    gray_img = cv.imread(SNAP_TURBID_RAW, cv.IMREAD_GRAYSCALE)
    cropped_image = gray_img[100:500, 200:600]
    cv.imwrite(SNAP_TURBID_IMG, cropped_image)

    blur_score = cv.Laplacian(cropped_image, cv.CV_64F).var()
    print("Turbidity Score = %d" % blur_score)

    if (blur_score <= 20):
        TurbidRating = 2
    elif (blur_score > 200):
        TurbidRating = 0
    else:
        TurbidRating = 1


    # RLF: Move this logic to UPDATE function
    #photo_file = Image.open(SNAP_TURBID_IMG).resize((200,200), Image.ANTIALIAS)
    #analyze_turbid_img = ImageTk.PhotoImage(photo_file)
    #photo_frame.configure(image=screens.analyze_turbid_img)


###############################################################################
###############################################################################
def stop_analysis():
    dcb.sendBacklightCommand('off')
    time.sleep(2)


###############################################################################
###############################################################################
def on_back_press():
    screens.play_key_tone()
    screens.show_analyze_main_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame, text="Turbidity:", font=LG_FONT, fg=ANALYZE_COLOR)
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_turbidity_photo(frame):
    global photo_frame

    this_frame = tk.Frame(frame)

    # Crop the raw image to get rid of borders 
    """
    bgr_img = cv.imread(SNAP_TURBID_RAW)
    cropped_image = bgr_img[100:500, 200:600]
    cv.imwrite(SNAP_TURBID_IMG, cropped_image)

    global analyze_turbid_img # Keeps it persistent in memory
    photo_file = Image.open(SNAP_TURBID_IMG).resize((200,200), Image.ANTIALIAS)
    analyze_turbid_img = ImageTk.PhotoImage(photo_file)

    photo_frame.configure(image=screens.analyze_turbid_img)
    """
    photo_frame = tk.Label(this_frame, bd=8)
    photo_frame.grid(row=0, column=0, padx=10, pady=20, sticky='n')

    back_button = tk.Button(this_frame)
    back_button.configure(image=screens.back_btn_icon, borderwidth=0)
    back_button.configure(command=on_back_press)
    back_button.grid(row=1, column=0, padx=20)

    return this_frame


###############################################################################
###############################################################################
def create_turbidity_chart(frame):
    this_frame = tk.Frame(frame)

    photo_frame = tk.Label(this_frame, image=screens.match_turbidity_img)
    photo_frame.grid(row=0, column=0, padx=40, pady=20)

    return this_frame


###############################################################################
###############################################################################
def populateRatingBox(turbid_box, turbid_rating):
    if (turbid_rating == 0):
        text_string = "Clear"
        text_color  = ANALYZE_COLOR
        color_fill  = '#FFFFFF'
    elif (turbid_rating == 1):
        text_string = "Partly Cloudy"
        text_color  = ANALYZE_COLOR
        color_fill  = '#FFFFFF'
    elif (turbid_rating == 2):
        text_string = "Cloudy"
        text_color  = ANALYZE_COLOR
        color_fill  = '#FFFFFF'
    else:
        text_string = "Analyzing..."
        text_color  = ANALYZE_COLOR
        color_fill  = '#FFFFFF'

    # Populate the specified Rating Box
    turbid_box[0].itemconfig(turbid_box[1], fill=color_fill)
    turbid_box[0].itemconfig(turbid_box[2], text=text_string, fill=text_color)


