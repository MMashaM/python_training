# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

testdata = [
        Contact(firstname="Masha", middlename="Alexandrovna", lastname="Chirva", nickname="Mmm",
                title="Test", company="Python", address="Address", home="55-55-55", mobile="11-11-11", work="no",
                fax="no", email="mariya.chirva@gmail.com", homepage="no",
                address2="no", phone2="no", notes="no"),
        Contact(firstname="", middlename="", lastname="", nickname="",
                                     title="", company="", address="", home="", mobile="", work="", fax="", email="", homepage="",
                                           address2="", phone2="", notes="")
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    pass
    #old_contacts = app.contact.get_contact_list()
    #app.contact.create(contact)
    #assert len(old_contacts) + 1 == app.contact.count()
    #new_contacts = app.contact.get_contact_list()
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

