import json

from mitmproxy import flow, http

import json

def response(flow):
    if "quote.json" in flow.request.pretty_url:
        # 返回结果json化
        res = json.loads(flow.response.content)
        # 对返回结果进行篡改
        res["data"]["items"][0]["quote"]["name"] = "hogwarts2020!!!!!"
        # 返回结果的二次赋值
        flow.response.text = json.dumps(res)
