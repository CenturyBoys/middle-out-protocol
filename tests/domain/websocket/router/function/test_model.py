from unittest.mock import patch

import pytest

from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.model import Response
from src.domain.websocket.router.function.model import Function


@pytest.mark.unit
class TestClass:
    @staticmethod
    def stub_route_function(connection: Connection, hand_shake: any, request: Request) -> Response:
        pass

    def test_should_create_valid_route_function(self):
        function = Function.create(callback=self.stub_route_function)

        is_callable = function.is_callable()
        is_valid_signature = function.is_valid_signature()
        is_valid_return = function.is_valid_return()
        assert is_callable
        assert is_valid_signature
        assert is_valid_return
        assert function.callback == self.stub_route_function
