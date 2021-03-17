# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="1", middlename="2", lastname="3", nickname="",
                               title="", company="", address="", home="", mobile="", work="",
                               fax="", email="", homepage="", bday="", bmonth="-", byear="",
                               aday="", amonth="-", ayear="", address2="", phone2="", notes=""))
    app.session.logout()