from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Contacts:
    def __init__(self):
        option = Options()
        option.debugger_address = "localhost:1111"
        self.driver = webdriver.Chrome(options=option)

    #获取成员信息
    def get_contact(self):
        # list1 = []
        """
        self.driver.find_element_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")这样拿到的是webelement对象

        """
        member_list = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        # list1 = []
        # for member in member_list:
        #     list1.append(member.get_attribute("title"))
        # return list1
        # 以下是列表推导式的写法
        return [member.get_attribute("title") for member in member_list]


