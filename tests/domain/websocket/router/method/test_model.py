import pytest

from src.domain.exception.server.model import (
    RouteFunctionIsNotCallableException,
    RouteFunctionHasInvalidSignatureException,
)
from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.method.enum import MethodType
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.code.enum import ResponseCode
from src.domain.websocket.response.model import Response
from src.domain.websocket.router.function.model import Function
from src.domain.websocket.router.method.model import Method


@pytest.mark.unit
class TestClass:
    @staticmethod
    def stub_route_function(
        connection: Connection, hand_shake: any, request: Request
    ) -> Response:
        pass

    @staticmethod
    @pytest.fixture
    def function(request):
        callback = request
        return Function.create(callback=TestClass.stub_route_function)

    @pytest.mark.parametrize(
        "method_type",
        [MethodType.GET, MethodType.POST, MethodType.SUB, MethodType.UNSUB],
    )
    def test_should_create_valid_method(
        self, method_type: MethodType, function: Function
    ):
        method = Method.create(method_type=method_type, function=function)
        assert method.type == method_type
        assert method.function == function

    @pytest.mark.parametrize(
        "method_type",
        [MethodType.GET, MethodType.POST, MethodType.SUB, MethodType.UNSUB],
    )
    def test_should_except_a_route_function_is_not_callable(
        self, method_type: MethodType
    ):
        with pytest.raises(RouteFunctionIsNotCallableException) as error:
            _ = Method.create(
                method_type=method_type,
                function=Function.create(callback="not_callable"),
            )

        assert error.value.message == "Route function is not a callable"
        assert error.value.code == ResponseCode.ROUTE_FUNCTION_IS_NOT_CALLABLE

    @pytest.mark.parametrize(
        "method_type",
        [MethodType.GET, MethodType.POST, MethodType.SUB, MethodType.UNSUB],
    )
    def test_should_except_a_invalid_route_function_signature(
        self, method_type: MethodType
    ):
        with pytest.raises(RouteFunctionHasInvalidSignatureException) as error:
            _ = Method.create(
                method_type=method_type, function=Function.create(callback=lambda x: x)
            )

        assert error.value.message == "Route function has a invalid signature"
        assert error.value.code == ResponseCode.ROUTE_FUNCTION_HAS_INVALID_SIGNATURE
