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

import flowrates
import color
import turbidity

import cartridge
import lights
import power

import shutdown



###############################################################################
###############################################################################
def show_home_screen():
    homescreen.show()


###############################################################################
###############################################################################
def show_setup_screen():
    setupscreen.show()


###############################################################################
###############################################################################
def show_analyze_screen():
    analyzescreen.show()


###############################################################################
###############################################################################
def show_status_screen():
    statusscreen.show()


###############################################################################
###############################################################################
def show_control_screen():
    controlscreen.show()


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
def show_analyze_flowrates_screen():
    flowrates.show_screen()


###############################################################################
###############################################################################
def show_analyze_color_screen():
    color.show_screen()


###############################################################################
###############################################################################
def show_analyze_turbidity_screen():
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
def show_control_power_screen():
    power.show_screen()


###############################################################################
###############################################################################
def show_shut_down_screen():
    shutdown.show_screen()


###############################################################################
###############################################################################
def play_key_tone():
    audio.play_key_tone()


###############################################################################
###############################################################################
def create(window):
    this_frame = tk.Frame(window)
    this_frame.grid(row=1, column=0, sticky='nsew')
    this_frame.grid(padx=10, pady=10)

    # Create the individual Screens
    s1  = homescreen.create(this_frame)

    s2  = setupscreen.create(this_frame)
    s3  = analyzescreen.create(this_frame)
    s4  = statusscreen.create(this_frame)
    s5  = controlscreen.create(this_frame)

    s6  = patient.create_screen(this_frame)
    s7  = clock.create_screen(this_frame)
    s8  = alarms.create_screen(this_frame)
    s9  = audio.create_screen(this_frame)
    s10 = timeouts.create_screen(this_frame)
    s11 = mcb_logging.create_screen(this_frame)
    s12 = calibrate.create_screen(this_frame)

    s13 = flowrates.create_screen(this_frame)
    s14 = color.create_screen(this_frame)
    s15 = turbidity.create_screen(this_frame)

    s16 = lights.create_screen(this_frame)
    s17 = cartridge.create_screen(this_frame)
    s18 = power.create_screen(this_frame)

    s19 = shutdown.create_screen(this_frame)

    """
    s20 = tankfullscreen.create(this_frame)
    """

    # Initialize to raise the 1st Screen
    show_home_screen()

    return this_frame

