from dataclasses import dataclass

from src.domain.websocket.request.args.model import Args
from src.domain.websocket.request.header.model import Header
from src.domain.websocket.request.id.model import Id
from src.domain.websocket.request.method.enum import Method
from src.domain.websocket.request.route.model import Route


@dataclass(slots=True)
class Request:
    __id: Id
    __args: Args
    __header: Header
    __route: Route
    __method: Method

    def __init__(self, id: str, args: dict, header: dict, route: str, method: str):
        self.__id = Id.create(id=id)
        self.__args = Args.create(args=args)
        self.__header = Header.create(header=header)
        self.__route = Route.create(route=route)
        self.__method = Method.create(method=method)

    @property
    def id(self):
        return self.__id.id

    @property
    def args(self):
        return self.__args.args

    @property
    def header(self):
        return self.__header.header

    @property
    def route(self):
        return self.__route.route

    @property
    def method(self):
        return self.__method



