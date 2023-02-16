from src.domain.exception.server.model import (
    RouteFunctionIsNotCallableException,
    RouteFunctionHasInvalidSignatureException,
)
from src.domain.websocket.request.method.enum import MethodType
from src.domain.websocket.router.function.model import Function


class Method:
    def __init__(self, method_type: MethodType, function: Function):
        self.__type: MethodType = method_type
        self.__function: Function = function

    @classmethod
    def create(cls, method_type: MethodType, function: Function):
        if not function.is_callable():
            raise RouteFunctionIsNotCallableException()

        if not function.is_valid_return() or not function.is_valid_signature():
            raise RouteFunctionHasInvalidSignatureException()

        return cls(method_type=method_type, function=function)

    @property
    def type(self):
        return self.__type

    @property
    def function(self):
        return self.__function
