import pytest

from contact import Contact
from fixture.app_manager import AppManager


@pytest.fixture
def app(request):
    fixture = AppManager()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):

    app.login(user_name='admin', password='secret')
    app.create_contact(Contact(firstname='Grigoriy', lastname='Kravchenko', nickname='grif0n', email='g300884@gmail.com', home='380637267402'))
    app.logout()