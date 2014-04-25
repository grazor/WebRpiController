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

    # Managed pins
    # Supported types:
    #   -> Out - simple output pin
    #   -> 1Ws - 1-wire sensor
    PINS = [ {'id': '12', 'type': u'out', 'name': u'LED'},
             {'id': '13', 'type': u'out', 'name': u'Dummy out'},
             {'id': '15', 'type': u'out', 'name': u'Dummy out'}, 
             {'id': '16', 'type': u'out', 'name': u'Dummy out'},
             {'id': '18', 'type': u'out', 'name': u'Dummy out'},
             {'id': '22', 'type': u'1ws', 'name': u'Dummy 1-wire sensor', 'unit': u'deg'}, ]


    # Sets GPIO polling delay in seconds. 0 = disabled
    GPIO_POLLING_DELAY = 3

    # Disables warnings from RPi.GPIO lib
    GPIO_WARNINGS = False

    # Displays pin number in pin list
    DISPLAY_PIN_ID = True


    
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