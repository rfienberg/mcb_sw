from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import cv2 as cv
from sklearn.cluster import KMeans
import screens
if (RUN_ON_CM4):
    from picamera import PiCamera


BIG_FONT = ("Georgia", 30)
BIG_FG = 'brown'
MY_FONT = ('Calibri', 18)
MY_FG = 'brown'

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


###############################################################################
###############################################################################
def create_screen(frame):
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
def show_screen():
    global this_screen
    this_screen.tkraise()


###############################################################################
###############################################################################
def take_snapshot(camera):
    if (RUN_ON_CM4):
        camera.capture(SNAP_COLOR_RAW)


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
def analyze():
    global analyze_color_img

    # Crop the raw image to get rid of borders
    bgr_img = cv.imread(SNAP_COLOR_RAW)
    cropped_image = bgr_img[100:500, 200:600]
    cv.imwrite(SNAP_COLOR_IMG, cropped_image)

    # Convert it to rgb from bgr
    rgb_img = cv.cvtColor(cropped_image, cv.COLOR_BGR2RGB)

    # get the image's dominant color (rgb) value
    color = getDominantColor(rgb_img)

    # Find the best match to one of our base colors
    match = getColorMatch(color)
    print("Matched Color #" + str(match))

    # Display the cropped image in the photo frame
    photo_file = Image.open(SNAP_COLOR_IMG).resize((200,200), Image.ANTIALIAS)
    analyze_color_img = ImageTk.PhotoImage(photo_file)
    photo_frame.configure(image=analyze_color_img)


###############################################################################
###############################################################################
def on_back_press():
    screens.play_key_tone()
    screens.show_analyze_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame, text="Color Analysis:", font=BIG_FONT, fg=MY_FG)
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

    global analyze_color_img # Keeps it persistent in memory
    photo_file = Image.open(SNAP_COLOR_IMG).resize((200,200), Image.ANTIALIAS)
    analyze_color_img = ImageTk.PhotoImage(photo_file)

    photo_frame = tk.Label(this_frame, bd=8)
    photo_frame.configure(image=analyze_color_img)
    photo_frame.grid(row=0, column=0, padx=10, pady=20, sticky='n')

    global back_btn_icon
    back_btn_img = Image.open("Icons/back_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    back_btn_icon = ImageTk.PhotoImage(back_btn_img)
    back_button = tk.Button(this_frame)
    back_button.configure(image=back_btn_icon, borderwidth=0)
    back_button.configure(command=on_back_press)
    back_button.grid(row=1, column=0, padx=20)

    return this_frame


###############################################################################
###############################################################################
def create_color_chart(frame):
    this_frame = tk.Frame(frame)

    global match_color_img # Keeps it persistent in memory
    photo_file = Image.open("Icons/color_chart.png").resize((150,260), Image.ANTIALIAS)
    match_color_img = ImageTk.PhotoImage(photo_file)
    chart_frame = tk.Label(this_frame, image=match_color_img)
    chart_frame.grid(row=0, column=0, padx=40, pady=20)

    return this_frame

