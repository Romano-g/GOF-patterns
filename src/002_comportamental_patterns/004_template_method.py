from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self): ...

    def base_class_method(self):
        print('Classe abstrata!')

    @abstractmethod
    def operation1(self): ...

    @abstractmethod
    def operation2(self): ...


class ConcreteClass(Abstract):
    def hook(self):
        print('Utilizando o hook')

    def operation1(self):
        print('Operação 1 concluída')

    def operation2(self):
        print('Operação 2 concluída')


class ConcreteClass2(Abstract):
    def operation1(self):
        print('Operação 1 incompleta')

    def operation2(self):
        print('Operação 2 incompleta')


if __name__ == '__main__':
    c1 = ConcreteClass()
    c2 = ConcreteClass2()

    c1.template_method()
    print()
    c2.template_method()
