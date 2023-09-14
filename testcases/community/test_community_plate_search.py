# @Time   ：2023/9/11 16:53
# @Author : Chao
# @File   : test_community_plate_search.py


import allure
from aikn_api.community_plate_search import community_plate_search
import requests

@allure.epic("知识库")
@allure.feature("社区")
@allure.story("查询社区版块成功")
def test_community_plate_search(login_fixture, base_url, random_fixture):
    r = community_plate_search(login_fixture, base_url)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功'
