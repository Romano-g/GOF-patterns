from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self) -> None:
        self.hook_before_add_ingredients()
        self.add_ingredients()
        self.hook_after_add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_add_ingredients(self) -> None: ...

    def hook_after_add_ingredients(self) -> None: ...

    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando pizza.')

    def serve(self):
        print(f'{self.__class__.__name__}: Servindo a pizza')

    @abstractmethod
    def add_ingredients(self) -> None: ...

    @abstractmethod
    def cook(self) -> None: ...


class HomeStylePizza(Pizza):
    def hook_before_add_ingredients(self) -> None:
        print('Preparando mise en place(presunto queijo e orégano)')

    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: Adiciona presunto queijo e oregano')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: Cozinha por 45 min forno a lenha')


class PepperoniPizza(Pizza):
    def add_ingredients(self) -> None:
        print(f'{self.__class__.__name__}: Adiciona peperroni e queijo')

    def hook_after_add_ingredients(self) -> None:
        print('Adicionando geleia de pimenta')

    def cook(self) -> None:
        print(f'{self.__class__.__name__}: Cozinha por 60 min forno comum')


if __name__ == '__main__':
    home_style_pizza = HomeStylePizza()
    pepperoni = PepperoniPizza()

    home_style_pizza.prepare()
    print()
    pepperoni.prepare()
