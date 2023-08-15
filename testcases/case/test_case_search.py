# @Time   ：2023/6/16 15:11
# @Author : Chao
# @File   : test_case_search.py

import allure
from aikn_api.case_search import case_search
import requests

@allure.epic("知识库")
@allure.feature("知识")
@allure.story("案例库")
@allure.title("查询案例知识成功")
def test_case_search(login_fixture, base_url):
    r = case_search(login_fixture, base_url)
    if r == None:
        print(r)
    else:
        print(r.text)
        assert r.json()["code"] == 1
        assert r.status_code == 200
        assert r.json()['message'] == '操作成功!'