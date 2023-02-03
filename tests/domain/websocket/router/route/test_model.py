import pytest

from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.method.enum import MethodType as MethodType
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.model import Response
from src.domain.websocket.router.function.model import Function
from src.domain.websocket.router.method.model import Method
from src.domain.websocket.router.route.model import Route


@pytest.mark.unit
class TestClass:

    @staticmethod
    @pytest.fixture(scope="function", autouse=True)
    def route():
        name = '/valid_route/'
        route = Route.create(name=name)
        return route

    @staticmethod
    def stub_callback(connection: Connection, hand_shake: any, request: Request) -> Response:
        pass

    def test_should_create_valid_route(self, route: Route):
        assert route.name == '/valid_route/'

    def test_should_add_get_method(self, route: Route):
        function = Function.create(callback=TestClass.stub_callback)
        method = Method.create(type=MethodType.GET, function=function)
        route.add_get_method(method=method)
        assert route._Route__get_method == method

    def test_should_add_post_method(self, route: Route):
        function = Function.create(callback=TestClass.stub_callback)
        method = Method.create(type=MethodType.POST, function=function)
        route.add_post_method(method=method)
        assert route._Route__post_method == method

    def test_should_add_sub_method(self, route: Route):
        function = Function.create(callback=TestClass.stub_callback)
        method = Method.create(type=MethodType.SUB, function=function)
        route.add_sub_method(method=method)
        assert route._Route__sub_method == method

    def test_should_add_unsub_method(self, route: Route):
        function = Function.create(callback=TestClass.stub_callback)
        method = Method.create(type=MethodType.UNSUB, function=function)
        route.add_unsub_method(method=method)
        assert route._Route__unsub_method == method

    def test_should_get_post_method(self, route: Route):
        function = Function.create(callback=TestClass.stub_callback)
        method = Method.create(type=MethodType.POST, function=function)
        route.add_post_method(method=method)
        post_method = route.get_method(method_type=MethodType.POST)
        assert post_method == method
