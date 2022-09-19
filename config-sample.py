# -*- coding: utf-8 -*-
"""Configuration File
This file is where you keep secret settings, passwords, and tokens!
If you put them in the code you risk committing that info or sharing it
you need to upload that file also on the Pico,
even if you are just testing your scripts.
"""

## Wifi Settings ##
wifissid = "<YourSSID>"
wifipassword = "<YOourWifiPassword>"
wificountrycode = "<CountryCode>" # "DE" for example

## Wifi Access Point Settings ##
wifiapssid = "<SSID>"
wifiappassword = "<WifiPassword>"

## DHT GPIO Pin Number ##
dhtgpiopin = 22

## MQTT Broker ##
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
homienodes="dht22"
# how often should be a publish to MQTT (in Seconds)
publishtime = 300

## LightSleep Mode ##
# Using LightSleep mode of Pico W to save power (True) just a Loop when "False"
usinglightsleep = True