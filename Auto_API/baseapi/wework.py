"""
复用token
"""
import requests
import yaml

from Auto_API.baseapi.base import BaseApi


class WeWork(BaseApi):
    def get_token(self, corpsecret):
        corpid = "ww1c405970872c0ce4"
        #corpsecret的获取方法变成一个参数，调用的时候只需要传参便行
        # params = {"corpid": corpid, "corpsecret": corpsecret}
        req = {
            "method":"get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken?",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        r = self.send_api(req)
        self.token = r.json()["access_token"]
        return self.token

    def yml_safe_load(self, file):
        return yaml.safe_load(open(file))