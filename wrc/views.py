#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, abort, render_template, session, redirect, url_for
import json
import md5

from wrc import app
from functions import getDeviceById, getState, requires_auth
from devices import setDeviceState


@app.route("/")
@requires_auth
def index():
    """Index page"""
    devices = getState()
    return render_template('index.html', devices=devices, polling=app.config['GPIO_POLLING_DELAY'], display=app.config['DISPLAY_PIN_ID'])


@app.route('/pin/', methods=['POST'])
@requires_auth
def setPinState():
    """Sets device state"""
    if request.method == 'POST':
        try:
            deviceId = int(request.form['deviceId'])
            value = request.form['value'] == 'true'


            device = getDeviceById(deviceId)
            if device:
                setDeviceState(device, value)
                return "Ok"
            else:
                return "Error"
        except:
            abort(403)
    else:
        abort(403)


@app.route('/state/')
@requires_auth
def getPinState():
    """Returns devices' state as JSON"""
    devices = getState()
    return json.dumps(devices)


@app.route('/login/', methods=['GET','POST'])
def login():
    """Generates authorisation page"""
    # Get page to be loaded after aithorisation
    next = request.args.get('next') or url_for('index')

    if not app.config['AUTHORISATION_ENABLED']:
        return redirect(next)

    # If user already authorised
    if 'user' in session:
        return redirect(next)

    # Authorisation
    error = ''
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        if login == app.config['USER_LOGIN'] and md5.new(password).digest() == app.config['USER_MD5_PASSWORD']:
            # Successful authorisation
            session['user'] = login
            return redirect(next)
        else:
            # Error message
            error = u'Wrong login or password'
    
    return render_template('login.html', error=error, next=next)


@app.route('/logout/')
@requires_auth
def logout():
    """Closes user session"""
    session.pop('user', None)
    return redirect(url_for('index'))