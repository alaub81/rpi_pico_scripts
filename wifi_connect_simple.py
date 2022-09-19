# -*- coding: utf-8 -*-
"""Wifi Connection Simple
Connecting to wifi
you'll need config.py to configure SSID and Password
"""

from time import sleep
import network
import config

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.wifissid, config.wifipassword)

while not wlan.isconnected() and wlan.status() >= 0:
  print("Waiting to connect:")
  sleep(1)
        
print(wlan.ifconfig())
print(wlan.isconnected())