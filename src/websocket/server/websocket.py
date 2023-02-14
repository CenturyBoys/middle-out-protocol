from typing import Optional

import websockets
from asyncio import Future
from websockets import WebSocketServer
from src.domain.websocket.subprotocol.model import Subprotocol
from src.domain.websocket.subprotocol.name.model import SubprotocolName


class MiddleOutServer:

    def __init__(self, host: str, port: int):
        self.__host: str = host
        self.__port: int = port
        self.__server_future: Future = Future()
        self.__websocket: Optional[WebSocketServer] = None

    @staticmethod
    async def __handler_connection(websocket: WebSocketServer):
        while True:
            message = await websocket.recv()

    async def start_server(self):
        async with websockets.serve(
                self.__handler_connection,
                host=self.__host,
                port=self.__port,
                create_protocol=Subprotocol,
                select_subprotocol=Subprotocol.subprotocol_callback,
                subprotocols=[SubprotocolName.MIDDLE_OUT.value]) as websocket:
            self.__websocket = websocket
            await self.__server_future
