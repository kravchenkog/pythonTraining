from model.group import Group


def test_group_creation(app):
    group_for_add = Group(name="test name", header="test header", footer="test footer")

    old_groups = app.group.get_group_list()
    app.group.create(group_for_add)
    new_groups = app.group.get_group_list()

    assert len(old_groups)+1 == len(new_groups)

    old_groups.append(group_for_add)


    assert sorted(new_groups, key = Group.id_or_max) == sorted(old_groups, key = Group.id_or_max)


def test_empty_group_creation(app):
    group_for_add = Group(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(group_for_add)
    new_groups = app.group.get_group_list()

    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group_for_add)
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)