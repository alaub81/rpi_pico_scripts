# -*- coding: utf-8 -*-
"""Pico Powerconsumption Test Script
This Script runs for a specified test time (testtime variable) some tests, 
so you are able to measure the consumed power of the pico.
first please copy wificonnection.py and configured config.py to the pico.
after that you can copy a configured main.py and the script itself to your pico.
"""

import machine
from umqtt.simple import MQTTClient
from dht import DHT22
import time
import wificonnection
import config

# How long testing in seconds
<<<<<<< HEAD
testtime=7
# MQTT Last Will
mqttlastwill = False
# DHT22 GPIO Pin Number
gpio=22
=======
testtime=5
>>>>>>> 4fe3c7221830d7f7d6ba6ae482988a648913b652

# Define LED
led = machine.Pin('LED', machine.Pin.OUT)
    
def ledblinking(blink):
    for i in range(blink):
        led.on()
        time.sleep(.2)
        led.off()
        time.sleep(.2)

def connect():
    global client
    client = MQTTClient(config.mqttclientid, config.mqttbroker, port=config.mqttport, user=config.mqttusername,
                            password=config.mqttpassword, keepalive=10, ssl=config.mqttssl)
    client.connect()

def publish(topic, payload):
    client.publish("homie/" + config.homieclientid + "/" + topic,
                   payload, retain=config.mqttretainmessage, qos=config.mqttqos)

def disconnect():
    client.disconnect()
    
def dht22sensor():
    degreecels = '\u00B0' + "C"
    # initializing GPIO and DHT22
    dht22_sensor = DHT22(machine.Pin(config.dhtgpiopin, machine.Pin.IN, machine.Pin.PULL_UP))
    dht22_sensor.measure()
    if dht22_sensor.temperature() == -50:
        dht22_sensor.measure()
    temperature = dht22_sensor.temperature()
    humidity = dht22_sensor.humidity()
    print('\nTemperature = ', temperature, degreecels)
    print('Humidity = ', humidity, '%', '\n')

# first sleep a bit
time.sleep(testtime)
led.on()
time.sleep(2)
led.off()
time.sleep(1)
# get the start time
st = time.time()

xtimes=1

# sleep test
ledblinking(xtimes)
xtimes += 1
print('\n * sleep test')
time.sleep(testtime)
print('   - sleep test: test number %i done' % xtimes)

# internal LED test
ledblinking(xtimes)
xtimes += 1
print('\n * internal led test')
time.sleep(.5)
led.on()
time.sleep(testtime)
led.off()
time.sleep(.5)
print('   - internal led test: test number %i done' % xtimes)

# external LED test
ledblinking(xtimes)
xtimes += 1
print('\n * external led test')
machine.Pin(11, machine.Pin.OUT, value=1)
machine.Pin(12, machine.Pin.OUT, value=1)
machine.Pin(13, machine.Pin.OUT, value=1)
time.sleep(testtime)
machine.Pin(11, machine.Pin.OUT, value=0)
machine.Pin(12, machine.Pin.OUT, value=0)
machine.Pin(13, machine.Pin.OUT, value=0)
print('   - internal led test: test number %i done' % xtimes)

# find sum to first 1 million numbers
ledblinking(xtimes)
xtimes += 1
print('\n * calculating test')
sum_x = 0
for i in range(500000):
    sum_x += i
print('Sum of first 500k numbers is:', sum_x)
print('   - calculating test: test number %i done' % xtimes)

# test with just some print()
ledblinking(xtimes)
xtimes += 1
for i in range(testtime * 20000):
    print('This will PRINT this message many times')
print('\n * print test: test number %i done' % xtimes)
time.sleep(.5)

# test dht22
ledblinking(xtimes)
xtimes += 1
print('\n * dht22 test')
for i in range(testtime * 2):
    dht22sensor()
    time.sleep(.1)
print('   - dht22 test: test number %i done' % xtimes)
time.sleep(.5)

# test connecting to wifi
ledblinking(xtimes)
xtimes += 1
print('\n * wifi connection test')
time.sleep(.5)
wificonnection.connect()
time.sleep(testtime)
print('   - wifi connection test: test number %i done' % xtimes)

# test mqtt connection
ledblinking(xtimes)
xtimes += 1
print('\n * mqtt connection test')
time.sleep(.5)
connect()
time.sleep(testtime)
print('   - mqtt connection test: test number %i done' % xtimes)

# test mqtt publishing
ledblinking(xtimes)
xtimes += 1
print('\n * mqtt publish test')
time.sleep(.5)
mqtt=1000
temperature = 1000000000000000000000000000.0
for i in range(mqtt * testtime):
    publish(config.homienodes + "/temperature", "{:.1f}".format(temperature))
    temperature += 0.1
    #time.sleep(.01)
print('   - mqtt publish test: test number %i done' % xtimes)  

# test mqtt disconnect
ledblinking(xtimes)
xtimes += 1
print('\n * mqtt disconnect test')
time.sleep(.5)
disconnect()
time.sleep(testtime)
print('   - mqtt disconnect test: test number %i done' % xtimes)
    
# test disconnecting wifi
ledblinking(xtimes)
xtimes += 1
print('\n * wifi connection test')
time.sleep(.5)
wificonnection.disconnect()
time.sleep(testtime)
print('   - wifi connection test: test number %i done' % xtimes)

# test with lightsleep mode
ledblinking(xtimes)
xtimes += 1
print('\n * lightsleep mode test')
time.sleep(.5)
machine.lightsleep(testtime * 1000)
print('   - lightsleep mode test: test number %i done' % xtimes)

# get the end time
et = time.time()

# calculate and print the execution time
print('Execution time:', et - st, 'seconds')

# last test with deepsleep mode
ledblinking(xtimes)
xtimes += 1
print('\n * deepsleep mode test')
time.sleep(.5)
machine.deepsleep(testtime * 1000)
