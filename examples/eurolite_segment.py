'''
    6-channel mode for Eurolite PIX-144

    channel | value     | function
    1       | 0 .. 255  | dimmer
    2       | 0 .. 255  | strobe
    3       | 0 .. 255  | red
    4       | 0 .. 255  | green
    5       | 0 .. 255  | blue
    6       | 0 .. 255  | speed (color after color)
'''
import os, sys
import time

sys.path.append(os.getcwd())
from dmxlib.DmxPy import DmxPy

dmx = DmxPy('/dev/tty.usbserial-EN305173')

INTENSITY = 255
LIFETIME = 3

dmx.setChannel(1, INTENSITY)
dmx.setChannel(2, 200)
dmx.setChannel(3, INTENSITY)
dmx.setChannel(4, INTENSITY)
dmx.setChannel(5, INTENSITY)
dmx.setChannel(6, 0)

dmx.render()

time.sleep(LIFETIME)
dmx.blackout()
dmx.render()