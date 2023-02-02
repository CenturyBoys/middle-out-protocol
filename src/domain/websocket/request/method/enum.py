from enum import Enum

from src.domain.exception.server.model import InvalidRequestMethodException


class Method(Enum):
    POST = "POST"
    GET = "GET"
    SUB = "SUB"
    UNSUB = "UNSUB"

    @staticmethod
    def create(method: str):
        try:
            upper_case_method = method.upper()
            method = Method[upper_case_method]
        except KeyError as error:
            # TODO: Log this error
            raise InvalidRequestMethodException(f"Method {method.upper()} is invalid")

        return method
