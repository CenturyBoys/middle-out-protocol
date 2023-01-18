class ServerException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidRequestMethodException(ServerException):
    def __init__(self, message: str):
        super().__init__(message)
