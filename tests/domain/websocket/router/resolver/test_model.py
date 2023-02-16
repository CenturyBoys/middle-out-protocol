from unittest.mock import patch, Mock, AsyncMock

import pytest

from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.method.enum import MethodType
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.model import Response
from src.domain.websocket.router.function.model import Function
from src.domain.websocket.router.method.model import Method
from src.domain.websocket.router.route.model import Route
from src.domain.websocket.router.resolver.model import Resolver
from src.websocket.controller.get.websocket import GetController


@pytest.mark.unit
class TestClass:
    @staticmethod
    def error_side_effect(route: Route):
        raise Exception()

    @staticmethod
    def stub_function(
        connection: Connection, hand_shake: any, request: Request
    ) -> Response:
        pass

    def test_should_create_get_resolver(self):
        resolver = Resolver(route=Route.create(name="name"), controller=GetController())

        assert isinstance(resolver._Resolver__route, Route)
        assert isinstance(resolver._Resolver__controller, GetController)

    @pytest.mark.asyncio
    async def test_should_call_valid_resolver(self):
        mocked_controller = AsyncMock()
        route = Route.create(name="name")
        await Resolver(route=route, controller=mocked_controller)()

        mocked_controller.on_request.assert_called_with(route=route)

    @pytest.mark.asyncio
    async def test_should_call_valid_resolver_with_error_side_effect(self):
        with patch("loglifos.error") as mocked_error_log:
            mocked_controller = AsyncMock()
            mocked_controller.on_request.side_effect = self.error_side_effect

            function = Function.create(callback=TestClass.stub_function)
            method = Method.create(method_type=MethodType.GET, function=function)
            route = Route.create(name="name")
            route.add_get_method(method=method)

            await Resolver(route=route, controller=mocked_controller)()
            mocked_error_log.assert_called_once()
