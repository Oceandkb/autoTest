# conding = utf-8
# import time
import allure
import requests
from requests import Response
# import os
# timestamp1 = str(int(round(time.time()*1000)))

# @allure.title("添加分类成功")
def dclassadd(s, base_url, domainId="2", name="2024", parentId="0") -> Response:
    urldclassadd = base_url + "/aikn-admin/knowledge/knowledge/v1/classes"
    r = requests.post(urldclassadd)
    cookie1 = dict(r.cookies)
    s.cookies.update(cookie1)
    url = base_url + "/aikn-admin/knowledge/knowledge/v1/classes"
    body = {
        "domainId": domainId,
        "name": name,
        "parentId": parentId,
    }
    res = s.post(url, json=body, cookies=cookie1)
    return res

if __name__ == '__main__':
    s = requests.Session()
    base_url = "https://v5-test.faqrobot.cn"
    from api.login_function import login

    login(s, base_url)
    r2 = dclassadd(s, base_url)
    print(r2.text)

