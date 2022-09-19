# -*- coding: utf-8 -*-
"""UMQTT Simple Installation
you need to copy wificonnection.py and config.py to pico first.
* installation umqtt.simple2
* Installation umqtt.robust2
"""

import wificonnection
import upip
from time import sleep

wificonnection.connect()
sleep(1)
upip.install("micropython-umqtt.simple2")
upip.install("micropython-umqtt.robust2")
wificonnection.disconnect()