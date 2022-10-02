# -*- coding: utf-8 -*-
"""BME680 Sensor 
reads Temperature, Humidity, Pressure and Gas of a BME680 sensor
you need to download first bme680.py from:
* https://raw.githubusercontent.com/alaub81/rpi_pico_scripts/main/lib/bme680.py
and upload it to the lib or root folder of your pico
"""

from bme680 import *
from machine import I2C, Pin
from time import sleep

# Initialize I2C-Pins
i2c_sda = Pin(20)
i2c_scl = Pin(21)

# change this to match the location's pressure (hPa) at sea level
sealevelpressure = 1013.25

# Initialize BME680 Sensor
bme680 = BME680_I2C(I2C(0, sda=i2c_sda,scl=i2c_scl))

# You will usually have to add an offset to account for the temperature of
# the sensor. This is usually around 5 degrees but varies by use. Use a
# separate temperature sensor to calibrate this one.
temperature_offset = -2

# set sealevel if it is conffigured
if 'sealevelpressure' in locals():
    bme680.sea_level_pressure = sealevelpressure

# degree symbol decleration
degreecels = '\u00B0' + "C"

while True:
    print("\nTemperature: %0.1f " % (bme680.temperature + temperature_offset) + degreecels)
    print("Gas: %d ohm" % bme680.gas)
    print("Humidity: %0.1f %%" % bme680.humidity)
    print("Pressure: %0.3f hPa" % bme680.pressure)
    print("Altitude = %0.2f meters" % bme680.altitude) 
    sleep(3)