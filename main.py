#!/usr/bin/python
import os, sys
from wallaby import *
import constants as c
import actions as a
import servo as s
import constants as c
# Great work so far, Tyler!
# Next up, let's put your constants and motor functions in different files. Try using the following structure:
# constants.py (holds your constants!)
# actions.py  (contains collections of motor and servo commands to perform an action. EX: grabCan() )
# servo.py (just holds servo related functions. Not motor commands, generally)
# motors.py (just holds your motor commands. drive(), driveTimed(), driveUntilBlackLine(), stuff like that.)
# main.py (where everything starts!)
# You're ready to move on. Try grabbing the can from off the line!
# -LMB
#adsf test asdfasdf

def main():
    print "Hello"

    a.warmUp()
    while True:
        camera_update()
        print get_object_count(c.coke)
        if get_object_count(c.coke) > 0:
            if get_object_center_x(c.coke, 0) < get_camera_width()/2-5:
                motor(c.lmotor, -10)
                motor(c.rmotor, 10)
            elif get_object_center_x(c.coke, 0) > get_camera_width()/2+5:
                motor(c.lmotor, 10)
                motor(c.rmotor, -10)
            else:
                motor(c.lmotor, 60) #Somewhere in here is causing me to spin in circles forever and i dont know what
                motor(c.rmotor, 60)
                msleep(4000)
                while not left_button():
                    pass
                s.closedClaw()
                s.highArm()
                msleep(100)
                motor(c.lmotor, 100)
                motor(c.rmotor, 20)
                msleep(1000)
                motor(c.lmotor, 100)
                motor(c.rmotor, 100)
                msleep(2000)
                s.lowArm()
                s.openClaw()
                print "Victory"
                break





        msleep(200)

    print "Bye"
    msleep(500)






if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();
