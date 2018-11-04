import constants as c
from wallaby import *


def openClaw():
    set_servo_position(c.cmotor, 1000) # Don't forget to use constants here (for servo ports!) -LMB
    msleep(500)


def closedClaw():
    set_servo_position(c.cmotor, 1675) # And constants here... -LMB
    msleep(500)


def lowArm():
    set_servo_position(c.amotor, 700) # and here... -LMB
    msleep(500)


def highArm():
    set_servo_position(c.amotor, 400) # You get the idea -LMB