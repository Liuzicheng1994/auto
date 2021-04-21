from selenium.webdriver.common.by import By

from homework.homework1.page.add_depart_page import AddDepart
from homework.homework1.page.basee_page import BasePage
from homework.homework1.page.contact_page import Contact


class AddMember(BasePage):
    def add_member(self):
        return Contact

    def goto_add_depart(self):
        self.driver.find_element(By.CSS_SELECTOR, (".member_colLeft_top_addBtnWrap.js_create_dropdown")).click()
        self.driver.find_element(By.CSS_SELECTOR, (".js_create_party")).click()

        return AddDepart(self.driver)