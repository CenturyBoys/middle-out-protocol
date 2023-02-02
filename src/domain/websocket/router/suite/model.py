from src.domain.websocket.request.method.enum import Method


class RouteSuite:
    def __init__(self):
        self.__suite: dict = {}

    def get(self, route: str):
        def register_route_in_suite(route_function):
            method = {
                Method.GET: route_function
            }
            route_to_register = {route: method}
            self.__suite.update(route_to_register)
        return register_route_in_suite

    def post(self, route: str):
        def register_route_in_suite(route_function):
            method = {
                Method.POST: route_function
            }
            route_to_register = {route: method}
            self.__suite.update(route_to_register)
        return register_route_in_suite

    def sub(self, route: str):
        def register_route_in_suite(route_function):
            method = {
                Method.SUB: route_function
            }
            route_to_register = {route: method}
            self.__suite.update(route_to_register)
        return register_route_in_suite

    def unsub(self, route: str):
        def register_route_in_suite(route_function):
            method = {
                Method.UNSUB: route_function
            }
            route_to_register = {route: method}
            self.__suite.update(route_to_register)
        return register_route_in_suite
