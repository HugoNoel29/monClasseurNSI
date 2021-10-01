#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from mouvements import *


def obstacle(distance):
    obstacle_sensor = UltrasonicSensor(Port.S4)
    if obstacle_sensor.distance() < distance :
        return True
    else :
        return False

#TEST
if __name__ == '__main__' :
    while toto == True :
        avancer(50)
        if obstacle(300) == True :
            robot.stop()
            robot.wait(50)
        else :
            avancer(50)
        
        