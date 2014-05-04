#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from time import time

# RPi.GPIO can be launched only at a raspberry, otherwise it'll raise RuntimeError
try:
    import RPi.GPIO as GPIO
    rpi = True
except RuntimeError:
    rpi = False

sensors = []

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

def init1WSensor(sensorId, devId=''):
    """Inits 1-wire sensor"""
    if rpi:
        os.system('modprobe wire')
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        with open('/sys/bus/w1/devices/w1_bus_master1/w1_master_slaves', 'r') as f:
            sensors = f.read().strip().split('\n')

        if not devId:
            if len(sensors) >= sersorId:
                return sensors[sensorId-1]
            else:
                return False
        else:
            if devId in sensors:
                return devId
            else:
                return False


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


def get1WSensorValue(devId):
    """Returns 1-wire sensor value"""
    value = 0
    
    timeDelta = 0
    prevValue = 0

    if rpi and devId in sensors:
        cache = 'cache%s.tmp' % devId
        if os.path.isfile(cache):
            try:
                with open(cache, 'r') as f:
                    prevTime, prevValue = f.read().strip().split(':')

                prevTime, prevValue = int(strip(prevTime)), int(strip(prevValue))
                timeDelta = int(time()) - prevTime


            except:
                pass

        if timeDelta < 60:
            value = prevValue
        else:
            value = readTemperature('/sys/bus/w1/devices/'+ devId +'/w1_slave')
            #TODO: save to cache
    return value



#------------------------------------------
def setOupPinState(pinId, value):
    """Sets pin value"""
    if rpi:
        GPIO.output(pinId, value)




#------------------------------------------
def readTemperature(file):
    tfile = open(file)
    text = tfile.read()
    tfile.close()
    lines = text.split("\n")
    if lines[0].find("YES") > 0:
        temp = float((lines[1].split(" ")[9])[2:])
        temp /= 1000
        return temp
    return 0
