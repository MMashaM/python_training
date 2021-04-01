# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    testdata = [
        Contact(firstname="Masha", middlename="Alexandrovna", lastname="Chirva", nickname="Mmm",
                title="Test", company="Python", address="Address", home="55-55-55", mobile="11-11-11", work="no",
                fax="no", email="mariya.chirva@gmail.com", homepage="no",
                # bday="18", bmonth="October", byear="1933", aday="18", amonth="December", ayear="1963",
                address2="no", phone2="no", notes="no"),
        Contact(firstname="", middlename="", lastname="", nickname="",
                                     title="", company="", address="", home="", mobile="", work="", fax="", email="", homepage="",
        #                              # bday="", bmonth="-", byear="",aday="", amonth="-", ayear="",
                                   address2="", phone2="", notes="")

    ]
    for contact in testdata:
        pass
        #old_contacts = app.contact.get_contact_list()
        #app.contact.create(contact)
        #assert len(old_contacts) + 1 == app.contact.count()
        #new_contacts = app.contact.get_contact_list()
        #old_contacts.append(contact)
        #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", middlename="", lastname="", nickname="",
#                               title="", company="", address="", home="", mobile="", work="", fax="", email="", homepage="",
#                              # bday="", bmonth="-", byear="",aday="", amonth="-", ayear="",
 #                              address2="", phone2="", notes="")
 #   app.contact.create(contact)
 #   assert len(old_contacts) + 1 == app.contact.count()
  #  new_contacts = app.contact.get_contact_list()
  #  old_contacts.append(contact)
  #  assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
