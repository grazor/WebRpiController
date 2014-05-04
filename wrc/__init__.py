#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from flask import Flask


app = Flask(__name__)


class Config(object):
    PERMANENT_SESSION_LIFETIME = 2592000

    DEBUG = False
    TESTING = False

    #Cookies
    SECRET_KEY = '\xc2\xd5E\xe3\xf1\x1fp\'<d\xd0]\xb9\x01I\x112\xc1w\xaa\x85x\x11\xde\xb3\xc5'

    # Authorisation
    AUTHORISATION_ENABLED = True
    USER_LOGIN = 'test'
    USER_MD5_PASSWORD = '\t\x8fk\xcdF!\xd3s\xca\xdeN\x83&\'\xb4\xf6' 

    # Managed devices
    # Supported types:
    #   -> Out - simple output pin
    #   -> IN  - simple input pin
    #   -> 1Ws - 1-wire sensor. If uid is not set, will be assigned automatically
    DEVICES = [ {'name': u'Red LED', 'type': u'out', 'pins': [12]},
                {'name': u'Green LED', 'type': u'out', 'pins': [8]},
                {'name': u'Button', 'type': u'in', 'pins': [10]},
                {'name': u'Temperature', 'type': u'1ws', 'units': u'°С', 'uid': '28-000004580f46', 'cacheValid': '10'},
              ]


    # Sets GPIO polling delay in seconds. 0 = disabled
    GPIO_POLLING_DELAY = 3

    # Disables warnings from RPi.GPIO lib
    GPIO_WARNINGS = False

    # Displays pin number in pin list
    DISPLAY_PIN_ID = True


    # Add devices' IDs
    uid = 1
    sid = 1
    for dev in DEVICES:
        dev['id'] = uid
        uid += 1

        if dev['type'] == u'1ws':
            dev['sid'] = sid
            sid += 1

    
class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


# Select config
app.config.from_object(DevelopmentConfig)


# Logging
formatter = logging.Formatter(fmt=u'%(asctime)s %(levelname)-8s %(filename)s[on line:%(lineno)d]# %(message)s')

handler = logging.FileHandler(os.path.join(os.getcwd(), 'error.log'), 'a')
handler.setFormatter(formatter)

logger = logging.getLogger('wrc')
logger.setLevel(logging.WARNING)
logger.addHandler(handler)


import wrc.views
import wrc.errors