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

    # Managed pins
    PINS = [ {'id': '1',  'name': u'Smth'},
             {'id': '4',  'name': u'Smth else'},
             {'id': '12', 'name': u'Another thing'},
             {'id': '15', 'name': u'Lalala'}, 
             {'id': '16', 'name': u'Pin'},
             {'id': '18', 'name': u'Pin'}, ]


    

""" Настройки сервера для разработки """
class DevelopmentConfig(Config):
    DEBUG = True


# Select config
app.config.from_object(DevelopmentConfig)



# Logging
formatter = logging.Formatter(fmt=u'%(asctime)s %(levelname)-8s %(filename)s[on line:%(lineno)d]# %(message)s')

handler = logging.FileHandler(os.path.join(os.getcwd(),'error.log'), 'a')
handler.setFormatter(formatter)

logger = logging.getLogger('wrc')
logger.setLevel(logging.WARNING)
logger.addHandler(handler)



import wrc.views
import wrc.errors