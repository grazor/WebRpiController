#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, abort, render_template
import json

from wrc import app

# RPi.GPIO can be launched only at raspberry, otherwise it'll raise RuntimeError
try:
    rpi = True
except RuntimeError:
    rpi = False


def getState():
    """ Polls all pins, returns its' states """
    watchPins = app.config['PINS']

    state = []
    for pin in watchPins:
        pinState = {'id': pin['id'], 'name': pin['name']}
        if rpi:
            try:
                pinState['state'] = "on" if GPIO.input(int(pin['id'])) == GPIO.HIGH else "off"
            except:
                pinState['state'] = "off"
        else:
            pinState['state'] = "off"

        state.append(pinState)
     
    return state


@app.route("/")
def index():
    """ Index page """
    pins = getState()
    return render_template('index.html', pins=pins, polling=app.config['ENABLE_POLLING'])


@app.route('/pin/', methods=['POST'])
def setPinState():
    """ Sets pin state """
    if request.method == 'POST':
            try:
                pin = int(request.form['pin'])
                value = request.form['value'] == 'true'

                if rpi:
                    GPIO.output(pin, value)

                return "Ok"
            except:
                abort(403)
    else:
        abort(403)

@app.route('/state/')
def getPinState():
    """ Returns pins state as JSON """
    pins = getState()
    return json.dumps(pins)