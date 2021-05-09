from appium.webdriver.common.mobileby import MobileBy
from homework.homework2.pages.base_page import BasePage
from homework.homework2.pages.contactlist_page import ContactListPage


class IndexPage(BasePage):

    def goto_contactlistpage(self):
        #click 通讯录
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return ContactListPage(self.driver)