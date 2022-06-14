from globals import *
from os.path import exists

###############################################################################
# Creates a new Patient Log File for the specified name
###############################################################################
def create(name):
    print("Created new log file: " + PATIENT_FILE + " for " + name)
    file = open(PATIENT_FILE, "w")
    file.write("Patient: " + name + "\n")
    file.close()


###############################################################################
###############################################################################
def get_patient_name():
    name = "UNKNOWN PATIENT"

    # Open (or create) the Patient Log File
    file = open_log("r")

    # Read the top line (i.e. Patient's Name)
    file.seek(0)
    line = file.readline()
    file.close()

    # If the Patient's Name is successfully found...
    if ('Patient:' in line):
        name = (line.split(':')[1]).rstrip()

    # If the Patient's Name is not found...
    else:
        create(name)

    return name


###############################################################################
###############################################################################
def write_line(line):
    file = open(PATIENT_FILE, "a")
    file.write(line)
    file.close()


###############################################################################
###############################################################################
def open_log(mode="a"):
    if (not exists(PATIENT_FILE)):
        create("UNKNOWN PATIENT")

    file = open(PATIENT_FILE, mode)
    return file


###############################################################################
###############################################################################
if __name__ == "__main__":
    patient = get_patient_name()
    print("Patient =" + patient)

