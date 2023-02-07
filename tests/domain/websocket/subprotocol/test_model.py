import pytest

from src.domain.websocket.subprotocol.model import Subprotocol
from src.domain.websocket.subprotocol.name.model import SubprotocolName


@pytest.mark.unit
class TestClass:
    @staticmethod
    def test_should_get_default_protocol():
        client_subprotocols = ["NO_REGISTER_PROTOCOL"]
        server_subprotocols = [SubprotocolName.MIDDLE_OUT.name]
        selected_subprotocol = Subprotocol.subprotocol_callback(
            client_subprotocols=client_subprotocols,
            server_subprotocols=server_subprotocols,
        )

        assert selected_subprotocol == SubprotocolName.MIDDLE_OUT.name

    def test_should_get_client_sent_protocol(self):
        client_subprotocols = ["A", "B"]
        server_subprotocols = ["B", "A"]
        selected_subprotocol = Subprotocol.subprotocol_callback(
            client_subprotocols=client_subprotocols,
            server_subprotocols=server_subprotocols,
        )

        assert selected_subprotocol == client_subprotocols[0]
