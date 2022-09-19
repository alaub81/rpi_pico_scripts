# -*- coding: utf-8 -*-
"""Pico LED Flash
flashes the Pico Status LED
"""

from machine import Pin
from time import sleep

pin = Pin('LED', Pin.OUT)

while True:
    pin.toggle()
    sleep(1)
