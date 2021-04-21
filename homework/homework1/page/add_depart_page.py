from selenium.webdriver.common.by import By

from homework.homework1.page.basee_page import BasePage
from homework.homework1.page.contact_page import Contact


class AddDepart(BasePage):
    def goto_contact(self,department):
        self.driver.find_element_by_xpath("//*[@id='__dialog__MNDialog__']/div/div[2]/div/form/div[1]/input").send_keys(department)
        self.driver.find_element(By.CSS_SELECTOR, (".qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list")).click()
        self.driver.find_element(By.CSS_SELECTOR, (".qui_dialog_body.ww_dialog_body [id='1688851084047901_anchor']")).click()
        self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        return Contact(self.driver)

    def goto_add_member(self):
        pass

    def goto_import_contact(self):
        pass