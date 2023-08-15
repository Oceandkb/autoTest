# @Time   ：2022/11/15 14:26
# @Author : Chao
# @File   : kn_att_public_cite.py

import allure
import requests
import random
from requests import Response


@allure.step("公共知识属性引用")
def kn_att_public_cite(s, base_url, cite_att_id) -> Response:

    url = base_url + "/aikn-admin/knowledge/field/v1/field-label"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "labelId":cite_att_id,
        "defaultValue":"",
        "searchCondition":1,
        "viewStyle":1,
        "need": 0,
        "questionType":"1",
        "fieldId":"-1"
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

@allure.step("百科分类知识属性引用")
def kn_att_wiki_class_cite(s, base_url, cite_att_id) -> Response:

    url = base_url + "/aikn-admin/knowledge/classes-label/v1/bind"

    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body ={
        "labelId":cite_att_id,
        "defaultValue":"",
        "viewStyle":1,
        "questionType":"1",
        "classesId":"-1",
        "domainId":1,
        "need": 0
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

@allure.step("领域知识属性引用")
def kn_att_field_cite(s, base_url, cite_att_id, field_id) -> Response:

    url = base_url + "/aikn-admin/knowledge/field/v1/field-label"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "alias": None,
        "labelId":cite_att_id,
        "defaultValue":"",
        "searchCondition":1,
        "viewStyle":1,
        "groupId":-1,
        "need": 0,
        "questionType":"6",
        "fieldId":field_id
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    public_cite_att_id = 4053
    res = kn_att_public_cite(s, base_url, cite_att_id)
    print(res.text)
