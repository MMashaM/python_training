# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="1", middlename="2", lastname="3", nickname="",
                                             title="", company="", address="", home="", mobile="", work="",
                                             fax="", email="", homepage="",
                                             # bday="", bmonth="-", byear="", aday="", amonth="-", ayear="",
                                             address2="", phone2="", notes="")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_firstname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="New firstname")
#    contact.id = old_contacts[0].id
#    app.contact.modify_first_contact(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(middlename="test"))
#    app.contact.modify_first_contact(Contact(middlename="New middlename"))
