from globals import *
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import telemetry
import patient
from time import strftime
import screens

MY_BG = '#0070C0'
MY_FG = 'white'
MY_FONT = ('Calibri', 14)

GOOD_COLOR = '#17F12C'
BAD_COLOR = 'red'


###############################################################################
###############################################################################
def create_bar(window):
    global this_frame, pname, tstamp, battery

    # Open up the image files and size them correctly
    global charging_yes_icon
    this_graphic = Image.open("Graphics/charging_yes.png").resize((25,25), Image.ANTIALIAS)
    charging_yes_icon = ImageTk.PhotoImage(this_graphic)
    global charging_no_icon
    this_graphic = Image.open("Graphics/charging_no.png").resize((25,25), Image.ANTIALIAS)
    charging_no_icon = ImageTk.PhotoImage(this_graphic)

    # Create the Frame for this bar
    this_frame = tk.LabelFrame(window)
    this_frame.configure(bg=MY_BG)
    this_frame.grid(row=0, column=0, sticky='new')

    # Create the Widgets for this bar
    pname   = create_patient_name(this_frame)
    tstamp  = create_date_time(this_frame)
    battery = create_battery(this_frame)

    # Place the Widgets into the Frame
    pname.grid(  row=0, column=0, padx=5)
    tstamp.grid( row=0, column=1, padx=40)
    battery.grid(row=0, column=2, padx=80)

    return this_frame


###############################################################################
# Update the Title Bar widgets with the latest data
###############################################################################
def update_bar():
    patient_name = patient.get_patient_name()
    datetime_string = strftime('%x   %I:%M:%S %p')
    batterypct = telemetry.getBatteryChargePercent()
    charge_status = telemetry.getBatteryChargeStatus()

    pname.configure(text=patient_name)
    tstamp.configure(text=datetime_string)

    pct_text = str(batterypct) + '%'
    batt_cv.itemconfig(batt_text, text=pct_text)
    batt_cv.coords(batt_bar, 0, 0, (50*(batterypct/100)), 20)

    if (batterypct > 10):
        batt_cv.itemconfig(batt_bar, fill=GOOD_COLOR)
    else:
        batt_cv.itemconfig(batt_bar, fill=BAD_COLOR)

    if (charge_status == "Charging"):
        charging_yes.tkraise()
    else:
        charging_no.tkraise()


###############################################################################
###############################################################################
def create_patient_name(frame):
    label = tk.Label(frame)
    label.configure(text="New Patient", width=20, anchor='w')
    label.configure(font=MY_FONT, bg=MY_BG, fg=MY_FG)
    return label


###############################################################################
###############################################################################
def create_date_time(frame):
    label = tk.Label(frame)
    label.configure(width=20, anchor='w')
    label.configure(font=MY_FONT, bg=MY_BG, fg=MY_FG)
    return label


###############################################################################
###############################################################################
def create_battery(frame):
    global charging_no, charging_yes
    global batt_cv, batt_bar, batt_text

    this_frame = tk.Frame(frame, bg=MY_BG)

    charging_no = tk.Label(this_frame, bg=MY_BG)
    charging_no.configure(image=charging_no_icon)
    charging_no.grid(row=0, column=0, padx=10)

    charging_yes = tk.Label(this_frame, bg=MY_BG)
    charging_yes.configure(image=charging_yes_icon)
    charging_yes.grid(row=0, column=0, padx=10)

    batt_cv = tk.Canvas(this_frame)
    batt_cv.configure(height=20, width=50, highlightthickness=1)
    batt_bar = batt_cv.create_rectangle(0, 0, 50, 20, fill=GOOD_COLOR, outline='gray')
    batt_text = batt_cv.create_text(25, 10, text="100", font=('Tahoma', 10), fill='black')
    batt_cv.grid(row=0, column=1)

    npl_cv = tk.Canvas(this_frame)
    npl_cv.configure(height=10, width=3)
    npl_cv.grid(row=0, column=2)

    return this_frame


