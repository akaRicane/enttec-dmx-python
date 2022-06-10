'''
    3-channel mode for Stairville LED Flood Panel 150

    channel | value     | function
    1       | 0 .. 255  | red
    2       | 0 .. 255  | green
    3       | 0 .. 255  | blue
'''
import os, sys
import time

sys.path.append(os.getcwd())
from dmxlib.DmxPy import DmxPy

dmx = DmxPy('/dev/tty.usbserial-EN305173')

INTENSITY = 200
LIFETIME = 2

dmx.setChannel(1, INTENSITY)
dmx.setChannel(2, INTENSITY)
dmx.setChannel(3, INTENSITY)

dmx.render()

time.sleep(LIFETIME)
dmx.blackout()
dmx.render()