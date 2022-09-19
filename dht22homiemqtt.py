# -*- coding: utf-8 -*-
"""DHT22 Homie MQTT
reads data (Temperature & Humidity) of DHT22 sensor and
sends values to a MQTT Broker in Homie MQTT Convention format
"""

import config
import wificonnection
from umqtt.simple2 import MQTTClient
from time import sleep
from dht import DHT22
import machine

#led declaration
led = machine.Pin('LED', machine.Pin.OUT)
#degree symbol decleration
degreecels = '\u00B0' + "C"

# Functions
def publish(topic, payload):
    client.publish("homie/" + config.homieclientid + "/" + topic,
                   payload, retain=config.mqttretainmessage, qos=config.mqttqos)


def mqttconnect():
    global client
    client = MQTTClient(config.mqttclientid, config.mqttbroker, port=config.mqttport, user=config.mqttusername,
                            password=config.mqttpassword, keepalive=10, ssl=config.mqttssl,
                            ssl_params={})
    client.set_last_will("homie/" + config.homieclientid + "/$state",
                            "lost", retain=config.mqttretainmessage, qos=config.mqttqos)
    client.connect()
    # homie client config
    publish("$state", "init")
    publish("$homie", "4.0")
    publish("$name", config.homieclientname)
    publish("$nodes", config.homienodes)
    # homie node config
    publish(config.homienodes + "/$name", "DHT22 Sensor")
    publish(config.homienodes + "/$properties", "temperature,humidity")
    publish(config.homienodes + "/temperature/$name", "Temperature")
    publish(config.homienodes + "/temperature/$unit", degreecels.encode('utf8'))
    publish(config.homienodes + "/temperature/$datatype", "float")
    publish(config.homienodes + "/temperature/$settable", "false")
    publish(config.homienodes + "/humidity/$name", "Humidity")
    publish(config.homienodes + "/humidity/$unit", "%")
    publish(config.homienodes + "/humidity/$datatype", "float")
    publish(config.homienodes + "/humidity/$settable", "false")
    # homie state ready
    publish("$state", "ready")


def sensorpublish():
    publish(config.homienodes + "/temperature", "{:.1f}".format(temperature))
    publish(config.homienodes + "/humidity", "{:.1f}".format(humidity))
    

def dht22sensor():
    global temperature
    global humidity
    # initializing GPIO and DHT22
    dht22_sensor = DHT22(machine.Pin(config.dhtgpiopin, machine.Pin.IN, machine.Pin.PULL_UP))
    dht22_sensor.measure()
    temperature = dht22_sensor.temperature()
    humidity = dht22_sensor.humidity()
   
   
# do the things
try:
    # connect to wifi
    wificonnection.connect()
    sleep(.5)
    # connect to mqtt broker and initialize homie convention
    mqttconnect()
    while True:
        led.value(True)
        dht22sensor()
        print('Temperatur = ', temperature, degreecels)
        print('Luftfeuchtigkeit = ', humidity, '%', '\n')
        sensorpublish()
        if config.usinglightsleep:
            publish("$state", "sleeping")
            sleep(1.5)
            client.disconnect()
            sleep(.5)
            wificonnection.disconnect()
            led.value(False)
            sleep(.5)
            machine.lightsleep((config.publishtime-15)*1000)
            break
        else:
            print("just a break for %s seconds" % config.publishtime)
            led.value(False)
            sleep(config.publishtime-15)
except RuntimeError as error:
    print(error.args[0])
    pass
except OSError as e:
    print(e.args[0])
    pass
print("done...")
sleep(2)
machine.reset()