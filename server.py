#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys

from wrc import app
from wrc.gpio import initGpio, cleanup
from wrc.devices import initDevice
    

def sigintHandler(signal, frame):
    """Catches stop server event, cleanups GPIO"""
    cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, sigintHandler)

if __name__ == '__main__':
    initGpio(app.config['GPIO_WARNINGS'])
    for device in app.config['DEVICES']:
        initDevice(device)
    
    app.run(host='0.0.0.0', port=8000)
