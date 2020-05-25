import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action.perform()
        sleep(3)


    def test_moveto(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(el)
        action.perform()
        sleep(3)

if __name__ == '__main__':
    pytest.main()
