# -*- coding: utf-8 -*-
"""Pico Temperature
Reads the Pico's temperature sensor data
"""
import machine
from time import sleep
 
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

#degree symbol decleration
degreecels = '\u00B0' + "C"
    
while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature, degreecels)
    sleep(10)