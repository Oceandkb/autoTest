# @Time   ：2022/11/18 14:43
# @Author : Chao
# @File   : test_entry_add.py

import allure
from aikn_api.entry_add import entry_add
from aikn_api.field_search import field_search
import requests

@allure.epic("知识库")
@allure.feature("词条")
@allure.story("新增词条成功")
def test_entry_add(login_fixture, base_url, random_fixture):
    r1 = field_search(login_fixture, base_url)
    _r1_ = r1.json()
    field_id = str(_r1_['data'][0]['id'])
    r = entry_add(login_fixture, base_url, random_fixture("词条"), field_id)
    print(r.text)
    assert r.json()["code"] == 1
    assert r.status_code == 200
    assert r.json()['message'] == '操作成功!'
