# -*- coding: utf-8 -*-
"""Logging Simple test Script
a simple script to play around with MicroPython-Logging
to install micropython-logging just connect to wifi and then
# import upip
# upip.install('micropython-logging')
"""

import logging

numbervariable = 23.456
stringvariable = "testing"

# Define loglevel ERROR, WARNING, INFO, DEBUG
loglevel = logging.DEBUG

#logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
logging.basicConfig(level=loglevel)

# Info Messages
logging.info('testing vars %.1f %s', numbervariable, stringvariable)
logging.info('Info test logging %f', numbervariable)
# Debug Message
logging.debug('Debug test logging %s', stringvariable)