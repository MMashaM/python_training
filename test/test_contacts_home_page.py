import re
from model.contact import Contact


def test_contacts_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert len(contact_from_home_page) == len(contact_from_db)
    #assert sorted(contact_from_home_page, key=Contact.id_or_max()) == sorted(contact_from_db, key=Contact.id_or_max())
    for i in range(len(contact_from_home_page)):
        contact_from_home_page_by_index = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)[i]
        contact_from_db_by_index = db.get_contact_list()[i]
        assert contact_from_home_page_by_index.firstname == contact_from_db_by_index.firstname
        assert contact_from_home_page_by_index.lastname == contact_from_db_by_index.lastname
        assert contact_from_home_page_by_index.address == contact_from_db_by_index.address
        assert contact_from_home_page_by_index.all_mail == merge_emails_like_on_home_page(contact_from_db_by_index)
        assert contact_from_home_page_by_index.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db_by_index)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.email, contact.email2, contact.email3]))))


