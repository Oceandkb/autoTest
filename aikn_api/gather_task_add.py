# @Time   ：2023/1/12 17:04
# @Author : Chao
# @File   : gather_task_add.py

import allure
import requests
import random
from requests import Response

@allure.step("新增采编任务-必填项")
def gather_task_add_required(s, base_url, task_name)  -> Response:

    url = base_url + "/aikn-admin/knowledge/gather/task/v1/add"
    h = {
        "Accept": "application/json, text/plain, */*"
    }

    #ran = str(random.randint(1,1000))
    body = {
        "name": task_name,
        "domainId": 0,
        "totalNum": 100,
        "integral": 5,
        "mainTaskSelectedInfo": None,
        "publishObjects": [{"ruleType": 0, "ruleId": 0}],
        "gatherTaskAssignList": [{"taskNum": 1, "assignObjects": [], "gatherTaskSelectedInfo": None, "selectType": 0}]

    }
    s.headers.update(h)
    return s.post(url, json=body)

if __name__ == '__main__':
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    r = lib_class_add(s, base_url)
    print(r.text)