from globals import *
import time
import tkinter as tk
from PIL import ImageTk, Image
import cv2 as cv
from sklearn.cluster import KMeans
import screens
if (RUN_ON_CM4):
    from picamera import PiCamera
import dcb



# List of base colors
COLOR_BINS = [
    ([250, 200, 195]), 
    ([210, 40, 5]), 
    ([132, 60, 12]), 
    ([250, 140, 5]), 
    ([250, 200, 5]), 
    ([250, 250, 5]), 
    ([226, 240, 217]), 
    ([100, 160, 220]), 
    ([200, 200, 200]) 
]

# Initialize COLOR rating to value for "Unknown"
ColorRating = 15


###############################################################################
###############################################################################
def create_details_screen(frame):
    global this_screen

    # Create and place the Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top = create_top_line(this_screen)
    photo = create_color_photo(this_screen)
    chart = create_color_chart(this_screen)

    # Place the Widgets
    top.grid(row=0, column=0, columnspan=4, sticky='nw')
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
def getColorRating():
    global ColorRating
    return ColorRating


###############################################################################
###############################################################################
def start_analysis():
    global ColorRating
    ColorRating = 15

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
def analyze():
    global ColorRating
    #global analyze_color_img

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
    print("Matched Color #" + str(ColorRating))

    # RLF: Move this logic to UPDATE function
    # Display the cropped image in the photo frame
    #photo_file = Image.open(SNAP_COLOR_IMG).resize((200,200), Image.ANTIALIAS)
    #analyze_color_img = ImageTk.PhotoImage(photo_file)
    #photo_frame.configure(image=screens.analyze_color_img)


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
    print(rgb_dom[0])

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

    #print(minimum)
    return match_index


###############################################################################
###############################################################################
def on_back_press():
    screens.play_key_tone()
    screens.show_analyze_main_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame, text="Color Analysis:", font=LG_FONT, fg=ANALYZE_COLOR)
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_color_photo(frame):
    global photo_frame

    this_frame = tk.Frame(frame)

    # Crop the raw image to get rid of borders
    bgr_img = cv.imread(SNAP_COLOR_RAW)
    cropped_image = bgr_img[100:500, 200:600]
    cv.imwrite(SNAP_COLOR_IMG, cropped_image)

    photo_frame = tk.Label(this_frame, bd=8)
    photo_frame.configure(image=screens.analyze_color_img)
    photo_frame.grid(row=0, column=0, padx=10, pady=20, sticky='n')

    back_button = tk.Button(this_frame)
    back_button.configure(image=screens.back_btn_icon, borderwidth=0)
    back_button.configure(command=on_back_press)
    back_button.grid(row=1, column=0, padx=20)

    return this_frame


###############################################################################
###############################################################################
def create_color_chart(frame):
    this_frame = tk.Frame(frame)

    chart_frame = tk.Label(this_frame, image=screens.match_color_img)
    chart_frame.grid(row=0, column=0, padx=40, pady=20)

    return this_frame


###############################################################################
###############################################################################
def populateRatingBox(color_box, color_rating):
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
        color_fill  = '#FFFF00'
    elif (color_rating == 5):
        text_string = "Yellow"
        text_color  = '#843C0C'
        color_fill  = '#FAFA05'
    elif (color_rating == 6):
        text_string = "Green"
        text_color  = '#385723'
        color_fill  = '#E2F0D9'
    elif (color_rating == 7):
        text_string = "Blue"
        text_color  = 'brown'
        color_fill  = '#FFFFFF'
    elif (color_rating == 8):
        text_string = "White"
        text_color  = '#000000'
        color_fill  = '#F2F2F2'
    else:
        text_string = "Analyzing..."
        text_color  = ANALYZE_COLOR
        color_fill  = '#FFFFFF'

    # Populate the specified Rating Box
    color_box[0].itemconfig(color_box[1], fill=color_fill)
    color_box[0].itemconfig(color_box[2], text=text_string, fill=text_color)




