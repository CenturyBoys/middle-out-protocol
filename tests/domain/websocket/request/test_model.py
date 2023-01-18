import pytest

from src.domain.exception.server.model import InvalidRequestMethodException
from src.domain.websocket.request.method.enum import Method
from src.domain.websocket.request.model import Request


@pytest.fixture
def valid_sub_request():
    request = Request(id="request", args={}, header={}, route="valid_route", method="sub")
    return request


@pytest.fixture
def valid_unsub_request():
    request = Request(id="request", args={}, header={}, route="valid_route", method="unsub")
    return request


@pytest.fixture
def valid_post_request():
    request = Request(id="request", args={}, header={}, route="valid_route", method="post")
    return request


@pytest.fixture
def valid_get_request():
    request = Request(id="request", args={}, header={}, route="valid_route", method="get")
    return request


@pytest.fixture
def request_with_invalid_method():
    with pytest.raises(InvalidRequestMethodException) as error:
        Request(id="request", args={}, header={}, route="valid_route", method="invalid_method")
    return error


def test_should_get_a_valid_sub_request_instance(valid_sub_request):
    assert valid_sub_request is not None
    assert isinstance(valid_sub_request, Request) is True


def test_should_get_a_sub_request_with_valid_properties(valid_sub_request):
    assert valid_sub_request is not None
    assert isinstance(valid_sub_request, Request) is True
    assert valid_sub_request.id == "request"
    assert valid_sub_request.args == {}
    assert valid_sub_request.header == {}
    assert valid_sub_request.route == "valid_route"
    assert valid_sub_request.method == Method.SUB


def test_should_get_a_valid_unsub_request_instance(valid_unsub_request):
    assert valid_unsub_request is not None
    assert isinstance(valid_unsub_request, Request) is True


def test_should_get_a_unsub_request_with_valid_properties(valid_unsub_request):
    assert valid_unsub_request is not None
    assert isinstance(valid_unsub_request, Request) is True
    assert valid_unsub_request.id == "request"
    assert valid_unsub_request.args == {}
    assert valid_unsub_request.header == {}
    assert valid_unsub_request.route == "valid_route"
    assert valid_unsub_request.method == Method.UNSUB


def test_should_get_a_valid_post_request_instance(valid_post_request):
    assert valid_post_request is not None
    assert isinstance(valid_post_request, Request) is True


def test_should_get_a_post_request_with_valid_properties(valid_post_request):
    assert valid_post_request is not None
    assert isinstance(valid_post_request, Request) is True
    assert valid_post_request.id == "request"
    assert valid_post_request.args == {}
    assert valid_post_request.header == {}
    assert valid_post_request.route == "valid_route"
    assert valid_post_request.method == Method.POST


def test_should_get_a_valid_get_request_instance(valid_get_request):
    assert valid_get_request is not None
    assert isinstance(valid_get_request, Request) is True


def test_should_get_a_get_request_with_valid_properties(valid_get_request):
    assert valid_get_request is not None
    assert isinstance(valid_get_request, Request) is True
    assert valid_get_request.id == "request"
    assert valid_get_request.args == {}
    assert valid_get_request.header == {}
    assert valid_get_request.route == "valid_route"
    assert valid_get_request.method == Method.GET


def test_should_except_a_invalid_request_method_exception(request_with_invalid_method):
    assert request_with_invalid_method.value.args[0] == "Invalid method send"


