from model.group import Group


def test_group_name_modification(app):
    list_of_group_old = app.group.get_group_list()
    app.group.modify(0, Group(name='SuperGroup'))
    list_of_group_new = app.group.get_group_list()

    assert len(list_of_group_old) == len(list_of_group_new)


def test_group_header_modification(app):
    list_of_group_old = app.group.get_group_list()
    app.group.modify(0, Group(header='bestHeader'))

    list_of_group_new = app.group.get_group_list()

    assert len(list_of_group_old) == len(list_of_group_new)