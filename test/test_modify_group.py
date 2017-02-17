from model.group import Group


def test_group_name_modification(app):
    app.session.login(user_name='admin', password='secret')
    app.group.modify(0, Group(name='SuperGroup'))  # 0 = removing first group in list of groups
    app.session.logout()


def test_group_header_modification(app):
    app.session.login(user_name='admin', password='secret')
    app.group.modify(0, Group(header='bestHeader'))  # 0 = removing first group in list of groups
    app.session.logout()