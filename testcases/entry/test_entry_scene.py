# @Time   ：2022/12/2 11:21
# @Author : Chao
# @File   : test_entry_scene.py

import allure
import pytest

from aikn_api.entry_search import *
from aikn_api.entry_detail import entry_detail
from aikn_api.entry_delete import entry_delete
from aikn_api.entry_modify import entry_modify
import requests


@allure.epic("知识库")
@allure.feature("词条")
@allure.story("词条使用场景：查询词条->查看词条详情页->删除词条")
@pytest.mark.usefixtures("entry_fixture")
#@pytest.mark.run(order = 1)
def test_entry_scene(login_fixture, base_url, entry_fixture):
    r = entry_elasticsearch(login_fixture, base_url, entry_fixture[0])
    t = entry_detail(login_fixture, base_url, entry_fixture[1])
    #u = entry_modify(login_fixture, base_url, entry_fixture[0], entry_fixture[1], entry_fixture[2])
    #r2 = entry_delete(login_fixture, base_url, entry_fixture[1])
    print(r.text)
    print(t.text)
    #print(u.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功'
    assert t.json()["code"] == 1
    assert t.status_code == 200
    assert t.json()['message'] == '操作成功'
    # assert u.json()["code"] == 1
    # assert u.status_code == 200
    # assert u.json()['message'] == '操作成功!'

