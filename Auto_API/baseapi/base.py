"""
封装基本的常用的方法
比如request，yaml

"""
import requests
import yaml


class BaseApi:
    def send_api(self, req):
        """
        request需要传入method，url，params等
        可以通过req结构体的方式传入，加入**是对结构体进行解包
        **代表对字典进行解包，使用K = V的形式进行传参

        :param req:
        :return:
        """
        return requests.request(**req)

    # def yml_safe_load(self,file):
    #     return yaml.safe_load(open(file))
