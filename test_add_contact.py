# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Masha", middlename="Alexandrovna", lastname="Chirva", nickname="Mmm",
                    title="Test", company="Python", address="Address", home="55-55-55", mobile="11-11-11", work="no",
                    fax="no", email="mariya.chirva@gmail.com", homepage="no", bday="18", bmonth="October", byear="1933",
                    aday="18", amonth="December", ayear="1963", address2="no", phone2="no", notes="no"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="",
                    title="", company="", address="", home="", mobile="", work="",
                    fax="", email="", homepage="", bday="", bmonth="-", byear="",
                    aday="", amonth="-", ayear="", address2="", phone2="", notes=""))
    app.logout()
