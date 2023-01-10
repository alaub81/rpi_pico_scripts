# -*- coding: utf-8 -*-
"""Main Script
to prevent always blank flashing the pico
GPIO(19) is used to detect, if the system will break
instead of running the MQTT script.
Just use a jumper cable to connect GND and GPIO(19)
or use a switch on these two pins.
* on exit you'll see led 5 times flashing
* on entering the python script led will flash 1 time
"""

import config
from time import sleep
from machine import Pin
from sys import exit

# declare EXIT Pin GPIO(19)
sw = Pin(19,Pin.IN,Pin.PULL_UP)
# declare LED variable
if config.ledstatus:
    led = Pin('LED', Pin.OUT)

# Check if GPIO19 is activated
if  sw.value():
    if config.ledstatus:
        # LED blink on Startup
        led.value(True)
        sleep(.3)
        led.value(False)
    # Loading DHT22 Sensor Script
    #import dht22homiemqtt.py
    #import dht22homiemqtt20.py
    # Loading BME680 Sensor Script
    #import bme680homiemqtt.py
    # Loading Pico Power Test Script
    import pico_power_tests.py
else:
    if config.ledstatus:
        blink = 5
        for i in range(blink):
            led.value(True)
            sleep(.1)
            led.value(False)
            sleep(.1)
    exit()