from typing import Any


class Function():
    @staticmethod
    def apply(*args, **kwargs):
        raise NotImplementedError

    @staticmethod
    def get_metadata() -> dict[str, Any]:
        raise NotImplementedError
