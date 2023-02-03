from typing import Optional

from src.domain.websocket.request.method.enum import MethodType
from src.domain.websocket.router.method.model import Method


class Route:
    def __init__(self, name: str):
        self.__name: str = name
        self.__get_method: Optional[Method] = None
        self.__post_method: Optional[Method] = None
        self.__sub_method: Optional[Method] = None
        self.__unsub_method: Optional[Method] = None

    @classmethod
    def create(cls, name: str):
        return cls(name=name)

    def add_get_method(self, method: Method):
        self.__get_method = method

    def add_post_method(self, method: Method):
        self.__post_method = method

    def add_sub_method(self, method: Method):
        self.__sub_method = method

    def add_unsub_method(self, method: Method):
        self.__unsub_method = method

    def get_method(self, method_type: MethodType):
        method_to_return = None

        if method_type == MethodType.GET:
            method_to_return = self.__get_method

        if method_type == MethodType.POST:
            method_to_return = self.__post_method

        if method_type == MethodType.SUB:
            method_to_return = self.__sub_method

        if method_type == MethodType.UNSUB:
            method_to_return = self.__unsub_method

        return method_to_return

    @property
    def name(self):
        return self.__name
