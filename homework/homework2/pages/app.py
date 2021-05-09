import logging
from appium import webdriver
from homework.homework2.pages.base_page import BasePage
from homework.homework2.pages.index_page import IndexPage


class App(BasePage):
    def start(self):
        if self.driver == None:
                desired_caps = {}
                desired_caps['platformName'] = 'Android'
                desired_caps['deviceName'] = '127.0.0.1:7555'
                desired_caps['appPackage'] = 'com.tencent.wework'
                desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
                # 防止清空缓存
                desired_caps["noReset"] = "true"
                # desired_caps['dontStopAppOnReset'] = "true"
                # desired_caps['skipDeviceInitialization'] = "true"
                # desired_caps['unicodeKeyboard'] = 'true',
                # desired_caps['resetKeyboard'] = 'true';
                self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
                self.driver.implicitly_wait(10)
        else:
            print("复用driver")
            self.restart()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        logging.info('入口')
        # 入口
        return IndexPage(self.driver)