import pytest

from src.domain.exception.server.model import (
    InvalidRequestMethodException,
    InvalidRequestArgsException,
    InvalidRequestIdException,
    InvalidRequestHeaderException,
    InvalidRequestRouteException,
)
from src.domain.websocket.request.method.enum import Method
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.code.enum import ResponseCode


@pytest.fixture
def valid_sub_request():
    request = Request(
        id="request", args={}, header={}, route="valid_route", method="sub"
    )
    return request


@pytest.fixture
def valid_unsub_request():
    request = Request(
        id="request", args={}, header={}, route="valid_route", method="unsub"
    )
    return request


@pytest.fixture
def valid_post_request():
    request = Request(
        id="request", args={}, header={}, route="valid_route", method="post"
    )
    return request


@pytest.fixture
def valid_get_request():
    request = Request(
        id="request", args={}, header={}, route="valid_route", method="get"
    )
    return request


@pytest.fixture
def request_with_invalid_method():
    with pytest.raises(InvalidRequestMethodException) as error:
        Request(
            id="request",
            args={},
            header={},
            route="valid_route",
            method="invalid_method",
        )
    return error


@pytest.fixture
def request_with_invalid_args():
    with pytest.raises(InvalidRequestArgsException) as error:
        Request(
            id="request",
            args="INVALID_ARGS",
            header={},
            route="valid_route",
            method="sub",
        )
    return error


@pytest.fixture
def request_with_invalid_id():
    with pytest.raises(InvalidRequestIdException) as error:
        Request(id=1234, args={}, header={}, route="valid_route", method="sub")
    return error


@pytest.fixture
def request_with_invalid_header():
    with pytest.raises(InvalidRequestHeaderException) as error:
        Request(
            id="request",
            args={},
            header="INVALID HEADER",
            route="valid_route",
            method="sub",
        )
    return error


@pytest.fixture
def request_with_invalid_route():
    with pytest.raises(InvalidRequestRouteException) as error:
        Request(id="request", args={}, header={}, route=1234, method="sub")
    return error


@pytest.mark.unit
class TestClass:
    @staticmethod
    def test_should_get_a_valid_sub_request_instance(valid_sub_request):
        assert valid_sub_request is not None
        assert isinstance(valid_sub_request, Request) is True

    @staticmethod
    def test_should_get_a_sub_request_with_valid_properties(valid_sub_request):
        assert valid_sub_request is not None
        assert isinstance(valid_sub_request, Request) is True
        assert valid_sub_request.id == "request"
        assert valid_sub_request.args == {}
        assert valid_sub_request.header == {}
        assert valid_sub_request.route == "valid_route"
        assert valid_sub_request.method == Method.SUB

    @staticmethod
    def test_should_get_a_valid_unsub_request_instance(valid_unsub_request):
        assert valid_unsub_request is not None
        assert isinstance(valid_unsub_request, Request) is True

    @staticmethod
    def test_should_get_a_unsub_request_with_valid_properties(valid_unsub_request):
        assert valid_unsub_request is not None
        assert isinstance(valid_unsub_request, Request) is True
        assert valid_unsub_request.id == "request"
        assert valid_unsub_request.args == {}
        assert valid_unsub_request.header == {}
        assert valid_unsub_request.route == "valid_route"
        assert valid_unsub_request.method == Method.UNSUB

    @staticmethod
    def test_should_get_a_valid_post_request_instance(valid_post_request):
        assert valid_post_request is not None
        assert isinstance(valid_post_request, Request) is True

    @staticmethod
    def test_should_get_a_post_request_with_valid_properties(valid_post_request):
        assert valid_post_request is not None
        assert isinstance(valid_post_request, Request) is True
        assert valid_post_request.id == "request"
        assert valid_post_request.args == {}
        assert valid_post_request.header == {}
        assert valid_post_request.route == "valid_route"
        assert valid_post_request.method == Method.POST

    @staticmethod
    def test_should_get_a_valid_get_request_instance(valid_get_request):
        assert valid_get_request is not None
        assert isinstance(valid_get_request, Request) is True

    @staticmethod
    def test_should_get_a_get_request_with_valid_properties(valid_get_request):
        assert valid_get_request is not None
        assert isinstance(valid_get_request, Request) is True
        assert valid_get_request.id == "request"
        assert valid_get_request.args == {}
        assert valid_get_request.header == {}
        assert valid_get_request.route == "valid_route"
        assert valid_get_request.method == Method.GET

    @staticmethod
    def test_should_except_a_invalid_request_method_exception(
        request_with_invalid_method,
    ):
        assert (
            request_with_invalid_method.value.args[0]
            == "Method INVALID_METHOD is invalid"
        )

    @staticmethod
    def test_should_except_a_invalid_request_method_exception_with_response_code(
        request_with_invalid_method,
    ):
        assert (
            request_with_invalid_method.value.message
            == "Method INVALID_METHOD is invalid"
        )
        assert (
            request_with_invalid_method.value.code
            == ResponseCode.INVALID_REQUEST_METHOD
        )

    @staticmethod
    def test_should_except_a_invalid_request_args_exception_with_response_code(
        request_with_invalid_args,
    ):
        assert (
            request_with_invalid_args.value.message
            == "Request args INVALID_ARGS is invalid"
        )
        assert request_with_invalid_args.value.code == ResponseCode.INVALID_REQUEST_ARGS

    @staticmethod
    def test_should_except_a_invalid_request_id_exception_with_response_code(
        request_with_invalid_id,
    ):
        assert request_with_invalid_id.value.message == "Request id 1234 is invalid"
        assert request_with_invalid_id.value.code == ResponseCode.INVALID_REQUEST_ID

    @staticmethod
    def test_should_except_a_invalid_request_header_exception_with_response_code(
        request_with_invalid_header,
    ):
        assert (
            request_with_invalid_header.value.message
            == "Request header INVALID HEADER is invalid"
        )
        assert (
            request_with_invalid_header.value.code
            == ResponseCode.INVALID_REQUEST_HEADER
        )

    @staticmethod
    def test_should_except_a_invalid_request_route_exception_with_response_code(
        request_with_invalid_route,
    ):
        assert (
            request_with_invalid_route.value.message == "Request route 1234 is invalid"
        )
        assert (
            request_with_invalid_route.value.code == ResponseCode.INVALID_REQUEST_ROUTE
        )
