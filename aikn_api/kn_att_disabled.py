# @Time   ：2022/11/15 16:44
# @Author : Chao
# @File   : kn_att_disabled.py
import allure
import requests
from requests import Response

@allure.step("禁用公共领域知识属性")
def public_kn_att_disabled(s, base_url, kn_public_att_id) -> Response:

    url = base_url + "/aikn-admin/knowledge/field/v1/field-label?id=" + kn_public_att_id
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    s.headers.update(h)
    r = s.get(url)
    #r_json = return ()
    return r

@allure.step("禁用百科分类关联的知识属性")
def wiki_class_kn_att_disabled(s, base_url, kn_class_att_id) -> Response:

    url = base_url + "/aikn-admin/knowledge/classes-label/v1/update-status/" + kn_class_att_id
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    s.headers.update(h)
    r = s.get(url)
    #r_json = return ()
    return r

@allure.step("禁用领域关联的知识属性")
def field_kn_att_disabled(s, base_url, kn_field_att_id) -> Response:

    url = base_url + "/aikn-admin/knowledge/field/v1/field-label?id=" + kn_field_att_id
    h = {
        "Accept": "application/json, text/plain, */*"
    }
    s.headers.update(h)
    r = s.get(url)
    #r_json = return ()
    return r

if __name__ == '__main__':
    s = requests.session()
    base_url = "https://v5-test.faqrobot.cn"
    from api.login_function import login
    login(s, base_url)
    public_kn_att_disabled(s, base_url, )
    res = public_kn_att_disabled(s, base_url, )
    print(res.text)