from storage.base_storage import Storage
from storage.exception import TooManyDifferentProducts


class Shop(Storage):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, amount):
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts

        super().add(name, amount)
