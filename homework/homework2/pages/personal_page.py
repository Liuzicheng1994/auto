from appium.webdriver.common.mobileby import MobileBy

from homework.homework2.pages.base_page import BasePage
from homework.homework2.pages.details_page import DetailsPage


class PersonalPage(BasePage):
    def goto_detailspage(self):
        self.find(MobileBy.XPATH, "//*[@text='13911111118']").click()
        return DetailsPage(self.driver)