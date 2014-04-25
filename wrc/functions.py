#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

from flask import g, session, url_for, redirect, request
from wrc import app
from gpio import getOutPinState


def getState():
    """ Polls all pins, returns its' states """
    watchPins = app.config['PINS']

    state = []
    for pin in watchPins:
        pinState = {'id': pin['id'], 'name': pin['name'], 'type': pin['type']}

        if pinState['type'] == u'out':
            pinState['state'] = getOutPinState(pinState['id'])
        elif pinState['type'] == u'1ws':
            pinState['state'] = '0'
            pinState['unit'] = pin['unit']

        state.append(pinState)
    
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
