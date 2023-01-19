from dataclasses import dataclass

from src.domain.exception.server.model import InvalidRequestArgsException


@dataclass(slots=True, init=True)
class Args:
    __args: dict

    @property
    def args(self):
        return self.__args

    @classmethod
    def create(cls, args: dict):
        args = cls.validate_args(args=args)
        return cls(args)

    @staticmethod
    def validate_args(args):
        is_dict_args = type(args) == dict
        if not is_dict_args:
            raise InvalidRequestArgsException(
                f"Request args {args} is invalid"
            )

        return args
