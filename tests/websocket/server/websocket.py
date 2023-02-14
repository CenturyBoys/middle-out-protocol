import asyncio
from unittest.mock import Mock, AsyncMock

import pytest
from websockets.legacy.server import WebSocketServer

from src.websocket.server.websocket import MiddleOutServer


@pytest.mark.unit
class TestClass:
    @pytest.mark.asyncio
    async def test_should_create_middle_out_server(self):
        server = MiddleOutServer(host="localhost", port=8001)
        try:
            await asyncio.wait_for(server.start_server(), timeout=1)
        except asyncio.TimeoutError:
            pass
        finally:
            assert server._MiddleOutServer__host == "localhost"
            assert server._MiddleOutServer__port == 8001
            assert isinstance(server._MiddleOutServer__websocket, WebSocketServer)
