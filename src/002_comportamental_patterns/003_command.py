from __future__ import annotations
from abc import ABC, abstractmethod


class Light:
    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'{self.name} do {self.room_name} está ON')

    def off(self) -> None:
        print(f'{self.name} do {self.room_name} está OFF')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'{self.name} do {self.room_name} está',
              self.color)


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None: ...

    @abstractmethod
    def undo(self) -> None: ...


class LightOnCommand(ICommand):
    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColor(ICommand):
    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    def __init__(self) -> None:
        self._buttons: dict[str, ICommand] = {}
        self._operations: list[tuple[str, str]] = []

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_execute(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._operations.append((name, 'execute'))

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._operations.append((name, 'undo'))

    def global_undo(self) -> None:
        if not self._operations:
            return None

        button_name, operation = self._operations[-1]

        if operation == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._operations.pop()


if __name__ == '__main__':
    bedroom_light = Light('Luz', 'Quarto')
    bathroom_light = Light('Luz', 'Banheiro')

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'Azul')
    bedroom_light_red = LightChangeColor(bedroom_light, 'Vermelho')

    remote = RemoteController()
    remote.button_add_command('First Button', bedroom_light_on)
    remote.button_add_command('Second Button', bathroom_light_on)
    remote.button_add_command('Third Button', bedroom_light_blue)
    remote.button_add_command('Fourth Button', bedroom_light_red)

    remote.button_execute('First Button')
    remote.button_undo('First Button')

    remote.button_execute('Second Button')
    remote.button_undo('Second Button')

    remote.button_execute('Third Button')
    remote.button_undo('Third Button')

    remote.button_execute('Fourth Button')
    remote.button_undo('Fourth Button')

    print()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
