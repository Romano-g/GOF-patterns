from random import choice
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def fetch_client(self) -> None: pass


class LuxuryCar(Vehicle):
    def fetch_client(self) -> None:
        print('O carro de luxo está buscando o cliente')


class PopularCar(Vehicle):
    def fetch_client(self) -> None:
        print('O carro popular está buscando o cliente')


class PopularMotorcycle(Vehicle):
    def fetch_client(self) -> None:
        print('A moto popular está buscando o cliente')


class LuxuryMotorcycle(Vehicle):
    def fetch_client(self) -> None:
        print('A moto de luxo está buscando o cliente')


class VehicleFactory:
    def __init__(self, type) -> None:
        self.vehicle = self.get_vehicle(type)

    @staticmethod
    def get_vehicle(type: str) -> Vehicle:
        if type == 'luxo':
            return LuxuryCar()
        if type == 'popular':
            return PopularCar()
        if type == 'moto':
            return PopularMotorcycle()
        if type == 'mluxo':
            return LuxuryMotorcycle()
        assert 0, 'O carro não existe'

    def fetch_client(self):
        self.vehicle.fetch_client()


if __name__ == '__main__':
    disponible_cars = ['luxo', 'popular', 'moto', 'mluxo']

    for i in range(10):
        car = VehicleFactory(choice(disponible_cars))
        car.fetch_client()
