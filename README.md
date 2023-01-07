# Raspberry Pi Pico MicroPython Script collection
That is a collection of all my Raspberry Pi Pico MicroPython Scripts.

* First Steps with Pico LED and Pico's Temperature sensor.
* Managing the Wifi connection
* Using Pico as Wifi Access Point
* Reading from a DHT22 Sensor
* Reading from a BME680 Sensor
* Reading from a bh1750 illuminance sensor
* first Steps with MQTT
* Sending Sensor Data to MQTT Broker
* Sample for logging in python
* Sample for measuring the time, a script needs to run

You will find a short Description of the Scripts on the top of each script.

If you need support or have questions, just open up an issue, or contact me directly.

# Configuration File `config.py`
most of the Scripts here are using for configuration the `config.py` file.  
There you will configure all the variables which are used in the other python scripts. 
For example wificonnnection scripts. SSID and Password is configured in the `config.py`.
Just copy the `config_sample.py` to `config.py`, configure it with your needs and then upload it to your Pico.

# Setup the Pico `setup_pico.py`
With the `setup_pico.py` file, you are able to install the follwing libraries:
* umqtt.simple
* logging
first the script will connect to wifi (it uses `config.py` for credentials) then it will install the libraries via `mip` after that, it just disconnects from wifi.

# Autostart Script `main.py`
To prevent always blank flashing the pico GPIO(19) is used to detect, if the system will break instead of running the MQTT script.
Just use a jumper cable to connect GND and GPIO(19) or use a switch on these two pins.
* On exit you'll see led 5 times flashing (GPIO19 on)
* on entering the python script led will flash 1 time (GPIO19 off)
* just put in the name of the python script you like to automaticaly start (in my sample: `import dht22homiemqtt.py`)

# Pico to Wifi `wificonnection.py`
to make thinks easier, I wrote that littel python script, which is able to connect, disconnect and print out the wifi status.
You can use it in other scripts, by just using:
* wificonnection.connect()
* wificonnection.disconnect()
* wificonnection.status()

# Installing `umqtt.simple` or `umqtt.robust`
for the mqtt Scripts you will need `umqtt.simple`.  
It is not a Standard Library in Micropython for the Pico, so you need to install it once on the Pico. You can use `setup_pico.py` to install, or just do it step by step.
* First connect pico to wifi (you can use the `wifi_connect_simple.py`). 
* Then use the following lines in REPL.

```python
import mip
upip.install("umqtt.simple")
# for the robust variant
upip.install("umqtt.robust")
```
After installation is done, you can use `wifi_disconnect.py` to close the wifi connection.

# Deprecated: Installing `umqtt.simple2` or `umqtt.robust2`

**Older Micropython Installation are using `upip` ... but the newer ones changed to `mip`**

for the mqtt Scripts you will need `umqtt.simple2`.  
It is not a Standard Library in Micropython for the Pico, so you need to install it once on the Pico.
First use the `wifi_connect_simple.py` to connect to your wifi. Then use the following lines in REPL.

```python
import upip
upip.install("micropython-umqtt.simple2")
# for the robust variant
upip.install("micropython-umqtt.robust2")
```
After installation is done, you can use `wifi_disconnect.py` to close the wifi connection.

# DHT22 Sensor
At first you need to connect your DHT22 Sensor to your Pico's GPIO Board.

| Pin Nr   | GPIO Name | DHT22 Sensor |
| -------- | --------- | ------------ |
| Pin 36   | 3V3 +3,3V | 1 (VCC) / +  |
| Pin 29   | GPIO 22   | 2 (Data)     |
| Pin 28   | GND       | 4 (GND) / -  |

then you can use the following scripts:
* dht22_sample.py
    * small Test Script, just run it via REPL
* dht22homiemqtt.py
    * you need to copy `wificonnection.py` and `config.py` to your pico first
    * and install [umqtt.simple2](#installing-umqttsimple2-or-umqttrobust2) on your board.

More Details here:
* https://www.laub-home.de/wiki/Raspberry_Pi_Pico_W_DHT22_Temperatur_Sensor

# BME680 Sensor
At first you need to connect your BME680 Sensor to your Pico's GPIO Board.
| Pin Nr   | GPIO Name      | BME680 Sensor |
| -------- | -------------- | ------------- |
| Pin 36   | 3V3 (OUT)      | VCC           |
| Pin 28   | GND            | GND           |
| Pin 27   | GP21(I2C0 SCL) | SCL           |
| Pin 26   | GP20(I2C0 SDA) | SDA           |

then you can use the following scripts:
* bme680_sample.py
    * you need to copy `lib/bme680.py` to your pico first 
* bme680homiemqtt.py
    * you need to copy `lib/bme680.py`, `wificonnection.py` and `config.py` to your pico first
    * and install [umqtt.simple](#installing-umqttsimple-or-umqttrobust) on your board.

More Details here:
* https://www.laub-home.de/wiki/Raspberry_Pi_Pico_W_BME680_Raumklima_Sensor

# BH1750 illuminance sensor
At first you need to connect your BH1750 sensor to your Pico's GPIO Board.
| Pin Nr   | GPIO Name      | BME680 Sensor |
| -------- | -------------- | ------------- |
| Pin 36   | 3V3 (OUT)      | VCC           |
| Pin 28   | GND            | GND           |
| Pin 27   | GP21(I2C0 SCL) | SCL           |
| Pin 26   | GP20(I2C0 SDA) | SDA           |

then you can use the following script:
* bh1750_sample.py
    * you need to copy `lib/bh1750.py` to your pico first

More Details here:
* https://www.laub-home.de/wiki/Raspberry_Pi_Pico_W_BH1750_Helligkeitssensor

# iPerf3 - Bandwidth testing `iperf.py`
If you like to know, how fast the wireless connection of your Raspberry Pi Pico is, try the `iperf.py` Script. It is able to connect to a configured iPerf3 server. You need to copy `wificonnection.py` and the configured `config.py` first. On the server side you need to start iPerf3 as a server:  
`iperf3 -s`
More Informations about iPerf you can find here:
* https://www.laub-home.de/wiki/IPerf_-_Netzwerkbandbreite_messen

# Installing Logging Library `logging`
for `logging_sample.py` you will need to first install the `logging` Library to your Pico.
So connect the pico to wifi and install the Library with `mip`
in the `logging_sample.py` you will find some examples for logging in different loglevels.

```python
import mip
mip.install('logging')
```

# Measuring execution time with `time_measurement_sample.`
If you like to know how much time a script takes for execution, just use the code in `time_measurement_sample`. Or just play around a bit with that sample script.

# If you like to PING
* Not tested yet
* I am not able to install uping at the moment
* WorkInProgress

enable the wificonnection at first!
```python
import upip
upip.install("micropython-uping")
import uping
# ping to google
uping.ping("google.de")
```

# Links
* https://www.laub-home.de/wiki/Raspberry_pi_pico_w_-_einstieg_mit_micropython
* https://www.laub-home.de/wiki/Raspberry_Pi_Pico_W_DHT22_Temperatur_Sensor
* https://www.laub-home.de/wiki/Raspberry_Pi_Pico_W_BME680_Raumklima_Sensor
* https://www.laub-home.de/wiki/Raspberry_Pi_Pico_W_BH1750_Helligkeitssensor
