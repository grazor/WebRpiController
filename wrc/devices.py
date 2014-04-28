#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gpio import *


def initDevice(device):
    """Inits device"""
    if device['type'] == 'out':
        initOutDevice(device['pins'][0])
    elif device['type'] == 'in':
        initInDevice(device['pins'][0])
    elif device['type'] == '1ws':
        init1WSensor(device['pins'][0], device['pins'][1], device['pins'][2])


def getDeviceState(device):
    """Returns device state"""
    state = None
    if device['type'] == 'out':
        state = getOutPinState(device['pins'][0])
    elif device['type'] == 'in':
        state = getInPinState(device['pins'][0])
    elif device['type'] == '1ws':
        state = get1WSensorValue(device['pins'][0], device['pins'][1], device['pins'][2])

    return state


def setDeviceState(device, value):
    """Sets device outout value"""
    if device['type'] == 'out':
        setOupPinState(device['pins'][0], value)
    else:
        pass