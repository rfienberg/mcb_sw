from globals import *
import tkinter as tk
import screens
import analyze
import status
import telemetry
import patientinfo

ShutDownRequested = False


###############################################################################
###############################################################################
def requestShutdown():
    # Indicate that a Shut-Down is in progress
    global ShutDownRequested
    ShutDownRequested = True

    # Write this event into the log file
    dts = getDateTimeStamp()
    shutdown_line = dts + "Shutting-down!"
    print(shutdown_line)
    patientinfo.write_log_line(shutdown_line)

    # Bring up the "Shutting Down" screen
    screens.show_shutting_down_screen()

    global shutting_down_screen
    shutting_down_screen.after(2000, perform_shut_down)


###############################################################################
###############################################################################
def isShutDownRequested():
    global ShutDownRequested
    return ShutDownRequested


###############################################################################
###############################################################################
def perform_shut_down():
    pass


###############################################################################
###############################################################################
def show_control_shutdown_screen():
    global verify_screen
    verify_screen.tkraise()


###############################################################################
###############################################################################
def show_shutting_down_screen():
    global shutting_down_screen
    shutting_down_screen.tkraise()


###############################################################################
###############################################################################
def upon_yes_press():
    # Chirp
    screens.play_key_tone()

    # Bring-up the "Shutting down!" screen
    requestShutdown()


###############################################################################
###############################################################################
def upon_no_press():
    # Chirp
    screens.play_key_tone()

    # Go back to display the parent screen
    screens.show_control_main_screen()


###############################################################################
###############################################################################
def create_control_shutdown_screen(frame):
    global verify_screen, ver_msg, off_msg

    # Create and place the Screen
    verify_screen = tk.Frame(frame)
    verify_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    top_line = create_top_line(verify_screen)
    msg_line = create_verify_message(verify_screen)

    # Place the Widgets
    top_line.grid(row=0, column=0, pady=10, sticky='w')
    msg_line.grid(row=1, column=0, pady=10)

    return verify_screen


###############################################################################
###############################################################################
def create_top_line(frame):
    this_frame = tk.Frame(frame)

    # Create the widgets
    l1 = tk.Label(this_frame, text="Shut-Down:")
    l1.configure(font=LG_FONT, fg=CONTROL_COLOR)
    l1.grid(row=0, column=0, padx=10)

    return this_frame


###############################################################################
###############################################################################
def create_verify_message(frame):
    this_frame = tk.Frame(frame)

    # Define the main left and right frames
    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f1.grid(row=0, column=0, padx=20)
    f2.grid(row=0, column=1, padx=20)

    # Define the right frame's top and bottom frames
    f3 = tk.Frame(f2)
    f4 = tk.Frame(f2)
    f3.grid(row=0, column=0, pady=20)
    f4.grid(row=1, column=0, pady=20)

    # Place an ICON into the left frame
    i1 = tk.Label(f1)
    i1.configure(image=screens.question_icon)
    i1.grid(row=0, column=0, padx=10)

    # Place a MESSAGE in the top frame
    m1 = tk.Label(f3)
    m1.configure(font=LG_FONT, fg=CONTROL_COLOR)
    m1.configure(text="Are you sure that you \n want to shut-down?")
    m1.grid(row=0, column=0)

    # Place two BUTTONS in the bottom frame
    b1 = tk.Button(f4)
    b1.configure(image=screens.yes_btn_icon, borderwidth=0)
    b1.configure(command=upon_yes_press)
    b2 = tk.Button(f4)
    b2.configure(image=screens.no_btn_icon, borderwidth=0)
    b2.configure(command=upon_no_press)
    b1.grid(row=0, column=0, padx=20)
    b2.grid(row=0, column=1, padx=20)

    return this_frame


###############################################################################
###############################################################################
def create_shutting_down_screen(frame):
    global shutting_down_screen

    # Create and place the Screen
    shutting_down_screen = tk.Frame(frame)
    shutting_down_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    sd = create_shutting_down_widget(shutting_down_screen)

    # Place the Widgets
    sd.grid(row=0, column=0, padx=20, pady=60, sticky='nsew')

    return shutting_down_screen


###############################################################################
###############################################################################
def create_shutting_down_widget(frame):
    this_frame = tk.Frame(frame)

    i1 = tk.Label(this_frame)
    i1.configure(image=screens.shutdown_icon)

    l1 = tk.Label(this_frame)
    l1.configure(font=GI_FONT, fg='red')
    l1.configure(text="Shutting down! \n Please wait...")

    i1.grid(row=0, column=0, padx=20, pady=40)
    l1.grid(row=0, column=1, padx=20, pady=40)

    return this_frame


