from appium.webdriver.common.mobileby import MobileBy

from homework.homework2.pages.base_page import BasePage
from homework.homework2.pages.details_page import DetailsPage


class PersonalPage(BasePage):
    def goto_detailspage(self, username):
        self.find(MobileBy.XPATH, f"//*[@text='{username}']").click()
        return DetailsPage(self.driver)