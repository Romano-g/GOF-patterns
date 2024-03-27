from __future__ import annotations
from copy import deepcopy


class Memento:
    def __init__(self, state: dict) -> None:
        self._state: dict
        super().__setattr__('_state', state)

    def get_state(self) -> dict:
        return self._state

    def __setattr__(self, name, value) -> None:
        raise AttributeError('Sou imutável')


class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}{self.__dict__}'


class Caretaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: list[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())


if __name__ == '__main__':
    img = ImageEditor('foto1.png', 111, 111)
    caretaker = Caretaker(img)

    caretaker.backup()

    img.name = 'foto2.jpg'
    img.width = 200
    img.height = 200
    caretaker.backup()

    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()

    print(img)
