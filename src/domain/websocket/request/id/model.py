from dataclasses import dataclass

from src.domain.exception.server.model import InvalidRequestIdException


@dataclass(slots=True)
class Id:
    __id: str

    @property
    def id(self):
        return self.__id

    @classmethod
    def create(cls, id: str):
        id = cls.validate_id(id=id)
        return cls(id)

    @staticmethod
    def validate_id(id: str):
        is_str_id = type(id) == str
        if not is_str_id:
            raise InvalidRequestIdException(
                f"Request id {id} is invalid"
            )

        return id
