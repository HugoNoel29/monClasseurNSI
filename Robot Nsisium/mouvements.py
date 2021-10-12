#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop, Direction
from time import sleep


ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)


def avancer(distance) :
    robot.straight(distance)



def stop() :
    robot.stop()



def tourner(angle):
    robot.turn(angle)


#TEST
if __name__ == '__main__' :
    avancer(100)
    stop()   
    sleep(2)
    tourner(90)
    tourner(-180)
    avancer(-100)

