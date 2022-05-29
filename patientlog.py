from globals import *
from os.path import exists

###############################################################################
###############################################################################
def create(name):
    print("Created new log file: " + PATIENT_FILE + " for " + name)
    file = open(PATIENT_FILE, "w")
    file.write("Patient: " + name)
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
def get_name():
    name = " UNKNOWN PATIENT"

    file = open_log("r")

    file.seek(0)
    line = file.readline()
    file.close()

    if ('Patient:' in line):
        name = line.split(':')[1]
    else:
        create(name)

    return name


###############################################################################
###############################################################################
if __name__ == "__main__":
    patient = get_name()
    print("Patient =" + patient)

