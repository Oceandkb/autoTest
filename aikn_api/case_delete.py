# @Time   ：2023/3/16 9:48
# @Author : Chao
# @File   : case_add.py

import allure
import requests
import random
from requests import Response


#ran = str(random.randint(1, 1000))
@allure.step("删除案例")
def case_delete(s, base_url, knowledge_id) \
        -> Response:
    url = base_url + "/aikn-admin/knowledge/knowledge/v1/recycle-bin/approve"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "knowledgeId": knowledge_id,
        "approveType": 1,
        "approveUserIds": []
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = case_delete(s, base_url, knowledge_id = 1056317)
    print(result.text)

