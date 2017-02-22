import pytest
from time import sleep
from fixture.app_manager import AppManager

fixture = None


@pytest.fixture
def app(request):
    global fixture

    if fixture is None:
        fixture = AppManager()
    else:
        if not fixture.is_valid():
            fixture = AppManager()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture