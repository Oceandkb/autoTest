# @Time   ：2023/6/16 15:06
# @Author : Chao
# @File   : case_search.py

import allure
import requests
from requests import Response


@allure.step("查询案例知识")
def case_search(s, base_url) -> Response:

    url = base_url + "/aikn-admin/knowledge/case/v1/list"
    h = {
        "Accept": "application/json, text/plain, */*"
    }

    body = {
        "pageNum":1,
        "pageSize":10,
        "data":{
            "classesIds":[],
            "domainId":19,
            "question":""
        }

    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = case_search(s, base_url)
    print(result.text)