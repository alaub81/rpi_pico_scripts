# Raspberry Pi Pico MicroPython Script collection
That is a collection of all my Raspberry Pi Pico MicroPython Scripts.

* First Steps with Pico LED and Pico's Temperature sensor.
* Managing the Wifi connection
* Using Pico as Wifi Access Point
* Reading from a DHT22 Sensor
* first Steps with MQTT
* Sending Sensor Data to MQTT Broker

You will find a short Description of the Scripts on the top of each script.

If you need support or have questions, just open up an issue, or contact me directly.

# Configuration File `config.py`
most of the Scripts here are using for configuration the `config.py` file.  
There you will configure all the variables which are used in the other python scripts. 
For example wificonnnection scripts. SSID and Password is configured in the `config.py`.
Just copy the `config-sample.py` to `config.py`, configure it with your needs and then upload it to your Pico.

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

# Installing umqtt.simple2 or umqtt.robust2
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



