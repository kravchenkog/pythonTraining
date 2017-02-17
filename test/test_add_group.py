from model.group import Group


def test_group_creation(app):

    app.session.login(user_name='admin', password='secret')
    app.group.create(Group(name="test name", header="test header", footer="test footer"))
    app.session.logout()


def test_empty_group_creation(app):

    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
