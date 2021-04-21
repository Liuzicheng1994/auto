from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework.homework1.page.basee_page import BasePage


class Contact(BasePage):
    def goto_add_member(self):
        from homework.homework1.page.add_member_page import AddMember
        return AddMember(self.driver)

    def goto_add_depart(self):
        from homework.homework1.page.add_depart_page import AddDepart
        self.driver.find_element(By.CSS_SELECTOR, (".member_colLeft_top_addBtnWrap.js_create_dropdown")).click()
        self.driver.find_element(By.CSS_SELECTOR, (".js_create_party")).click()
        return AddDepart(self.driver)

    def goto_import_contact(self):
        from homework.homework1.page.import_contact_page import ImportContact
        return ImportContact(self.driver)

    def get_member_list(self):
        pass

    def get_depart_list(self):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, "新建部门成功")))
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".jstree-anchor")
        name_list = [i.text for i in ele_list]


        return name_list


    def get_import_contact(self):
        pass
