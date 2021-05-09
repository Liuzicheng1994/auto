from appium.webdriver.common.mobileby import MobileBy
from homework.homework2.pages.base_page import BasePage


class EditPage(BasePage):
    def del_person(self):
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()