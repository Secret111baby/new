from test_op1.page.index_page import IndexPage


class TestRegister:
    #验证去登陆页面进行注册
    def test_login_register(self):
        #对Page进行实例化
        index = IndexPage()
        index.goto_login().goto_register().register()
