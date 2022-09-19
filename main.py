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


import machine
from time import sleep

# declare LED variable
led = machine.Pin('LED', machine.Pin.OUT)
# declare EXIT Pin GPIO(19)
sw = machine.Pin(19,machine.Pin.IN,machine.Pin.PULL_UP)

# Check if GPIO19 is activated
if  sw.value():
    # LED blink on Startup
    led.value(True)
    sleep(.3)
    led.value(False)
    import dht22homiemqtt.py
else:
    blink = 5
    for i in range(blink):
        led.value(True)
        sleep(.1)
        led.value(False)
        sleep(.1)
    sys.exit()