# @Time   ：2022/12/2 14:49
# @Author : Chao
# @File   : test_entry_detail.py


import allure
import pytest

from aikn_api.entry_detail import entry_detail
from aikn_api.entry_search import entry_list_search
import requests

@allure.epic("知识库")
@allure.feature("词条")
@allure.story("查看词条详情")
#@pytest.mark.usefixtures("entry_fixture")
def test_entry_detail(login_fixture, base_url):
    r = entry_list_search(login_fixture, base_url).json()
    entry_id = str(r['data']['list'][0]['id'])
    r1 = entry_detail(login_fixture, base_url, entry_id)
    print(r1.text)
    assert r1.json()["code"] == 1
    assert r1.status_code == 200
    assert r1.json()['message'] == '操作成功'