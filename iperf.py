# -*- coding: utf-8 -*-
"""iperf3 Client Script
iperf3 client connects to defined server IP or Name
* you will need to copy also wificonnetion.py and config.py to Pico
"""
import wificonnection
import config
import sys

# Starting Wifi Connection
wificonnection.connect()

# check if uiperf3 module is already installed
try:
    import uiperf3
except ModuleNotFoundError or ImportError:
    print("Module uiperf3 not found, try to install it now...")
    import upip
    upip.install("uiperf3")
    try:
        import uiperf3
    except ModuleNotFoundError or ImportError:
        print("Module uiperf3 still not available... EXIT")
        sys.exit(1)
# Starting Client to iperf3 server
uiperf3.client(config.iperfserver)
