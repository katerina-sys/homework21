from storage.courier import Courier
from storage.exception import InvalidRequest, BaseError
from storage.request import Request
from storage.shop import Shop
from storage.store import Store

store = Store(items={
    "печеньки": 25,
    "собачка": 25,
    "елка": 25
})

shop = Shop(items={
    "печеньки": 2,
    "собачка": 2,
    "елка": 2
})

storages = {
    "магазин": shop,
    "склад": store
}


def main():
    print('\nДобрый день!\n')

    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}\n {storages[storage_name].get_items()}')

        user_input = input(
            "Введите товар, который хотите приобрести в таком формате: Доставить 3 печеньки из склад в магазин.\n"
            "Введите слово 'стоп' или 'stop', если хотите закончить покупку:\n"
        )
        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request=user_input)
        except InvalidRequest as error:
            print(error.message)
            continue

        courier = Courier(
            request=request,
            storages=storages
        )
        try:
            courier.move()
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
