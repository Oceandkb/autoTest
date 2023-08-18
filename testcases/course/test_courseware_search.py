# @Time   ：2023/8/18 13:58
# @Author : Chao
# @File   : test_courseware_search.py

import allure
import pytest
from aikn_api.field_search import field_search
from aikn_api.courseware_search import courseware_search
import requests

@allure.epic("知识库")
@allure.feature("学院")
@allure.story("课程")
@allure.title("搜索课件成功")
def test_courseware_search(login_fixture, base_url, field_search_fixture):
    r = courseware_search(login_fixture, base_url, field_search_fixture)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功'