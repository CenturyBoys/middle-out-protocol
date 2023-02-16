from typing import List

import pytest

from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.method.enum import MethodType
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.model import Response
from src.domain.websocket.router.method.model import Method
from src.domain.websocket.router.model import Router
from src.domain.websocket.router.route.model import Route
from src.domain.websocket.router.suite.model import Suite


@pytest.mark.unit
class TestClass:
    @staticmethod
    @pytest.fixture
    def router_with_empty_suite():
        suite = Suite()
        router = Router()
        router.add_suite(suite=suite)
        return router

    @staticmethod
    @pytest.fixture
    def suite_with_get_router_factory():
        def make_suite(name: str):
            suite = Suite()
            decorator = suite.get(name=name)
            decorator(callback=TestClass.stub_function)

            return suite

        return make_suite

    @staticmethod
    def stub_function(
        connection: Connection, hand_shake: any, request: Request
    ) -> Response:
        pass

    def test_should_add_suite_into_router(self, router_with_empty_suite):
        assert router_with_empty_suite._Router__routes == {}

    @staticmethod
    def assert_that_is_valid_router(route: Route):
        assert isinstance(route, Route)
        assert isinstance(route.get_method(), Method)
        assert route._Route__post_method is None
        assert route._Route__sub_method is None
        assert route._Route__unsub_method is None

    def test_should_add_suite_with_get_into_router(self, suite_with_get_router_factory):
        router = Router()
        name = "/values_from_disk"

        suite = suite_with_get_router_factory(name)
        router.add_suite(suite)
        added_route = router._Router__routes.get(name)
        routes_names = router._Router__routes.keys()

        assert len(routes_names) == 1
        assert list(routes_names)[0] == name

        self.assert_that_is_valid_router(added_route)

    def test_should_add_suites_with_get_into_router(
        self, suite_with_get_router_factory
    ):
        router = Router()

        first_suite = suite_with_get_router_factory(name="/values_from_disk1")
        second_suite = suite_with_get_router_factory(name="/values_from_disk2")
        router.add_suite(suite=first_suite)
        router.add_suite(suite=second_suite)

        first_added_route = router._Router__routes.get("/values_from_disk1")
        second_added_route = router._Router__routes.get("/values_from_disk2")

        added_routes = [first_added_route, second_added_route]

        route_names = router._Router__routes.keys()
        route_names_list = list(route_names)

        assert len(route_names) == 2
        assert route_names_list[0] == "/values_from_disk1"
        assert route_names_list[1] == "/values_from_disk2"

        for added_route in added_routes:
            self.assert_that_is_valid_router(added_route)
