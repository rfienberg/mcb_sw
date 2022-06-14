from globals import *
import tkinter as tk

import homescreen

import setupscreen
import analyzescreen
import statusscreen
import controlscreen

import patient
import clock
import alarms
import audio
import timeouts
import mcb_logging
import calibrate

import flowrate
import color
import turbidity

import cartridge
import lights

import shutdown



###############################################################################
###############################################################################
def create_screens(window):
    this_frame = tk.Frame(window)
    this_frame.grid(row=1, column=0, sticky='nsew')
    this_frame.grid(padx=10, pady=10)

    # Create the individual Screens
    s1  = homescreen.create_screen(this_frame)

    s2  = setupscreen.create_screen(this_frame)
    s3  = analyzescreen.create_screen(this_frame)
    s4  = statusscreen.create_screen(this_frame)
    s5  = controlscreen.create_screen(this_frame)

    s6  = patient.create_screen(this_frame)
    s7  = clock.create_screen(this_frame)
    s8  = alarms.create_screen(this_frame)
    s9  = audio.create_screen(this_frame)
    s10 = timeouts.create_screen(this_frame)
    s11 = mcb_logging.create_screen(this_frame)
    s12 = calibrate.create_screen(this_frame)

    s13 = flowrate.create_screen(this_frame)
    s14 = color.create_screen(this_frame)
    s15 = turbidity.create_screen(this_frame)

    s16 = lights.create_screen(this_frame)
    s17 = cartridge.create_screen(this_frame)

    s18 = shutdown.create_verify_shutdown_screen(this_frame)
    s19 = shutdown.create_shutting_down_screen(this_frame)

    """
    s20 = tankfullscreen.create(this_frame)
    """

    # Initialize to raise the 1st Screen
    show_home_screen()

    return this_frame


###############################################################################
###############################################################################
def update_screens():
    statusscreen.update_screen()


###############################################################################
###############################################################################
def show_home_screen():
    homescreen.show_screen()


###############################################################################
###############################################################################
def show_setup_screen():
    setupscreen.show_screen()


###############################################################################
###############################################################################
def show_analyze_screen():
    analyzescreen.show_screen()


###############################################################################
###############################################################################
def show_status_screen():
    statusscreen.show_screen()


###############################################################################
###############################################################################
def show_control_screen():
    controlscreen.show_screen()


###############################################################################
###############################################################################
def show_set_patient_screen():
    patient.show_screen()


###############################################################################
###############################################################################
def show_set_clock_screen():
    clock.show_screen()


###############################################################################
###############################################################################
def show_set_alarms_screen():
    alarms.show_screen()


###############################################################################
###############################################################################
def show_set_audio_screen():
    audio.show_screen()


###############################################################################
###############################################################################
def show_set_timeouts_screen():
    timeouts.show_screen()


###############################################################################
###############################################################################
def show_set_logging_screen():
    mcb_logging.show_screen()


###############################################################################
###############################################################################
def show_calibrate_screen():
    calibrate.show_screen()


###############################################################################
###############################################################################
def show_flowrate_history_screen():
    flowrate.show_screen()


###############################################################################
###############################################################################
def show_color_details_screen():
    color.show_screen()


###############################################################################
###############################################################################
def show_turbidity_details_screen():
    turbidity.show_screen()


###############################################################################
###############################################################################
def show_control_cartridge_screen():
    cartridge.show_screen()


###############################################################################
###############################################################################
def show_control_lights_screen():
    lights.show_screen()


###############################################################################
###############################################################################
def show_verify_shutdown_screen():
    shutdown.show_verify_shutdown_screen()


###############################################################################
###############################################################################
def show_shutting_down_screen():
    shutdown.show_shutting_down_screen()


###############################################################################
###############################################################################
def play_key_tone():
    audio.play_key_tone()


