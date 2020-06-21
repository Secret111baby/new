# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python


"""
测试用例：企业微信添加联系人
步骤：
1.进入通讯录页面
2.点击添加成员
3.点击手动输入添加
4.输入相关字段（姓名，性别，手机号）
5.点击保存


"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestWechat:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = "launch.WwMainActivity"
        caps["noReset"] = "True"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def teardown(self):
        self.driver.quit()

    def test_add(self):
        # 点击添加成员
        self.driver.find_element(MobileBy.id, "//*[@text='添加成员']").click()
        #点击手动输入添加
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        #输入姓名
        self.driver.find_element_by_xpath("//*[@text='必填']").send_keys("王五")
        #选择性别
        self.driver.find_element_by_xpath("//*[@text='男']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dsp' and @text='男']").click()
        # 输入手机号
        self.driver.find_element_by_id("com.tencent.wework:id/esx").send_keys("13153336222")
        # 点击保存
        self.driver.find_element_by_id("com.tencent.wework:id/gyt").click()


