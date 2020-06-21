"""
获取token
封装yaml方法

"""
import yaml

from API_Test.Base.Base import Base


class WeWork(Base):
    def get_token(self, corpsecret):
        corpid = "ww1c405970872c0ce4"
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken?",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        self.token = self.send_api(req)
        return self.token

    def yaml(self, file):
        return yaml.safe_load(open(file))
