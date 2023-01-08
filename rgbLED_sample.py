# -*- coding: utf-8 -*-
"""RGB LED
Small script to use a rgb led connected to the pico
"""

from time import sleep
from machine import Pin

# Set the Variables
# set red,green and blue pins
redPin = 11
greenPin = 12
bluePin = 13

# define the the LED Pins
redled = Pin(redPin, Pin.OUT, value=0)
greenled = Pin(greenPin, Pin.OUT, value=0)
blueled = Pin(bluePin, Pin.OUT, value=0)

# turn on the led colors
redled.on()
sleep(3)
redled.off()

greenled.on()
sleep(3)
greenled.off()

blueled.on()
sleep(3)
blueled.off()

# makes white
blueled.on()
redled.on()
greenled.on()
sleep(3)
blueled.off()
redled.off()
greenled.off()