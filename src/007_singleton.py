# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('Executou o Call da meta')
#         return super().__call__(*args, **kwargs)


# class Person(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('Executou o New')
#         return super().__new__(cls)

#     def __init__(self, name):
#         print('Executou o Init')
#         self.name = name

#     def __call__(self, x, y):
#         print('Call chamado', self.name, x + y)


# if __name__ == '__main__':
#     p1 = Person('Caio')
#     p1(2, 2)
#     print(p1.name)


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'Tema escuro'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'Tema claro'
    print(as1.tema)

    as2 = AppSettings()
    print(as1.tema == as2.tema)
