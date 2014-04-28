#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

from flask import g, session, url_for, redirect, request
from wrc import app
from devices import getDeviceState


def getDeviceById(uid):
    """Returns device information by its id"""
    try:
        uid = int(uid)
    except:
        uid = -1

    for dev in app.config['DEVICES']:
        if dev['id'] == uid:
            return dev

    return None


def getState():
    """Polls all devices, returns its' states"""
    devices = app.config['DEVICES']

    state = []
    for dev in devices:
        devState = {'name': dev['name'], 'type': dev['type'], 'pins': dev['pins'], 'id': dev['id']}
        if 'units' in dev: devState['units'] = dev['units']

        devState['state'] = getDeviceState(devState)
        state.append(devState)
    return state


@app.before_request
def before_request():
    if 'user' in session and session['user'] is not None:
        g.user = session['user']


def requires_auth(f):
    """Decorator. Checks if user authorsed, otherwise redirects to login page"""
    @wraps(f)
    def decorated(*args, **kwargs):
        if app.config['AUTHORISATION_ENABLED'] and 'user' not in session:
            return redirect(url_for('login', next=request.path))
        return f(*args, **kwargs)
    return decorated


@app.context_processor
def inject_user():
    """Provides template processor information about user"""
    user = getattr(g, 'user', None)
    return dict(user=user, authorisation=app.config['AUTHORISATION_ENABLED'])
