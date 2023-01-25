from websockets import WebSocketServerProtocol

from src.domain.websocket.controller.manager.model import MethodManager



class Connection:

    def __init__(self, ws: WebSocketServerProtocol):
        self.__ws = ws
        self.__path = ws.path
        self.__connection_hash = ws.__hash__()
        self.__ip_remote_address = ws.remote_address[0]
        self.__sub_protocol = ws.request_headers["Sec-WebSocket-Protocol"]

        self.__post_manager: MethodManager = MethodManager()
        self.__get_manager: MethodManager = MethodManager()
        self.__channel_sub_manager: MethodManager = MethodManager()
        self.__channel_unsub_manager: MethodManager = MethodManager()
        self.__broadcast_sub_manager: MethodManager = MethodManager()
        self.__broadcast_unsub_manager: MethodManager = MethodManager()

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
