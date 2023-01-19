from dataclasses import dataclass

from src.domain.websocket.request.args.model import Args
from src.domain.websocket.request.method.enum import Method


@dataclass(slots=True)
class Request:
    __id: str
    __args: Args
    __header: dict
    __route: str
    __method: Method

    def __init__(self, id: str, args: dict, header: dict, route: str, method: str):
        self.__id = id
        self.__args = Args.create(args=args)
        self.__header = header
        self.__route = route
        self.__method = Method.validate_method(method=method)

    @property
    def id(self):
        return self.__id

    @property
    def args(self):
        return self.__args.args

    @property
    def header(self):
        return self.__header

    @property
    def route(self):
        return self.__route

    @property
    def method(self):
        return self.__method



