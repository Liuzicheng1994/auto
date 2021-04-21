from selenium.webdriver.common.by import By

from homework.homework1.page.add_member_page import AddMember
from homework.homework1.page.basee_page import BasePage
from homework.homework1.page.contact_page import Contact


class Main(BasePage):
    def goto_contact(self):
        self.find(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        return Contact(self.driver)

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, (".ww_indexImg.ww_indexImg_AddMember")).click()
        return AddMember(self.driver)