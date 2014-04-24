#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

from flask import g, session, url_for, redirect, request
from wrc import app

# RPi.GPIO can be launched only at raspberry, otherwise it'll raise RuntimeError
try:
    import RPi.GPIO as GPIO
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


@app.before_request
def before_request():
    if 'user' in session and session['user'] is not None:
        g.user = session['user']


def requires_auth(f):
    """Декоратор, проверяет, авторизован ли пользователь. Если нет — перенаправляет на страницу авторизации."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if app.config['AUTHORISATION_ENABLED'] and 'user' not in session:
            return redirect(url_for('login', next=request.path))
        return f(*args, **kwargs)
    return decorated


@app.context_processor
def inject_user():
    """Передаёт шаблонизатору информацию о пользователе"""
    user = getattr(g, 'user', None)
    return dict(user=user, authorisation=app.config['AUTHORISATION_ENABLED'])
