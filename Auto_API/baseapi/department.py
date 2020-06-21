"""
页面主要方法执行
"""


import requests

from Auto_API.baseapi.wework import WeWork


class Department(WeWork):


    def create_department(self, name, name_en, c_id, parentid=1, order=1):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create?"
        params = {
            "access_token": self.token
        }
        json = {"name": name, "name_en": name_en, "parentid": parentid, "order": order, "id": c_id}
        r = requests.post(url=url, params=params, json=json)
        return r.json()

    """
    通过传参的方式设置包体，这样就可以在测试用例中通过设置不同的数据进行测试，不用来改动封装好的方法，如上，如下
    位置参数不能放在最后
    且id是内置参数，自定义参数的时候不能与内置参数冲突
    """

    def update_department(self, name, name_en, c_id, parentid=1, order=1):
        req = {
            "method":"post",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/department/update?",
            "params": {"access_token": self.token},
            "json" : {"name": name, "name_en": name_en, "parentid": parentid, "order": order, "id": c_id}
        }
        r = self.send_api(req)
        print(r.json())
        return r.json()

    def delete_department(self, c_id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete?"
        params = {"access_token": self.token, "ID":c_id}
        # json = {
        #     "name": "北京研发1",
        #     "name_en": "beij",
        #     "parentid": 1,
        #     "order": 1,
        #     "id": 5
        # }
        r = requests.get(url=url, params=params)
        return r.json()
