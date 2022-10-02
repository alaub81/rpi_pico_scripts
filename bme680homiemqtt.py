# -*- coding: utf-8 -*-
"""BME680 Homie MQTT
reads data (Temperature, Humidity, Pressure, Gas, Altitude) of BME680 sensor and
sends values to a MQTT Broker in Homie MQTT Convention format
You are able to set a value, when humidity alarm is fired.
"""

import config
import wificonnection
from umqtt.simple2 import MQTTClient
from time import sleep
from bme680 import *
from machine import I2C, Pin
import machine


# led declaration
if config.ledstatus:
    led = Pin('LED', Pin.OUT)
# degree symbol decleration
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
    publish(config.homienodes + "/$name", "BME680 Sensor")
    publish(config.homienodes + "/$properties", "temperature,humidity,humidityalarm,pressure,gas,altitude")
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
    publish(config.homienodes + "/pressure/$name", "Pressure")
    publish(config.homienodes + "/pressure/$unit", "hPa")
    publish(config.homienodes + "/pressure/$datatype", "float")
    publish(config.homienodes + "/pressure/$settable", "false")
    publish(config.homienodes + "/gas/$name","Gas")
    publish(config.homienodes + "/gas/$unit","ohm")
    publish(config.homienodes + "/gas/$datatype","integer")
    publish(config.homienodes + "/gas/$settable","false")
    publish(config.homienodes + "/altitude/$name","Altitude")
    publish(config.homienodes + "/altitude/$unit","m")
    publish(config.homienodes + "/altitude/$datatype","float")
    publish(config.homienodes + "/altitude/$settable","false")
    # homie state ready
    publish("$state", "ready")


def sensorpublish():
    publish(config.homienodes + "/temperature", "{:.1f}".format(temperature))
    publish(config.homienodes + "/humidity", "{:.1f}".format(humidity))
    publish(config.homienodes + "/pressure", "{:.1f}".format(pressure))
    publish(config.homienodes + "/gas", "{:.1f}".format(gas))
    publish(config.homienodes + "/altitude", "{:.1f}".format(altitude))
    if humidity >= config.humidityalarm:
        publish(config.homienodes + "/humidityalarm", "true")
    else:
        publish(config.homienodes + "/humidityalarm", "false")
    

def bme680sensor():
    global temperature
    global humidity
    global pressure
    global gas
    global altitude
    # Initialize BME680 Sensor
    bme680 = BME680_I2C(I2C(0, sda=Pin(config.i2c_sda),scl=Pin(config.i2c_scl)))
    # set sealevel if it is conffigured
    if 'config.sealevelpressure' in locals():
        bme680.sea_level_pressure = config.sealevelpressure
    temperature = (bme680.temperature + config.temperature_offset)
    humidity = bme680.humidity
    pressure = bme680.pressure
    gas = bme680.gas
    altitude = bme680.altitude
 

# do the things
try:
    # connect to wifi
    wificonnection.connect()
    # connect to mqtt broker and initialize homie convention
    mqttconnect()
    while True:
        if config.ledstatus:
            led.value(True)
        bme680sensor()
        print('Temperature = ', temperature, degreecels)
        print('Humidty = ', humidity, '%')
        print('Pressure = ', pressure, 'hPa')
        print('Gas = ', gas, 'ohm')
        print('Altitude = ', altitude, 'm', '\n')       
        sensorpublish()
        sleep(.5)
        if config.usinglightsleep:
            publish("$state", "sleeping")
            sleep(.5)
            client.disconnect()
            sleep(.5)
            wificonnection.disconnect()
            print("done...")
            #sleep(.5)
            if config.ledstatus:
                led.value(False)
                machine.lightsleep((config.publishtime)*1000-13100)
            else:
                machine.lightsleep((config.publishtime)*1000-10600)
            break
        else:
            print("just a break for %s seconds" % config.publishtime)
            if config.ledstatus:
                led.value(False)
                sleep(config.publishtime-15)
            else:
                sleep(config.publishtime-10)
except RuntimeError as error:
    print(error.args[0])
    pass
except OSError as e:
    print(e.args[0])
    pass
machine.reset()