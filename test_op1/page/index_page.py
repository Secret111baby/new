from test_op1.page.login_page import LoginPage
from test_op1.page.register_page import RegisterPage



#首页主要有这三个模块，分别是注册，登陆，下载
class IndexPage:

    #点击注册按钮，跳转到注册页面
    def goto_register(self):
        """
        点击立即注册按钮，跳转到注册页面
        self.driver.find_element(By.ID, 'xxx").click()
        :return:
        """
        return RegisterPage()

    #点击登陆按钮，跳转到登陆页面
    def goto_login(self):
        """
        输入用户名等信息，


        :return:
        """
        return LoginPage()

    def goto_download(self):
        pass