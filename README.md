WebRpiController
================
This project provides simple mobile web-interface for controlling Raspberry Pi's GPIO pins.
Web-server is based on python and [flask framework](http://flask.pocoo.org/); interface utilizes [Ratchet ftamework](http://goratchet.com/); GPIO is contolled by [RPi.GPIO framework](http://sourceforge.net/projects/raspberry-gpio-python/).


Table of Contents
-----------------
**[Supported features](#what-is-done)**  
**[Installation](#installation)**  
**[Configuration](#configuration)**  
**[Launching](#launching)**  
**[Screenshots](#screenshots)**  


What is done?
-------------
- [X] Control GPIO outputs
- [X] Input pins
- [X] 1-wire sensors
- [X] custom shell commands
- [X] Authorisation


Installation
------------
```bash
git clone https://github.com/grazor/WebRpiController.git
cd WebRpiController
sudo apt-get install python-pip
sudo pip install -r pip_requirements
```

Default login-password: test-test.


Configuration
-------------
### Controlled pins
Managed pins are listed in `wrc/__init__.py` file. Pins are named as on the board.
```python
    # Managed devices
    # Supported types:
    #   -> Out   - simple output pin
    #   -> IN    - simple input pin
    #   -> 1Ws   - 1-wire sensor. If uid is not set, will be assigned automatically
    #   -> Shell - shell commands
    DEVICES = [ {'name': u'Red LED', 'type': u'out', 'pins': [12]},
                {'name': u'Green LED', 'type': u'out', 'pins': [8]},
                {'name': u'Button', 'type': u'in', 'pins': [10]},
                {'name': u'Temperature', 'type': u'1ws', 'units': u'°С', 'uid': '28-000004580f46', 'cacheValid': '60'},
                {'name': u'Datetime', 'type': u'shell', 'command': 'date'},
              ]
```


### Polling
Modify this varriable to set GPIO polling delay (in seconds), 0 = disabled:
```python
    GPIO_POLLING_DELAY = 3
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

### Authorisation
Enable authorisation (default login-password: test-test):
```python
    AUTHORISATION_ENABLED = True
    USER_LOGIN = 'test'
    USER_MD5_PASSWORD = '\t\x8fk\xcdF!\xd3s\xca\xdeN\x83&\'\xb4\xf6' 
```

Generate MD5(password):
```bash
./passgen.py password
```

### Cookie secret key
Don't forget to generate different secret key!
```python
python
>>> import os
>>> os.urandom(24)
```

```python
    SECRET_KEY = 'your-key-here'
```


Launching
---------
### Run with flask internal server
This method is recommended only for testing and debugging.
```bash
sudo ./server.py
```

Run in background
```bash
screen -S web sudo ./server.py
Ctrl+A, D
```

### Run with lighttpd
Visit [flask manual](http://flask.pocoo.org/docs/deploying/fastcgi/)


Screenshots
-----------
![Screenshot](https://cloud.githubusercontent.com/assets/1236070/2872795/4b44924e-d377-11e3-864c-5e9c5a8d73f6.png)
