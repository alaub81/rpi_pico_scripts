# -*- coding: utf-8 -*-
"""BH1750 Sensor 
reads iluminance of a BH1750 sensor
you need to download first bh1750.py from:
* https://raw.githubusercontent.com/alaub81/rpi_pico_scripts/main/lib/bh1750.py
and upload it to the lib or root folder of your pico
"""

#import machine
from machine import I2C, Pin
from bh1750 import BH1750
from time import sleep

# Initialize I2C-Pins
i2c_sda = Pin(0)
i2c_scl = Pin(1)

bh1750 = BH1750(I2C(0, sda=i2c_sda,scl=i2c_scl))

while True:
    bh1750.luminance(BH1750.ONCE_HIRES_1)
    print("Iluminance: %f lux \n" % bh1750.luminance(BH1750.ONCE_HIRES_1))
    sleep(3)