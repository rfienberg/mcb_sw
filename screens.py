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

import flow
import color
import turbidity

import cartridge
import lights

import shutdown



###############################################################################
###############################################################################
def create_screens(window):
    global this_frame

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
    s8  = alarms.create_setup_screen(this_frame)
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
def show_set_alarms_screen():
    alarms.show_setup_screen()


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


