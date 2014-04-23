WebRpiController
================

About
-----
This project provides simple mobile web-interface for controlling Raspberry Pi's GPIO pins.
Web-server is based on python and flask framework (http://flask.pocoo.org/); interface utilizes Ratchet ftamework (http://goratchet.com/); GPIO is contolled by RPi.GPIO framework (http://sourceforge.net/projects/raspberry-gpio-python/).

What's done?
------------
* Control GPIO outputs

What isn't done?
----------------
* Authorisation
* Control PWN
* Input pins

Installation
------------
```bash
sudo apt-get install python-pip
sudo pip install -r pip_requirements.txt
```

Configuration
-------------
Managed pins are listed in `wrc/__init__.py` file
```python
    PINS = [ {'id': '1',  'name': u'Smth'},
             {'id': '4',  'name': u'Smth else'},
             {'id': '12', 'name': u'Another thing'},
             {'id': '15', 'name': u'Lalala'}, 
             {'id': '16', 'name': u'Pin'},
             {'id': '18', 'name': u'Pin'}, ]
```

Modify this varriable to set GPIO polling delay (in seconds)
```python
    GPIO_POLLING_DELAY = 3
```

Launching
---------
```bash
sudo ./server.py
```