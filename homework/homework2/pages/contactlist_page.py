from appium.webdriver.common.mobileby import MobileBy
from homework.homework2.pages.base_page import BasePage
from homework.homework2.pages.personal_page import PersonalPage


class ContactListPage(BasePage):
    def goto_addmemberpage(self):
        #点击 添加成员
        from homework.homework2.pages.addmember_page import AddMemberPage
        #self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    def goto_personalpage(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/h86").click()
        return PersonalPage(self.driver)