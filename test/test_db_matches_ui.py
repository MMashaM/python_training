from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), numner=1))
    def clean (group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list(), numner=1))
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)