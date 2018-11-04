from wallaby import *
import constants as c
from servo import *


def warmUp():
    camera_open_black()
    enable_servos()
    msleep(3000)
    openClaw()
    msleep(200)
    lowArm()
    msleep(300)


def lineFollowTick():
    if analog(c.tophat) > 3800:
        motor(c.lmotor, 100)
        motor(c.rmotor, 10)
    else:
        motor(c.lmotor, 10)
        motor(c.rmotor, 100)
    msleep(5)