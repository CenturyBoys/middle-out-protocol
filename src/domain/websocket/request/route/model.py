from dataclasses import dataclass

from src.domain.exception.server.model import InvalidRequestRouteException


@dataclass(slots=True)
class Route:
    __route: str

    @property
    def route(self):
        return self.__route

    @classmethod
    def create(cls, route: str):
        route = cls.validate_route(route=route)
        return cls(route)

    @staticmethod
    def validate_route(route: str):
        is_str_route = type(route) == str
        if not is_str_route:
            raise InvalidRequestRouteException(
                f"Request route {route} is invalid"
            )

        return route
