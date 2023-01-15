# @Time   ：2022/11/15 15:59
# @Author : Chao
# @File   : kn_att_class_cite.py

import allure
import requests
import random
from requests import Response


@allure.step("百科分类知识属性引用")
def kn_att_wiki_class_cite(s, base_url, cite_att_id) -> Response:

    url = base_url + "/aikn-admin/knowledge/classes-label/v1/bind"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "labelId": cite_att_id,
        "defaultValue":"",
        "viewStyle":1,
        "questionType":"1",
        "classesId":"-1",
        "domainId":1
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r


if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    res = kn_att_public_cite(s, base_url, cite_att_id)
    print(res.text)