from __future__ import annotations
from abc import ABC, abstractmethod


class IObservable(ABC):
    @property
    @abstractmethod
    def state(self): ...

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: ...

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: ...

    @abstractmethod
    def notify_observers(self) -> None: ...


class WeatherStation(IObservable):
    def __init__(self) -> None:
        self._observers: list[IObserver] = []
        self._state: dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: dict) -> None:
        new_state: dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: ...


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(
            f'{self.name}, o objeto {observable_name} foi atualizado =>',
            f'{self.observable.state}'
        )


class Notebook(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def show(self):
        print(f'Sou o {self.name}, os dados são => {self.observable.state}')

    def update(self) -> None:
        self.show()


if __name__ == '__main__':
    weather_station = WeatherStation()

    iphone = Smartphone('iPhone', weather_station)
    samsung = Smartphone('Samsung', weather_station)
    notebook = Notebook('Sony', weather_station)

    weather_station.add_observer(iphone)
    weather_station.add_observer(samsung)
    weather_station.add_observer(notebook)

    weather_station.state = {'temperature': '30'}
    weather_station.state = {'temperature': '30'}
    print()
    weather_station.state = {'temperature': '32', 'humidity': '90%'}
    print()

    weather_station.remove_observer(samsung)
    weather_station.reset_state()
