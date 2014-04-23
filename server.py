#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys

from wrc import app


def initGpio():
    try:
        import RPi.GPIO as GPIO
        GPIO.setwarnings(app.config['GPIO_WARNINGS'])
        GPIO.setmode(GPIO.BOARD)
        for pin in app.config['PINS']:
            GPIO.setup(int(pin['id']), GPIO.OUT)
    except:
        pass

def sigintHandler(signal, frame):
    try:
        import RPi.GPIO as GPIO
        GPIO.cleanup()
    except:
        pass
    sys.exit(0)


signal.signal(signal.SIGINT, sigintHandler)

if __name__ == '__main__':
    initGpio()
    app.run(host='0.0.0.0',port=8000)
