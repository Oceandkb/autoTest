# @Time   ：2023/9/15 17:38
# @Author : Chao
# @File   : test_community_plate_add.py


import allure
from aikn_api.community_plate_add import community_plate_add
import requests

@allure.epic("知识库")
@allure.feature("社区")
@allure.story("新增社区版块成功")
def test_community_plate_search(login_fixture, base_url, random_fixture):
    r = community_plate_add(login_fixture, base_url, random_fixture('版块'))
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功'
