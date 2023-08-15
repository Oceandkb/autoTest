# @Time   ：2023/3/3 10:22
# @Author : Chao
# @File   : class_add.py

import allure
import requests
import random
from requests import Response


#ran = str(random.randint(1, 1000))
@allure.step("新增知识分类")
def class_add(s, base_url, class_name, domain_id) -> Response:
    '''
    :param domain_id: 知识类型id，知识点：1 文库：2 案例：19 视频：18
    :param s:
    :param base_url:
    :param class_name: 知识分类的名称
    :return:
    '''
    url = base_url + "/aikn-admin/knowledge/knowledge/v1/classes"
    h = {
        "Accept": "application/json, text/plain, */*"
    }

    body = {
        "name": class_name,
        "parentId": "0",
        "domainId": domain_id
    }

    s.headers.update(h)
    r = s.post(url, json=body)
    print(r.request.body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = class_add(s, base_url, "1234", 19)
    print(result.text)