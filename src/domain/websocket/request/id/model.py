from dataclasses import dataclass

from src.domain.exception.server.model import InvalidRequestIdException


@dataclass(slots=True)
class Id:
    __id: str

    # pylint: disable=redefined-builtin, invalid-name
    @property
    def id(self):
        return self.__id

    @classmethod
    def create(cls, id: str):
        id = cls.validate_id(id=id)
        return cls(id)

    @staticmethod
    def validate_id(id: str):
        if not isinstance(id, str):
            raise InvalidRequestIdException(f"Request id {id} is invalid")

        return id

    # pylint: enable=redefined-builtin, invalid-name
