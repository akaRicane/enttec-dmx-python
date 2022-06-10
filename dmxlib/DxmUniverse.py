import time
from random import randint

from dmxlib.DmxPy import DmxPy
from dmxlib.DmxLight import DmxLight


class DmxUniverse:

    # ----------------------------------- CORE ----------------------------------- #
    def __init__(self, serialPort: str) -> None:
        self.dmx = DmxPy(serialPort=serialPort)
        self.lights = []

    def addLight(self, start: int = 1, nchannel: int = 4) -> None:
        self.lights.append(DmxLight(start=start, nchannel=nchannel))

    def setValuesOfLight(self, lightIndex: int, values: list[int]) -> None:
        self.lights[lightIndex].setValues(values)

    def render(self, duration: float = 1.0) -> None:
        for light in self.lights:
            for channel in light.channels:
                idx = channel.id
                value = channel.value
                self.dmx.setChannel(idx, value)
        self.dmx.render()
        time.sleep(duration)

    def closeSession(self) -> None:
        time.sleep(0.1)
        self.dmx.blackout()
        self.dmx.render()

    # ----------------------------- CUSTOM FUNCTIONS ----------------------------- #
    def crazyRandom(self, dimming = 255) -> None:
        self.dmx.setChannel(1, dimming)
        self.dmx.setChannel(2, randint(0, 255))
        self.dmx.setChannel(3, randint(0, 255))
        self.dmx.setChannel(4, randint(0, 255))