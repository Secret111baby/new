"""
测试用例的执行

"""
import requests
import yaml

from Auto_API.baseapi.department import Department
from Auto_API.baseapi.wework import WeWork


class TestApi:
    #token只需要每个用例执行前执行一次，所以设置成setupclass就行
    def setup_class(self):
        # self.wework = WeWork()
        self.department = Department()
        # secret = {
        #     "corpsecret" : "GaD7ackReOLGLXG6aD-QnH7p9h7yC1BydUC93uEH-EE",
        #     "agent": "xxx"
        #
        # }
        """
        通过读取文件的方法进行传参，这样可以在不改变代码逻辑的基础上只改变数据
        """
        self.token = self.department.get_token(self.department.yml_safe_load("config.yml")["corpsecret"])
        # print(self.token)

    def test_create_department(self):
        r = self.department.create_department("深圳研发中心", "shenzhende", 111)
        assert r["errcode"] == 0

    def test_update_department(self):
        r = self.department.update_department("深圳研发中心ddd", "shenzhende", 111)
        assert r["errmsg"] == "updated"

    def test_delete_department(self):
        r = self.department.delete_department(111)
        assert r["errmsg"] == "deleted"

