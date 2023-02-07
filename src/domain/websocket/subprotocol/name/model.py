from enum import Enum


class SubprotocolName(Enum):
    MIDDLE_OUT = "middle-out-protocol"

    @classmethod
    def get_subprotocols(cls):
        return [cls.MIDDLE_OUT]
