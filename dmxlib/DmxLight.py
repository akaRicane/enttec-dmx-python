from dmxlib.DmxChannel import DmxChannel


class DmxLight:

    def __init__(self, start: int = 1, nchannel: int = 4) -> None:
        self.start = start
        self.nchannel = nchannel
        self.channels = []

        for i in range(self.nchannel):
            self.channels.append(DmxChannel(id=(i + start)))

    def setValues(self, values: list[int]) -> None:
        if len(values) != self.nchannel:
            raise ValueError("Mismatch len of input values")
        else:
            for channel, value in zip(self.channels, values):
                channel.setValue(value)
