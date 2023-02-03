import pytest

from src.domain.websocket.subprotocol.name.model import SubprotocolName


@pytest.mark.unit
class TestClass:

    def test_should_get_array_of_protocols_name(self):
        subprotocols = SubprotocolName.get_subprotocols()
        assert subprotocols == [SubprotocolName.MIDDLE_OUT]
