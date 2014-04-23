WebRpiController
================

About
-----
This project provides simple mobile web-interface for controlling Raspberry Pi's GPIO pins.
Web-server is based on python and flask framework (http://flask.pocoo.org/); interface utilizes Ratchet ftamework (http://goratchet.com/); GPIO is contolled by RPi.GPIO framework (http://sourceforge.net/projects/raspberry-gpio-python/)

What's done?
------------
[X] Control GPIO outputs
[ ] Authorisation
[ ] Control PWN
[ ] Input pins

Configuration
-------------
Managed pins are listed in wrc/__init__.py file
```python
    # Managed pins
    PINS = [ {'id': '1',  'name': u'Smth'},
             {'id': '4',  'name': u'Smth else'},
             {'id': '12', 'name': u'Another thing'},
             {'id': '15', 'name': u'Lalala'}, 
             {'id': '16', 'name': u'Pin'},
             {'id': '18', 'name': u'Pin'}, ]
```

Installation
------------
```bash
sudo apt-get install pip
sudo pip install -r pip_requirements.txt
```


Launching
---------
```bash
./server.py
```