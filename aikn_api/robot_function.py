import time
import requests
from requests import Response
timestamp1 = str(int(round(time.time()*1000)))


def robotInt(s, base_url, sysNum="1645680632827", sourceId="1665",question="你好") -> Response:
    urlInt = base_url + "/chatbot/web/init/1645680632827?sysNum={}&sourceId={}&lang=zh_CN&_=".format(sysNum,sourceId) + timestamp1
    r = requests.get(urlInt)
    Cookie1 = dict(r.cookies)
    s.cookies.update(Cookie1)
    url = base_url + "/chatbot/web/chat/{}?sourceId={}".format(sysNum,sourceId)
    body = {
        "content": question,
        "type": 0,
        "x": 0,
        "y": 0
    }
    res = s.post(url, json=body, cookies=Cookie1)
    return res


if __name__ == '__main__':
    s1 = requests.session()
    base_url="https://v5-test.faqrobot.cn"
    r2 = robotInt(s1,base_url)
    print(r2.text)
