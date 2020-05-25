import time

from selenium import webdriver
from time import sleep

class TestOne():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_lo(self):
        self.driver.get("http://www.testerhome.com")
        # time.sleep(2)
        self.driver.find_element_by_link_text("社团").click()
