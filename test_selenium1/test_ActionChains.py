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

    @pytest.mark.skip
    def test_moveto(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_xpath("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(el)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_draganddrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        source_ele = self.driver.find_element_by_id("dragger")
        drop_ele = self.driver.find_element_by_xpath("/html/body/div[2]")

        action = ActionChains(self.driver)
        #drag and drop的用法，传入两个参数，分别是要点击，放开的元素
        # action.drag_and_drop(source_ele, drop_ele).perform()
        #click and hold 起始元素，放开最终元素
        action.click_and_hold(source_ele).release(drop_ele).perform()
        sleep(3)

if __name__ == '__main__':
    pytest.main()
