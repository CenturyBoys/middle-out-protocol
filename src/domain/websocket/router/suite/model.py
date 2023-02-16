from typing import Callable

from src.domain.websocket.request.method.enum import MethodType
from src.domain.websocket.router.function.model import Function
from src.domain.websocket.router.method.model import Method
from src.domain.websocket.router.route.model import Route


class Suite:
    def __init__(self):
        self.__suite: dict = {}

    def get(self, name: str):
        def register_suite_element(callback: Callable):
            function = Function.create(callback=callback)
            method = Method.create(method_type=MethodType.GET, function=function)
            route = Route.create(name=name)
            route.add_get_method(method=method)

            suite_element = {name: route}
            self.__suite.update(suite_element)

        return register_suite_element

    def post(self, name: str):
        def register_suite_element(callback: Callable):
            function = Function.create(callback=callback)
            method = Method.create(method_type=MethodType.POST, function=function)
            route = Route.create(name=name)
            route.add_post_method(method=method)

            suite_element = {name: route}
            self.__suite.update(suite_element)

        return register_suite_element

    def sub(self, name: str):
        def register_suite_element(callback: Callable):
            function = Function.create(callback=callback)
            method = Method.create(method_type=MethodType.SUB, function=function)
            route = Route.create(name=name)
            route.add_sub_method(method=method)

            suite_element = {name: route}
            self.__suite.update(suite_element)

        return register_suite_element

    def unsub(self, name: str):
        def register_suite_element(callback: Callable):
            function = Function.create(callback=callback)
            method = Method.create(method_type=MethodType.UNSUB, function=function)
            route = Route.create(name=name)
            route.add_unsub_method(method=method)

            suite_element = {name: route}
            self.__suite.update(suite_element)

        return register_suite_element

    @property
    def suite(self):
        return self.__suite
