# -*- coding: utf-8 -*-
"""Pico Access Point
Enables Pico as Wifi Access Point
you'll need config.py to configure SSID and Password 
"""

import network
import config

ap = network.WLAN(network.AP_IF)
ap.config(essid=config.wifiapssid, password=config.wifiappassword)
ap.active(True)

print("Wifi State:", ap.status())
print("AP enabled:", ap.isconnected())