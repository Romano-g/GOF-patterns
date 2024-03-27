from collections.abc import Iterable, Iterator


class MyIterator(Iterator):
    def __init__(self, collection) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection) -> None:
        self._collection = collection
        self._index = -1

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self) -> None:
        self._items: list = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value) -> None:
        self._items.append(value)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}{self._items}'


if __name__ == '__main__':
    my_list = MyList()
    my_list.add('Caio')
    my_list.add('Vickvi')
    my_list.add('Tutu')

    # print(my_list)

    for value in my_list:
        print(value)

    print()

    for value in my_list.reverse_iterator():
        print(value)
