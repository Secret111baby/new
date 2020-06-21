from API_Test.Base.wework import WeWork


class Tag(WeWork):
    def create_tag(self,name,c_id):
        req = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/tag/create?",
            "params": {"access_token", self.token},
            "json": {"tagname":name, "tagid":c_id}
        }
        r = self.send_api(req)
        print(r.json())
        return r.json()