from typing import Optional

from src.domain.websocket.router.suite.model import Suite


class Router:
    def __init__(self):
        self.__routes: Optional[dict] = {}

    def add_suite(self, suite: Suite):
        self.__routes.update(suite.suite)
