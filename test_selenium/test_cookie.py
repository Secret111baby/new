import json
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestCookie:
    def setup(self):
        # option = Options()
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def teardown(self):
        pass

    def test_cookie(self):
        time.sleep(10)
        co = self.driver.get_cookies()
        with open("co.json", 'w') as f:
            json.dump(obj=co, fp=f)


    def test_login(self):
        # co = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851854231312'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '3WBDXh0cBnMOgLPmUUwSTVirEg84kYLgxXJzpHHvhMYTCFL0XPtO302SYLKdpLuESGz4T2CgdPspzJgwb8QvB-uLnJ_x6g415VcHbZwBjanAAM9xL3WyOPWbxDgoe6vWRYIzUnhw8mdAGUz-oUOz1S4_KI25DBjA4eJfFrrmk3iN1lnkEC44ZTLw3crrlEYMTnBC-o0_HUd1h_4g-tle3d8LWAGO94gRvbIut0xkeZUfeoNopT8RJf-g6I1Pxp9rCVJuBhI9EG_LIvMocYSpNA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851854231312'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324977131732'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5236761'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.qq.com', 'expiry': 1590670913, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.221541619.1590584507'}, {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '2841389286'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '12032324773528718'}, {'domain': '.qq.com', 'expiry': 1590584566, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1653656513, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1154177571.1590584507'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'hNfq9wvPcEuotPl67COP78CUgcNgs_lUb5-U-Kb8UnvxOSduTm_urP4Yw7Y4ZQK4'}, {'domain': '.work.weixin.qq.com', 'expiry': 1593176515, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        co = json.load(open("./co.json"))
        for cookie in co:
            if 'expiry' in co:
                co.pop('expiry')
            self.driver.add_cookie(cookie)

        # self.driver.find_element_by_id("indexTop").click()
        time.sleep(2)
        # self.driver.refresh()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, "index_service_cnt_itemWrap:nth-child(2)").click()
        time.sleep(2)
        #上传文件前提文件的标签必须是input，send_keys里面的文件必须是绝对路径
        dir = os.path.dirname(__file__)
        self.driver.find_element_by_id("js_upload_file_input").send_keys(dir)