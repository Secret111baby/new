import requests


class TestApi:
    def setup(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
        params = {
            "corpid": "ww1c405970872c0ce4",
            "corpsecret": "GaD7ackReOLGLXG6aD-QnH7p9h7yC1BydUC93uEH-EE"
        }
        r = requests.get(url, params)
        self.token = r.json()["access_token"]
        # print(self.token)

    def test_create_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create?"
        params = {
            "access_token": self.token
        }
        json = {
            "name": "北京研发",
            "name_en": "beij",
            "parentid": 1,
            "order": 1,
            "id": 5
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())

    def test_update_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update?"
        params = {
            "access_token": self.token
        }
        json = {
            "name": "北京研发1",
            "name_en": "beij",
            "parentid": 1,
            "order": 1,
            "id": 5
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())

    def test_delete_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete?"
        params = {
            "access_token": self.token,
            "ID":5
        }
        # json = {
        #     "name": "北京研发1",
        #     "name_en": "beij",
        #     "parentid": 1,
        #     "order": 1,
        #     "id": 5
        # }
        r = requests.get(url=url, params=params)
        print(r.json())

