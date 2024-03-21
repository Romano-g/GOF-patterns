from __future__ import annotations
from copy import deepcopy


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}: ({params})'

    def __repr__(self) -> str:
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.addresses: list[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':
    caio = Person('Caio', 'Romano')
    address_caio = Address('Av. Brasil', '250')
    caio.add_address(address_caio)

    esposa_caio = caio.clone()
    esposa_caio.name = 'Vickvi'

    print(caio)
    print(esposa_caio)
