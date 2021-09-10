from test_appium.test2.page.app import App


class TestSearch:
    def setup(self):
        self.app = App().start()
    def test_search(self):
        self.app.main().goto_market().goto_search().search("jd")