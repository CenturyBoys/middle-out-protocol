from unittest.mock import patch

import pytest

from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.method.enum import Method
from src.domain.websocket.request.model import Request
from src.domain.websocket.router.suite.model import RouteSuite


@pytest.mark.unit
class TestClass:

    @staticmethod
    def route_suite_get_decorator():
        route_suite = RouteSuite()
        return route_suite, route_suite.get

    @staticmethod
    def route_suite_post_decorator():
        route_suite = RouteSuite()
        return route_suite, route_suite.post

    @staticmethod
    def route_suite_sub_decorator():
        route_suite = RouteSuite()
        return route_suite, route_suite.sub

    @staticmethod
    def route_suite_unsub_decorator():
        route_suite = RouteSuite()
        return route_suite, route_suite.unsub

    @staticmethod
    def stub_function(connection: Connection, hand_shake: any, request: Request):
        pass

    @staticmethod
    @pytest.fixture
    def make_route_to_register_metadata(request):
        route, method, route_suite, decorator = request.param
        _method = {
            method: TestClass.stub_function
        }
        route_to_register = {route: _method}
        return route_to_register, route_suite, decorator

    @pytest.mark.parametrize(
        'make_route_to_register_metadata',
        [("/values_from_disk", Method.GET, *route_suite_get_decorator()),
         ("/values_from_disk", Method.POST, *route_suite_post_decorator()),
         ("/values_from_disk", Method.SUB, *route_suite_sub_decorator()),
         ("/values_from_disk", Method.UNSUB, *route_suite_unsub_decorator())],
        indirect=["make_route_to_register_metadata"]
    )
    def test_should_register_get_method_into_route_suite(self, make_route_to_register_metadata):
        route_to_register, route_suite, decorator = make_route_to_register_metadata
        with patch.object(route_suite, "_RouteSuite__suite") as suite:
            register_route_in_suite = decorator("/values_from_disk")
            register_route_in_suite(self.stub_function)
            suite.update.assert_called_with(route_to_register)
