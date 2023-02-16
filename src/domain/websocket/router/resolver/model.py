import loglifos

from src.core.websocket.controller.base.interface import BaseController
from src.domain.websocket.router.route.model import Route


class Resolver:
    def __init__(self, route: Route, controller: BaseController):
        self.__route: Route = route
        self.__controller: BaseController = controller

    async def __call__(self):
        try:
            await self.__controller.on_request(route=self.__route)
        except IndexError as error:
            loglifos.error(
                msg="Error when resolve request",
                error=error,
                route_name=self.__route.name,
                method_type=self.__route.get_method().type.value,
            )
        except Exception as error:  # pylint: disable=broad-exception-caught
            loglifos.error(
                msg="Error when resolve request",
                error=error,
                route_name=self.__route.name,
                method_type=self.__route.get_method().type.value,
            )
