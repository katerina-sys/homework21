from storage.abstract_method import AbstractStorage
from storage.exception import NotEnoughSpace, NotEnoughProduct


class Storage(AbstractStorage):

    def __init__(self, items, capacity):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, amount):
        """
        увеличивает запас items
        """
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        if name in self.__items:
            self.__items[name] += amount
        else:
            self.__items[name] = amount

    def remove(self, name, amount):
        """
        уменьшает запас items
        """
        if self.__items[name] < amount:
            raise NotEnoughProduct
        self.__items[name] -= amount
        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self):
        """
        вернуть количество свободных мест
        :return:
        """
        free_space = 0
        for value in self.__items.values():
            free_space += value

        return self.__capacity - free_space

    def get_items(self):
        """
        Возвращаем весь товар
        :return:
        """
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items)
