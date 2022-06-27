from globals import *
import tkinter as tk
from PIL import ImageTk, Image

import homescreen

import setupscreen
import analyzescreen
import statusscreen
import controlscreen

import patient
import clock
import alerts
import audio
import timeouts
import mcb_logging
import calibrate

import flow
import color
import turbidity

import cartridge
import lights

import shutdown



###############################################################################
###############################################################################
def update_screens():
    statusscreen.update_screen()


###############################################################################
###############################################################################
def show_home_screen():
    homescreen.show_menu_screen()


###############################################################################
###############################################################################
def show_setup_main_screen():
    setupscreen.show_main_screen()


###############################################################################
###############################################################################
def show_analyze_main_screen():
    analyzescreen.show_main_screen()


###############################################################################
###############################################################################
def show_status_main_screen():
    statusscreen.show_main_screen()


###############################################################################
###############################################################################
def show_control_main_screen():
    controlscreen.show_main_screen()


###############################################################################
###############################################################################
def show_set_patient_screen():
    patient.show_setup_screen()


###############################################################################
###############################################################################
def show_set_clock_screen():
    clock.show_setup_screen()


###############################################################################
###############################################################################
def show_set_alerts_screen():
    alerts.show_setup_screen()


###############################################################################
###############################################################################
def show_set_audio_screen():
    audio.show_setup_screen()


###############################################################################
###############################################################################
def show_set_timeouts_screen():
    timeouts.show_setup_screen()


###############################################################################
###############################################################################
def show_set_logging_screen():
    mcb_logging.show_setup_screen()


###############################################################################
###############################################################################
def show_set_lights_screen():
    lights.show_setup_screen()


###############################################################################
###############################################################################
def show_calibrate_setup_screen():
    calibrate.show_setup_screen()


###############################################################################
###############################################################################
def show_flowrate_history_screen():
    flow.show_history_screen()


###############################################################################
###############################################################################
def show_color_details_screen():
    color.show_details_screen()


###############################################################################
###############################################################################
def show_turbidity_details_screen():
    turbidity.show_details_screen()


###############################################################################
###############################################################################
def show_control_cartridge_screen():
    cartridge.show_control_screen()


###############################################################################
###############################################################################
def show_control_lights_screen():
    lights.show_control_screen()


###############################################################################
###############################################################################
def show_verify_shutdown_screen():
    shutdown.show_control_shutdown_screen()


###############################################################################
###############################################################################
def show_shutting_down_screen():
    shutdown.show_shutting_down_screen()


###############################################################################
###############################################################################
def play_key_tone():
    audio.play_key_tone()


###############################################################################
###############################################################################
def create_screens(window):
    global this_frame

    create_graphics()

    this_frame = tk.Frame(window)
    this_frame.grid(row=1, column=0, sticky='nsew')
    this_frame.grid(padx=10, pady=10)

    # Create the individual Screens
    s1  = homescreen.create_menu_screen(this_frame)

    s2  = setupscreen.create_main_screen(this_frame)
    s3  = analyzescreen.create_main_screen(this_frame)
    s4  = statusscreen.create_main_screen(this_frame)
    s5  = controlscreen.create_main_screen(this_frame)

    s6  = patient.create_setup_screen(this_frame)
    s7  = audio.create_setup_screen(this_frame)
    s8  = alerts.create_setup_screen(this_frame)
    s9  = calibrate.create_setup_screen(this_frame)
    s10 = clock.create_setup_screen(this_frame)
    s11 = timeouts.create_setup_screen(this_frame)
    s12 = mcb_logging.create_setup_screen(this_frame)
    s13 = lights.create_setup_screen(this_frame)

    s14 = lights.create_control_screen(this_frame)
    s15 = cartridge.create_control_screen(this_frame)
    s16 = shutdown.create_control_shutdown_screen(this_frame)

    s17 = flow.create_history_screen(this_frame)
    s18 = color.create_details_screen(this_frame)
    s19 = turbidity.create_details_screen(this_frame)

    s20 = shutdown.create_shutting_down_screen(this_frame)

    """
    s20 = tankfullscreen.create(this_frame)
    """

    # Initialize to raise the 1st Screen
    show_home_screen()

    return this_frame


###############################################################################
###############################################################################
def create_graphics():
    # Open up the image files and size them correctly
    global analyze_btn_icon
    this_graphic = Image.open("Graphics/brn_analyze.png").resize((145,250), Image.ANTIALIAS)
    analyze_btn_icon = ImageTk.PhotoImage(this_graphic)
    global control_btn_icon
    this_graphic = Image.open("Graphics/grn_control.png").resize((140,250), Image.ANTIALIAS)
    control_btn_icon = ImageTk.PhotoImage(this_graphic)
    global setup_btn_icon
    this_graphic = Image.open("Graphics/blue_setup.png").resize((140,250), Image.ANTIALIAS)
    setup_btn_icon = ImageTk.PhotoImage(this_graphic)
    global status_btn_icon
    this_graphic = Image.open("Graphics/purp_status.png").resize((140,250), Image.ANTIALIAS)
    status_btn_icon = ImageTk.PhotoImage(this_graphic)

    # Open up the image files and size them correctly
    global brn_gohome_btn_icon
    this_graphic = Image.open("Graphics/brn_go_home.png").resize((100,50), Image.ANTIALIAS)
    brn_gohome_btn_icon = ImageTk.PhotoImage(this_graphic)
    global grn_gohome_btn_icon
    this_graphic = Image.open("Graphics/grn_go_home.png").resize((100,50), Image.ANTIALIAS)
    grn_gohome_btn_icon = ImageTk.PhotoImage(this_graphic)
    global pur_gohome_btn_icon
    this_graphic = Image.open("Graphics/purp_go_home.png").resize((100,50), Image.ANTIALIAS)
    pur_gohome_btn_icon = ImageTk.PhotoImage(this_graphic)
    global blu_gohome_btn_icon
    this_graphic = Image.open("Graphics/blue_go_home.png").resize((100,50), Image.ANTIALIAS)
    blu_gohome_btn_icon = ImageTk.PhotoImage(this_graphic)

    # Open up the images for this screen and keep them global
    global history_btn_icon
    this_graphic = Image.open("Graphics/brn_btn_history.png").resize((150,50), Image.ANTIALIAS)
    history_btn_icon = ImageTk.PhotoImage(this_graphic)
    global details_btn_icon
    this_graphic = Image.open("Graphics/brn_btn_details.png").resize((150,50), Image.ANTIALIAS)
    details_btn_icon = ImageTk.PhotoImage(this_graphic)

    # Open up the images for this screen and keep them global
    global yes_btn_icon
    this_graphic = Image.open("Graphics/grn_btn_yes.png").resize((150,50), Image.ANTIALIAS)
    yes_btn_icon = ImageTk.PhotoImage(this_graphic)
    global no_btn_icon
    this_graphic = Image.open("Graphics/grn_btn_no.png").resize((150,50), Image.ANTIALIAS)
    no_btn_icon = ImageTk.PhotoImage(this_graphic)
    global grn_ok_btn_icon
    this_graphic = Image.open("Graphics/grn_btn_ok.png").resize((150,50), Image.ANTIALIAS)
    grn_ok_btn_icon = ImageTk.PhotoImage(this_graphic)
    global grn_cartridge_icon
    this_graphic = Image.open("Graphics/grn_cartridge.png").resize((100,100), Image.ANTIALIAS)
    grn_cartridge_icon = ImageTk.PhotoImage(this_graphic)
    global grn_bulb_icon
    this_graphic = Image.open("Graphics/grn_bulb.png").resize((100,100), Image.ANTIALIAS)
    grn_bulb_icon = ImageTk.PhotoImage(this_graphic)
    global grn_power_btn_icon
    this_graphic = Image.open("Graphics/grn_power_btn.png").resize((100,100), Image.ANTIALIAS)
    grn_power_btn_icon = ImageTk.PhotoImage(this_graphic)
    global question_icon
    this_graphic = Image.open("Graphics/grn_question.png").resize((120,120), Image.ANTIALIAS)
    question_icon = ImageTk.PhotoImage(this_graphic)
    global shutdown_icon
    this_graphic = Image.open("Graphics/sleep.png").resize((150,150), Image.ANTIALIAS)
    shutdown_icon = ImageTk.PhotoImage(this_graphic)

    # Open up the images for this screen and keep them global
    global patient_btn_icon
    this_graphic = Image.open("Graphics/blue_patient.png").resize((100,100), Image.ANTIALIAS)
    patient_btn_icon = ImageTk.PhotoImage(this_graphic)
    global datetime_btn_icon
    this_graphic = Image.open("Graphics/blue_datetime.png").resize((100,100), Image.ANTIALIAS)
    datetime_btn_icon = ImageTk.PhotoImage(this_graphic)
    global alerts_btn_icon
    this_graphic = Image.open("Graphics/blue_bell.png").resize((100,100), Image.ANTIALIAS)
    alerts_btn_icon = ImageTk.PhotoImage(this_graphic)
    global audio_btn_icon
    this_graphic = Image.open("Graphics/blue_speaker.png").resize((100,100), Image.ANTIALIAS)
    audio_btn_icon = ImageTk.PhotoImage(this_graphic)
    global calibrate_btn_icon
    this_graphic = Image.open("Graphics/blue_wrench.png").resize((100,100), Image.ANTIALIAS)
    calibrate_btn_icon = ImageTk.PhotoImage(this_graphic)
    global blu_lights_btn_icon
    this_graphic = Image.open("Graphics/blue_bulb.png").resize((100,100), Image.ANTIALIAS)
    blu_lights_btn_icon = ImageTk.PhotoImage(this_graphic)
    global cal_inprogress_icon
    this_graphic = Image.open("Graphics/blue_in_progress.png").resize((150,150), Image.ANTIALIAS)
    cal_inprogress_icon = ImageTk.PhotoImage(this_graphic)
    global cal_complete_icon
    this_graphic = Image.open("Graphics/blue_thumbs_up.png").resize((130,130), Image.ANTIALIAS)
    cal_complete_icon = ImageTk.PhotoImage(this_graphic)

    """
    global timeouts_btn_icon
    image = Image.open("Graphics/set_timeouts_btn_img.png").resize((100,100), Image.ANTIALIAS)
    timeouts_btn_icon = ImageTk.PhotoImage(image)
    global logging_btn_icon
    image = Image.open("Graphics/logging_btn_img.png").resize((100,100), Image.ANTIALIAS)
    logging_btn_icon = ImageTk.PhotoImage(image)
    """

    # Open up the images for this screen and keep them global
    global no_flow_icon
    this_graphic = Image.open("Graphics/purp_flow_no.png").resize((40,40), Image.ANTIALIAS)
    no_flow_icon = ImageTk.PhotoImage(this_graphic)
    global yes_flow_icon
    this_graphic = Image.open("Graphics/purp_flow_yes.png").resize((40,40), Image.ANTIALIAS)
    yes_flow_icon = ImageTk.PhotoImage(this_graphic)

    """
    global light_bulb_icon
    light_bulb_img = Image.open("Graphics/status_lightbulb_icon.png").resize((50,50), Image.ANTIALIAS)
    light_bulb_icon = ImageTk.PhotoImage(light_bulb_img)
    """

    # Open up the images for this screen and keep them global
    global back_btn_icon
    this_graphic = Image.open("Graphics/brn_btn_back.png").resize((150,50), Image.ANTIALIAS)
    back_btn_icon = ImageTk.PhotoImage(this_graphic)
    global past_arrow_icon
    this_graphic = Image.open("Graphics/brn_to_past.png").resize((150,40), Image.ANTIALIAS)
    past_arrow_icon = ImageTk.PhotoImage(this_graphic)
    global analyze_color_img # Keeps it persistent in memory
    this_graphic = Image.open(SNAP_COLOR_IMG).resize((200,200), Image.ANTIALIAS)
    analyze_color_img = ImageTk.PhotoImage(this_graphic)
    global match_color_img # Keeps it persistent in memory
    this_graphic = Image.open("Graphics/color_chart.png").resize((150,260), Image.ANTIALIAS)
    match_color_img = ImageTk.PhotoImage(this_graphic)
    global match_turbidity_img # Keeps it persistent in memory
    this_graphic = Image.open("Graphics/turbidity_chart.png").resize((110,280), Image.ANTIALIAS)
    match_turbidity_img = ImageTk.PhotoImage(this_graphic)
    """
    global turb_clear_icon
    this_graphic = Image.open("Graphics/turb_clear.png").resize((200,70), Image.ANTIALIAS)
    turb_clear_icon = ImageTk.PhotoImage(this_graphic)
    """

    # Open up the images for this screen and keep them global
    global start_btn_icon
    this_graphic = Image.open("Graphics/blue_btn_start.png").resize((150,50), Image.ANTIALIAS)
    start_btn_icon = ImageTk.PhotoImage(this_graphic)
    global blu_ok_btn_icon
    this_graphic = Image.open("Graphics/blue_btn_ok.png").resize((150,50), Image.ANTIALIAS)
    blu_ok_btn_icon = ImageTk.PhotoImage(this_graphic)
    global blu_cancel_btn_icon
    this_graphic = Image.open("Graphics/blue_btn_cancel.png").resize((150,50), Image.ANTIALIAS)
    blu_cancel_btn_icon = ImageTk.PhotoImage(this_graphic)
    global checkbox_yes_icon
    this_graphic = Image.open("Graphics/blue_box_checked.png").resize((25,25), Image.ANTIALIAS)
    checkbox_yes_icon = ImageTk.PhotoImage(this_graphic)
    global checkbox_no_icon
    this_graphic = Image.open("Graphics/blue_box_uncheck.png").resize((25,25), Image.ANTIALIAS)
    checkbox_no_icon = ImageTk.PhotoImage(this_graphic)
    global inc_btn_icon
    this_graphic = Image.open("Graphics/blue_arrow.png").resize((45,23), Image.ANTIALIAS)
    inc_btn_icon = ImageTk.PhotoImage(this_graphic)
    global dec_btn_icon
    this_graphic = this_graphic.rotate(180)
    dec_btn_icon = ImageTk.PhotoImage(this_graphic)


###############################################################################
###############################################################################
def popup_tank_warning():
    global tank_level_warning

    tank_level_warning = tk.Toplevel(this_frame)
    tank_level_warning.title("Warning!")
    tank_level_warning.minsize(800, 350)

    f1 = tk.LabelFrame(tank_level_warning)
    f1.grid(row=0, column=0, sticky='nsew')

    b1 = tk.Button(f1)
    b1.configure(text="OK")
    b1.configure(command=popdown_tank_warning)
    b1.grid(row=0, column=0, sticky='nsew')

    tank_level_warning.mainloop()


###############################################################################
###############################################################################
def popdown_tank_warning():
    global tank_level_warning
    tank_level_warning.destroy()


