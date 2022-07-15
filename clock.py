from globals import *
import tkinter as tk
import datetime
import screens


ADJ_FONT = ('Calibri', 22)



###############################################################################
###############################################################################
def show_setup_screen():
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
    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def on_cancel_press():
    screens.play_key_tone()
    screens.show_setup_main_screen()


###############################################################################
###############################################################################
def create_setup_screen(frame):
    global this_screen

    # Create the Frame for this screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets for this screen
    top_line = create_top_line(this_screen)
    time_adj = create_time_adjuster(this_screen)
    date_adj = create_date_adjuster(this_screen)
    bot_line = create_bottom_line(this_screen)

    # Place the Widgets into the Frame
    top_line.grid(row=0, column=0, columnspan=10, sticky='nw')
    time_adj.grid(row=1, column=0, padx=40, pady=10, sticky='ew')
    date_adj.grid(row=2, column=0, padx=40, pady=10, sticky='ew')
    bot_line.grid(row=3, column=0, pady=20)

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(text="Set Time/Date:", font=LG_FONT, fg=SETUP_COLOR)
    l1.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_time_adjuster(window):
    this_frame = tk.LabelFrame(window)

    l1 = tk.Label(this_frame, text="Time:")
    l1.configure(font=MD_FONT, fg=SETUP_COLOR)
    sl = tk.Label(this_frame)

    a1 = create_hour_adjuster(this_frame)
    a2 = create_minute_adjuster(this_frame)
    a3 = create_ampm_adjuster(this_frame)

    l1.grid(row=0, column=0, padx=10)
    a1.grid(row=0, column=1, padx=5)
    a2.grid(row=0, column=2, padx=5)
    a3.grid(row=0, column=3, padx=5)
    sl.grid(row=0, column=4, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_date_adjuster(window):
    this_frame = tk.LabelFrame(window)

    l1 = tk.Label(this_frame, text="Date:")
    l1.configure(font=MD_FONT, fg=SETUP_COLOR)
    sl = tk.Label(this_frame)

    a1 = create_month_adjuster(this_frame)
    a2 = create_day_adjuster(this_frame)
    a3 = create_year_adjuster(this_frame)

    l1.grid(row=0, column=0, padx=10)
    a1.grid(row=0, column=1, padx=5)
    a2.grid(row=0, column=2, padx=5)
    a3.grid(row=0, column=3, padx=5)
    sl.grid(row=0, column=4, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_bottom_line(frame):
    this_frame = tk.Frame(frame)

    b1 = tk.Button(this_frame)
    b1.configure(image=screens.blu_ok_btn_icon, borderwidth=0)
    b1.configure(command=on_ok_press)

    sl = tk.Label(this_frame)

    b2 = tk.Button(this_frame)
    b2.configure(image=screens.blu_cancel_btn_icon, borderwidth=0)
    b2.configure(command=on_cancel_press)

    b1.grid(    row=0, column=0, pady=10)
    sl.grid( row=0, column=1, padx=80)
    b2.grid(row=0, column=2, pady=10)

    return this_frame


###############################################################################
###############################################################################
def create_hour_adjuster(window):
    global new_hour
    new_hour = tk.StringVar()

    this_frame = tk.Frame(window)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=0, column=1, sticky='s')

    l1 = tk.Label(f1)
    l1.configure(fg=SETUP_COLOR, text="Hour")
    e1 = tk.Entry(f1)
    e1.configure(width=4, justify='center', bd=4, relief='groove')
    e1.configure(font=ADJ_FONT, fg=SETUP_COLOR, bg='white')
    e1.configure(textvariable=new_hour)
    l1.grid(row=0, column=0)
    e1.grid(row=1, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.inc_btn_icon, borderwidth=0)
    b1.configure(repeatdelay=500, repeatinterval=100)
    b1.configure(command=inc_hours)
    b2 = tk.Button(f2)
    b2.configure(image=screens.dec_btn_icon, borderwidth=0)
    b2.configure(repeatdelay=500, repeatinterval=100)
    b2.configure(command=dec_hours)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_minute_adjuster(window):
    global new_minute
    new_minute = tk.StringVar()

    this_frame = tk.Frame(window)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=0, column=1, sticky='s')

    l1 = tk.Label(f1)
    l1.configure(fg=SETUP_COLOR, text="Minute")
    e1 = tk.Entry(f1)
    e1.configure(width=4, justify='center', bd=4, relief='groove')
    e1.configure(font=ADJ_FONT, fg=SETUP_COLOR, bg='white')
    e1.configure(textvariable=new_minute)
    l1.grid(row=0, column=0)
    e1.grid(row=1, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.inc_btn_icon, borderwidth=0)
    b1.configure(repeatdelay=500, repeatinterval=100)
    b1.configure(command=inc_minutes)
    b2 = tk.Button(f2)
    b2.configure(image=screens.dec_btn_icon, borderwidth=0)
    b2.configure(repeatdelay=500, repeatinterval=100)
    b2.configure(command=dec_minutes)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_ampm_adjuster(window):
    global new_ampm
    new_ampm = tk.StringVar()

    this_frame = tk.Frame(window)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=0, column=1, sticky='s')

    l1 = tk.Label(f1)
    l1.configure(fg=SETUP_COLOR, text="AM/PM")
    e1 = tk.Entry(f1)
    e1.configure(width=4, justify='center', bd=4, relief='groove')
    e1.configure(font=ADJ_FONT, fg=SETUP_COLOR, bg='white')
    e1.configure(textvariable=new_ampm)
    l1.grid(row=0, column=0)
    e1.grid(row=1, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.inc_btn_icon, borderwidth=0)
    b1.configure(repeatdelay=500, repeatinterval=100)
    b1.configure(command=inc_ampm)
    b2 = tk.Button(f2)
    b2.configure(image=screens.dec_btn_icon, borderwidth=0)
    b2.configure(repeatdelay=500, repeatinterval=100)
    b2.configure(command=dec_ampm)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_month_adjuster(window):
    global new_month
    new_month = tk.StringVar()

    this_frame = tk.Frame(window)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=0, column=1, sticky='s')

    l1 = tk.Label(f1)
    l1.configure(fg=SETUP_COLOR, text="Month")
    e1 = tk.Entry(f1)
    e1.configure(width=4, justify='center', bd=4, relief='groove')
    e1.configure(font=ADJ_FONT, fg=SETUP_COLOR, bg='white')
    e1.configure(textvariable=new_month)
    l1.grid(row=0, column=0)
    e1.grid(row=1, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.inc_btn_icon, borderwidth=0)
    b1.configure(repeatdelay=500, repeatinterval=100)
    b1.configure(command=inc_months)
    b2 = tk.Button(f2)
    b2.configure(image=screens.dec_btn_icon, borderwidth=0)
    b2.configure(repeatdelay=500, repeatinterval=100)
    b2.configure(command=dec_months)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_day_adjuster(window):
    global new_day
    new_day = tk.StringVar()

    this_frame = tk.Frame(window)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=0, column=1, sticky='s')

    l1 = tk.Label(f1)
    l1.configure(fg=SETUP_COLOR, text="Day")
    e1 = tk.Entry(f1)
    e1.configure(width=4, justify='center', bd=4, relief='groove')
    e1.configure(font=ADJ_FONT, fg=SETUP_COLOR, bg='white')
    e1.configure(textvariable=new_day)
    l1.grid(row=0, column=0)
    e1.grid(row=1, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.inc_btn_icon, borderwidth=0)
    b1.configure(repeatdelay=500, repeatinterval=100)
    b1.configure(command=inc_days)
    b2 = tk.Button(f2)
    b2.configure(image=screens.dec_btn_icon, borderwidth=0)
    b2.configure(repeatdelay=500, repeatinterval=100)
    b2.configure(command=dec_days)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    return this_frame


###############################################################################
###############################################################################
def create_year_adjuster(window):
    global new_year
    new_year = tk.StringVar()

    this_frame = tk.Frame(window)
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0)
    f2.grid(row=0, column=1, sticky='s')

    l1 = tk.Label(f1)
    l1.configure(fg=SETUP_COLOR, text="Year")
    e1 = tk.Entry(f1)
    e1.configure(width=4, justify='center', bd=4, relief='groove')
    e1.configure(font=ADJ_FONT, fg=SETUP_COLOR, bg='white')
    e1.configure(textvariable=new_year)
    l1.grid(row=0, column=0)
    e1.grid(row=1, column=0)

    b1 = tk.Button(f2)
    b1.configure(image=screens.inc_btn_icon, borderwidth=0)
    b1.configure(repeatdelay=500, repeatinterval=100)
    b1.configure(command=inc_years)
    b2 = tk.Button(f2)
    b2.configure(image=screens.dec_btn_icon, borderwidth=0)
    b2.configure(repeatdelay=500, repeatinterval=100)
    b2.configure(command=dec_years)
    b1.grid(row=0, column=0)
    b2.grid(row=1, column=0)

    return this_frame


