# -*- coding: utf-8 -*-
"""Pico LED
Switches the Pico Status LED on and off
"""

from time import sleep
from machine import Pin

led = Pin('LED', Pin.OUT)
print("LED on")
led.value(1)
sleep(5)
led.value(0)
print("LED off")