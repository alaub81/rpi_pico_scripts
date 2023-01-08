# -*- coding: utf-8 -*-
"""Controlling RGB LED with hex code
Small script to use a rgb led connected to the pico.
You can use hexcodes to show different colors
"""

from machine import Pin, PWM
from time import sleep

# Color in RGB-Hexcode (6 characters)
# https://www.rgbtohex.net/rgb/
color = '191970'
# set red,green and blue pins
redPin = 11
greenPin = 12
bluePin = 13

# do the stuff
print('color hexcode:', color)

if (len(color) == 6):
    color_red = int(color[0].strip() + color[1].strip(), 16)
    print('R:', color_red)
    color_green = int(color[2].strip() + color[3].strip(), 16)
    print('G:', color_green)
    color_blue = int(color[4].strip() + color[5].strip(), 16)
    print('B:', color_blue)
else:
    print('wrong colorcode!')
    exit

red = PWM(Pin(redPin))
red.freq(1000)
red.duty_u16(color_red * 256)

green = PWM(Pin(greenPin))
green.freq(1000)
green.duty_u16(color_green * 256)

blue = PWM(Pin(bluePin))
blue.freq(1000)
blue.duty_u16(color_blue * 256)