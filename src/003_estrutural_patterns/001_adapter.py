from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: ...

    @abstractmethod
    def right(self) -> None: ...

    @abstractmethod
    def down(self) -> None: ...

    @abstractmethod
    def left(self) -> None: ...


class Control(IControl):
    def top(self) -> None:
        print('Movendo para cima.')

    def right(self) -> None:
        print('Movendo para a direita.')

    def down(self) -> None:
        print('Movendo para baixo.')

    def left(self) -> None:
        print('Movendo para a esquerda.')


class NewControl:
    def move_top(self) -> None:
        print('Movendo para cima.')

    def move_right(self) -> None:
        print('Movendo para a direita.')

    def move_down(self) -> None:
        print('Movendo para baixo.')

    def move_left(self) -> None:
        print('Movendo para a esquerda.')


class ControlAdapterObject:
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()

    def right(self) -> None:
        self.new_control.move_right()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()


class ControlAdapterClass(Control, NewControl):
    def top(self) -> None:
        self.move_top()

    def right(self) -> None:
        self.move_right()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()


if __name__ == '__main__':
    new_control = NewControl()
    c1 = ControlAdapterObject(new_control)
    c2 = ControlAdapterClass()

    c1.top()
    c1.down()
    c1.left()
    c1.right()
    print()
    c2.top()
    c2.down()
    c2.left()
    c2.right()
