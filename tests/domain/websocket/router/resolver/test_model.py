import pytest

from src.domain.websocket.router.route.model import Route
from src.domain.websocket.router.resolver.model import Resolver
from src.websocket.controller.get.websocket import GetController


@pytest.mark.unit
class TestClass:
    def test_should_create_get_resolver(self):
        resolver = Resolver(route=Route.create(name="name"), controller=GetController())

        assert isinstance(resolver._Resolver__route, Route)
        assert isinstance(resolver._Resolver__controller, GetController)
