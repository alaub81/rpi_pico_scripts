# -*- coding: utf-8 -*-
"""DHT22 Homie MQTT
reads data (Temperature & Humidity) of DHT22 sensor and
sends values to a MQTT Broker in Homie MQTT Convention format
You are able to set a value, when humidity alarm is fired.

You need to copy wificonnection.py and a configured config.py to your pico!
umqtt.simple will install, if not available on the pico
"""

import config
from wificonnection import connect, disconnect
from time import sleep
from dht import DHT22
from machine import reset, lightsleep, Pin

#led declaration
if config.ledstatus:
    led = Pin('LED', Pin.OUT)
    led.value(True)
#degree symbol decleration
degreecels = '\u00B0' + "C"

# Functions
def loadumqtt():
    global MQTTClient
    try:
        from umqtt.simple import MQTTClient
    except ImportError:
        print("Module umqtt.simple not found, try to install it now...")
        import mip
        mip.install("umqtt.simple")
        try:
            from umqtt.simple import MQTTClient
        except ImportError:
            print("Module umqtt.simple still not available... EXIT")
            reset()


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
    publish(config.homienodes + "/$properties", "temperature,humidity,humidityalarm")
    publish(config.homienodes + "/temperature/$name", "Temperature")
    publish(config.homienodes + "/temperature/$unit", degreecels.encode('utf8'))
    publish(config.homienodes + "/temperature/$datatype", "float")
    publish(config.homienodes + "/temperature/$settable", "false")
    publish(config.homienodes + "/humidity/$name", "Humidity")
    publish(config.homienodes + "/humidity/$unit", "%")
    publish(config.homienodes + "/humidity/$datatype", "float")
    publish(config.homienodes + "/humidity/$settable", "false")
    publish(config.homienodes + "/humidityalarm/$name", "Humidity Alarm")
    publish(config.homienodes + "/humidityalarm/$datatype", "boolean")
    publish(config.homienodes + "/humidityalarm/$settable", "false")
    # homie state ready
    publish("$state", "ready")


def sensorpublish():
    publish(config.homienodes + "/temperature", "{:.1f}".format(temperature))
    publish(config.homienodes + "/humidity", "{:.1f}".format(humidity))
    if humidity >= config.humidityalarm:
        publish(config.homienodes + "/humidityalarm", "true")
    else:
        publish(config.homienodes + "/humidityalarm", "false")
    

def dht22sensor():
    global temperature
    global humidity
    # initializing GPIO and DHT22
    dht22_sensor = DHT22(Pin(config.dhtgpiopin, Pin.IN, Pin.PULL_UP))
    dht22_sensor.measure()
    if dht22_sensor.temperature() == -50:
        dht22_sensor.measure()
    temperature = dht22_sensor.temperature()
    humidity = dht22_sensor.humidity()
    print('\nTemperature = ', temperature, degreecels)
    print('Humidity = ', humidity, '%', '\n')
 

# do the things
try:
    # read sensor
    dht22sensor()
    # connect to wifi
    connect()
    # install / load umqtt
    loadumqtt()
    if config.ledstatus:
        led.value(True)
    # connect to mqtt broker and initialize homie convention
    mqttconnect()    
    sensorpublish()
    sleep(.3)
    if config.usinglightsleep:
        publish("$state", "sleeping")
        sleep(.3)
        client.disconnect()
        sleep(.3)
        disconnect()
        print("going to lightsleep for %s seconds" % config.publishtime)
        if config.ledstatus:
            led.value(False)
        sleep(.1)
        lightsleep((config.publishtime)*1000)
        #deepsleep((config.publishtime)*1000)
    else:
        while True:    
            print("just a break for %s seconds" % config.publishtime)
            if config.ledstatus:
                led.value(False)
            sleep(config.publishtime)
            if config.ledstatus:
                led.value(True)
            dht22sensor()
            sensorpublish()
except RuntimeError as error:
    print('Runtime Error: ', error.args[0])
    pass
except OSError as e:
    print('OS Error: ', e.args[0])
    pass
sleep(0.1)
print("machine reset ...")
reset()