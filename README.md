WebRpiController
================

This project provides simple mobile web-interface for controlling Raspberry Pi's GPIO pins.
Web-server is based on python and flask framework (http://flask.pocoo.org/); interface utilizes Ratchet ftamework (http://goratchet.com/); GPIO is contolled by RPi.GPIO framework (http://sourceforge.net/projects/raspberry-gpio-python/).

What's done?
------------
- [X] Control GPIO outputs
- [X] Authorisation
- [_] 1-wire sensors
- [_] Control PWM
- [_] Input pins


Installation
------------
```bash
sudo apt-get install python-pip
sudo pip install -r pip_requirements.txt
```

Configuration
-------------
### Controlled pins
Managed pins are listed in `wrc/__init__.py` file. Pins are named as on the board.
```python
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
```

### Polling
Modify this varriable to set GPIO polling delay (in seconds):
```python
    GPIO_POLLING_DELAY = 3
```

### Authorisation
Enable authorisation (default login-password: test-test):
```python
    AUTHORISATION_ENABLED = True
    USER_LOGIN = 'test'
    USER_MD5_PASSWORD = '\t\x8fk\xcdF!\xd3s\xca\xdeN\x83&\'\xb4\xf6' 
```

Generate MD5(password):
```python
import md5
password = 'test'
md5.new(password).digest()
```

### GPIO warnings
Warnings from RPi.GPIO lib:
```python
    GPIO_WARNINGS = False
```

### Display pins
Displays pin number in pin list:
```python
    DISPLAY_PIN_ID = True
```

### Cookie secret key
Don't forget to generate another secret key!
```python
import os
os.urandom(24)
```

```python
    SECRET_KEY = 'your-key-here'
```


Launching
---------
```bash
sudo ./server.py
```

Run in background
```bash
screen -S web sudo ./server.py
Ctrl+A, D
```