from globals import *
import tkinter as tk
import screens
import analyze
import status
import telemetry
import patient

ShutDownRequested = False


###############################################################################
###############################################################################
def requestShutdown():
    # Indicate that a Shut-Down is in progress
    global ShutDownRequested
    ShutDownRequested = True

    # Write this event into the log file
    dts = getDateTimeStamp()
    shutdown_line = dts + "Shutting-down!\n"
    patient.write_log_line(shutdown_line)

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
def create_control_shutdown_screen(frame):
    global verify_screen, ver_msg, off_msg

    # Create and place the Screen
    verify_screen = tk.Frame(frame)
    verify_screen.grid(row=0, column=0, sticky='nsew')

    # Create the Widgets
    ver_msg = create_verify_widget(verify_screen)

    # Place the Widgets
    ver_msg.grid(row=0, column=0, sticky='nsew')

    return verify_screen


###############################################################################
###############################################################################
def show_control_shutdown_screen():
    global verify_screen
    verify_screen.tkraise()


###############################################################################
###############################################################################
def on_yes_press():
    # Chirp
    screens.play_key_tone()

    # Bring-up the "Shutting down!" screen
    requestShutdown()


###############################################################################
###############################################################################
def on_no_press():
    # Chirp
    screens.play_key_tone()

    # Go back to display the parent screen
    screens.show_control_main_screen()


###############################################################################
###############################################################################
def create_verify_widget(frame):
    this_frame = tk.Frame(frame)

    f1 = tk.Frame(this_frame)
    f2 = tk.Frame(this_frame)
    f3 = tk.Frame(this_frame)

    title_label = tk.Label(f1)
    title_label.configure(font=("Georgia", 30), fg=CONTROL_COLOR)
    title_label.configure(text="Shut-Down:")
    title_label.grid(row=0, column=0, padx=10)

    mark_label = tk.Label(f2)
    mark_label.configure(image=screens.question_icon)
    text_label = tk.Label(f2)
    text_label.configure(font=GI_FONT, fg=CONTROL_COLOR)
    text_label.configure(text="Are you sure that you \n want to shut-down?")
    mark_label.grid(row=0, column=0, padx=10)
    text_label.grid(row=0, column=1, padx=10)

    yes_button = tk.Button(f3)
    yes_button.configure(image=screens.yes_btn_icon, borderwidth=0)
    yes_button.configure(command=on_yes_press)
    no_button = tk.Button(f3)
    no_button.configure(image=screens.no_btn_icon, borderwidth=0)
    no_button.configure(command=on_no_press)
    yes_button.grid(row=0, column=0, padx=60)
    no_button.grid(row=0, column=1, padx=60)

    f1.grid(row=0, column=0, padx=10, sticky='w')
    f2.grid(row=1, column=0, padx=30, pady=40, sticky='w')
    f3.grid(row=2, column=0, padx=30, pady=40, sticky='w')

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
def show_shutting_down_screen():
    global shutting_down_screen
    shutting_down_screen.tkraise()


###############################################################################
###############################################################################
def create_shutting_down_widget(frame):
    this_frame = tk.Frame(frame)

    sleep_label = tk.Label(this_frame)
    sleep_label.configure(image=screens.shutdown_icon)

    text_label = tk.Label(this_frame)
    text_label.configure(font=GI_FONT, fg='red')
    text_label.configure(text="Shutting down! \n Please wait...")

    sleep_label.grid(row=0, column=0, padx=20, pady=40)
    text_label.grid(row=0, column=1, padx=20, pady=40)

    return this_frame


