# -*- coding: utf-8 -*-
"""Wifi Disconnect
Disconnecting wifi
"""

import network

wlan = network.WLAN(network.STA_IF)

wlan.disconnect()
wlan.active(False)
wlan.deinit()
print("    Wifi State:", wlan.status())
print("Wifi connected:", wlan.isconnected())