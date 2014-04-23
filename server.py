#!/usr/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys

from wrc import app


def signal_handler(signal, frame):
        try:
            import RPi.GPIO as GPIO
            GPIO.cleanup()
        except:
            pass
        sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
