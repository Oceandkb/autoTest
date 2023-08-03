# @Time   ：2023/3/16 9:33
# @Author : Chao
# @File   : test_case_add.py

import allure
from aikn_api.case_delete import case_delete
from aikn_api.case_search import case_search
import requests

@allure.epic("知识库")
@allure.feature("知识")
@allure.story("案例库")
@allure.title("删除案例成功")
def test_case_delete(login_fixture, base_url):
    r1 = case_search(login_fixture, base_url)
    if r1 is None:
        print(r1)
    else:
        _knowledge_id_ = str(r1.json()['data']['list'][0]['id'])
        r = case_delete(login_fixture, base_url, _knowledge_id_)
        print(r.text)
        assert r.json()["code"] == 1
        assert r.status_code == 200
        assert r.json()['message'] == '操作成功!'