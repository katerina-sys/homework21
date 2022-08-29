from storage.base_storage import Storage


class Store(Storage):
    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)