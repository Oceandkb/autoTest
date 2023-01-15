# @Time   ：2022/11/4 13:38
# @Author : Chao
# @File   : test_kn_att_modify.py
'''
import random
import allure
import requests
from aikn_api.kn_att_modify import kn_att_modify
from aikn_api.kn_att_search import kn_att_search

@allure.epic("知识库")
@allure.feature("属性")
@allure.story("知识属性")
@allure.title('修改知识属性成功')
#@pytest.mark.smoke
def test_kn_att_modify(login_fixture, base_url):
    r_search = kn_att_search(login_fixture, base_url)
    r_search_json = r_search.json()
    kn_att_id = r_search_json['data']['list'][0]['id']
    r = kn_att_modify(login_fixture, base_url, kn_att_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'
'''