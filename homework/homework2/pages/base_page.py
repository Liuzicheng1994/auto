from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging
root=logging.getLogger()
print(root.handlers)
for h in root.handlers[:]:
    root.removeHandler(h)


class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by ,value):
        logging.info(by)
        logging.info(value)
        return self.driver.find_element(by, value)

    def swipe_find(self, text, num=3):
        for i in range(0, num):
            if i == num-1:
                raise NoSuchElementException("找了{num-1}次没有找到元素")
            try:
                return self.find(MobileBy.XPATH, f"//*[@text='{text}']")
            except:
                print("未找到滑动")
                # 'width', 'height'
                size =self.driver.get_window_size()
                width = size['width']
                heigth = size['height']

                startx = width/2
                starty = heigth*0.8
                endx = startx
                endy = heigth*0.3
                duration = 2000
                self.driver.swipe(startx, starty, endx, endy, duration)