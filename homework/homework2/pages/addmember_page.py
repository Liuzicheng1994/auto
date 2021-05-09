from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from homework.homework2.pages.base_page import BasePage
from homework.homework2.pages.contactlist_page import ContactListPage


class AddMemberPage(BasePage):
    def addmember_bymenual(self):
        # click 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from homework.homework2.pages.editmember_page import EditMemberPage
        return EditMemberPage(self.driver)

    def verify_ok(self):
        WebDriverWait(self.driver, 10).until(lambda x:x.find_element(MobileBy.XPATH, "//*[@text='添加成功']"))
        sleep(3)
        return ContactListPage(self.driver)


