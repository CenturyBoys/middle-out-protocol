from enum import Enum

from src.domain.exception.server.model import InvalidRequestMethodException


class Method(Enum):
    POST = "POST"
    GET = "GET"
    SUB = "SUB"
    UNSUB = "UNSUB"

    @staticmethod
    def validate_method(method: str):
        try:
            upper_case_method = method.upper()
            method = Method[upper_case_method]
        except KeyError as error:
            raise InvalidRequestMethodException("Invalid method send")

        return method
