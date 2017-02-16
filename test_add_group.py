import pytest
from app_manager import AppManager
from group import Group


@pytest.fixture
def app(request):
    fixture = AppManager()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group_creation(app):

    app.login(user_name='admin', password='secret')
    app.create_group(Group(name="test name", header="test header", footer="test footer"))
    app.logout()


def test_empty_group_creation(app):

    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

