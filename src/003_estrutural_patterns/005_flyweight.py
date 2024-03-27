from __future__ import annotations


class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: list = []

        self.address_number: str
        self.address_detail: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_detail)


class Address:
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            self._street, address_number, self._neighborhood, address_details,
            self._zip_code,
        )


class AddressFactory:
    _addresses: dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self, **kwargs):
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('Usando objeto já criado.')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto.')

        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av. Brasil',
        neighborhood='Centro',
        zip_code='000000-00'
    )

    a2 = address_factory.get_address(
        street='Av. Brasil',
        neighborhood='Centro',
        zip_code='000000-00'
    )

    a3 = address_factory.get_address(
        street='Av. Brasil',
        neighborhood='Centro',
        zip_code='000000-00'
    )

    print()

    caio = Client('Caio')
    caio.address_number = '35'
    caio.address_detail = 'Casa'
    caio.add_address(a1)
    caio.list_addresses()

    print()

    vickvi = Client('Vickvi')
    vickvi.address_number = '350A'
    vickvi.address_detail = 'Trabalho'
    vickvi.add_address(a2)
    vickvi.list_addresses()
