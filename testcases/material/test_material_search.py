# @Time   ：2023/8/16 15:56
# @Author : Chao
# @File   : test_material_search.py

import allure
import pytest

from aikn_api.material_search import material_search
import requests

@allure.epic("知识库")
@allure.feature("素材")
@allure.story("素材管理")
@allure.title("搜索素材内容")
def test_material_search(login_fixture, base_url):
    r = material_search(login_fixture, base_url, material_type = "1")
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'