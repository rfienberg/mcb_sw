from globals import *
import tkinter as tk
from PIL import ImageTk, Image
from os.path import exists
import cv2 as cv
from sklearn.cluster import KMeans
import screens
if (RUN_ON_CM4):
    from picamera import PiCamera
import dcb
import time


BOX_START_X = 4
BOX_START_Y = 4
BOX_WIDTH = 156
BOX_HEIGHT = 32
BOX_MID_X = (BOX_START_X + (BOX_WIDTH/2))
BOX_MID_Y = (BOX_START_Y + (BOX_HEIGHT/2))

ARROW_COLOR = ANALYZE_COLOR
TRI_START_X = 0
TRI_WIDTH   = 32
TRI_HEIGHT  = 32
TAIL_WIDTH  = 42
TAIL_HEIGHT = 16


# List of base colors
COLOR_BINS = [
    # Pink
    ([250, 200, 195]), 
    # Red
    ([210, 40, 5]), 
    # Dark
    ([132, 60, 12]), 
    # Orange
    ([250, 140, 5]), 
    # Amber
    ([250, 200, 5]), 
    # Yellow
    ([250, 250, 5]), 
    # Green
    ([226, 240, 217]), 
    # Bloe
    ([100, 160, 220]), 
    # White (Clear)
    ([200, 200, 200]) 
]


# Initialize COLOR rating to value for "Unknown"
UNKNOWN_RATING = 15
ColorRating = UNKNOWN_RATING


###############################################################################
###############################################################################
def getColorRating():
    global ColorRating
    return ColorRating


###############################################################################
###############################################################################
def start_analysis():
    global ColorRating
    ColorRating = UNKNOWN_RATING

    dcb.sendBacklightCommand('white')
    time.sleep(5)


###############################################################################
###############################################################################
def take_snapshot(camera):
    if (RUN_ON_CM4):
        camera.capture(SNAP_COLOR_RAW)
    time.sleep(1)


###############################################################################
###############################################################################
def analyze_snapshot():
    global ColorRating

    if (exists(SNAP_COLOR_RAW)):

        # Crop the raw image to get rid of borders
        bgr_img = cv.imread(SNAP_COLOR_RAW)
        cropped_image = bgr_img[100:500, 200:600]

        # Save it as the new COLOR image
        cv.imwrite(SNAP_COLOR_IMG, cropped_image)

        # Convert it from BGR to RGB
        rgb_img = cv.cvtColor(cropped_image, cv.COLOR_BGR2RGB)

        # get the image's dominant color (rgb) value
        color = getDominantColor(rgb_img)

        # Find the best match to one of our base colors
        ColorRating = getColorMatch(color)
        #print("Matched Color #" + str(ColorRating))


###############################################################################
###############################################################################
def stop_analysis():
    dcb.sendBacklightCommand('off')
    time.sleep(2)


###############################################################################
###############################################################################
def getDominantColor(rgb_img):
    # reshaping to a list of pixels
    pixels = rgb_img.reshape((rgb_img.shape[0] * rgb_img.shape[1], 3))

    # using k-means to cluster pixels
    kmeans = KMeans(n_clusters=1)
    kmeans.fit(pixels)

    # the cluster centers are our dominant colors.
    rgb_dom = kmeans.cluster_centers_.astype(int)
    #print(rgb_dom[0])

    return rgb_dom[0]


###############################################################################
###############################################################################
def getColorMatch(rgb):
    minimum = 10000
    match_index = 0

    for i in range(len(COLOR_BINS)):
        rdelta = abs(rgb[0] - COLOR_BINS[i][0])
        gdelta = abs(rgb[1] - COLOR_BINS[i][1])
        bdelta = abs(rgb[2] - COLOR_BINS[i][2])
        delta = (rdelta + gdelta + bdelta)
        #print(delta)

        if (delta <= minimum):
            minimum = delta
            match_index = i

    return match_index


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
    if (exists(SNAP_COLOR_IMG)):
        global analyze_color_img # Keeps it persistent in memory
        this_graphic = Image.open(SNAP_COLOR_IMG).resize((200,200), Image.ANTIALIAS)
        analyze_color_img = ImageTk.PhotoImage(this_graphic)

        photo_frame.configure(image=analyze_color_img)

    # As long as we have a color rating to display...
    if (ColorRating != UNKNOWN_RATING):

        # Update the rating ARROW with the latest COLOR rating
        x1 = x2 = x3 = x4 = x5 = 0
        y1 = y2 = y3 = y4 = y5 = 0

        # As long as the color rating is legal...
        if (ColorRating < 9):
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

            # Adjust the ARROW coordinates based on the color rating
            rating = ColorRating
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
    section2 = create_color_rater(this_screen)

    # Place the Widgets
    top_line.grid(row=0, column=0, columnspan=2, pady=10, sticky='nw')
    section1.grid(row=1, column=0, padx=20, sticky='e')
    section2.grid(row=1, column=1, padx=20)

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=LG_FONT, fg=ANALYZE_COLOR)
    l1.configure(text="Color Analysis:")
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
def create_color_rater(frame):
    this_frame = tk.Frame(frame)

    w1 = create_rating_chart(this_frame)
    w2 = create_rating_arrow(this_frame)
    w1.grid(row=0, column=0)
    w2.grid(row=0, column=1)

    return this_frame


###############################################################################
###############################################################################
def create_rating_chart(frame):
    # Create and place the Frames
    this_frame = tk.Frame(frame)
    f1 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)

    # Create and place the Canvas
    c1 = tk.Canvas(f1, width=160, height=295)
    c1.grid(row=0, column=0)

    # The x coordinates will be fixed
    x1 = BOX_START_X
    x2 = x1+BOX_WIDTH
    x3 = x1 + (BOX_WIDTH/2)

    # For each of 9 color ratings...
    for c in range(9):

        # Compute this rectangle's coordinates
        y1 = BOX_START_Y + (c*BOX_HEIGHT)
        y2 = y1 + BOX_HEIGHT
        y3 = y1 + (BOX_HEIGHT/2)

        # Create a rectangle and it's items
        rect_item = c1.create_rectangle(x1, y1, x2, y2)
        text_item = c1.create_text(x3, y3)
        c1.itemconfig(rect_item, width=2)
        c1.itemconfig(rect_item, outline=ANALYZE_COLOR)
        c1.itemconfig(text_item, font=("Arial", 12))
        color_items = (c1, rect_item, text_item)

        # Populate this rectangle with color and text string
        populateRatingBox(color_items, c)

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
def getColorRatingParams(color_rating):
    if (color_rating == 0):
        text_string = "Pink"
        text_color  = '#D22805'
        color_fill  = '#FAC8C3'
    elif (color_rating == 1):
        text_string = "Red"
        text_color  = '#FAC8C3'
        color_fill  = '#D22805'
    elif (color_rating == 2):
        text_string = "Dark"
        text_color  = '#FFFFB7'
        color_fill  = '#843C0C'
    elif (color_rating == 3):
        text_string = "Orange"
        text_color  = '#D22805'
        color_fill  = '#FF8C00'
    elif (color_rating == 4):
        text_string = "Amber"
        text_color  = '#7F6000'
        color_fill  = '#FAC800'
    elif (color_rating == 5):
        text_string = "Yellow"
        text_color  = '#843C0C'
        color_fill  = '#FAFA00'
    elif (color_rating == 6):
        text_string = "Green"
        text_color  = '#385723'
        color_fill  = '#E2F0D9'
    elif (color_rating == 7):
        text_string = "Blue"
        text_color  = 'brown'
        color_fill  = '#64A0DC'
    elif (color_rating == 8):
        text_string = "White"
        text_color  = '#000000'
        color_fill  = '#F2F2F2'
    else:
        text_string = "Analyzing..."
        text_color  = ANALYZE_COLOR
        color_fill  = '#FFFFFF'

    return (text_string, text_color, color_fill)


###############################################################################
###############################################################################
def populateRatingBox(rating_box, color_rating):
    # Get this Color Rating's corresponding parameters
    (text_string, text_color, color_fill) = getColorRatingParams(color_rating)

    # Unpack the "rating_box" argument:
    canvas  = rating_box[0]
    rect_id = rating_box[1]
    text_id = rating_box[2]

    # Populate the specified Rating Box
    canvas.itemconfig(rect_id, fill=color_fill)
    canvas.itemconfig(text_id, fill=text_color)
    canvas.itemconfig(text_id, text=text_string)




