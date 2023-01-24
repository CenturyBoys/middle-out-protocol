from websockets import WebSocketServerProtocol

from src.domain.websocket.controller.manager.base import BaseManager
from src.domain.websocket.controller.manager.broadcast.sub.model import BroadCastSubManager
from src.domain.websocket.controller.manager.broadcast.unsub.model import BroadCastUnsubManager
from src.domain.websocket.controller.manager.channel.sub.model import ChannelSubManager
from src.domain.websocket.controller.manager.channel.unsub.model import ChannelUnsubManager
from src.domain.websocket.controller.manager.get.model import GetManager
from src.domain.websocket.controller.manager.post.model import PostManager


class Connection:

    def __init__(self, ws: WebSocketServerProtocol):
        self.__ws = ws
        self.__path = ws.path
        self.__connection_hash = ws.__hash__()
        self.__ip_remote_address = ws.remote_address[0]
        self.__sub_protocol = ws.request_headers["Sec-WebSocket-Protocol"]

        self.__post_manager: BaseManager = PostManager()
        self.__get_manager: BaseManager = GetManager()
        self.__channel_sub_manager: BaseManager = ChannelSubManager()
        self.__channel_unsub_manager: BaseManager = ChannelUnsubManager()
        self.__broadcast_sub_manager: BaseManager = BroadCastSubManager()
        self.__broadcast_unsub_manager: BaseManager = BroadCastUnsubManager()

    @property
    def ws(self):
        return self.__ws

    @property
    def path(self):
        return self.__path

    @property
    def connection_hash(self):
        return self.__connection_hash

    @property
    def ip_remote_address(self):
        return self.__ip_remote_address

    @property
    def sub_protocol(self):
        return self.__sub_protocol

    @property
    def post_manager(self):
        return self.__post_manager

    @property
    def get_manager(self):
        return self.__get_manager

    @property
    def channel_sub_manager(self):
        return self.__channel_sub_manager

    @property
    def channel_unsub_manager(self):
        return self.__channel_unsub_manager

    @property
    def broadcast_sub_manager(self):
        return self.__broadcast_sub_manager

    @property
    def broadcast_unsub_manager(self):
        return self.__broadcast_unsub_manager
