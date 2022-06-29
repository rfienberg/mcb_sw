from globals import *
import tkinter as tk
import screens
import dcb



###############################################################################
###############################################################################
def show_control_screen():
    global this_screen, unlock_msg

    # Display the "Unlocking" message screen
    unlock_msg.tkraise()
    this_screen.tkraise()

    # Stop fluid flow (i.e. close all valves) to unlock cartridge
    dcb.sendValveFlowCommand("Stop")

    # Now display the "Ready" message screen
    this_screen.after(1000, on_remove_ready)


###############################################################################
###############################################################################
def on_remove_ready():
    global ready_msg

    # Display the "Ready" message screen
    ready_msg.tkraise()


###############################################################################
###############################################################################
def on_ok_press():
    screens.play_key_tone()
    screens.show_control_main_screen()

    # Allow fluid flow again
    dcb.sendValveFlowCommand("Auto")


###############################################################################
###############################################################################
def create_control_screen(frame):
    global this_screen, unlock_msg, ready_msg

    # Create and place the Screen
    this_screen = tk.Frame(frame)
    this_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top = create_top_line(this_screen)
    unlock_msg = create_unlocking_widget(this_screen)
    ready_msg = create_safe_widget(this_screen)

    # Place the Widgets
    top.grid(row=0, column=0, sticky='nw')
    unlock_msg.grid(row=1, column=0, padx=40, pady=20, sticky='nsew')
    ready_msg.grid( row=1, column=0, padx=40, pady=20, sticky='nsew')

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
def create_unlocking_widget(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=MD_FONT, fg=CONTROL_COLOR)
    l1.configure(text="Unlocking Cartridge! Please wait...")
    l1.grid(row=0, column=0, columnspan=10, padx=20, pady=40)

    return this_frame


###############################################################################
###############################################################################
def create_safe_widget(frame):
    this_frame = tk.Frame(frame)

    l1 = tk.Label(this_frame)
    l1.configure(font=MD_FONT, fg=CONTROL_COLOR)
    l1.configure(text="It is now safe to remove the Cartridge")
    l1.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    l2 = tk.Label(this_frame)
    l2.configure(font=MD_FONT, fg=CONTROL_COLOR)
    l2.configure(text="Press OK when done...")
    l2.grid(row=1, column=0, padx=20, sticky='ew')

    b1 = tk.Button(this_frame, image=screens.grn_ok_btn_icon, borderwidth=0)
    b1.configure(command=on_ok_press)
    b1.grid(row=2, column=0, pady=30)

    return this_frame


