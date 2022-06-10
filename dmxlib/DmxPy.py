"""
    full credits to: https://github.com/davepaul0/DmxPy

    MIT License

    Copyright (c) 2018 L Trevor Davies

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

"""
import serial, sys, time


DMXOPEN = bytes([126])
DMXCLOSE = bytes([231])
DMXINTENSITY = bytes([6]) + bytes([1]) + bytes([2])				
DMXINIT1 = bytes([3]) + bytes([2]) + bytes([0]) + bytes([0]) + bytes([0])
DMXINIT2 = bytes([10]) + bytes([2]) + bytes([0]) + bytes([0]) + bytes([0])


class DmxPy:
    def __init__(self, serialPort):
        try:
            self.serial = serial.Serial(serialPort, baudrate=57600)
        except:
            print("Error: could not open Serial Port")
            sys.exit(0)
        self.serial.write(DMXOPEN + DMXINIT1 + DMXCLOSE)
        self.serial.write(DMXOPEN + DMXINIT2 + DMXCLOSE)
        
        self.dmxData = [bytes([0])] * 513   #128 plus "spacer".

    def setChannel(self, chan, intensity):
        if chan > 512: chan = 512
        if chan < 0: chan = 0
        if intensity > 255: intensity = 255
        if intensity < 0: intensity = 0
        self.dmxData[chan] = bytes([intensity])

    def blackout(self):
        for i in range(1, 512, 1):
            self.dmxData[i] = bytes([0])

    def render(self):
        sdata = b''.join(self.dmxData)
        self.serial.write(DMXOPEN + DMXINTENSITY + sdata + DMXCLOSE)
