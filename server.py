#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys

from wrc import app
from wrc.gpio import initGpio, initOutPin, cleanup
    

def sigintHandler(signal, frame):
    cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, sigintHandler)

if __name__ == '__main__':
    initGpio(app.config['GPIO_WARNINGS'])
    for pin in app.config['PINS']:
        initOutPin(int(pin['id']))
    
    app.run(host='0.0.0.0',port=8000)
