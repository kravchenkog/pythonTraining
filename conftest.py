import pytest
from fixture.app_manager import AppManager


@pytest.fixture(scope='session')
def app(request):
    fixture = AppManager()
    request.addfinalizer(fixture.destroy)
    return fixture