# -*- coding: utf-8 -*-
"""MQTT Simple test
a simple script to send a message to the MQTT Broker
to install umqtt.simple just have look at install_umqtt.py
Use and upload config.py and wificonnection.py to Pico at first
umqtt.simple Documentation:
* https://mpython.readthedocs.io/en/master/library/mPython/umqtt.simple.html
"""

from umqtt.simple import MQTTClient
from time import sleep
import config
import wificonnection
import ssl

wificonnection.connect()
wificonnection.status()

client = MQTTClient(config.mqttclientid, config.mqttbroker, port=config.mqttport, user=config.mqttusername,
                            password=config.mqttpassword, keepalive=5, ssl=config.mqttssl)
client.connect()
client.ping()
client.publish(b"TESTTOPIC", b"TESTPayload 22,5", retain=True, qos=0)
client.disconnect()

sleep(1)
wificonnection.disconnect()