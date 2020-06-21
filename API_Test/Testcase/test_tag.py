from API_Test.Base.tag import Tag


class TestTag():
    def setup_class(self):
        """
        读取token
        :return:
        """
        self.tag = Tag()
        self.token = self.tag.get_token(self.tag.yaml("token.yml")["corpsecret"])

    def test_create_tag(self):
        r = self.tag.create_tag("ui",12)
        print(r)
        # assert r["errcode"] == 0