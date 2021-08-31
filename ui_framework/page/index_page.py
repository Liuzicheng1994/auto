
from ui_framework.base_page import BasePage


class IndexPage(BasePage):
    def goto_market(self):
        # self.find("xpath", "//*[@text='行情']").click()
        self.run_steps("../page/index_page.yaml", "goto_market")