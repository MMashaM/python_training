# -*- coding: utf-8 -*-


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact()
    app.session.logout()