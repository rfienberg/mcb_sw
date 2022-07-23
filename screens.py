from globals import *
import tkinter as tk
from PIL import ImageTk, Image
import time

import tones

import mcb_config

import homescreen

import analyzescreen
import controlscreen
import setupscreen
import infoscreen

import newpatient
import clock
import alerts
import audio
import lights
import calibrate

import flow
import color
import turbidity

import cartridge
import lightup

import tankinfo
import patientinfo
import engineering

import shutdown



###############################################################################
###############################################################################
def play_key_tone():
    if (mcb_config.getPlayKeyPressTone()):
        tones.generate_tone(2500, 25)
        time.sleep(.100)
        tones.generate_tone(0)


###############################################################################
###############################################################################
def update_screens():
    infoscreen.update_screen()


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
def show_info_main_screen():
    infoscreen.show_main_screen()


###############################################################################
###############################################################################
def show_control_main_screen():
    controlscreen.show_main_screen()


###############################################################################
###############################################################################
def show_set_patient_screen():
    newpatient.show_setup_screen()


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
    lightup.show_control_screen()


###############################################################################
###############################################################################
def show_verify_shutdown_screen():
    shutdown.show_control_shutdown_screen()


###############################################################################
###############################################################################
def show_tank_info_screen():
    tankinfo.show_info_screen()


###############################################################################
###############################################################################
def show_patient_info_screen():
    patientinfo.show_info_screen()


###############################################################################
###############################################################################
def show_engineering_screen():
    engineering.show_info_screen()


###############################################################################
###############################################################################
def show_shutting_down_screen():
    shutdown.show_shutting_down_screen()


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

    s2  = analyzescreen.create_main_screen(this_frame)
    s3  = controlscreen.create_main_screen(this_frame)
    s4  = setupscreen.create_main_screen(this_frame)
    s5  = infoscreen.create_main_screen(this_frame)

    s6 = flow.create_history_screen(this_frame)
    s7 = color.create_details_screen(this_frame)
    s8 = turbidity.create_details_screen(this_frame)

    s9  = lightup.create_control_screen(this_frame)
    s10 = cartridge.create_control_screen(this_frame)
    s11 = shutdown.create_control_shutdown_screen(this_frame)
    s12 = shutdown.create_shutting_down_screen(this_frame)

    s13 = tankinfo.create_info_screen(this_frame)
    s14 = patientinfo.create_info_screen(this_frame)
    s15 = engineering.create_info_screen(this_frame)

    s16 = newpatient.create_setup_screen(this_frame)
    s17 = audio.create_setup_screen(this_frame)
    s18 = alerts.create_setup_screen(this_frame)
    s19 = calibrate.create_setup_screen(this_frame)
    s20 = clock.create_setup_screen(this_frame)
    s21 = lights.create_setup_screen(this_frame)

    # Initialize to raise the HOME Screen
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
    global info_btn_icon
    this_graphic = Image.open("Graphics/purp_info.png").resize((140,250), Image.ANTIALIAS)
    info_btn_icon = ImageTk.PhotoImage(this_graphic)

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

    # Open up the images for this screen and keep them global
    global pur_ok_btn_icon
    this_graphic = Image.open("Graphics/purp_btn_ok.png").resize((150,50), Image.ANTIALIAS)
    pur_ok_btn_icon = ImageTk.PhotoImage(this_graphic)
    global tank_levels_icon
    this_graphic = Image.open("Graphics/purp_tanks.png").resize((100,100), Image.ANTIALIAS)
    tank_levels_icon = ImageTk.PhotoImage(this_graphic)
    global patient_info_icon
    this_graphic = Image.open("Graphics/purp_patient.png").resize((100,100), Image.ANTIALIAS)
    patient_info_icon = ImageTk.PhotoImage(this_graphic)
    global about_icon
    this_graphic = Image.open("Graphics/purp_about.png").resize((100,100), Image.ANTIALIAS)
    about_icon = ImageTk.PhotoImage(this_graphic)
    global no_flow_icon
    this_graphic = Image.open("Graphics/purp_flow_no.png").resize((40,40), Image.ANTIALIAS)
    no_flow_icon = ImageTk.PhotoImage(this_graphic)
    global yes_flow_icon
    this_graphic = Image.open("Graphics/purp_flow_yes.png").resize((40,40), Image.ANTIALIAS)
    yes_flow_icon = ImageTk.PhotoImage(this_graphic)


    # Open up the images for this screen and keep them global
    global back_btn_icon
    this_graphic = Image.open("Graphics/brn_btn_back.png").resize((150,50), Image.ANTIALIAS)
    back_btn_icon = ImageTk.PhotoImage(this_graphic)
    global past_arrow_icon
    this_graphic = Image.open("Graphics/brn_to_past.png").resize((150,40), Image.ANTIALIAS)
    past_arrow_icon = ImageTk.PhotoImage(this_graphic)
    global match_turbidity_icon # Keeps it persistent in memory
    this_graphic = Image.open("Graphics/turbidity_chart.png").resize((110,280), Image.ANTIALIAS)
    match_turbidity_icon = ImageTk.PhotoImage(this_graphic)

    global turb_analyzing_icon
    this_graphic = Image.open("Graphics/turbidity_analyzing.png").resize((175,55), Image.ANTIALIAS)
    turb_analyzing_icon = ImageTk.PhotoImage(this_graphic)
    global turb_clear_icon
    this_graphic = Image.open("Graphics/turbidity_clear.png").resize((175,55), Image.ANTIALIAS)
    turb_clear_icon = ImageTk.PhotoImage(this_graphic)
    global turb_partly_icon
    this_graphic = Image.open("Graphics/turbidity_partly.png").resize((175,55), Image.ANTIALIAS)
    turb_partly_icon = ImageTk.PhotoImage(this_graphic)
    global turb_cloudy_icon
    this_graphic = Image.open("Graphics/turbidity_cloudy.png").resize((175,55), Image.ANTIALIAS)
    turb_cloudy_icon = ImageTk.PhotoImage(this_graphic)


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


    # Open up the images for this screen and keep them global
    global warning_icon
    this_graphic = Image.open("Graphics/warning_icon.png").resize((90,110), Image.ANTIALIAS)
    warning_icon = ImageTk.PhotoImage(this_graphic)
    global alert_icon
    this_graphic = Image.open("Graphics/alert_icon.png").resize((90,110), Image.ANTIALIAS)
    alert_icon = ImageTk.PhotoImage(this_graphic)
    global urgent_icon
    this_graphic = Image.open("Graphics/urgent_icon.png").resize((90,110), Image.ANTIALIAS)
    urgent_icon = ImageTk.PhotoImage(this_graphic)
    global blk_dismiss_btn_icon
    this_graphic = Image.open("Graphics/black_btn_dismiss.png").resize((150,60), Image.ANTIALIAS)
    blk_dismiss_btn_icon = ImageTk.PhotoImage(this_graphic)


