from selenium.webdriver.common.by import By
from selenium.teacher_code import AddMember
from selenium.teacher_code import BasePage
from selenium.teacher_code import Contact


class Main(BasePage):

    def goto_add_member(self):
        # 点击跳转
        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()

        return AddMember(self.driver)

    def goto_contact(self):
        self.find(By.ID, "menu_contacts").click()
        return Contact(self.driver)