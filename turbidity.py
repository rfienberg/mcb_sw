from globals import *
import time
import tkinter as tk
from PIL import ImageTk, Image
from os.path import exists
import cv2 as cv
import numpy as np
import screens
if (RUN_ON_CM4):
    from picamera import PiCamera
import dcb

BOX_START_X = 4
BOX_START_Y = 10
BOX_WIDTH   = 180
BOX_HEIGHT  = 50
BOX_MID_X = (BOX_START_X + (BOX_WIDTH/2))
BOX_MID_Y = (BOX_START_Y + (BOX_HEIGHT/2))

ARROW_COLOR = ANALYZE_COLOR
TRI_START_X = 0
TRI_WIDTH   = 32
TRI_HEIGHT  = 32
TAIL_WIDTH  = 42
TAIL_HEIGHT = 16

CLEAR_SCORE_THRESHOLD  = 140
CLOUDY_SCORE_THRESHOLD = 20

CLEAR_RATING  = 0
PARTLY_RATING = 1
CLOUDY_RATING = 2

# Initialize TURBIDITY rating to value for "Unknown"
UNKNOWN_RATING = 15
TurbidRating = 15


###############################################################################
###############################################################################
def getTurbidRating():
    global TurbidRating
    return TurbidRating


###############################################################################
###############################################################################
def start_analysis():
    global TurbidRating
    TurbidRating = UNKNOWN_RATING

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
def analyze_snapshot():
    global TurbidRating

    if (exists(SNAP_TURBID_RAW)):

        gray_img = cv.imread(SNAP_TURBID_RAW, cv.IMREAD_GRAYSCALE)
        cropped_image = gray_img[100:500, 200:600]
        cv.imwrite(SNAP_TURBID_IMG, cropped_image)

        blur_score = cv.Laplacian(cropped_image, cv.CV_64F).var()
        print("Turbidity Score = %d" % blur_score)

        if (blur_score <= CLOUDY_SCORE_THRESHOLD):
            TurbidRating = CLOUDY_RATING
        elif (blur_score > CLEAR_SCORE_THRESHOLD):
            TurbidRating = CLEAR_RATING
        else:
            TurbidRating = PARTLY_RATING


###############################################################################
###############################################################################
def stop_analysis():
    dcb.sendBacklightCommand('off')
    time.sleep(2)


###############################################################################
###############################################################################
def show_details_screen():
    global this_screen
    this_screen.tkraise()
    periodic_screen_update()


###############################################################################
###############################################################################
def periodic_screen_update():
    global this_screen, updates

    # Update with the latest snapshot image
    if (exists(SNAP_TURBID_IMG)):
        global analyze_turbid_img # Keeps it persistent in memory
        this_graphic = Image.open(SNAP_TURBID_IMG).resize((200,200), Image.ANTIALIAS)
        analyze_turbid_img = ImageTk.PhotoImage(this_graphic)

        # Display the updated photo image in its frame
        photo_frame.configure(image=analyze_turbid_img)

    # Update the rating ARROW with the latest TURBIDITY rating
        x1 = x2 = x3 = x4 = x5 = 0
        y1 = y2 = y3 = y4 = y5 = 0

        # As long as the turbidity rating is legal...
        if (TurbidRating < 3):
            # Initialize the ARROW coordinates to the top
            x1 = TRI_WIDTH
            x2 = TRI_START_X
            x3 = TRI_WIDTH
            x4 = x3
            x5 = x4 + TAIL_WIDTH

            y2 = BOX_MID_Y
            y1 = y2 - (TRI_HEIGHT/2)
            y3 = y2 + (TRI_HEIGHT/2)
            y4 = y2 - (TAIL_HEIGHT/2)
            y5 = y2 + (TAIL_HEIGHT/2)

            # Adjust the ARROW coordinates based on the turbidity rating
            rating = TurbidRating
            y1 = y1 + (rating * TRI_HEIGHT)
            y2 = y2 + (rating * TRI_HEIGHT)
            y3 = y3 + (rating * TRI_HEIGHT)
            y4 = y4 + (rating * TRI_HEIGHT)
            y5 = y5 + (rating * TRI_HEIGHT)

        # Now apply the new ARROW coordinates
        points = [x1,y1, x2,y2, x3,y3]
        arrow = rating_arrow[0]
        triangle = rating_arrow[1]
        rectangle = rating_arrow[2]
        arrow.coords(triangle, points)
        arrow.coords(rectangle, x4,y4, x5,y5)

    # Schedule the next screen update
    updates = this_screen.after(5000, periodic_screen_update)


###############################################################################
###############################################################################
def on_back_press():
    global this_screen, updates

    this_screen.after_cancel(updates)

    screens.play_key_tone()
    screens.show_analyze_main_screen()


###############################################################################
###############################################################################
def create_details_screen(frame):
    global this_screen

    # Create and place the Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top_line = create_top_line(this_screen)
    section1 = create_photo_frame(this_screen)
    section2 = create_turbidity_rater(this_screen)

    # Place the Widgets
    top_line.grid(row=0, column=0, columnspan=2, pady=10, sticky='nw')
    section1.grid(row=1, column=0, padx=20)
    section2.grid(row=1, column=1, padx=20)

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=LG_FONT, fg=ANALYZE_COLOR)
    l1.configure(text="Turbidity Analysis:")
    l1.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_photo_frame(frame):
    global photo_frame

    this_frame = tk.Frame(frame)
    f1 = tk.LabelFrame(this_frame, bd=4)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, padx=10, pady=10)
    f2.grid(row=1, column=0, padx=10, pady=10)

    p1 = tk.Label(f1)
    p1.grid(row=0, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.back_btn_icon, borderwidth=0)
    b1.configure(command=on_back_press)
    b1.grid(row=0, column=0)

    photo_frame = p1

    return this_frame


###############################################################################
###############################################################################
def create_turbidity_rater(frame):
    this_frame = tk.Frame(frame)

    w1 = create_rating_chart(this_frame)
    w2 = create_rating_arrow(this_frame)
    w1.grid(row=0, column=0)
    w2.grid(row=0, column=1)

    return this_frame


###############################################################################
###############################################################################
def create_rating_chart(frame):
    global turbid_items

    this_frame = tk.Frame(frame)

    f1 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)

    # Create and place the Canvas
    c1 = tk.Canvas(f1, width=BOX_WIDTH+4, height=295)
    c1.grid(row=0, column=0)

    # The x coordinates will be fixed
    x1 = BOX_START_X
    x2 = x1+BOX_WIDTH
    x3 = x1 + (BOX_WIDTH/2)

    # For each of 3 turbidity ratings...
    for t in range(3):

        # Compute this rectangle's coordinates
        y1 = BOX_START_Y + (t*BOX_HEIGHT)
        y2 = y1 + BOX_HEIGHT
        y3 = y1 + (BOX_HEIGHT/2) + 4

        # Create a rectangle and it's items
        rect_item = c1.create_rectangle(x1,y1, x2,y2, width=3, outline=ANALYZE_COLOR)
        text_item = c1.create_text(110, 60, font=("Arial", 22))
        image_item = c1.create_image(x3, y3)

        turbid_items = (c1, rect_item, image_item)

        # Populate this rectangle with turbidity rating
        populateRatingBox(turbid_items, t)

    return this_frame


###############################################################################
###############################################################################
def create_rating_arrow(frame):
    global rating_arrow

    # Create and place the Frames
    this_frame = tk.Frame(frame)
    f1 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)

    # Create and place the Canvas
    c1 = tk.Canvas(f1, width=80, height=295)
    c1.grid(row=0, column=0)

    points = [0,0, 0,0, 0,0]
    t1 = c1.create_polygon(points, fill=ARROW_COLOR)
    r1 = c1.create_rectangle(0,0, 0,0, fill=ARROW_COLOR)
    rating_arrow = (c1, t1, r1)

    return this_frame


###############################################################################
###############################################################################
def populateRatingBox(rating_box, turbid_rating):
    if (turbid_rating == CLEAR_RATING):
        turb_image  = screens.turb_clear_icon
    elif (turbid_rating == PARTLY_RATING):
        turb_image  = screens.turb_partly_icon
    elif (turbid_rating == CLOUDY_RATING):
        turb_image  = screens.turb_cloudy_icon
    else:
        turb_image  = screens.turb_analyzing_icon

    # Unpack the "rating_box" argument:
    canvas  = rating_box[0]
    rect_id = rating_box[1]
    pict_id = rating_box[2]

    # Populate the specified Rating Box
    canvas.itemconfig(rect_id, fill='white')
    canvas.itemconfig(pict_id, image=turb_image)

