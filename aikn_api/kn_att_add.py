import allure
import requests
import random
from requests import Response


#ran = str(random.randint(1, 1000))
@allure.step("新增文本知识属性")
def kn_text_att_add(s, base_url, kn_text_att_name) -> Response:
    '''
    新增文本知识属性
    :param s:
    :param base_url:
    :return:
    '''
    url = base_url + "/aikn-admin/knowledge/v1/dynamic-label"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    #kn_text_att_name = "Auto" + ran
    body = {
        "name": kn_text_att_name,
        "content": "",
        "nodeType": 1,
        "viewStyle": 1
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

@allure.step("新增树型知识属性的父属性")
def kn_tree_parent_att_add(s, base_url, kn_tree_parent_att_name) -> Response:
    '''
    新增树型知识属性的父属性
    :param s:
    :param base_url:
    :return:
    '''
    url = base_url + "/aikn-admin/knowledge/v1/dynamic-label"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "name": kn_tree_parent_att_name,
        "content": "",
        "nodeType": 0
    }
    s.headers.update(h)
    rp = s.post(url, json=body)
    rp_json = rp.json()  # 将response返回的json类型的数据转换
    global kn_tree_att_parentId  # 声明parentId为全局变量，方便在增加子级的函数中引用
    kn_tree_att_parentId = rp_json['data']['id']  # 提取post请求的response中的id值
    print(rp_json)
    print(type(kn_tree_att_parentId))
    return rp

@allure.step("新增树型知识属性的子属性")
def kn_tree_kids_att_add(s, base_url, kn_tree_kids_att_name) -> Response:
    '''
    新增树型知识属性的子属性
    :param s:
    :param base_url:
    :return:
    '''
    global kn_tree_att_parentId
    url = base_url + "/aikn-admin/knowledge/v1/dynamic-label"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "name": kn_tree_kids_att_name,
        "parentId": kn_tree_att_parentId
    }

    s.headers.update(h)
    rk = s.post(url, json=body)
    return rk

@allure.step("新增时间类型知识属性")
def kn_day_att_add(s, base_url, vs, time_name) -> Response:
    '''

    :param s:
    :param base_url:
    :param vs: 时间类型
    :param time_name: 时间类型知识属性的名称
    :return:
    '''
    url = base_url + "/aikn-admin/knowledge/v1/dynamic-label"
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    body = {
        "name": time_name,
        "content": "",
        "nodeType": 2,
        "viewStyle": vs
    }
    s.headers.update(h)
    r = s.post(url, json=body)
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v6-stable.faqrobot.com.cn"
    from aikn_api.login_function import login
    login(s, base_url)
    result = kn_tree_parent_att_add(s, base_url, 1335)
    print(result.text)
