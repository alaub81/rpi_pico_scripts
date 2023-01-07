# -*- coding: utf-8 -*-
"""Logging Simple test Script
a simple script to play around with MicroPython-Logging
to install micropython-logging just connect to wifi and then
# import mip
# mip.install('logging')
"""

import logging

# Define loglevel ERROR, WARNING, INFO, DEBUG
loglevel = logging.DEBUG

#logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
logging.basicConfig(format='%(levelname)s: %(message)s', level=loglevel)

# Log Message Samples
logging.debug('Here you have some information for debugging.')
logging.info('Everything is normal. Relax!')
logging.warning('Something unexpected but not important happend.')
logging.error('Something unexpected and important happened.')
logging.critical('OMG!!! A critical error happend and the code cannot run!')

numbervariable = 23.456
stringvariable = "testing"

logging.info('testing vars %.1f %s', numbervariable, stringvariable)
logging.info('Info test logging %f', numbervariable)
logging.debug('Debug test logging %s', stringvariable)