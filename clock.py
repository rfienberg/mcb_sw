from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import datetime
import screens


BIG_FONT = ("Georgia", 30)
MY_FONT = ('Calibri', 30)
MY_FG = '#0070C0'

###############################################################################
###############################################################################
def create_screen(frame):
    global this_screen

    # Open up the image files and size them correctly
    global inc_btn_icon
    inc_img = Image.open("Icons/arrow_up.png").resize((40,40), Image.ANTIALIAS)
    inc_btn_icon = ImageTk.PhotoImage(inc_img)
    global dec_btn_icon
    dec_img = inc_img.rotate(180)
    dec_btn_icon = ImageTk.PhotoImage(dec_img)
    global ok_btn_icon
    ok_btn_img = Image.open("Icons/ok_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    ok_btn_icon = ImageTk.PhotoImage(ok_btn_img)
    global cancel_btn_icon
    cancel_btn_img = Image.open("Icons/cancel_btn_icon.png").resize((150,50), Image.ANTIALIAS)
    cancel_btn_icon = ImageTk.PhotoImage(cancel_btn_img)

    # Create the Frame for this screen
    this_screen = tk.LabelFrame(frame, text="Set Date/Time Screen")
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets for this screen
    top = create_top_line(this_screen)
    time_adj = create_time_adjuster(this_screen)
    date_adj = create_date_adjuster(this_screen)
    bot = create_bottom_line(this_screen)

    # Place the Widgets into the Frame
    top.grid(row=0, column=0, columnspan=10, sticky='nw')
    time_adj.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
    date_adj.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
    bot.grid(row=10, column=0, columnspan=10, pady=20)

    return this_screen


###############################################################################
###############################################################################
def show_screen():
    global this_screen

    now = datetime.datetime.now()
    new_hour.set(now.strftime("%I"))
    new_minute.set(now.strftime("%M"))
    new_ampm.set(now.strftime("%p"))
    new_month.set(now.strftime("%m"))
    new_day.set(now.strftime("%d"))
    new_year.set(now.strftime("%y"))

    this_screen.tkraise()


###############################################################################
###############################################################################
def inc_hours():
    hours = int(new_hour.get())
    if (hours < 12):
        hours = hours + 1
        screens.play_key_tone()
    new_hour.set(str(hours).zfill(2))


###############################################################################
###############################################################################
def dec_hours():
    hours = int(new_hour.get())
    if (hours > 1):
        hours = hours - 1
        screens.play_key_tone()
    new_hour.set(str(hours).zfill(2))


###############################################################################
###############################################################################
def inc_minutes():
    minutes = int(new_minute.get())
    if (minutes < 59):
        minutes = minutes + 1
        screens.play_key_tone()
    new_minute.set(str(minutes).zfill(2))


###############################################################################
###############################################################################
def dec_minutes():
    minutes = int(new_minute.get())
    if (minutes > 0):
        minutes = minutes - 1
        screens.play_key_tone()
    new_minute.set(str(minutes).zfill(2))


###############################################################################
###############################################################################
def inc_ampm():
    if (new_ampm.get() != "PM"):
        screens.play_key_tone()
        new_ampm.set("PM")


###############################################################################
###############################################################################
def dec_ampm():
    if (new_ampm.get() != "AM"):
        screens.play_key_tone()
        new_ampm.set("AM")


###############################################################################
###############################################################################
def inc_months():
    months = int(new_month.get())
    if (months < 12):
        months = months + 1
        screens.play_key_tone()
    new_month.set(str(months).zfill(2))


###############################################################################
###############################################################################
def dec_months():
    months = int(new_month.get())
    if (months > 1):
        months = months - 1
        screens.play_key_tone()
    new_month.set(str(months).zfill(2))


###############################################################################
###############################################################################
def inc_days():
    days = int(new_day.get())
    if (days < 31):
        days = days + 1
        screens.play_key_tone()
    new_day.set(str(days).zfill(2))


###############################################################################
###############################################################################
def dec_days():
    days = int(new_day.get())
    if (days > 1):
        days = days - 1
        screens.play_key_tone()
    new_day.set(str(days).zfill(2))


###############################################################################
###############################################################################
def inc_years():
    years = int(new_year.get())
    if (years < 99):
        years = years + 1
        screens.play_key_tone()
    new_year.set(str(years).zfill(2))


###############################################################################
###############################################################################
def dec_years():
    years = int(new_year.get())
    if (years > 22):
        years = years - 1
        screens.play_key_tone()
    new_year.set(str(years).zfill(2))


###############################################################################
###############################################################################
def on_ok_press():
    screens.play_key_tone()
    screens.show_setup_screen()


###############################################################################
###############################################################################
def on_cancel_press():
    screens.play_key_tone()
    screens.show_setup_screen()


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    title_label = tk.Label(this_frame)
    title_label.configure(text="Set Time/Date:", font=BIG_FONT, fg=MY_FG)
    title_label.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_hour_adjuster(window):
    global new_hour

    new_hour = tk.StringVar()
    new_hour.set("12")

    this_frame = tk.Frame(window)
    ent_frame = tk.Frame(this_frame)
    btn_frame = tk.Frame(this_frame)

    my_label = tk.Label(ent_frame)
    my_entry = tk.Entry(ent_frame)

    my_label.configure(fg=MY_FG, text="Hour")
    my_entry.configure(width=4, justify='center', bd=4, relief='groove')
    my_entry.configure(font=MY_FONT, fg=MY_FG, bg='white')
    my_entry.configure(textvariable=new_hour)

    my_label.grid(row=0, column=0)
    my_entry.grid(row=1, column=0)

    inc_btn = tk.Button(btn_frame)
    dec_btn = tk.Button(btn_frame)

    inc_btn.configure(image=inc_btn_icon, borderwidth=0)
    inc_btn.configure(repeatdelay=500, repeatinterval=100)
    inc_btn.configure(command=inc_hours)
    dec_btn.configure(image=dec_btn_icon, borderwidth=0)
    dec_btn.configure(repeatdelay=500, repeatinterval=100)
    dec_btn.configure(command=dec_hours)

    inc_btn.grid(row=0, column=0)
    dec_btn.grid(row=1, column=0)

    ent_frame.grid(row=0, column=0)
    btn_frame.grid(row=0, column=1)

    return this_frame


###############################################################################
###############################################################################
def create_minute_adjuster(window):
    global new_minute

    new_minute = tk.StringVar()
    new_minute.set("30")

    this_frame = tk.Frame(window)
    ent_frame = tk.Frame(this_frame)
    btn_frame = tk.Frame(this_frame)

    my_label = tk.Label(ent_frame)
    my_entry = tk.Entry(ent_frame)

    my_label.configure(fg=MY_FG, text="Minute")
    my_entry.configure(width=4, justify='center', bd=4, relief='groove')
    my_entry.configure(font=MY_FONT, fg=MY_FG, bg='white')
    my_entry.configure(textvariable=new_minute)

    my_label.grid(row=0, column=0)
    my_entry.grid(row=1, column=0)

    inc_btn = tk.Button(btn_frame)
    dec_btn = tk.Button(btn_frame)

    inc_btn.configure(image=inc_btn_icon, borderwidth=0)
    inc_btn.configure(repeatdelay=500, repeatinterval=100)
    inc_btn.configure(command=inc_minutes)
    dec_btn.configure(image=dec_btn_icon, borderwidth=0)
    dec_btn.configure(repeatdelay=500, repeatinterval=100)
    dec_btn.configure(command=dec_minutes)

    inc_btn.grid(row=0, column=0)
    dec_btn.grid(row=1, column=0)

    ent_frame.grid(row=0, column=0)
    btn_frame.grid(row=0, column=1)

    return this_frame


###############################################################################
###############################################################################
def create_ampm_adjuster(window):
    global new_ampm

    new_ampm = tk.StringVar()
    new_ampm.set("AM")

    this_frame = tk.Frame(window)
    ent_frame = tk.Frame(this_frame)
    btn_frame = tk.Frame(this_frame)

    my_label = tk.Label(ent_frame)
    my_entry = tk.Entry(ent_frame)

    my_label.configure(fg=MY_FG, text="AM/PM")
    my_entry.configure(width=4, justify='center', bd=4, relief='groove')
    my_entry.configure(font=MY_FONT, fg=MY_FG, bg='white')
    my_entry.configure(textvariable=new_ampm)

    my_label.grid(row=0, column=0)
    my_entry.grid(row=1, column=0)

    inc_btn = tk.Button(btn_frame)
    dec_btn = tk.Button(btn_frame)

    inc_btn.configure(image=inc_btn_icon, borderwidth=0)
    inc_btn.configure(command=inc_ampm)
    dec_btn.configure(image=dec_btn_icon, borderwidth=0)
    dec_btn.configure(command=dec_ampm)

    inc_btn.grid(row=0, column=0)
    dec_btn.grid(row=1, column=0)

    ent_frame.grid(row=0, column=0)
    btn_frame.grid(row=0, column=1)

    return this_frame


###############################################################################
###############################################################################
def create_month_adjuster(window):
    global new_month

    new_month = tk.StringVar()
    new_month.set("01")

    this_frame = tk.Frame(window)
    ent_frame = tk.Frame(this_frame)
    btn_frame = tk.Frame(this_frame)

    my_label = tk.Label(ent_frame)
    my_entry = tk.Entry(ent_frame)

    my_label.configure(fg=MY_FG, text="Month")
    my_entry.configure(width=4, justify='center', bd=4, relief='groove')
    my_entry.configure(font=MY_FONT, fg=MY_FG, bg='white')
    my_entry.configure(textvariable=new_month)

    my_label.grid(row=0, column=0)
    my_entry.grid(row=1, column=0)

    inc_btn = tk.Button(btn_frame)
    dec_btn = tk.Button(btn_frame)

    inc_btn.configure(image=inc_btn_icon, borderwidth=0)
    inc_btn.configure(repeatdelay=500, repeatinterval=100)
    inc_btn.configure(command=inc_months)
    dec_btn.configure(image=dec_btn_icon, borderwidth=0)
    dec_btn.configure(repeatdelay=500, repeatinterval=100)
    dec_btn.configure(command=dec_months)

    inc_btn.grid(row=0, column=0)
    dec_btn.grid(row=1, column=0)

    ent_frame.grid(row=0, column=0)
    btn_frame.grid(row=0, column=1)

    return this_frame


###############################################################################
###############################################################################
def create_day_adjuster(window):
    global new_day

    new_day = tk.StringVar()
    new_day.set("01")

    this_frame = tk.Frame(window)
    ent_frame = tk.Frame(this_frame)
    btn_frame = tk.Frame(this_frame)

    my_label = tk.Label(ent_frame)
    my_entry = tk.Entry(ent_frame)

    my_label.configure(fg=MY_FG, text="Day")
    my_entry.configure(width=4, justify='center', bd=4, relief='groove')
    my_entry.configure(font=MY_FONT, fg=MY_FG, bg='white')
    my_entry.configure(textvariable=new_day)

    my_label.grid(row=0, column=0)
    my_entry.grid(row=1, column=0)

    inc_btn = tk.Button(btn_frame)
    dec_btn = tk.Button(btn_frame)

    inc_btn.configure(image=inc_btn_icon, borderwidth=0)
    inc_btn.configure(repeatdelay=500, repeatinterval=100)
    inc_btn.configure(command=inc_days)
    dec_btn.configure(image=dec_btn_icon, borderwidth=0)
    dec_btn.configure(repeatdelay=500, repeatinterval=100)
    dec_btn.configure(command=dec_days)

    inc_btn.grid(row=0, column=0)
    dec_btn.grid(row=1, column=0)

    ent_frame.grid(row=0, column=0)
    btn_frame.grid(row=0, column=1)

    return this_frame


###############################################################################
###############################################################################
def create_year_adjuster(window):
    global new_year

    new_year = tk.StringVar()
    new_year.set("22")

    this_frame = tk.Frame(window)
    ent_frame = tk.Frame(this_frame)
    btn_frame = tk.Frame(this_frame)

    my_label = tk.Label(ent_frame)
    my_entry = tk.Entry(ent_frame)

    my_label.configure(fg=MY_FG, text="Year")
    my_entry.configure(width=4, justify='center', bd=4, relief='groove')
    my_entry.configure(font=MY_FONT, fg=MY_FG, bg='white')
    my_entry.configure(textvariable=new_year)

    my_label.grid(row=0, column=0)
    my_entry.grid(row=1, column=0)

    inc_btn = tk.Button(btn_frame)
    dec_btn = tk.Button(btn_frame)

    inc_btn.configure(image=inc_btn_icon, borderwidth=0)
    inc_btn.configure(repeatdelay=500, repeatinterval=100)
    inc_btn.configure(command=inc_years)
    dec_btn.configure(image=dec_btn_icon, borderwidth=0)
    dec_btn.configure(repeatdelay=500, repeatinterval=100)
    dec_btn.configure(command=dec_years)

    inc_btn.grid(row=0, column=0)
    dec_btn.grid(row=1, column=0)

    ent_frame.grid(row=0, column=0)
    btn_frame.grid(row=0, column=1)

    return this_frame


###############################################################################
###############################################################################
def create_time_adjuster(window):
    this_frame = tk.LabelFrame(window)

    time_label = tk.Label(this_frame, text="Time:")
    time_label.configure(font=MY_FONT, fg=MY_FG)

    hour_adj   = create_hour_adjuster(this_frame)
    minute_adj = create_minute_adjuster(this_frame)
    ampm_adj   = create_ampm_adjuster(this_frame)

    time_label.grid( row=0, column=0, padx=10)
    hour_adj.grid( row=0, column=1, padx=5)
    minute_adj.grid(row=0, column=2, padx=5)
    ampm_adj.grid(row=0, column=3, padx=5)

    return this_frame


###############################################################################
###############################################################################
def create_date_adjuster(window):
    this_frame = tk.LabelFrame(window)

    date_label = tk.Label(this_frame, text="Date:")
    date_label.configure(font=MY_FONT, fg=MY_FG)

    month_adj = create_month_adjuster(this_frame)
    day_adj   = create_day_adjuster(this_frame)
    year_adj  = create_year_adjuster(this_frame)

    date_label.grid( row=0, column=0, padx=10)
    month_adj.grid( row=0, column=1, padx=5)
    day_adj.grid(row=0, column=2, padx=5)
    year_adj.grid(row=0, column=3, padx=5)

    return this_frame


###############################################################################
###############################################################################
def create_bottom_line(frame):
    this_frame = tk.Frame(frame)

    ok_button = tk.Button(this_frame)
    ok_button.configure(image=ok_btn_icon, borderwidth=0)
    ok_button.configure(command=on_ok_press)
    ok_button.grid(row=0, column=0, padx=40, sticky='w')

    padding = tk.Label(this_frame)
    padding.grid(row=0, column=1, padx=100)

    cancel_button = tk.Button(this_frame)
    cancel_button.configure(image=cancel_btn_icon, borderwidth=0)
    cancel_button.configure(command=on_cancel_press)
    cancel_button.grid(row=0, column=2, padx=40)

    return this_frame


