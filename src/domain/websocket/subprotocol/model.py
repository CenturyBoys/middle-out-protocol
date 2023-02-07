from typing import List, Optional, Sequence
from websockets import WebSocketServerProtocol
from websockets.datastructures import Headers
from websockets.headers import (
    parse_subprotocol,
)
from websockets.typing import Subprotocol as WebosockestSubprotocol


class Subprotocol(WebSocketServerProtocol):
    @staticmethod
    def subprotocol_callback(
        client_subprotocols: List[str], server_subprotocols: List[str]
    ):
        selected_subprotocol = server_subprotocols[0]

        for client_subprotocol in client_subprotocols:
            for server_subprotocol in server_subprotocols:
                selected_subprotocol = (
                    client_subprotocol
                    if client_subprotocol == server_subprotocol
                    else server_subprotocol
                )

        return selected_subprotocol

    def process_subprotocol(
        self, headers: Headers, available_subprotocols: Optional[Sequence[WebosockestSubprotocol]]
    ) -> Optional[WebosockestSubprotocol]:
        subprotocol: Optional[Subprotocol] = None

        header_values = headers.get_all("Sec-WebSocket-Protocol")

        if available_subprotocols:
            if not header_values:
                header_values = []

            parsed_header_values: List[Subprotocol] = sum(
                [parse_subprotocol(header_value) for header_value in header_values], []
            )

            subprotocol = self.select_subprotocol(
                parsed_header_values, available_subprotocols
            )

        return subprotocol
