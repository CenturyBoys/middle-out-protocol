from enum import Enum


class ResponseCode(Enum):
    # RANGE: 0 TO 1000
    INVALID_REQUEST_METHOD = 0
    INVALID_REQUEST_ARGS = 1
    INVALID_REQUEST_ID = 2
    INVALID_REQUEST_HEADER = 2
