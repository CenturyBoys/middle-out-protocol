from typing import Callable
from inspect import signature

from src.domain.exception.server.model import RouteFunctionIsNotCallableException, \
    RouteFunctionHasInvalidSignatureException
from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.method.enum import Method as MethodType
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.model import Response


class Method:
    def __init__(self, type: MethodType, route_function: Callable):
        self.__type: MethodType = type
        self.__route_function: Callable = route_function

    @classmethod
    def create(cls, type: MethodType, route_function: Callable):
        is_callable = callable(route_function)
        if not is_callable:
            # TODO: ADD WARNING LOG
            raise RouteFunctionIsNotCallableException()

        route_function_signature = signature(route_function)
        is_valid_return = route_function_signature.return_annotation == Response
        connection = route_function_signature.parameters.get("connection")
        hand_shake = route_function_signature.parameters.get("hand_shake")
        request = route_function_signature.parameters.get("request")

        has_connection = connection is not None
        has_hand_shake = hand_shake is not None
        has_request = request is not None
        has_all_params = all([has_connection, has_hand_shake, has_request])
        is_valid_params = has_all_params and len(route_function_signature.parameters) == 3

        if not is_valid_params or not is_valid_return:
            # TODO: ADD WARNING LOG
            raise RouteFunctionHasInvalidSignatureException()

        is_valid_param_types = all([connection.annotation == Connection, hand_shake.annotation == any, request.annotation == Request])
        if not is_valid_param_types:
            # TODO: ADD WARNING LOG
            raise RouteFunctionHasInvalidSignatureException()

        return cls(type=type, route_function=route_function)

    @property
    def type(self):
        return self.__type

    @property
    def route_function(self):
        return self.__route_function
