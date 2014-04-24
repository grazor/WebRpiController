#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, abort, render_template, session, redirect, url_for
import json
import md5

from wrc import app
from functions import getState, requires_auth


controlledPins = []

# RPi.GPIO can be launched only at raspberry, otherwise it'll raise RuntimeError
try:
    import RPi.GPIO as GPIO
    rpi = True
except RuntimeError:
    rpi = False

for pin in app.config['PINS']:
    controlledPins.append(int(pin['id']))



@app.route("/")
@requires_auth
def index():
    """ Index page """
    pins = getState()
    return render_template('index.html', pins=pins, polling=app.config['GPIO_POLLING_DELAY'], display=app.config['DISPLAY_PIN_ID'])


@app.route('/pin/', methods=['POST'])
def setPinState():
    """ Sets pin state """
    if request.method == 'POST':
        try:
            pin = int(request.form['pin'])
            value = request.form['value'] == 'true'

            if pin in controlledPins and rpi:
                GPIO.output(pin, value)

            return "Ok"
        except:
            abort(403)
    else:
        abort(403)


@app.route('/state/')
@requires_auth
def getPinState():
    """ Returns pins state as JSON """
    pins = getState()
    return json.dumps(pins)



@app.route("/login/", methods=['GET','POST'])
def login():
    """Формирует страницу авторизации, в случае успешной авторизации перенаправляет на исходную страницу, с которой мы перешли сюда."""
    # Получение страницы, на которую необходимо перейти после успешной авторизации
    next = request.args.get('next') or url_for('index')

    if not app.config['AUTHORISATION_ENABLED']:
        return redirect(next)

    # Если пользователь уже авторизован, сразу перейдём на указанную страницу
    if 'user' in session:
        return redirect(next)

    # Авторизация
    error = ''
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        if login == app.config['USER_LOGIN'] and md5.new(password).digest() == app.config['USER_MD5_PASSWORD']:
            # Если удалось создать пользователя — авторизация прошла успешно
            session['user'] = login
            return redirect(next)
        else:
            # Иначе отобразим сообщение об ошибке
            error = u'Неверный логин или пароль'
    
    return render_template('login.html', error=error, next=next)


@app.route("/logout/", methods=['GET','POST'])
@requires_auth
def logout():
    """Заверщает сессию пользователя."""
    session.pop('user', None)
    return redirect(url_for('index'))