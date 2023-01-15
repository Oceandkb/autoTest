# @Time   ：2022/11/18 14:48
# @Author : Chao
# @File   : test_entry.py

import allure
import pytest
from aikn_api.entry_add import entry_add
from aikn_api.entry_search import entry_list_search
from aikn_api.entry_delete import entry_delete
import requests

@allure.epic("知识库")
@allure.feature("词条")
@allure.story("新增词条成功")
@pytest.mark.run(order = 1)
def test_entry_add(login_fixture, base_url, random_fixture):
    r = entry_add(login_fixture, base_url, random_fixture)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

@allure.epic("知识库")
@allure.feature("词条")
@allure.story("查询词条成功")
@pytest.mark.run(order = 2)
def test_entry_search(login_fixture, base_url):
    r = entry_list_search(login_fixture, base_url)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'

@allure.epic("知识库")
@allure.feature("词条")
@allure.story("删除词条成功")
@pytest.mark.run(order = 3)
def test_entry_delete(login_fixture, base_url):
    r_entry_search = entry_list_search(login_fixture, base_url)
    r_json = r_entry_search.json()
    entry_id = r_json['data']['list'][0]['id']
    r1 = entry_delete(login_fixture, base_url, entry_id)
    print(r1.text)
    assert r1.json()["code"] == 1
    assert r1.status_code == 200
    assert r1.json()['message'] == '操作成功!'
