"""
测试用例:
        打开雪球应用
        点击搜索框
        输入阿里巴巴或者小米
        点击第一个搜索结果
        判断股票价格
        利用参数化


"""
import pytest
from appium import webdriver
from hamcrest import assert_that, close_to


class TestPa:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        #dontstop是指停止应用
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
        # 获取到第一个价格以后需要点击取消退出当前页面再次输入
        # self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()
        # pass


    # 参数化设置，方法内设定参数，并给好相应的数组（元组形式的）
    @pytest.mark.parametrize('searchkey, title, price', [
        ('alibaba', 'BABA', 200),
        ('xiaomi', '01810', 13)
    ])
    def test_canshu(self, searchkey, title, price):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element_by_xpath(f"//*[@text='{title}']").click()
        stock = self.driver.find_element_by_xpath(f"//*[@text='{title}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price= float(stock.text)
        # 断言价格浮动不超过price*0.1
        assert_that(current_price, close_to(price, price*0.1))