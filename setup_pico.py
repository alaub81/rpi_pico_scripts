# -*- coding: utf-8 -*-
"""Setup Pico
connecting to wifi
install needed libraries
disconnect wifi
you need first transfer config.py to pico
"""

from time import sleep
import network
import config
import mip

# Connecting to Wifi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.wifissid, config.wifipassword)

while not wlan.isconnected() and wlan.status() >= 0:
  print("Waiting to connect:")
  sleep(1)
        
print(wlan.ifconfig())
print(wlan.isconnected())

# Install Libraries
mip.install('umqtt.simple')
sleep(1)
mip.install('logging')
sleep(1)

# Disconnect Wifi
wlan.disconnect()
wlan.active(False)
wlan.deinit()
print("    Wifi State:", wlan.status())
print("Wifi connected:", wlan.isconnected())