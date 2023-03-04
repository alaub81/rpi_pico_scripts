# -*- coding: utf-8 -*-
"""Wifi Connection Module
Connecting Wifi, disconnecting Wifi and Wifi status
you'll need config.py to configure SSID, Password and CountryCode
* wificonnection.connect()
* wificonnection.disconnect()
* wificonnection.status()
"""

import config
from machine import reset, Pin
from time import sleep
import network

# wlan declearation
wlan = network.WLAN(network.STA_IF)
# led declaration
if config.ledstatus:
    led = Pin('LED', Pin.OUT)


def connect():
    # Setting Country Code
    network.country(config.wificountrycode)
    
    # Setting Hostname
    network.hostname(config.wifihostname)

    # activate wifi
    wlan.active(True)
    wlan.connect(config.wifissid, config.wifipassword)
    #wlan.connect(config.wifissid, config.wifipassword, hostname=config.wifihostname)

    # Wait for connect or fail
    print('waiting for wifi connection ...')
    max_wait = 30
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        sleep(.2)

    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('wifi connection failed')
        reset()
    else:
        # LED blinking
        if config.ledstatus:
            for i in range(wlan.status()):
                led.on()
                sleep(.1)
                led.off()
                sleep(.1)
        print('wifi connected: ' + str(wlan.status()))
        status = wlan.ifconfig()
        print('ip = ' + status[0])


def disconnect():
    wlan.disconnect()
    wlan.active(False)
    wlan.deinit()
    # Quick Fix for deinit and lightsleep mode problem https://github.com/micropython/micropython/discussions/10889
    wlanled = Pin('LED', Pin.OUT)
    print('wifi disconnected: ' + str(wlan.status()))
    

def status():
    print("wifi status: " + str(wlan.isconnected()))