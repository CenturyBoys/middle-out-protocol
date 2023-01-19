from src.domain.websocket.response.code.enum import ResponseCode


class ServerException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidRequestMethodException(ServerException):
    def __init__(self, message: str = "Invalid request method sent"):
        self.message: str = message
        self.code = ResponseCode.INVALID_REQUEST_METHOD
        super().__init__(message)


class InvalidRequestArgsException(ServerException):
    def __init__(self, message: str = "Invalid request args sent"):
        self.message: str = message
        self.code = ResponseCode.INVALID_REQUEST_ARGS
        super().__init__(message)


class InvalidRequestIdException(ServerException):
    def __init__(self, message: str = "Invalid request id sent"):
        self.message: str = message
        self.code = ResponseCode.INVALID_REQUEST_ID
        super().__init__(message)
