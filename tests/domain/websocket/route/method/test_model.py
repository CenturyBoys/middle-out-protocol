import pytest

from src.domain.exception.server.model import RouteFunctionIsNotCallableException, \
    RouteFunctionHasInvalidSignatureException
from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.method.enum import Method as MethodType
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.code.enum import ResponseCode
from src.domain.websocket.route.method.model import Method


@pytest.mark.unit
class TestClass:
    @staticmethod
    def stub_route_function(connection: Connection, hand_shake: any, request: Request):
        pass

    @pytest.mark.parametrize(
        "method_type",
        [MethodType.GET, MethodType.POST, MethodType.SUB, MethodType.UNSUB],
    )
    def test_should_create_valid_get_method(self, method_type: MethodType):
        method = Method(type=method_type, route_function=self.stub_route_function)
        assert method.type == method_type
        assert method.route_function == self.stub_route_function

    @pytest.mark.parametrize(
        "method_type",
        [MethodType.GET, MethodType.POST, MethodType.SUB, MethodType.UNSUB],
    )
    def test_should_except_a_invalid_route_function(self, method_type: MethodType):
        with pytest.raises(RouteFunctionIsNotCallableException) as error:
            _ = Method.create(type=method_type, route_function="this_is_not_a_function")

        assert (
                error.value.message
                == "Route function is not a callable"
        )
        assert error.value.code == ResponseCode.ROUTE_FUNCTION_IS_NOT_CALLABLE

    @pytest.mark.parametrize(
        "method_type",
        [MethodType.GET, MethodType.POST, MethodType.SUB, MethodType.UNSUB],
    )
    def test_should_except_a_invalid_route_function_signature(self, method_type: MethodType):
        with pytest.raises(RouteFunctionHasInvalidSignatureException) as error:
            _ = Method.create(type=method_type, route_function=lambda x: x)

        assert (
                error.value.message
                == "Route function has a invalid signature"
        )
        assert error.value.code == ResponseCode.ROUTE_FUNCTION_HAS_INVALID_SIGNATURE

