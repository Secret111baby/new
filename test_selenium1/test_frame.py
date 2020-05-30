#浏览器的当前窗口唯一标识叫句柄
"""
driver.window_handles 所有窗口
driver.current_window_handles当前窗口

"""
from time import sleep

from test_selenium1.base import Base


class TestFrame(Base):

    def test_windows(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        # print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        # print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("secret")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys("11111111001")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__password"]').send_keys("he134562")
        sleep(2)

