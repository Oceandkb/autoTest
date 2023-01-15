# @Time   ：2022/11/3 15:24
# @Author : Chao
# @File   : lib_class_add.py

import time
import allure
import requests
import random
from requests import Response
timestamp1 = str(int(round(time.time()*1000)))

@allure.step("新增文库分类")
def lib_class_add(s, base_url, domainId, lib_class_parentId)  -> Response:
    '''

    :param s:
    :param base_url:
    :param domainId: 知识类型的id
    :param lib_class_parentId: 父分类的id
    :return:
    '''
    url_lib_class_add = base_url + "/aikn-admin/knowledge/knowledge/v1/classes" + timestamp1
    r = requests.post(url_lib_class_add)
    cookie1 = dict(r.cookies)
    s.cookies.update(cookie1)
    url = base_url + "/aikn-admin/knowledge/knowledge/v1/classes"

    ran = str(random.randint(1,1000))
    name = "Auto_lib_class" + ran
    body = {
        "domainId": domainId,
        "name": name,
        "parentId": lib_class_parentId,
    }
    return s.post(url, json=body, cookies=cookie1)

if __name__ == '__main__':
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    r = lib_class_add(s, base_url)
    print(r.text)
