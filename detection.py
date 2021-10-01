#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port


def detection():
    detecteur = ColorSensor(Port.S4)
    return detecteur.reflection()


#TEST
if __name__ == '__main__' :
    for i in range(5) :
        print("Il y a ", 100 - detection(),"%","de NSISIUM")