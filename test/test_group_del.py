

def test_group_removal(app):

    list_of_group_old = app.group.get_group_list()
    app.group.remove(0)  # 0 = removing first group in list of groups
    list_of_group_new = app.group.get_group_list()

    assert len(list_of_group_old)-1 == len(list_of_group_new)

    list_of_group_old[0:1] = []
    assert list_of_group_old == list_of_group_new