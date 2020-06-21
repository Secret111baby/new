from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.test_op import Contacts


class AddMember:
    def __init__(self):
        option = Options()
        option.debugger_address = "localhost:1111"
        self.driver = webdriver.Chrome(options=option)

    def add_contact(self):
        """
        输入相关信息并点击保存按钮，进入到通讯录页面

        :return:
        """
        #用户名
        self.driver.find_element(By.ID, 'username').send_keys("stary")
        #账号
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys("67835632")
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys("13105067009")
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        return Contacts()

