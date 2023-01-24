from unittest.mock import Mock

import pytest

from src.domain.websocket.connection.model import Connection
from src.domain.websocket.controller.manager.base import BaseManager
from src.domain.websocket.controller.manager.broadcast.sub.model import BroadCastSubManager
from src.domain.websocket.controller.manager.broadcast.unsub.model import BroadCastUnsubManager
from src.domain.websocket.controller.manager.channel.sub.model import ChannelSubManager
from src.domain.websocket.controller.manager.channel.unsub.model import ChannelUnsubManager
from src.domain.websocket.controller.manager.get.model import GetManager
from src.domain.websocket.controller.manager.post.model import PostManager


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
        assert isinstance(connection_context.post_manager, PostManager)
        assert isinstance(connection_context.get_manager, GetManager)
        assert isinstance(connection_context.channel_sub_manager, ChannelSubManager)
        assert isinstance(connection_context.channel_unsub_manager, ChannelUnsubManager)
        assert isinstance(connection_context.broadcast_sub_manager, BroadCastSubManager)
        assert isinstance(connection_context.broadcast_unsub_manager, BroadCastUnsubManager)

    @staticmethod
    def test_should_get_a_connection_context_with_method_manager_with_base_manager(
        valid_stub_websocket_server_protocol
    ):

        connection_context = Connection(ws=valid_stub_websocket_server_protocol)

        assert connection_context is not None
        assert isinstance(connection_context, Connection)
        assert issubclass(type(connection_context.post_manager), BaseManager)
        assert issubclass(type(connection_context.get_manager), BaseManager)
        assert issubclass(type(connection_context.channel_sub_manager), BaseManager)
        assert issubclass(type(connection_context.channel_unsub_manager), BaseManager)
        assert issubclass(type(connection_context.broadcast_sub_manager), BaseManager)
        assert issubclass(type(connection_context.broadcast_unsub_manager), BaseManager)
