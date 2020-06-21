import pytest
from appium import webdriver


"""
测试用例：
      打开雪球app；
      点击搜索框输入“阿里巴巴”；
      在搜索结果里面选择“阿里巴巴”,然后进行点击；
      获取这只的价格，并判断，>200


执行失败了，原因是找不到阿里巴巴-sw的股价这个元素
换个方式定位元素就能执行成功了
"""

class TestAli:
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

  def test_ali(self):
    self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
    self.driver.find_element_by_xpath("//*[@text='BABA']").click()
    stock = self.driver.find_element_by_xpath("//*[@text='BABA']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
    current_price = float(stock.text)
    assert current_price > 200
    # self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
    # stock = float(self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/current_price' and @text='1217.99']").text)
    # assert stock > 200
    # if stock > 200:
    #   print("搜索成功")
    # else:
    #   print("搜索失败")

  if __name__ == '__main__':
      pytest.main()


