from abc import ABC

from src.domain.websocket.router.route.model import Route


class BaseController(ABC):
    async def on_request(self, route: Route):
        pass
