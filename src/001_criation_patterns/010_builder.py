from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}: ({params})'

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin):
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = None
        self.phone = []
        self.address = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): ...

    @abstractmethod
    def add_name(self, name): ...

    @abstractmethod
    def add_surname(self, surname): ...

    @abstractmethod
    def add_age(self, age): ...

    @abstractmethod
    def add_phone(self, phone): ...

    @abstractmethod
    def add_address(self, address): ...


class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_name(self, name):
        self._result.name = name
        return self

    def add_surname(self, surname):
        self._result.surname = surname
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone(self, phone):
        self._result.phone.append(phone)
        return self

    def add_address(self, address):
        self._result.address.append(address)
        return self


class UserDirector:
    def __init__(self, builder) -> None:
        self._builder: UserBuilder = builder

    def with_age(self, name, surname, age):
        self._builder.add_name(name)\
            .add_surname(surname)\
            .add_age(age)
        return self._builder.result

    def with_address(self, name, surname, address):
        self._builder.add_name(name)\
            .add_surname(surname)\
            .add_address(address)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user1 = user_director.with_age('Caio', 'Romano', 23)
    user2 = user_director.with_address('Vickvi', 'Rabello', 'Rua maracanã')

    print(user1)
    print(user2)
