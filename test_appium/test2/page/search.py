from test_appium.test2.page.base_page import BasePage


class Search(BasePage):
    def search(self, value):
        self._params["value"] = value
        self.steps("../page/steps.yaml")