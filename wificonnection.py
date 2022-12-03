# -*- coding: utf-8 -*-
"""Wifi Connection Module
Connecting Wifi, disconnecting Wifi and Wifi status
you'll need config.py to configure SSID, Password and CountryCode
* wificonnection.connect()
* wificonnection.disconnect()
* wificonnection.status()
"""

import config
import machine
from time import sleep
import network
import rp2
import machine

# wlan declearation
wlan = network.WLAN(network.STA_IF)
# led declaration
if config.ledstatus:
    led = machine.Pin('LED', machine.Pin.OUT)


def connect():
    # Setting Country
    rp2.country(config.wificountrycode)

    # activate wifi
    wlan.active(True)
    wlan.connect(config.wifissid, config.wifipassword)

    # Wait for connect or fail
    max_wait = 15
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
        machine.reset()
    else:
        # LED blinking
        if config.ledstatus:
            for i in range(wlan.status()):
                led.on()
                sleep(.1)
                led.off()
                sleep(.1)
        print('connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])


def disconnect():
    wlan.disconnect()
    wlan.active(False)
    wlan.deinit()
    print("Disconnected: " + str(wlan.status()))
    

def status():
    print("Connected: " + str(wlan.isconnected()))