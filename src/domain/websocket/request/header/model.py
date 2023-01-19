
from dataclasses import dataclass

from src.domain.exception.server.model import InvalidRequestIdException, InvalidRequestHeaderException


@dataclass(slots=True)
class Header:
    __header: dict

    @property
    def header(self):
        return self.__header

    @classmethod
    def create(cls, header: dict):
        header = cls.validate_header(header=header)
        return cls(header)

    @staticmethod
    def validate_header(header: dict):
        is_dict_header = type(header) == dict
        if not is_dict_header:
            raise InvalidRequestHeaderException(
                f"Request header {header} is invalid"
            )

        return header
