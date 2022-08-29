from storage.exception import InvalidRequest


class Request:

    def __init__(self, request):
        double_request = request.lower().split(' ')

        if len(double_request) != 7:
            raise InvalidRequest

        self.amount = int(double_request[1])
        self.product = double_request[2]
        self.from_storage = double_request[4]
        self.to_store = double_request[6]
