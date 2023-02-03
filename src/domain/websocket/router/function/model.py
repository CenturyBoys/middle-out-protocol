from inspect import signature
from typing import Callable

from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.model import Response


class Function:
    def __init__(self, callback: Callable):
        self.__callback = callback

    @classmethod
    def create(cls, callback: Callable):
        return cls(callback=callback)

    def is_callable(self):
        # TODO: ADD WARNING LOG
        is_callable = callable(self.__callback)
        return is_callable

    def is_valid_return(self):
        # TODO: ADD WARNING LOG
        callback_signature = signature(self.__callback)
        is_valid_return = callback_signature.return_annotation == Response
        return is_valid_return

    def is_valid_signature(self):
        # TODO: ADD WARNING LOG
        _, connection, hand_shake, request = self.__get_callback_params()

        is_valid_signature = False
        is_valid_params = self.__is_valid_params()

        if is_valid_params:
            is_valid_signature = all(
                [
                    connection.annotation == Connection,
                    hand_shake.annotation == any,
                    request.annotation == Request,
                ]
            )

        return is_valid_params and is_valid_signature

    def __is_valid_params(self):
        callback_signature, connection, hand_shake, request = self.__get_callback_params()

        has_params = all(
            [connection is not None, hand_shake is not None, request is not None]
        )
        has_len_min_params = len(callback_signature.parameters) == 3

        return has_params and has_len_min_params

    def __get_callback_params(self):
        callback_signature = signature(self.__callback)
        connection = callback_signature.parameters.get("connection")
        hand_shake = callback_signature.parameters.get("hand_shake")
        request = callback_signature.parameters.get("request")
        return callback_signature, connection, hand_shake, request

    @property
    def callback(self):
        return self.__callback
