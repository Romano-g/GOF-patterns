from abc import ABC, abstractmethod


class LuxuryVehicle(ABC):
    @abstractmethod
    def fetch_client(self) -> None: pass


class PopularVehicle(ABC):
    @abstractmethod
    def fetch_client(self) -> None: pass


class LuxuryCarNorthZone(LuxuryVehicle):
    def fetch_client(self) -> None:
        print('O carro de luxo da zona norte está buscando o cliente')


class PopularCarNorthZone(PopularVehicle):
    def fetch_client(self) -> None:
        print('O carro popular da zona norte está buscando o cliente')


class PopularMotorcycleNorthZone(PopularVehicle):
    def fetch_client(self) -> None:
        print('A moto popular da zona norte está buscando o cliente')


class LuxuryMotorcycleNorthZone(LuxuryVehicle):
    def fetch_client(self) -> None:
        print('A moto de luxo da zona norte está buscando o cliente')


class LuxuryCarSouthZone(LuxuryVehicle):
    def fetch_client(self) -> None:
        print('O carro de luxo da zona sul está buscando o cliente')


class PopularCarSouthZone(PopularVehicle):
    def fetch_client(self) -> None:
        print('O carro popular da zona sul está buscando o cliente')


class PopularMotorcycleSouthZone(PopularVehicle):
    def fetch_client(self) -> None:
        print('A moto popular da zona sul está buscando o cliente')


class LuxuryMotorcycleSouthZone(LuxuryVehicle):
    def fetch_client(self) -> None:
        print('A moto de luxo da zona sul está buscando o cliente')


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_luxury_car() -> LuxuryVehicle: ...
    @staticmethod
    @abstractmethod
    def get_popular_car() -> PopularVehicle: ...
    @staticmethod
    @abstractmethod
    def get_luxury_motorcycle() -> LuxuryVehicle: ...
    @staticmethod
    @abstractmethod
    def get_popular_motorcycle() -> PopularVehicle: ...


class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return LuxuryCarNorthZone()

    @staticmethod
    def get_popular_car() -> PopularVehicle:
        return PopularCarNorthZone()

    @staticmethod
    def get_luxury_motorcycle() -> LuxuryVehicle:
        return LuxuryMotorcycleNorthZone()

    @staticmethod
    def get_popular_motorcycle() -> PopularVehicle:
        return PopularMotorcycleNorthZone()


class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return LuxuryCarSouthZone()

    @staticmethod
    def get_popular_car() -> PopularVehicle:
        return PopularCarSouthZone()

    @staticmethod
    def get_luxury_motorcycle() -> LuxuryVehicle:
        return LuxuryMotorcycleSouthZone()

    @staticmethod
    def get_popular_motorcycle() -> PopularVehicle:
        return PopularMotorcycleSouthZone()


class Customer:
    def fetch_client(self):
        for factory in [NorthZoneVehicleFactory(), SouthZoneVehicleFactory()]:
            popular_car = factory.get_popular_car()
            popular_car.fetch_client()

            luxury_car = factory.get_luxury_car()
            luxury_car.fetch_client()

            luxury_motorcycle = factory.get_luxury_motorcycle()
            luxury_motorcycle.fetch_client()

            popular_motorcycle = factory.get_popular_motorcycle()
            popular_motorcycle.fetch_client()


if __name__ == '__main__':
    customer = Customer()
    customer.fetch_client()
