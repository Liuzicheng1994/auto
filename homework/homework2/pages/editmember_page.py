from appium.webdriver.common.mobileby import MobileBy

from homework.homework2.pages.addmember_page import AddMemberPage
from homework.homework2.pages.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, username, phonenum):
        # edit username
        self.find(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(username)
        # edit phonenum
        self.find(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        return AddMemberPage(self.driver)