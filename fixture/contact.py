from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("add new").click()

    # wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        # wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_homepage()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)
        # wd.find_element_by_name("bday").click()
        # Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        # wd.find_element_by_xpath("//option[@value='18']").click()
        # wd.find_element_by_name("bmonth").click()
        # Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        # wd.find_element_by_xpath("//option[@value='October']").click()
        # wd.find_element_by_name("byear").click()
        # wd.find_element_by_name("byear").clear()
        # wd.find_element_by_name("byear").send_keys(contact.byear)
        # wd.find_element_by_name("aday").click()
        #  Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        # wd.find_element_by_xpath("(//option[@value='18'])[2]").click()
        # wd.find_element_by_name("amonth").click()
        # Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        # wd.find_element_by_xpath("(//option[@value='December'])[2]").click()
        # wd.find_element_by_name("ayear").click()
        # wd.find_element_by_name("ayear").clear()
        # wd.find_element_by_name("ayear").send_keys(contact.ayear)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        # fill contact form
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_homepage()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_homepage()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_css_selector("input[id='%s']" % id).click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        # self.app.return_to_homepage()
        # self.open_home_page()
        # select first contact
        # wd.find_element_by_name("selected[]").click()
        self.select_contact_by_index(index)
        # submit edit
        wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()
        # wd.find_element_by_name("firstname").click()
        # wd.find_element_by_name("firstname").clear()
        # wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # wd.find_element_by_name("middlename").click()
        # wd.find_element_by_name("middlename").clear()
        # wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # wd.find_element_by_name("lastname").click()
        # wd.find_element_by_name("lastname").clear()
        # wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # wd.find_element_by_xpath("//form[@action='edit.php']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        # wd.find_element_by_link_text("home page").click()
        self.app.return_to_homepage()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        # self.app.return_to_homepage()
        # self.open_home_page()
        # select first contact
        # wd.find_element_by_name("selected[]").click()
        self.select_contact_by_id(id)
        # submit edit
        #wd.find_elements_by_xpath("(//img[@alt='Edit'])").click()
        wd.find_element_by_xpath("//img[@title='Edit']//parent::a[contains(@href,'id=" + id + "')]").click()
        # wd.find_element_by_name("firstname").click()
        # wd.find_element_by_name("firstname").clear()
        # wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # wd.find_element_by_name("middlename").click()
        # wd.find_element_by_name("middlename").clear()
        # wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # wd.find_element_by_name("lastname").click()
        # wd.find_element_by_name("lastname").clear()
        # wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # wd.find_element_by_xpath("//form[@action='edit.php']").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        # wd.find_element_by_link_text("home page").click()
        self.app.return_to_homepage()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_first_contact(0)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        # self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

# метод тренера get_contact_list
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails,
                                                  address=address))
        return list(self.contact_cache)

# мой метод get_contact_list
#    def get_contact_list(self):
#        if self.contact_cache is None:
#            wd = self.app.wd
#            self.app.open_home_page()
#            self.contact_cache = []
#            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
#                firstname = element.find_element_by_xpath("./td[3]").text
#                lastname = element.find_element_by_xpath("./td[2]").text
#                id = element.find_element_by_name("selected[]").get_attribute("value")
#                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
#        return list(self.contact_cache)

# открыть страницу редактирования контакта
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

# открыть страницу просмотра детальной информации контакта
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

# получить данных контакта со страницы редактирования контакта
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, mobile=mobile, work=work, phone2=phone2,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work,
                       phone2=phone2)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("to_group").click()
        for in_group in wd.find_elements_by_xpath("//select[@name='to_group']//option"):
            if in_group.get_attribute("value") == group.id:
                in_group.click()
        wd.find_element_by_name("add").click()
        # return
        self.app.open_home_page()
        self.contact_cache = None

    def del_contact_from_group(self, contact, group):
        wd = self.app.wd
        # выбрать группу из выпадающего списка
        for in_group in wd.find_elements_by_xpath("//select[@name='group']//option"):
            if in_group.get_attribute("value") == group.id:
                wd.find_element_by_name("group").click()
                in_group.click()
                break
        self.select_contact_by_id(contact.id)
        wd.find_element_by_name("remove").click()
        # return
        self.app.open_home_page()
        self.contact_cache = None