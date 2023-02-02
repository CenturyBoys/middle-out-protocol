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


class InvalidRequestHeaderException(ServerException):
    def __init__(self, message: str = "Invalid request header sent"):
        self.message: str = message
        self.code = ResponseCode.INVALID_REQUEST_HEADER
        super().__init__(message)


class InvalidRequestRouteException(ServerException):
    def __init__(self, message: str = "Invalid request route sent"):
        self.message: str = message
        self.code = ResponseCode.INVALID_REQUEST_ROUTE
        super().__init__(message)


class RouteFunctionIsNotCallableException(ServerException):
    def __init__(self, message: str = "Route function is not a callable"):
        self.message: str = message
        self.code = ResponseCode.ROUTE_FUNCTION_IS_NOT_CALLABLE
        super().__init__(message)


class RouteFunctionHasInvalidSignatureException(ServerException):
    def __init__(self, message: str = "Route function has a invalid signature"):
        self.message: str = message
        self.code = ResponseCode.ROUTE_FUNCTION_HAS_INVALID_SIGNATURE
        super().__init__(message)
