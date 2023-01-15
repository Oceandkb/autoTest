# @Time   ：2022/11/3 16:57
# @Author : Chao
# @File   : kn_att_modify.py
import allure
import requests
import random
from requests import Response
from aikn_api.kn_att_search import kn_all_att_search

@allure.step("修改知识属性")
def kn_att_modify(s, base_url, kn_att_id) -> Response:
    '''
    修改知识属性
    :param s:
    :param base_url:
    :param kn_att_id: 修改的知识属性的id
    :return:
    '''
    url = base_url + "/aikn-admin/knowledge/v1/dynamic-label/modify"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    ran = str(random.randint(1, 1000))
    kn_att_name = "Auto_kn_att_mod" + ran
    body = {
        "id" : kn_att_id,
        "name" : kn_att_name
        #"content" : ""
    }
    s.headers.update(h)
    r = s.post(url, json=body)

    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    kn_att_modify(s, base_url)
    result = kn_att_modify(s, base_url, kn_att_id)
    print(result.text)
