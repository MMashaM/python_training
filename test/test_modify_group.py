# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="New group 2", header="New group 3", footer="New group 4"))