from __future__ import annotations
from abc import ABC, abstractmethod


class BoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None: ...

    @abstractmethod
    def get_price(self) -> float: ...

    def add(self, child: BoxStructure) -> None: ...

    def remove(self, child: BoxStructure) -> None: ...


class Box(BoxStructure):
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: list[BoxStructure] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    camiseta1 = Product('camisa 1', 49.90)
    camiseta2 = Product('camisa 2', 39.90)
    camiseta3 = Product('camisa 3', 29.90)

    caixa_de_camisas = Box('Caixa de camisetas')
    caixa_de_camisas.add(camiseta1)
    caixa_de_camisas.add(camiseta2)
    caixa_de_camisas.add(camiseta3)

    smartphone1 = Product('smartphone 1', 9000)
    smartphone2 = Product('smartphone 2', 11000)

    caixa_smartphone = Box('Caixa de smartphone')
    caixa_smartphone.add(smartphone1)
    caixa_smartphone.add(smartphone2)

    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_de_camisas)
    caixa_grande.add(caixa_smartphone)
    caixa_grande.print_content()

    print('\nValor total:')
    print(caixa_grande.get_price())
