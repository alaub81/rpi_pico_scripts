# -*- coding: utf-8 -*-
"""Configuration File
This file is where you keep secret settings, passwords, and tokens!
If you put them in the code you risk committing that info or sharing it
you need to upload that file also on the Pico,
even if you are just testing your scripts.
"""

### Board Configuration ###
## Status LED ##
# LED can show you the status of the running scripts
# e.g. Wifi Connection Status Code
ledstatus = True

## LightSleep Mode ##
# Using LightSleep mode of Pico W to save power (True) just a Loop when "False"
usinglightsleep = True

## Wifi ##
# Wifi Connection Settings
wifissid = "<YourSSID>"
wifipassword = "<YOourWifiPassword>"
# Optional: if you like to use, uncomment the country code lines in wificonnection.py
wificountrycode = "<CountryCode>" # "DE" for example
# Wifi Access Point Settings
wifiapssid = "<SSID>"
wifiappassword = "<WifiPassword>"


### MQTT Broker ###
mqttbroker = "<FQDN / IP of MQTTBroker>"
mqttport = 1883 # 8883 for TLS
mqttusername = "<MQTT-Username>"
mqttpassword = "<MQTT-Password"
mqttclientid = "<UniqueMQTTClientID>" # "pico-w-001" for example
# if you like to generate a unique ID:
#import ubinascii
#mqttclientid = ubinascii.hexlify(machine.unique_id())
mqttssl = False # True for TLS connection
mqttqos = 0 # only 0 and 1 is supported
mqttretainmessage = True # True or False
# Homie Configuration / Naming
homieclientid = "<UniqueHomieClientID>" # "pico-w-001-dht22" for example
homieclientname = "<Name your Homie Device>" # "Pico W 001 DHT22 Sensor" for example
homienodes="<sensorname>" # for example "dht22" or "bme680"
# how often should be a publish to MQTT (in Seconds)
publishtime = 300


### Sensor Configurations ###
# At which value humidity alarm will be fired (x in %)
humidityalarm = 70

## DHT22 Sensor ##
# DHT22 GPIO Pin Number
dhtgpiopin = 22

## BME680 Sensor ##
# Initialize BME680 I2C-Pins
i2c_sda = 20
i2c_scl = 21
# change this to match the location's pressure (hPa) at sea level
sealevelpressure = 1013.25
# You will usually have to add an offset to account for the temperature of
# the sensor. This is usually around 5 degrees but varies by use. Use a
# separate temperature sensor to calibrate this one.
temperature_offset = -2


### iPerf3 ###
# where to connect (Server IP or ServerName)?
iperfserver = '<serverip/servername>'