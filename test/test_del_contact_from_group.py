# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, ormdb):
    if len(ormdb.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(ormdb.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contact = random.choice(ormdb.get_contact_list())
    list_groups_for_contact = ormdb.get_groups_for_contact(contact)
    if (len(list_groups_for_contact)) == 0:
        group = random.choice(ormdb.get_group_list())
        app.contact.add_contact_to_group(contact, group)
    else:
        index = random.randrange(len(list_groups_for_contact))
        group = list_groups_for_contact[index]
    app.contact.del_contact_from_group(contact, group)
    assert group not in ormdb.get_groups_for_contact(contact)