from src.domain.websocket.connection.model import Connection
from src.domain.websocket.request.method.enum import MethodType
from src.domain.websocket.request.model import Request
from src.domain.websocket.response.model import Response
from src.domain.websocket.router.function.model import Function
from src.domain.websocket.router.method.model import Method
from src.domain.websocket.router.model import Router
from src.domain.websocket.router.route.model import Route
from src.domain.websocket.router.suite.model import Suite


class TestClass:
    @staticmethod
    def stub_function(
        connection: Connection, hand_shake: any, request: Request
    ) -> Response:
        pass

    def test_should_add_suite_into_router(self):
        suite = Suite()
        router = Router()
        router.add_suite(suite=suite)

        assert router._Router__routes == {}

    def test_should_add_suite_with_get_into_router(self):
        name = "/values_from_disk"
        suite = Suite()
        decorator = suite.get(name=name)
        decorator(callback=TestClass.stub_function)

        router = Router()
        router.add_suite(suite=suite)

        added_route = router._Router__routes.get(name)

        assert len(router._Router__routes.keys()) == 1
        assert list(router._Router__routes.keys())[0] == name
        assert isinstance(added_route, Route)
        assert isinstance(added_route.get_method(method_type=MethodType.GET), Method)
        assert added_route.get_method(method_type=MethodType.POST) is None
        assert added_route.get_method(method_type=MethodType.SUB) is None
        assert added_route.get_method(method_type=MethodType.UNSUB) is None

    def test_should_add_suites_with_get_into_router(self):
        router = Router()

        name1 = "/values_from_disk"
        suite1 = Suite()
        decorator = suite1.get(name=name1)
        decorator(callback=TestClass.stub_function)
        router.add_suite(suite=suite1)

        name2 = "/values_from_disk2"
        suite2 = Suite()
        decorator = suite2.get(name=name2)
        decorator(callback=TestClass.stub_function)
        router.add_suite(suite=suite2)

        added_route1 = router._Router__routes.get(name1)
        added_route2 = router._Router__routes.get(name2)

        assert len(router._Router__routes.keys()) == 2
        assert list(router._Router__routes.keys())[0] == name1
        assert list(router._Router__routes.keys())[1] == name2
        assert isinstance(added_route1, Route)
        assert isinstance(added_route1.get_method(method_type=MethodType.GET), Method)
        assert added_route1.get_method(method_type=MethodType.POST) is None
        assert added_route1.get_method(method_type=MethodType.SUB) is None
        assert added_route1.get_method(method_type=MethodType.UNSUB) is None

        assert isinstance(added_route2, Route)
        assert isinstance(added_route2.get_method(method_type=MethodType.GET), Method)
        assert added_route2.get_method(method_type=MethodType.POST) is None
        assert added_route2.get_method(method_type=MethodType.SUB) is None
        assert added_route2.get_method(method_type=MethodType.UNSUB) is None
