# -*- coding: utf-8 -*-
import random


def test_add_contact_to_group(app, ormdb):
    exception_group_list = []
    contact = random.choice(ormdb.get_contact_list())
    list_groups_for_contact = ormdb.get_groups_for_contact(contact)
    list_all_groups = ormdb.get_group_list()
    for g in list_all_groups:
        if g not in list_groups_for_contact:
            exception_group_list.append(g)
    if len(exception_group_list) == 0:
        group = list_groups_for_contact[random.randrange(len(list_groups_for_contact))]
        app.contact.remove_from_group(contact, group)
    else:
        index = random.randrange(len(exception_group_list))
        group = list_all_groups[index]
    app.contact.add_contact_to_group(contact, group)
    #assert group in ormdb.get_groups_for_contact(contact)