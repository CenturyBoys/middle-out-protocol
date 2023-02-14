from unittest.mock import patch

import pytest

from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.method.enum import MethodType as MethodType
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.model import Response
from src.domain.websocket.router.function.model import Function
from src.domain.websocket.router.method.model import Method
from src.domain.websocket.router.route.model import Route
from src.domain.websocket.router.suite.model import Suite


@pytest.mark.unit
class TestClass:

    @staticmethod
    def get_metadata(name: str):
        suite = Suite()
        route = Route.create(name=name)
        return name, suite, suite.get, route, route.add_get_method

    @staticmethod
    def post_metadata(name: str):
        suite = Suite()
        route = Route.create(name=name)
        return name, suite, suite.post, route, route.add_post_method

    @staticmethod
    def sub_metadata(name: str):
        suite = Suite()
        route = Route.create(name=name)
        return name, suite, suite.sub, route, route.add_sub_method

    @staticmethod
    def unsub_metadata(name: str):
        suite = Suite()
        route = Route.create(name=name)
        return name, suite, suite.unsub, route, route.add_unsub_method

    @staticmethod
    def stub_function(
        connection: Connection, hand_shake: any, request: Request
    ) -> Response:
        pass

    @staticmethod
    @pytest.fixture
    def make_route_to_register_metadata(request):
        method_type, name, suite, decorator, route, add_method = request.param

        function = Function.create(callback=TestClass.stub_function)
        method = Method.create(type=method_type, function=function)
        route.add_get_method(method=method)
        suite_element = {name: route}

        return suite_element, function, method, route, suite, decorator

    @pytest.mark.parametrize(
        "make_route_to_register_metadata",
        [
            (MethodType.GET, *get_metadata(name="/values_from_disk")),
            (MethodType.POST, *post_metadata(name="/values_from_disk")),
            (MethodType.SUB, *sub_metadata(name="/values_from_disk")),
            (MethodType.UNSUB, *unsub_metadata(name="/values_from_disk")),
        ],
        indirect=["make_route_to_register_metadata"],
    )
    def test_should_register_method_into_route_suite(
        self, make_route_to_register_metadata
    ):
        (
            suite_element,
            function,
            method,
            route,
            suite,
            decorator,
        ) = make_route_to_register_metadata
        with patch.object(suite, "_Suite__suite") as suite:
            with patch.object(Function, "create", return_value=function):
                with patch.object(Method, "create", return_value=method):
                    with patch.object(Route, "create", return_value=route):
                        register_route_in_suite = decorator("/values_from_disk")
                        register_route_in_suite(self.stub_function)
                        suite.update.assert_called_with(suite_element)
