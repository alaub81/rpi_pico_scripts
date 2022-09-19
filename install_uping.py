# you need to copy wificonnection.py and config.py to pico first.

import wificonnection
import upip
from time import sleep

wificonnection.connect()
sleep(1)
#upip.install("micropython-uping")
wificonnection.disconnect()