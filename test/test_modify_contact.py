# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="1", middlename="2", lastname="3", nickname="",
                                             title="", company="", address="", home="", mobile="", work="",
                                             fax="", email="", homepage="",
                                             # bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",
                                             address2="", phone2="", notes=""))


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="test"))
    app.contact.modify_first_contact(Contact(middlename="New middlename"))
