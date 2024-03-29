# @Time   ：2022/11/4 14:26
# @Author : Chao
# @File   : kn_att_search.py

import allure
import requests
from requests import Response

@allure.step("搜索全部知识属性")
def kn_all_att_search(s, base_url) -> Response:

    url = base_url + "/aikn-admin/knowledge/v1/dynamic-label/list-page"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "data":{"nodeType":""},
        "pageNum":1,
        "pageSize":10
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    # global modify_id
    # modify_id = r_json['data']['list'][0]['id']
    #print(r)
    if len(r.json()["data"]["list"]) > 0:
        return r
    else:
        print("列表为空")

@allure.step("搜索引用的公共属性")
def kn_public_att_search(s, base_url) -> Response:

    url = base_url + "/aikn-admin/knowledge/field/v1/field-label/list"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "pageNum":1,
        "pageSize":10,
        "data":{"fieldId":-1,"status":""}
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    if len(r.json()["data"]["list"]) > 0:
        return r
    else:
        print("列表为空")

@allure.step("搜索百科分类关联的知识属性")
def kn_wiki_class_att_search(s, base_url) -> Response:

    url = base_url + "/aikn-admin/knowledge/classes-label/v1/query/list"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "pageNum":1,
        "pageSize":10,
        "data":{"classesId":"-1","domainId":1,"status":""}
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    if len(r.json()["data"]["list"]) > 0:
        return r
    else:
        print("列表为空")

@allure.step("搜索领域关联的知识属性")
def kn_field_att_search(s, base_url, field_id) -> Response:

    url = base_url + "/aikn-admin/knowledge/field/v1/field-label/list"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "pageNum":1,
        "data":{
            "groupId":-1,
            "fieldId":field_id,
            "status":""
        }
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    r_json = r.json()
    if len(r_json["data"]["list"]) > 0:
        return r
    else:
        print("列表为空")

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = kn_field_att_search(s, base_url, 197)
    print(result.text)


