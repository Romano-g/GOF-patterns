class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}: ({params})'

    def __repr__(self) -> str:
        return self.__str__()


class MonoState(StringReprMixin):
    _state: dict = {}

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state

        return obj

    def __init__(self, name=None, surname=None) -> None:
        if name is not None:
            self.name = name

        if surname is not None:
            self.surname = surname


class A(MonoState):
    pass


if __name__ == '__main__':
    m1 = MonoState(name='Vickvi')
    m2 = MonoState(surname='Romano')
    a1 = A()

    print('m1:', m1)
    print('m2:', m2)
    print('a1:', a1)
