from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.test_op import AddMember


class Main:
    def __init__(self):
        option = Options()
        option.debugger_address = "localhost:1111"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(5)

    def goto_addcontact(self):
        #点击添加成员按钮
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        #跳转到添加成员页面
        return AddMember()
