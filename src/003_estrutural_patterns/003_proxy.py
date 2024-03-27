from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep


class IUser(ABC):
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> list[dict]: ...

    @abstractmethod
    def get_all_user_data(self) -> dict: ...


class RealUser(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> list[dict]:
        sleep(2)
        return [
            {'rua': 'Av. Brasil', 'numero': 500},
        ]

    def get_all_user_data(self) -> dict:
        sleep(2)
        return {
            'CPF': '111.111.111-11',
            'RG': '11.111.111-1',
        }


class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self._real_user: RealUser

        self._cached_addresses: list[dict]
        self._all_user_data: dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> list[dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == '__main__':
    caio = UserProxy('Caio', 'Romano')

    print(caio.firstname, caio.lastname)

    # print(caio.get_all_user_data())
    # print(caio.get_addresses())
    print()
    print('CACHED DATA:')

    for i in range(10):
        print(caio.get_all_user_data())
        print(caio.get_addresses())
