#!/usr/bin/env python
# -*- coding: utf-8 -*-


# RPi.GPIO can be launched only at a raspberry, otherwise it'll raise RuntimeError
try:
    import RPi.GPIO as GPIO
    rpi = True
except RuntimeError:
    rpi = False


def initGpio(warnings):
    """Inits GPIO with default settings"""
    if rpi:
        GPIO.setwarnings(warnings)
        GPIO.setmode(GPIO.BOARD)


def cleanup():
    """Cleanups GPIO data"""
    if rpi:
        GPIO.cleanup()


#------------------------------------------
def initInDevice(pinId):
    """Inits input pin"""
    if rpi:
        GPIO.setup(int(pinId), GPIO.IN)

def initOutDevice(pinId):
    """Inits output pin"""
    if rpi:
        GPIO.setup(int(pinId), GPIO.OUT)

def init1WSensor(somePinId, anotherPinId, oneMorePinId):
    """Inits 1-wire sensor"""
    if rpi:
        pass


#------------------------------------------
def getInPinState(pinId):
    """Returns pin's state. 'on' or 'off'. If app running not on a raspberry, returns 'off'"""
    state = 'off'
    if rpi:
        try:
            state = 'on' if GPIO.input(int(pinId)) == GPIO.HIGH else 'off'
        except:
            state = 'off'
    return state


def getOutPinState(pinId):
    """Returns pin's state. 'on' or 'off'. If app running not on a raspberry, returns 'off'"""
    return getInPinState(pinId)


def get1WSensorValue(somePinId, anotherPinId, oneMorePinId):
    """Returns 1-wire sensor value"""
    value = 0
    if rpi:
        pass
    return value



#------------------------------------------
def setOupPinState(pinId, value):
    """Sets pin value"""
    if rpi:
        GPIO.output(pinId, value)
