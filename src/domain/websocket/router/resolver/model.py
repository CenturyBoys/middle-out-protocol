from src.core.websocket.controller.base.interface import BaseController
from src.domain.websocket.router.route.model import Route


class Resolver:
    def __init__(self, route: Route, controller: BaseController):
        self.__route: Route = route
        self.__controller: BaseController = controller

    def resolve_request(self):
        pass

    @property
    def route(self):
        return self.__route

    @property
    def controller(self):
        return self.__controller
