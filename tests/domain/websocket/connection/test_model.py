from unittest.mock import Mock

import pytest

from src.domain.websocket.connection.model import Connection
from src.domain.websocket.controller.manager.model import MethodManager


@pytest.mark.unit
class TestClass:

    @staticmethod
    @pytest.fixture
    def valid_stub_websocket_server_protocol():
        websocket_mocked = Mock()
        websocket_mocked.remote_address = ['127.0.0.1']
        websocket_mocked.path = '/service?token=valid_token'
        websocket_mocked.request_headers = {'Sec-WebSocket-Protocol': 'middle-out-protocol'}
        return websocket_mocked

    @staticmethod
    def test_should_get_a_valid_connection_context_instance(valid_stub_websocket_server_protocol):
        connection_context = Connection(ws=valid_stub_websocket_server_protocol)

        assert connection_context is not None
        assert isinstance(connection_context, Connection)

    @staticmethod
    def test_should_get_a_connection_context_with_websocket_server_attributes(
        valid_stub_websocket_server_protocol
    ):

        connection_context = Connection(ws=valid_stub_websocket_server_protocol)

        assert connection_context is not None
        assert isinstance(connection_context, Connection)
        assert connection_context.path == '/service?token=valid_token'
        assert connection_context.ip_remote_address == '127.0.0.1'
        assert connection_context.sub_protocol == 'middle-out-protocol'
        assert connection_context.connection_hash == valid_stub_websocket_server_protocol.__hash__()

    @staticmethod
    def test_should_get_a_connection_context_with_method_manager(
        valid_stub_websocket_server_protocol
    ):

        connection_context = Connection(ws=valid_stub_websocket_server_protocol)

        assert connection_context is not None
        assert isinstance(connection_context, Connection)
        assert isinstance(connection_context.post_manager, MethodManager)
        assert isinstance(connection_context.get_manager, MethodManager)
        assert isinstance(connection_context.channel_sub_manager, MethodManager)
        assert isinstance(connection_context.channel_unsub_manager, MethodManager)
        assert isinstance(connection_context.broadcast_sub_manager, MethodManager)
        assert isinstance(connection_context.broadcast_unsub_manager, MethodManager)
