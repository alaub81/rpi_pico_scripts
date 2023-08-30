# -*- coding: utf-8 -*-
"""UMQTT Simple Installation
you need to copy wificonnection.py and config.py to pico first.
* installation umqtt.simple
or optional:
* Installation umqtt.robust
"""

import wificonnection
import mip
from time import sleep

wificonnection.connect()
sleep(1)
mip.install('umqtt.simple')
# uncomment for the robust variant
#mip.install("umqtt.robust")
wificonnection.disconnect()