from src.domain.websocket.response.code.enum import ResponseCode


class ServerException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidRequestMethodException(ServerException):
    def __init__(self, message: str = "Invalid method send"):
        self.message: str = message
        self.code = ResponseCode.INVALID_METHOD
        super().__init__(message)
