

def test_group_removal(app):

    app.session.login(user_name='admin', password='secret')
    app.group.remove(0)  # 0 = removing first group in list of groups
    app.session.logout()