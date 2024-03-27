from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass


@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotato(Ingredient):
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    price: float = 0.99


class Hotdog:
    _name: str
    _ingredients: list[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> list[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}: (R$ {self.price}) -> {self.ingredients}'


class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'Simple Hotdog'
        self._ingredients: list[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks(),
        ]


class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'Special Hotdog'
        self._ingredients: list[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotato(),
            PotatoSticks(),
        ]


class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        self.hotdog = hotdog
        self._ingredient = ingredient

        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'


if __name__ == '__main__':
    simple_hotdog = SimpleHotdog()
    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())
    bacon_egg_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())
    bacon_egg_mashed_simple_hotdog = HotdogDecorator(
        bacon_egg_simple_hotdog, MashedPotato()
    )

    print(simple_hotdog)
    print(f'\n{bacon_simple_hotdog}')
    print(f'\n{bacon_egg_simple_hotdog}')
    print(f'\n{bacon_egg_mashed_simple_hotdog}')
