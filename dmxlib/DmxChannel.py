from dataclasses import dataclass


@dataclass
class DmxChannel:
    value: int = 255
    id: int = 1

    def setValue(self, value) -> None:
        self.value = value
