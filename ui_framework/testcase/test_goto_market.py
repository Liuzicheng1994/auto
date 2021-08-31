from ui_framework.app import App


class TestGoToMarket:
    def setup(self):
        #  生成 appium 的实例 并传给后面的 page 类
        self.app = App().start()

    def test_go_to_market(self):
        self.app.goto_main().goto_market()