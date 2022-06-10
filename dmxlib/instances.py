from dataclasses import dataclass

@dataclass
class DmxValue:
    value: int = 255
    prev: int = 255

    def setValue(self, value):
        self.prev = int(self.value)
        self.value = int(value)
        print(self.value)

    def linearBackAndForth(self):
        copy = int(self.value)
        if self.value == 0:
            self.value = 1
        elif self.value == 255:
            self.value = 254
        elif self.prev < self.value:
            self.value += 1
        else:
            self.value -= 1
        self.prev = copy
        return self.value


