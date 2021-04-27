from selenium import webdriver


class BasePage:
    """
    封装页面通用方法，比如driver实例化
    """
    def __init__(self, base_driver=None):

        #使用浏览器服用模式
        if base_driver is not None:
            self.driver =base_driver
        else:
            chrome_arg = webdriver.ChromeOptions()
            #加入调试地址
            chrome_arg.debugger_address = '127.0.0.1:9222'
            #实例化driver对象
            self.driver = webdriver.Chrome(options=chrome_arg)
            # self.driver = webdriver.Chrome()

            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            self.driver.implicitly_wait(10)


    def find(self, by,locator):
        #解元祖
        return self.driver.find_element(by,locator)


