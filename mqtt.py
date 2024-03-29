# -*- coding: utf-8 -*-
"""MQTT Managing
Using MQTT Connection as Modules.
to install umqtt.simple2 just have look at install_umqtt.py
Use and upload config.py and wificonnection.py to Pico at first
umqtt.simple Documentation:
* https://mpython.readthedocs.io/en/master/library/mPython/umqtt.simple.html
import mip
mip.install('umqtt.simple')
# for the robust variant
mip.install("umqtt.robust")
"""

from umqtt.simple import MQTTClient
from time import sleep
import config
import ssl

# MQTT Last Will
mqttlastwill = False

def connect():
    global client
    client = MQTTClient(config.mqttclientid, config.mqttbroker, port=config.mqttport, user=config.mqttusername,
                            password=config.mqttpassword, keepalive=10, ssl=config.mqttssl)
    if mqttlastwill:
        client.set_last_will("homie/" + config.homieclientid + "/$state",
                                "lost", retain=config.mqttretainmessage, qos=config.mqttqos)
    client.connect()


def publish(topic, payload):
    client.publish(topic, payload, retain=config.mqttretainmessage, qos=config.mqttqos)


def disconnect():
    client.disconnect()