from globals import *
import tkinter as tk
import screens
import telemetry



###############################################################################
# Display the ENGINEERING screen in the screen area
###############################################################################
def show_info_screen():
    global this_screen
    this_screen.tkraise()
    periodic_screen_update()


###############################################################################
# Update the ENGINEERING screen widgets based on the latest data
###############################################################################
def periodic_screen_update():
    global telem_box
    global this_screen, updates

    telem = telemetry.getLatestTelemetry().rstrip()
    #print(telem)
    telem_box.config(text=telem)

    # Schedule the next screen update
    updates = this_screen.after(1000, periodic_screen_update)


###############################################################################
# Exits back to the INFO main screen
###############################################################################
def on_back_press():
    global this_screen, updates

    this_screen.after_cancel(updates)

    # Chirp
    screens.play_key_tone()

    # Go back to the main screen
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
    bline.grid(row=1, column=0, padx=80, pady=20)

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the widgets
    l1 = tk.Label(this_frame, text="Engineering Info")
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
    global telem_box

    this_frame = tk.Frame(frame)

    f1 = tk.LabelFrame(this_frame)
    f2 = tk.LabelFrame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=1, column=0)

    telem_lab = tk.Label(f1)
    telem_lab.configure(text="Telemetry: ")
    telem_box = tk.Label(f1)
    telem_box.configure(width=70, bg="white", relief=tk.SUNKEN, anchor=tk.W)
    telem_lab.grid(row=0, column=0, padx=10, pady=10)
    telem_box.grid(row=0, column=1, padx=10, pady=10)

    return this_frame


