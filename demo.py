from mitmproxy import http


# request不能被改变
def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.
#判断某个文件是否存在
    if "quote.json" in flow.request.pretty_url:
        #打开本地的文件，编码格式为utf-8
        with open("C:/Users/Administrator/Desktop/tmp.json", encoding="utf-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                #读取文件
                f.read(),  # (optional) content
                #格式为json
                {"Content-Type": "application/json"}  # (optional) headers
            )