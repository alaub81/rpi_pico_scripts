# -*- coding: utf-8 -*-
"""DHT22 Sensor 
reads Temperature and Humidity of a DHT22 sensor
"""

from machine import Pin
from time import sleep
from dht import DHT22

# GPIO Pin Number
gpio=22

# initializing GPIO and DHT22
sleep(1)
dht22_sensor = DHT22(Pin(gpio, Pin.IN, Pin.PULL_UP))

#degree symbol decleration
degreecels = '\u00B0' + "C"
# do the things
while True:
    dht22_sensor.measure()
    if dht22_sensor.temperature() == -50:
        dht22_sensor.measure()
    temperature = dht22_sensor.temperature()
    humidity = dht22_sensor.humidity()
    print('Temperature:', temperature, degreecels)
    print('   Humidity:', humidity, '%', '\n')
    sleep(3)