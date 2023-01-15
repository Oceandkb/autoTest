# @Time   ：2022/11/18 13:43
# @Author : Chao
# @File   : test_entry_search.py

import allure
import pytest

from aikn_api.entry_search import *
import requests

#
# @allure.epic("知识库")
# @allure.feature("词条")
# @allure.story("总览词条查询成功")
# @pytest.mark.run(order = 1)
# def test_entry_elasticsearch(login_fixture, base_url, entry_fixture):
#     r = entry_elasticsearch(login_fixture, base_url, entry_fixture)
#     print(r.text)
#     assert r.json()["code"] == 1
#     assert r.status_code == 200
#     assert r.json()['message'] == '操作成功'


@allure.epic("知识库")
@allure.feature("词条")
@allure.story("列表词条查询成功")
@pytest.mark.run(order = 2)
def test_entry_list_search(login_fixture, base_url):
    r = entry_list_search(login_fixture, base_url)
    r_json = r.json()
    entry_name = r_json['data']['list'][0]['questions'][0]['question']
    print(r.text)
    print(entry_name)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'


