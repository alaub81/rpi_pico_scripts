# -*- coding: utf-8 -*-
"""Wifi Connection Advanced
Connecting to wifi
you will need config.py to configure SSID, Password and CountryCode
"""
import network
import config
import time

# Setting Country
import rp2
rp2.country(config.wificountrycode)
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.wifissid, config.wifipassword)
 
# Wait for connect or fail
max_wait = 10
while max_wait > 0:
  if wlan.status() < 0 or wlan.status() >= 3:
    break
  max_wait -= 1
  print('waiting for connection...')
  time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
   raise RuntimeError('network connection failed')
else:
  print('connected')
  status = wlan.ifconfig()
  print( 'ip = ' + status[0] )