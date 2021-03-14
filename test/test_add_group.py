# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # app.session.login(username="admin", password="secret")
    app.group.create(Group(name="New group 1", header="New group 1", footer="New group 1"))
    # app.session.logout()


def test_add_empty_group(app):
    # app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    # app.session.logout()