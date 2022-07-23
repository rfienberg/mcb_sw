from globals import *
import tkinter as tk
import screens
import dcb



###############################################################################
###############################################################################
def show_control_screen():
    global this_screen, message1

    # Display the "Unlocking" message screen
    message1.tkraise()
    this_screen.tkraise()

    # Stop fluid flow (i.e. close all valves) to unlock cartridge
    dcb.sendValveFlowCommand("Stop")

    # Now display the "Ready" message screen
    this_screen.after(1000, upon_remove_ready)


###############################################################################
###############################################################################
def upon_remove_ready():
    # Display the "Ready" message screen
    global message2
    message2.tkraise()


###############################################################################
###############################################################################
def upon_ok_press():
    # Chirp
    screens.play_key_tone()

    # Allow fluid to flow again
    dcb.sendValveFlowCommand("Auto")

    # Go back to the CONTROL main screen
    screens.show_control_main_screen()


###############################################################################
###############################################################################
def create_control_screen(frame):
    global this_screen, message1, message2

    # Create and place the Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top_line = create_top_line(this_screen)
    message1 = create_unlocking_message(this_screen)
    message2 = create_completed_widget(this_screen)

    # Place the Widgets
    top_line.grid(row=0, column=0, sticky='nw')
    message1.grid(row=1, column=0, padx=40, pady=20, sticky='nsew')
    message2.grid(row=1, column=0, padx=40, pady=20, sticky='nsew')

    return this_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=LG_FONT, fg=CONTROL_COLOR)
    l1.configure(text="Remove Cartridge:")
    l1.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_unlocking_message(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=MD_FONT, fg=CONTROL_COLOR)
    l1.configure(text="Unlocking Cartridge! Please wait...")
    l1.grid(row=0, column=0, columnspan=10, padx=20, pady=40)

    return this_frame


###############################################################################
###############################################################################
def create_completed_widget(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=MD_FONT, fg=CONTROL_COLOR)
    l1.configure(text="It is now safe to remove the Cartridge")

    l2 = tk.Label(this_frame)
    l2.configure(font=MD_FONT, fg=CONTROL_COLOR)
    l2.configure(text="Press OK when done...")

    b1 = tk.Button(this_frame, image=screens.grn_ok_btn_icon, borderwidth=0)
    b1.configure(command=upon_ok_press)

    l1.grid(row=0, column=0, padx=20, pady=20, sticky='ew')
    l2.grid(row=1, column=0, padx=20, sticky='ew')
    b1.grid(row=2, column=0, pady=30)

    return this_frame


