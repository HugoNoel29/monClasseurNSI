#!/usr/bin/env pybricks-micropython

from time import sleep
from random import randint
from detection import *
from mouvements import *
from ultrasons import *

ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)




for i in range(3) :

    distance = randint(5,500)
    
    avancer(distance*1.5)
    tourner(distance - ( distance % 2 ))
    avancer(-distance/4)
    tourner(-distance/2)
    print(detection())



j = 0
while j < 20 :
    if obsatcle(300) == Flase :
        avancer(250)
        j += 1
    else :
        tourner(45)
        j += 1
