from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self) -> None: ...

    @abstractmethod
    def decrease_volume(self) -> None: ...

    @abstractmethod
    def power(self) -> None: ...


class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice) -> None:
        self._device = device

    def increase_volume(self) -> None:
        self._device.volume += 10

    def decrease_volume(self) -> None:
        self._device.volume -= 10

    def power(self) -> None:
        self._device.power = not self._device.power


class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: ...

    @volume.setter
    def volume(self, volume: int) -> None: ...

    @property
    @abstractmethod
    def power(self) -> bool: ...

    @power.setter
    def power(self, power: bool) -> None: ...


class TV(IDevice):
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self.power:
            print(f'ERRO: A {self._name} está desligada.')
            return

        if volume > 100:
            return

        if volume < 0:
            return

        self._volume = volume
        print(f'Volume: {self._volume}')

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power

        power_status = 'ligada' if self._power else 'desligada'

        print(f'A {self._name} está {power_status}')


if __name__ == '__main__':
    tv = TV()
    remote = RemoteControl(tv)

    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()

    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()

    remote.power()
    remote.decrease_volume()
