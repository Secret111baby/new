"""
封装request方法
"""
import requests


class Base:
    def send_api(self, req):
        return requests.request(**req)