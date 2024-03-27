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


class WeatherStationFacade:
    def __init__(self) -> None:
        self.weather_station = WeatherStation()

        self.iphone = Smartphone('iPhone', self.weather_station)
        self.samsung = Smartphone('Samsung', self.weather_station)
        self.notebook = Notebook('Sony', self.weather_station)

        self.weather_station.add_observer(self.iphone)
        self.weather_station.add_observer(self.samsung)
        self.weather_station.add_observer(self.notebook)

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver) -> None:
        self.weather_station.remove_observer(observer)

    def change_state(self, state: dict) -> None:
        self.weather_station.state = state

    def remove_smartphone(self) -> None:
        self.weather_station.remove_observer(self.samsung)

    def reset_state(self) -> None:
        self.weather_station.reset_state()


if __name__ == '__main__':
    weather_station = WeatherStationFacade()

    weather_station.change_state({'temperature': '30'})
    weather_station.change_state({'temperature': '32'})
    weather_station.change_state({'temperature': '32', 'humidity': '90%'})

    print()

    weather_station.remove_smartphone()
    weather_station.reset_state()

    print()

    weather_station.change_state({'temperature': '30'})
    weather_station.change_state({'temperature': '32'})
    weather_station.change_state({'temperature': '32', 'humidity': '90%'})
