# 基类， 完成底层封装，比如一些方法， 初始化 driver find。。
# 实现底层封装， 它也可以被复用， 所以这段代码属于框架层
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import logging
root = logging.getLogger()
print(root.handlers)
for h in root.handlers[:]:
    root.removeHandler(h)


class BasePage:
    logging.basicConfig(level=logging.INFO)
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 如果添加的功能越来越多， find 方法会无限增长
    # 如果 find 方法代码增加非常多的话 ，会很难维护
    # 解决： 利用装饰器进行功能增加，把黑名单放到装饰器，增强 find 方法
    def find(self, by, value):
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
    # 关键字驱动
    # 功能： 可以解析关键字文件， 对文件中的字符串进行一一处理， 从而实现关键字操作
    def run_steps(self, path, function_name):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        steps = data.get(function_name)
        # 每一个 step 的格式 是{'action': , 'by':, 'value':}
        for step in steps:
            # 如果键的值是click 的话， 代表想要点击元素
            if step.get("action") == "click":
                self.find(step.get("by"), step.get("value")).click()
            # 封装输入框关键字
            if step.get("action") == "send_keys":
                self.find(step.get("by"), step.get("value")).send_keys(step.get("content"))
