from appium.webdriver.common.mobileby import MobileBy

from homework.homework2.pages.base_page import BasePage
from homework.homework2.pages.edit_page import EditPage


class DetailsPage(BasePage):
    def goto_editpage(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/h8g").click()
        self.find(MobileBy.ID, "com.tencent.wework:id/b49").click()
        return EditPage(self.driver)