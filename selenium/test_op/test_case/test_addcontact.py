from selenium.test_op import Main


class TestAddContact:
    def test_addcontact(self):
        #对主页实例化，可以调用里面的方法
        main = Main()
        #做断言，查看成员是否添加成功
        assert "stary" in main.goto_addcontact().add_contact().get_contact()