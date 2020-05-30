"""
复用浏览器的登陆方式

"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWeChatLogin:
    # def setup(self):
    #     option = Options()
    #     option.debugger_address = "localhost:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #
    # def teardown(self):
    #     pass

    def test_wechat(self):
        #实例化Options
        option = Options()
        #获取已开通的本地端口号
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        #获取网址并进入
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.find_element_by_xpath()
