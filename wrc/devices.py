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
        if 'uid' in device:
            init1WSensor(device['sid'], device['uid'])
        else:
            device['uid'] = init1WSensor(device['sid'])
    elif device['type'] == 'shell':
        pass


def getDeviceState(device):
    """Returns device state"""
    state = None
    if device['type'] == 'out':
        state = getOutPinState(device['pins'][0])
    elif device['type'] == 'in':
        state = getInPinState(device['pins'][0])
    elif device['type'] == '1ws':
        try:
            cacheValid = int(device['cacheValid'])
        except:
            cacheValid = 60
        state = get1WSensorValue(device['uid'], cacheValid)
    elif device['type'] == 'shell':
        q = os.popen(device['command'])
        state = ''.join(q.readlines()).decode('utf-8')
        q.close()

    return state


def setDeviceState(device, value):
    """Sets device outout value"""
    if device['type'] == 'out':
        setOupPinState(device['pins'][0], value)
    else:
        pass